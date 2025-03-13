h = int(input()) #Tempo gasto em horas
vel = int(input()) #Velocidade média do veículo
km_l = 12 #Distancia por Litro

dist_perc = h * vel 

consumo = dist_perc / km_l

print(f'{consumo:.3f}')
