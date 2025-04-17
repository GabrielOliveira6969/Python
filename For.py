num = 50
for num in range(50, 100, 1):
  print(num)

#Neste exemplo temos três argumentos dentro do For, sendo eles start, stope step (inicio, fim, passo).
#O passo nada mais é do que a indicação do valor que será verificado e somado durante a execução do programa.

####################################################

num = int(input('Escolha un número inteiro: ')) 
x = 0 

for num in range(x, num + 1, 2): 
  print(num)

#Neste exemplo temos a soma do valor final para verificação do valor da variável.
#Caso a condição seja verdadeira(True), o programa itera o valor que será calculado e seguede com a execução.

####################################################

x = 1000
for x in range (x, 2000, 1):
  if x % 11 == 5: 
    print(x)

#Neste exemplo temos a verificação de números que tenham o resto 5 quando são dividos por 11.
#Sendo X o valor incial, 2000 o valor final e 1 o valor que define de quantos em quantos números o programa irá executar a verificação.
