# Solicita valores ao usuário
distancia = float(input('Qual a distância a ser percorrida (km)? '))
consumo = float(input('Qual o valor de km/L? '))
preco_por_litro = float(input('Qual o valor do litro? '))

# Calcula a quantidade de litros necessários
litros_necessarios = distancia / consumo

# Calcula o custo total
custo_total = litros_necessarios * preco_por_litro

# Exibe o resultado
print(f'A distância é {distancia} km, o consumo é de {consumo} km/L, sendo necessário {litros_necessarios:.2f} litros de combustível.')
print(f'O preço final da viagem será de R$ {custo_total:.2f}.')
