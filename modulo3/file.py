import csv
#Escribir dentro del archivo
def save_csv(inventory):
    with open('bd_inventory.CSV', 'w', newline = "") as file:
        wrt = csv.writer(file)
        wrt.writerow(["name", "price", "quanty",])
        for i in inventory:
            wrt.writerow = ([i["name"], i["price"], i["quanty"]])


#Leer el archivo CSV
def load_csv(inventory):
    with open('bd_inventory.CSV', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            inventory.append(
                {
                    "name": row[0],
                    "price": row[1],
                    "quanty": row[2]
                }
            )

