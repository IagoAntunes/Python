
#Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.


vel = int(input("Velocidade do Carro:"))
if(vel > 80):
    multa = vel - 80
    print(f"Voce foi Multado!! \nPreço:R$ {multa * 7}")