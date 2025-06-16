#1)Faça um algoritmo que leia um número inteiro e escreva seu antecessor e
sucessor.
numero = float(input('Digite um valor:'))
ant = numero-1
suc = numero+1
print("O valor escolhido foi {}, seu antecessor é {} e seu sucessor é
{}".format(numero,ant,suc))
#2. Faça um algoritmo que leia o ano de nascimento de uma pessoa e calcule a idade
que completará em 2025
ano_nascimento = int(input("Digite seu ano de nascimento:"))
idade = 2025 - ano_nascimento
print("Você completará {} anos em 2025!".format(idade))
#3)Faça um algoritmo que receba o salário de um profissional e calcule quantos
salário mínimos ele recebe.
salario = float(input('Digite seu salário:'))
salMin= salario / 1518
print("Você recebe {} salários mínimos!".format(salMin))
#4.Faça um algoritmo que recebe o valor de um produto e calcule os seguintes
valores: (1) a vista ...
produtoInicial = float(input('Digite o Valor inicial do produto:'))
vista = produtoInicial * 95/100
parcela = produtoInicial / 2
parcelaAcrescimo = (produtoInicial/3)*105/100
print("Seu valor á vista fica em {}R$,parcelado em duas vezes fica {}R$ e parcelado
em três vezes com acréscimo de 5% no valor final fica
{:>.4}R$".format(vista,parcela,parcelaAcrescimo))
#5)Faça um algoritmo que calcule o consumo médio de um automóvel (medido em km/l),
distancia = float(input('Digite a distância total(km):'))
print('Será necessário {} litros'.format(distancia)
#6). Faça um algoritmo que calcule a quantidade de latas de tintas necessárias...
altura = int(input('Digite sua altura (m):'))
raio = int(input('Digite seu raio(m):'))
area = 2 * 3.14*raio*altura + 2*3.14*raio**2
litro= float(area/3)
lata = 5*litro
preco = lata* 50
print('Área total {:>.2f}, {:>.2f} Litros necessários ,{:>.2f} latas Necessária e
preço total {:>.2f}'.format(area,litro,lata,preco))
