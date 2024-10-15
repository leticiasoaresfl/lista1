nome = input('Qual o seu nome completo? ')
nascimento = input('Qual a sua data de nascimento? (DD/MM/AAAA) ')
str2 = nome[0:3]
str3 = nascimento[6:8]
tamanho = len(nome)
print(str2.upper() + str3 + ' ' + str(tamanho) + '!')
