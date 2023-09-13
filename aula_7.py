#criando um arquivo csv ou também pode importar um arquivo
import csv

# Crie um objeto CSVWriter para escrever o arquivo CSV
with open('arquivo.csv', 'w', newline='',encoding='utf-8') as csvfile:

    # Crie um escritor de CSV
    writer = csv.writer(csvfile, delimiter=',') # , ou ; ou tab-> "  "

    # Escreva as linhas do arquivo CSV
    writer.writerow(['nome', 'idade', 'cidade'])
    writer.writerow(['João', 25, 'São Paulo'])
    writer.writerow(['Maria', 30, 'Rio de Janeiro'])
    writer.writerow(['José', 40, 'Belo Horizonte'])
    writer.writerow(['Ana', 50, 'Curitiba'])
    writer.writerow(['Pedro', 60, 'Porto Alegre'])