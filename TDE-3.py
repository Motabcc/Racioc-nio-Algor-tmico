
# 1. Imprima os números de 1 até 99, com incremento de 2. Exemplo: 1, 3, 5.....97,99
for numeros in range(1,100,2):
    print(numeros)
# 2. Imprima os números de 50 até 0 com decremento de 5. Exemplo: 50, 45, 40.....5,
for numeros in range(50,-1,-5):
    print(numeros)
# 3. Imprima os números de -100 até 100, com incremento de 10. Exemplo: -100, -90,-80.....90, 100
for numeros in range(-100,101,10):
    print(numeros)
# 4. Imprima os números múltiplos de 4 existentes no intervalo aberto de 1 a 100.
for numeros in range(1,101):
    if numeros % 4 == 0:
        print(f'Os números divisiveis por 4 são {numeros}')
# 5. Imprima os números ímpares de 1 até n, sendo n fornecido pelo usuário
lim_final = 0
lim_final = int(input('Digite até que número: '))
for i in range(1,lim_final):
    if i%2 != 0:
        print(f'{i} É um número ímpar ')
# 6. Imprima uma tabela de conversão de polegadas para centímetros, cuja escala vaide 1 a 20 polegadas...
polegada= float(input('Digite um número em polegadas: '))
centimetro = polegada * 2.54
if 1<=polegada<=20:
    print(f'{centimetro:.2f}')
else:
    print('Digite um número entre 1 e 20!')
# 7. Considerando que 1 milha vale exatamente 1.609,344 metros, imprima uma tabelade conversã...
metros = int(input('Digite um número entre 20 a 160 km(metros): '))
milha = metros * 1609
if 20<= metros <=160:
    for c in range(20,metros,10):
        print(f'{metros} metros em milha vira {milha} , {c}km !')
#8.Elabore um algoritmo que leia um conjunto de 10 números inteiros. Mostre entãoqual o valor da soma ...
soma = contador = 0
while resposta <= 10:
    resposta +=1
    n = int(input("Digite um número: "))
    contador +=1
    soma += n
media = soma/contador
print(f'A soma dos 10 números digitados são{soma} e sua mé dia é {media}')
#9. Imprima os números múltiplos de 3 entre li (limite inicial
li =0
li = int(input('Numero pra comecar: '))
lf = int(input("Até : "))
while li <= lf :
    if li %3 == 0:
        print(f'{li} é multiplo de 3!')
    li +=1
    if li %3 !=0 and lf %3 !=0 :
        print("Não há números multiplos de 3 !")
#10 ...
moeda = str(input("Digite o tipo da moeda[D,L,E]: ")).strip().capitalize()[0]
qnt = float(input('Digite a quantia: '))
if moeda == 'D':
    dolar = qnt / 5.91
if dolar < 1000:
    imp = dolar*105/100
    print(f'{qnt:.2f}U$ em reais é {dolar:.2f}R$, com imposto é {imp}R$')
elif dolar>= 1000:
    imp = dolar*103/100
    print(f'{qnt:.2f}U$ em reais é {dolar:.2f}R$, com imposto é {imp}R$')
elif moeda == 'L':
    libra = qnt / 7.53
if libra < 1000:
    imp = libra*105/100
    print(f'{qnt:.2f}U$ em reais é {libra:.2f}R$, com imposto é {imp}R$')
elif libra>= 1000:
    imp = libra*103/100
    print(f'{qnt:.2f}U$ em reais é {libra:.2f}R$, com imposto é {imp}R$')
elif moeda == 'E':
    euro = qnt / 6.45
if euro < 1000:
    imp = euro*105/100
    print(f'{qnt:.2f}U$ em reais é {euro:.2f}R$, com imposto é {imp}R$')
elif euro>= 1000:
    imp = euro*103/100
    print(f'{qnt:.2f}U$ em reais é {euro:.2f}R$, com imposto é {imp}R$')
#11. Construa a tabela de multiplicação de 1 a 10. (Ex: 1x1 = 1, 1x2=2, 10x10 =100)
num = float(input("Qual número você deseja multiplicar: "))
for i in range(0,11):
    print(f'{num:.1f} x {i:.1f} = {num*i:.1f}')
