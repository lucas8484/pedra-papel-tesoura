# -*- coding: utf-8 -*-
"""ppt.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10ie4TAFQ_qKnP9I4fcoq2ppfcWJQ67ul
"""

from random import randint

d = ['pedra','papel','tesoura' ]

b = randint(0,2)

print('pedra  - papel  - tesoura ')

print('=-'*30)

while True:
  try:

    c = str(input('qual e a sua jogada?: '))
    a = c.strip()
    a = d.index(a)
    
  except ValueError:
    print('ERRO')
  
  else:
    break

print('=-'*30)

print(f'vc jogou  {d[a]}')

print(f'a maquina  jogou {d[b]}')


if b == 0:
  if a == 0:
    print('empate')
  elif a == 1:
    print('vc ganhou')
  elif a == 2:
    print('vc perdeu')


if b == 1:
  if a == 1:
    print('empate')
  elif a == 2:
    print('vc ganhou')
  elif a == 0:
    print('vc perdeu')


if b == 2:
  if a == 2:
    print('empate')
  elif a == 0:
    print('vc ganhou')
  elif a == 1:
    print('vc perdeu')