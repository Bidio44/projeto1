# Faça um Programa que leia três números e mostre o maior e o menor deles.
n1 = float(input("Digite o 1º Número: "))
n2 = float(input("Digite o 2º Número: "))
if n1 > n2:
    print("{} é maior que {}".format(n1, n2))
elif n1 < n2:
    print("{} é maior que {}".format(n2, n1))
else:
    print("{} e {} são iguais".format(n2, n1))


# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
n1 = float(input("Digite o 1º Número: "))
if n1 == 0:
    print("zero não é negativo nem positivo e sim neutro!")
if n1 > 0:
    print("O número escolhido é positivo")
else:
    print("O número escolhido é negativo")


# Faça um Programa que verifique se uma letra digitada é "F" ou "M"
sexo = str(input("Qual o seu sexo, F ou M: ").upper())
if sexo == "F":
    print("Sexo Feminio")
elif sexo == "M":
    print("Sexo masculino")
else:
    print("Escolha invalida")


# Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
letra = input("Digite uma letra: ").upper()
vogal = ['A', 'E', 'I', 'O', 'U']
if letra in vogal:
    print("A letra é uma vogal")
else:
    print("A Letra é um Consoante!")


#Faça um programa para a leitura de duas notas parciais de um aluno.
n1 = float(input("Digite a 1ª Nota:"))
n2 = float(input("Digite a 2ª Nota: "))
if (n2 + n1) / 2 >= 7:
    print("Aluno aprovado")
else:
    print("Aluno reprovado")


# Faça um Programa que leia três números e mostre o maior e o menor deles.
n1 = float(input("Digite o 1º Número: "))
n2 = float(input("Digite o 2º Número: "))
n3 = float(input("Digite o 3º Número: "))
if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print("O maior é {} e o menor {}".format(maior, menor))


# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar...
p1 = float(input("Qual o valor do produto 01 R$ "))
p2 = float(input("Qual o valor do produto 02 R$ "))
p3 = float(input("Qual o valor do produto 03 R$ "))
if p1 < p2 and p1 < p3:
    print("Compre o produto com o preço de R${}".format(p1))
if p2 >= p1 or p2 >= p3:
    print("Compre o produto com o preço de R${}".format(p3))
else:
    print("Compre o produto com o preço de R${}".format(p2))



# Faça um Programa que leia três números e mostre o maior e o menor deles.
n1 = float(input("Digite o 1º Número: "))
n2 = float(input("Digite o 2º Número: "))
n3 = float(input("Digite o 3º Número: "))
lista = [n1, n2, n3]
lista.sort(reverse=True)
print(lista)

# Faça um Programa que pergunte em que turno você estuda, Peça para digitar M-Matutino ou V- Vespertino ou N- Noturno
turno = str(input('Em que turno você estuda? M-Matutino ou V- Vespertino ou N- Noturno: ').upper())
if turno == 'M':
    print('Bom dia!')
elif turno == 'V':
    print('Boa Tarde')
elif turno == 'N':
    print('Boa Noite!')
else:
    print('Escolha inválida')


# As Organizações Tabajara ...
salario = float(input('Qual o salário atual R$ '))
if salario <= 280:
    aumento = salario * 0.2
    print('O salário antes do reajuste {} \nO percentual de aumento foi de: 20% \nO Valor do aumento foi de: R$ {}'
          .format(salario, aumento))
    print('O novo sálario será R$ {}'.format(salario + aumento))

elif 280 < salario <= 700:
    aumento = salario * 0.15
    print('O salário antes do reajuste {} \nO percentual de aumento foi de: 15% \nO Valor do aumento foi de: R$ {}'
          .format(salario, aumento))
    print('O novo sálario será R$ {}'.format(salario + aumento))

elif salario > 700 and salario <= 1500:
    aumento = salario * 0.1
    print('O salário antes do reajuste {} \nO percentual de aumento foi de: 10% \nO Valor do aumento foi de: R$ {}'
          .format(salario, aumento))
    print('O novo sálario será R$ {}'.format(salario + aumento))

elif salario > 1500:
    aumento = salario * 0.05
    print('O salário antes do reajuste {} \nO percentual de aumento foi de: 5% \nO Valor do aumento foi de: R$ {}'
          .format(salario, aumento))
    print('O novo sálario será R$ {}'.format(salario + aumento))


#Faça um programa para o cálculo de uma folha de pagamento
horas = float(input("Qual a quantidade de horas trabalhadas neste mês:  "))
custo = float(input("Qual o custo da sua hora trabalhada: "))
salario = horas * custo
fgts = (salario * 0.11)
sind = (salario * 0.03)

if salario <= 900:
    print(
        'Sál. Isento de IR \nFGTS: R$ {} \nSindicato: R$: {} \nSál. liquido: R$ {}'.format(fgts, sind, salario - sind))

elif salario > 900 and salario <= 1500:
    ir = salario * 0.05
    print('IR: R$ {} \nFGTS: R$ {} \nSindicato: R$: {} \nliquido: R$ {}'.format(ir, fgts, sind, salario - sind - ir))

elif salario > 1500 and salario <= 2500:
    ir = salario * 0.1
    print('IR: R$ {} \nFGTS: R$ {} \nSindicato: R$: {} \nliquido: R$ {}'.format(ir, fgts, sind, salario - sind - ir))

