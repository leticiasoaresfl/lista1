# ALGORITMO DE VERIFICAÇÃO CPF/CNPJ
# solicita o dado ao usuário 
CNPJ = input("Digite o CNPJ para verificação: ")

# faz a verificação da quantidade de caracteres 
condicao1 = (len(CNPJ) == 18)

# condicao2 verifica a pontuação 
condicao2 = CNPJ[2] == "." and CNPJ[6] == "." and CNPJ[10] == "/"

# condicao4 verifica a estrutura do CNPJ
condicao3 = CNPJ[11:15] == "0001"

# retorno ao usuário 
if condicao1 and condicao2 and condicao3:
    print("Verificação correta")
else:
    print("CNPJ inválido")

