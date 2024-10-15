# Solicita valores ao usuário
real = float(input('Qual valor em reais? '))
dolar = float(input('Qual o valor da taxa do dólar atual? '))

# Calcula o valor em dólares
resultado = real * dolar

# Exibe o resultado
print(f'O valor em reais é {real} e a taxa atual está em {dolar}, sendo o valor em dólares de {resultado}.')

#-------------------------------------------------------------------------------------------------
euro = 5.8 
conversao = float (real) / float (euro)
print (f' O valor em euro sera de: {conversao: .2f}')