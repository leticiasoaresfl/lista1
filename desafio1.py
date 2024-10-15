# ALGORITMO DE VERIFICAÇÃO CPF/CNPJ
# solicita o dado ao usuário 
cpf = input("Digite o CPF para verificação: ")

# faz a verificação da quantidade de caracteres 
condicao1 = (len(cpf) == 14)

# condicao2 verifica a pontuação 
condicao2 = cpf[3] == "." and cpf[7] == "."

# condicao3
condicao3 = cpf[11] == "-"

# retorno ao usuário 
if condicao1 and condicao2 and condicao3:
    print("Verificação correta")
else:
    print("CPF inválido")

