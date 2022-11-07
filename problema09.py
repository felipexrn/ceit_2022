'''
Ao se comparar se uma string é maior que outra, considera-se a ordem alfabética ou lexicográfica. No caso, “abcd” < “adbc” < “bacd”.

Escreva uma função que receba uma string A e retorne uma string B, sendo que B é composta pelos mesmos caracteres que A reordenados.

B deve obedecer às seguintes condições:

Ser maior que A
Ser a menor string possível que cumpra as condições acima
Caso não seja possível encontrar uma string que cumpra as condições, retorne a string “sem reposta”.
Por exemplo:

A = “ab”
Logo, o resultado será “ba”

A = “abcde”
Logo, o resultado será “abced”

A = “ba”
Nesse caso, o resultado será “sem resposta"
'''
def menor_string_maior(name):
  print(name)
  maior = False
  name_maior = name
  n1 = []
  for i in name:
    n1.append(i)
  tam = len(n1) - 1
  parte1 = []
  parte2 = []
  mensagem = ""
  for i in range(tam + 1):
    if n1[tam - i] > n1[tam - i - 1]:
      maior = n1[tam - i]
      n1[tam - i] = n1[tam - i - 1]
      n1[tam - i - 1] = maior
      parte1 = n1[:tam - i]
      parte2 = n1[tam - i:]
      if len(parte2) > 2:
        parte2.sort()
      break
  for i in parte1:
    mensagem += i
  for i in parte2:
    mensagem += i
  if name == "" or mensagem < name:
    mensagem = "sem resposta"
  return mensagem