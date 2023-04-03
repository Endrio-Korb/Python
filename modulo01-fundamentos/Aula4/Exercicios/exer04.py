import os
import csv

if __name__ == "__main__":

    with open(os.path.join(os.getcwd(), "sales.csv"), "r") as arquivo:
        arquivo_csv = csv.reader(arquivo, delimiter = ";")

        for i, linha in enumerate(arquivo_csv):
            if i == 0:
                print("Cabeçãlho" + str(linha))
            else:
                print(f"Vendas: " + str(linha))