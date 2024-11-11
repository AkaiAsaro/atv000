from datetime import datetime
def saudacao_horario(horario):
  if horario >= 6 and horario < 12:
    return 'Bom dia'
  elif horario >= 12 and horario < 18:
    return 'Boa tarde'
  elif horario >= 18 and horario < 24:
    return 'boa noite'
  else:
    return 'horario invalido'


try:
  pedir = int(input('digite seu horario no formato HH:MM: '))

  tempo = datetime.strptime(pedir, '%H%M')
except  ValueError:
  print('numero invalido, tente novamente')

saudacao_horario(horario)