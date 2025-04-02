## Neste método o código irá passar por cada etapa individualmente, pedindo a entrada ao usuário sempre que for realizar uma nova etapa 

def idadeMeses(idade):
  print('Sua idade em meses é: ', idade * 12)

def idadeSemanas(idade):
  print('Sua idade em semanas é: ', idade * 52)

def idadeDias(idade):
  print('Sua idade em dias é: ', idade * 365)

def idadeAnos():
  aa = int(input('Digite o ano atual '))
  an = int(input('Digite seu ano de nascimento '))
  idadeAnos = aa - an
  print('Sua idade é: ', idadeAnos)

  return idadeAnos 

idadeAnos()
idadeMeses(idadeAnos())
idadeSemanas(idadeAnos())
idadeDias(idadeAnos())

##exemplo de saída 
##Digite o ano atual 2025
##Digite seu ano de nascimento 2003
##Sua idade é:  22
##Digite o ano atual 2025
##Digite seu ano de nascimento 2003
##Sua idade é:  22
##Sua idade em meses é:  264
##Digite o ano atual 2025
##Digite seu ano de nascimento 2003
##Sua idade é:  22
##Sua idade em semanas é:  1144
##Digite o ano atual 2025
##Digite seu ano de nascimento 2003
##Sua idade é:  22
##Sua idade em dias é:  8030

########################################################################

## Neste outro método o código irá passar por cada etapa individualmente, porém, requisitando a entrada ao usuário somente uma vez e retornando todos os valores em sequencia  

def idadeMeses(idade):
  print('Sua idade em meses é: ', idade * 12)

def idadeSemanas(idade):
  print('Sua idade em semanas é: ', idade * 52)

def idadeDias(idade):
  print('Sua idade em dias é: ', idade * 365)

def idadeAnos():
  aa = int(input('Digite o ano atual '))
  an = int(input('Digite seu ano de nascimento '))
  idadeAnos = aa - an
  print('Sua idade é: ', idadeAnos)

  return idadeMeses(idadeAnos), idadeSemanas(idadeAnos), idadeDias(idadeAnos())

idadeAnos()

##exemplo de saída
##Digite o ano atual 2025
##Digite seu ano de nascimento 2003
##Sua idade é:  22
##Sua idade em meses é:  264
##Sua idade em semanas é:  1144
##Sua idade em dias é:  8030
