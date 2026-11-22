

<h1 align="center">📊 SensorLogger</h1>

<p align="center">
  A lightweight Python serial data logger with CSV export.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3">
  <img src="https://img.shields.io/badge/PySerial-Virtual%20Serial-4F46E5?style=for-the-badge" alt="PySerial">
  <img src="https://img.shields.io/badge/Output-CSV-16A34A?style=for-the-badge" alt="CSV">
</p>

<p align="center">
  Simple • Open Source • Hardware-Free
</p>

---


## About

SensorLogger is a Python-based project designed to simulate serial data acquisition and store the received values in a CSV file.

It uses PySerial's virtual serial port (`loop://`) to send and receive simulated temperature values without requiring physical hardware.

## Technologies

- **Python 3** — Main programming language.
- **PySerial** — Handles virtual serial communication.
- **CSV** — Python's built-in module for storing data in CSV files.
- **Git & GitHub** — Version control and source code hosting.

## How it works

1. The program creates a virtual serial connection using PySerial's `loop://` interface.
2. It generates 10 simulated temperature values, from 20 to 29.
3. Each value is encoded into bytes and sent through the virtual serial port.
4. The program reads the received bytes and converts them into integers.
5. Each value is displayed in the terminal and saved to `temperature.csv`.

The CSV file contains two columns:
- `numero`: The measurement number.
- `temperatura`: The simulated temperature value.

### Data Flow


### Data Flow

```mermaid
flowchart LR
    subgraph S1["01 · DATA SOURCE"]
        A["🌡️ Simulated Values<br/>20–29"]
    end

    subgraph S2["02 · SERIAL COMMUNICATION"]
        B["Encode<br/>UTF-8"]
        C["PySerial<br/>loop://"]
        D["Read & Decode<br/>Bytes → Integer"]
        B --> C --> D
    end

    subgraph S3["03 · DATA OUTPUT"]
        E["Terminal<br/>Live Output"]
        F["temperature.csv<br/>10 Measurements"]
    end

    A --> B
    D --> E
    D --> F

    classDef source fill:#DBEAFE,stroke:#2563EB,color:#1E3A8A,stroke-width:2px
    classDef process fill:#EDE9FE,stroke:#7C3AED,color:#4C1D95,stroke-width:2px
    classDef output fill:#D1FAE5,stroke:#059669,color:#065F46,stroke-width:2px

    class A source
    class B,C,D process
    class E,F output

    style S1 fill:transparent,stroke:#93C5FD,stroke-width:1px
    style S2 fill:transparent,stroke:#C4B5FD,stroke-width:1px
    style S3 fill:transparent,stroke:#6EE7B7,stroke-width:1px
```


### Sample Output

The following table shows a preview of the simulated temperature measurements stored in `temperature.csv`.

| Measurement  | Temperature (simulated) |
|:-------------:|:-----------------------:|
| 01 | 20 |
| 02 | 21 |
| 03 | 22 |
| 04 | 23 |
| 05 | 24 |
| ... | ... |
| 10 | 29 |

> **Note:** Values are simulated and do not represent actual sensor readings.

### Terminal Output

When executed, SensorLogger displays the received values in the terminal:

```text
Valore ricevuto: 20
Valore ricevuto: 21
Valore ricevuto: 22
Valore ricevuto: 23
Valore ricevuto: 24
Valore ricevuto: 25
Valore ricevuto: 26
Valore ricevuto: 27
Valore ricevuto: 28
Valore ricevuto: 29
```

The generated data is also saved automatically to `temperature.csv`.


## How to run

### Requirements

- Python 3
- Git
- PySerial

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/noticso/SensorLogger.git
   ```

2. Navigate to the project directory:

   ```bash
   cd SensorLogger
   ```

3. Install PySerial:

   ```bash
   python -m pip install pyserial
   ```

### Usage

Run the Python script:

```bash
python lettore.py
```

The program generates 10 simulated temperature values, displays them in the terminal, and saves them to `temperature.csv`.

No physical Arduino or serial device is required.
