L1 = float(input('Digite o valor do primeiro lado do triângulo: '))
L2 = float(input('Digite o valor do segundo lado do triângulo: '))
L3 = float(input('Digite o valor do terceiro lado do triângulo: '))


### A condição para se formar um triangulo é: A soma de dois lados quaisquer deve ser maior que o terceiro lado para que o triangulo possa ser formado ###
if L1 + L2 > L3: 
    print('É possível formar um triângulo com esses lados.')
else:
    print('Não é possível formar um triângulo com esses lados.')
print('RA: 2404126')
