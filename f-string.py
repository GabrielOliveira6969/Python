# 1-) Crie um programa que receba 3 notas, calcule a média e exiba APROVADO ou REPROVADO se o aluno tiver a média menor que 6

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

media = (n1 + n2 + n3) / 3
print(f'Média: {media:.1f}')

if media >= 6:
  print('APROVADO')
else:
  print('REPROVADO')


#################################################################################################################################################

#2-) Receba 2 notas, calcule a média e exiba Reprovado para méda de 0 até 4, Exame de 4 até 6 e Aprovado para média de 6 até 10

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

media = (n1 + n2) / 2
print(f'Média: {media:.1f}')

if media >= 6:
  print('APROVADO')
elif media >= 4 and media < 6:
  print('EXAME')
else:
  print('REPROVADO')
