
#Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais

n1 = int(input("Numero1: "))
n2 = int(input("Numero2: "))

if(n1 == n2):
    print("Numeros Iguais!")
elif(n2 > n1):
    print("Segundo Valor é Maior!")
elif(n1 > n2):
    print("Primeiro Valor é Maior!")