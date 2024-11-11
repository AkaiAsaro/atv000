


def calcular():
  operação = input('digite a operação (+, -, *, /):')
  num1 = float(input('digite um numero:'))
  num2 = float(input('digite um numero:'))

  if operação == '+':
    print (num1 + num2)
  elif operação == '-':
    print (num1 - num2)
  elif operação == "*":
    print (num1 * num2)
  elif operação == "/":
    print (num1 / num2)
  else:
    print('operação invalida, tente novamente')


  while True:
    print('--menu--')
    print('1. calcular')
    print('2. sair')
escolha = int(input('digite a opção desejada: ')) 
if escolha == 1:
  calcular()
LAQDRG














