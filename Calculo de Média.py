#A,B e C = notas
A = float(input()) 
B = float(input())
C = float(input())

#P1,P2 e P3 = peso das notas em porcentagem
P1 = 0.2
P2 = 0.3
P3 = 0.5

m = (A * P1) + (B * P2) + (C * P3)
print(f'MEDIA = {m:.1f}')
