montante = float
print('Seja bem-vindo')
print('--------------')
investimento = float(input('Qual o valor do investimento? '))
taxa = float(input ('Qual o valor do juros atual?'))
estimativa = int(input('Para o cálculo, digite 1 para calcular em anos OU 2 para calcular em meses: '))

if estimativa == 1:
    anos = int(input('Para quantos anos seria o investimento? '))
    montante = investimento * (1 + taxa*anos)
    
else:
    meses = int(input('Para quantos meses seria o investimento? '))
    conversao = meses/12
    montante = investimento * (1 + taxa*conversao)
    
print(f'Para o valor de investimento {investimento} com a taxa atual de {taxa} ficará o valor de {montante}')
