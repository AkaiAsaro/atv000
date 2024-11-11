lista_qualquer = [ ]



def numeros_pares(lista:list):
  for numero in lista:
    if numero % 2 == 0:
      print(numero)

while True:
  quantidade = input('digite seus numeros (ou sair para fechar o programa): ')
  if quantidade == 'sair':
    print('vtnc')
    break
  lista_qualquer.append(int(quantidade))
  numeros_pares(lista_qualquer)