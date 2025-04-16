########################## WHILE ##########################

num = int(input('Escolha um número: '))
while num <= 100:
  print(num)
  num += 1

############# a diferença no operador lógico se deve a diferença de recebimento de argumento. 
############# Quando temos uma entrada manual devemos iterar com +=, enquanto iteramos apenas com + quando temos valor pré defiinido;

num = 50
while num <= 100:
  print(num)
  num = num + 1

####################################################

num = int(input('Escolha um número inteiro: ')) 
x = 0 

while x <= num: 
  print(x)
  x = x + 2
