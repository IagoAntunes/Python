
#Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

num = int(input("Digite um Numero: "))
razao = int(input("Razão: "))
decimo = num + (10 - 1) * razao

for c in range(num,decimo,razao):
    print(c)