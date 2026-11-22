import csv
import requests
import matplotlib.pyplot as plt
from pathlib import Path
from datetime import datetime
import matplotlib.dates as mdates

def timestamp_exists(csv_path, timestamp):
    if not csv_path.exists():
        return False
    with open(csv_path, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            if row['timestamp'] == timestamp:
                return True
    return False

def calculate_average(csv_path):
    if not csv_path.exists():
        return None
    somma = 0
    count = 0
    with open(csv_path, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            somma += float(row['temperature'])
            count += 1
    if count == 0:
        return None
    return somma/count

def fetch_weather(url, params):
    r = requests.get(url, params=params, timeout=10)
    r.raise_for_status()
    data = r.json()
    current = data['current']
    temp = current['temperature_2m']
    time = current['time']
    return time, temp

def save_measurement(csv_path, timestamp, temperature):
    if not timestamp_exists(csv_path, timestamp):
        write_header = not csv_path.exists() or csv_path.stat().st_size == 0
        with open(csv_path, "a", newline='') as csv_file:
            writer = csv.writer(csv_file)
            if write_header:
                writer.writerow(['timestamp', 'temperature'])
            writer.writerow([timestamp, temperature])
        return True
    else:
        return False
    
def load_measurements(csv_path):
    if not csv_path.exists():
        return [], []
    timestamps = []
    temperatures = []
    with open(csv_path, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            timestamps.append(row['timestamp'])
            temperatures.append(float(row['temperature']))
    return timestamps, temperatures

def plot_temperatures(csv_path):
    timestamps, temperatures = load_measurements(csv_path)

    if not timestamps:
        print("No measurements to plot.")
        return

    dates = [datetime.fromisoformat(t) for t in timestamps]
    measurements = sorted(zip(dates, temperatures))
    dates, temperatures = zip(*measurements)

    bg, cyan, muted = "#101827", "#22D3EE", "#94A3B8"

    plt.style.use("dark_background")
    fig, ax = plt.subplots(figsize=(11, 6))
    fig.patch.set_facecolor(bg)
    ax.set_facecolor(bg)

    # Temperature chart
    ax.plot(dates, temperatures, color=cyan, linewidth=2.5, marker="o")
    ax.fill_between(
        dates, temperatures, min(temperatures),
        color=cyan, alpha=0.12
    )

    # Axes
    ax.xaxis.set_major_locator(mdates.AutoDateLocator(maxticks=6))
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))
    ax.grid(axis="y", linestyle="--", alpha=0.15)
    ax.tick_params(colors=muted)

    for spine in ax.spines.values():
        spine.set_visible(False)

    # Dashboard header
    fig.suptitle(
        "SENSORLOGGER  /  TEMPERATURE MONITORING",
        fontsize=16, fontweight="bold", color="white"
    )

    # Statistics
    stats = (
        f"CURRENT  {temperatures[-1]:.1f}°C       "
        f"MIN  {min(temperatures):.1f}°C       "
        f"MAX  {max(temperatures):.1f}°C"
    )

    fig.text(0.5, 0.05, stats, ha="center", color=cyan, fontsize=12)
    fig.subplots_adjust(top=0.83, bottom=0.20, left=0.09, right=0.95)

    plt.show()
    plt.close(fig)

url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 45.07,
    "longitude": 7.69,
    "current": "temperature_2m",
    "timezone": "Europe/Rome",
}
csv_path = Path('weather.csv')
try:
    time, temp = fetch_weather(url, params)
    saved = save_measurement(csv_path, time, temp)
    if saved:
        print(f"Saved measurement: {time}, {temp}°C")
    else:
        print(f"Measurement for {time} already exists.")
    average = calculate_average(csv_path)
    if average is not None:
        print(f"Average temperature: {average:.2f}°C")
    else:
        print("No measurements available.")
    plot_temperatures(csv_path)
except requests.exceptions.RequestException as e:
    print(f"Error fetching weather data: {e}")




