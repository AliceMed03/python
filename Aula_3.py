#Estrutura if else
'''
if é o se
elif é o senor se
else é o senão
'''

idade = 62
if idade >= 18 :
    print('É maior de idade.')
else:
    print('É menor de idade')

'''
Saber se a pessoa é :
-Criança 0 a 12 anos
-Adolescente 13 a 17 anos
-Adulto 18 a 59 anos
-Idoso acima de 60 anos
'''
if idade <= 12:
    print('é uma criança')
elif idade < 18: #idade >= 13 and idade <= 17
    print('é um adolescente')
elif idade < 60: #idade >= 18 and idade <= 59
    print('é um adulto')
else:
    print('é um idoso')

'''
Operadores lógicos
E é and
OU é or
not para contrário
'''
salario = 7001
profissao = 'd'

'''
Se a pessoa for 'dev' e tiver salário = 2000, imprimir 'é junior'
Se a pessoa for 'dev' e tiver salário entre 2000 e 7000, imprimir 'é pleno'
Se a pessoa for 'dev' e tiver salário maior que 7000, imprimir 'é senior'

Imprima as mensagens conforme cada situação
'''
if salario == 2000 and profissao == 'dev':
    print('é junior')
elif salario <= 7000 and profissao == 'dev':
    print('é pleno')
elif salario > 7000 and profissao == 'dev':
    print('é senior')
else:
    print('A pessoa não é dev ou ganha menos que 2000')

#Loops
#Loop for
lojas = ['Americanas','Pernambucanas', 'Casas Bahia']
#A variável loja percorre item por item no vetor loja
for loja in lojas:
  print(loja)
'''
for i in range(5):
  print(i)

#Faça um for para contar do 1 até 50

for i in range(1,51):
  print(i)
'''
#Loop while ou enquanto
i=1
while i < 10:
    print(i)
    i+=1

esta_chovendo = False
while not esta_chovendo:
    chuva = input('Está chovendo? Digite s para Sim e n para Não: ')
    if chuva == 's':
        print('Tá chovendo!')
        esta_chovendo = True
    elif chuva == 'n':
        print('Não está chovendo!')
        esta_chovendo = False
    else:
        print('Digite s ou n')