import csv
import serial
serial_port = serial.serial_for_url("loop://", timeout=1)


with open('./temperature.csv', "w", newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['numero', 'temperatura'])
    for measurement_id, temperature in enumerate(range(20, 30),start=1):
        message = f"{temperature}\n"
        encoded_data = message.encode("utf-8")
        serial_port.write(encoded_data)

        received_bytes = serial_port.readline()
        received_value = int(received_bytes.decode("utf-8"))

        print(f"Received value: {received_value}")
        writer.writerow([measurement_id, received_value])
    serial_port.close()