import csv
import serial
porta = serial.serial_for_url("loop://", timeout=1)


with open('./temperature.csv', "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['numero', 'temperatura'])
    for index, num in enumerate(range(20, 30),start=1):
        mess = f"{num}\n"
        dati = mess.encode("utf-8")
        porta.write(dati)

        val_byte = porta.readline()
        value = int(val_byte.decode("utf-8"))

        print(f"Valore ricevuto: {value}")
        writer.writerow([index, value])
    porta.close()