elif salario > 2500:
    ir = salario * 0.2
    print('IR: R$ {} \nFGTS: R$ {} \nSindicato: R$: {} \nliquido: R$ {}'.format(ir, fgts, sind, salario - sind - ir))


#Faça um Programa que leia um número e exiba o dia correspondente da semana
numero = int(input('Digite um numero de 1 a 7: '))
if numero == 1:
    print('Domingo')
elif numero == 2:
    print('Segunda-feira')
elif numero == 3:
    print('Terça-feira')
elif numero == 4:
    print('Quarta-feira')
elif numero == 5:
    print('Quinta-feira')
elif numero == 6:
    print('Sexta-feira')
elif numero == 7:
    print('Sábado')
else:
    print('Comando invalido')


#Faça um programa que lê as duas notas parciais obtidas por um aluno
nota1 = float(input('Digite a 1ª Nota: '))
nota2 = float(input('Digite a 2ª Nota: '))
media = (nota1 + nota2) / 2
if media >= 9:
    conceito = "A"
    print('1ª Nota: {} \n2ª Nota: {} \nMédia : {} \nConceito : {} \nAprovado'.format(nota1, nota2, media, conceito))

elif media < 9 and media >= 7.5:
    conceito = "B"
    print('1ª Nota: {} \n2ª Nota: {} \nMédia : {} \nConceito : {} \nAprovado'.format(nota1, nota2, media, conceito))

elif media < 7.5 and media >= 6:
    conceito = "C"
    print('1ª Nota: {} \n2ª Nota: {} \nMédia : {} \nConceito : {} \nAprovado'.format(nota1, nota2, media, conceito))

elif media < 6 and media >= 4:
    conceito = "D"
    print('1ª Nota: {} \n2ª Nota: {} \nMédia : {} \nConceito : {} \nReprovado'.format(nota1, nota2, media, conceito))

elif media < 4 and media >= 0:
    conceito = "E"
    print('1ª Nota: {} \n2ª Nota: {} \nMédia : {} \nConceito : {} \nReprovado'.format(nota1, nota2, media, conceito))
else:
    print("Algo deu errado tente novamente!")


# Faça um Programa que peça os três lados de um triângulo:
ladoA = float(input('Digite o tamanho do lado A:  '))
ladoB = float(input('Digite o tamanho do lado B:  '))
ladoC = float(input('Digite o tamanho do lado C:  '))

if ladoA > (ladoB + ladoC) or ladoB > (ladoA + ladoB) or ladoC > (ladoA + ladoB):
    print('Não é possivel formar um triângulo!.')
elif ladoA == ladoB and ladoA == ladoC and ladoB == ladoC:
    print('Equilátero')
elif ladoA == ladoB or ladoA == ladoC or ladoB == ladoC:
    print('Isósceles')
else:
    print('Escaleno')


#Faça um programa que calcule as raízes de uma equação do segundo grau
import math

a = int(input(' Qual o valor de - a: '))
if (a == 0):
    print('Erro, a não pode ser igual a 0')
else:
    b = int(input('Qual o valor de - b:  '))
    c = int(input('Qual o valor de - c: '))
    delta = b * b - (4 * a * c)
    if delta < 0:
        print('Delta menor que 0, a equação não possuirá valores reais')
    elif delta == 0:
        raiz = -b / (2 * a)
        print('Delta=0 , raiz = ', raiz)
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)
        print('Raizes: {:.2f} e {:.2f} '.format(raiz1, raiz2))

#Faça um Programa que peça um número correspondente a um determinado ano
ano = int(input('Digite um ano: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('{} é um ano bissexto'.format(ano))
else:
    print("{} não é bissexto ".format(ano))

#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
data = input("Digite uma data (dd/mm/aaaa): ").split("/")
dia = int(data[0])
mes = int(data[1])
ano = int(data[2])

if ano > 0:
  if mes > 0 and mes <= 12:
    if mes in [1, 3, 5, 7, 8, 10, 12]:
      if dia > 0 and dia <= 31:
        print("Essa é uma data válida!")
      else:
        print("Essa é uma data inválida!")
    elif mes == 2:
      if ano % 4 == 0:
        if dia > 0 and dia <= 29:
          print("Essa é uma data válida!")
        else:
          print("Essa é uma data inválida!")
      else:
        if dia > 0 and dia <= 28:
          print("Essa é uma data válida!")
        else:
          print("Essa é uma data inválida!")
    else:
      if dia > 0 and dia <= 30:
        print("Essa é uma data válida!")
      else:
        print("Essa é uma data inválida!")
  else:
    print("Essa é uma data inválida!")
else:
  print("Essa é uma data inválida!")



# Faça um Programa que leia um número inteiro menor que 1000
num = int(input('Informe um número menor que 1000:'))
u = num//1 % 10
d = num//10 % 10
c = num//100 % 10
m = num//1000 % 10
if num < 1000:
    print('Analisando o número: {}' .format(num))
    print('Analisando unidadde:{}' .format(u))
    print('Analisando dezena: {}' .format(d))
    print('Analisando centena: {}' .format(c))
else:
    print('Comando invalido!')