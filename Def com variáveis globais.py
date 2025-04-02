## Utilizando uma variável global

n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))

def soma (n1, n2):
    print('A soma é: ', n1 + n2)

def sub(n1, n2):
    print('A subtração é: ', n1 - n2)

def div(n1, n2):
    print('A divisão é: ', n1 // n2)


######################################################################

div(n1, n2)
soma(n1, n2)
sub(n1, n2)

at = int(input('Qual o ano atual? '))
an = int(input('Qual o ano do seu nascimento? '))
idade = at - an

def idadeAnos(idade):
  print('Sua idade é: ', idade)
    
def idadeMeses(idade):
  print('Sua idade em meses é: ', (idade * 12))
  
idadeAnos()
idadeMeses()
