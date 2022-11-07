'''
Um grande amigo seu mora numa cidade pequena, onde existem apenas duas empresas de táxi - a Empresa 1 e a Empresa 2. Ambas mudam suas taxas a cada dia e calculam o valor de suas corridas da seguinte forma: uma taxa fixa mais um valor por quilômetro rodado.
Seu amigo é fisioterapeuta e pega táxis diariamente para visitar seus clientes ao redor da cidade. Você decidiu escrever um código para ajudá-lo a decidir qual empresa escolher para cada uma das corridas, baseado no preço.

Sua função receberá 4 valores: TF1 (a taxa fixa da empresa 1), VQR1 (o valor por quilômetro rodado da empresa 1), TF2 (a taxa fixa da empresa 2), VQR2 (o valor por quilômetro rodado da empresa 2), todos em formato string. Seu retorno deve ser uma string em uma das seguintes formas:

“Tanto faz” - para o caso de o valor das duas empresas para qualquer corrida ser igual
“Empresa 1” - se o valor da Empresa 1 for sempre menor que o da Empresa 2
“Empresa 2” - para o caso contrário do citado acima
“Empresa Xpto quando a distância < N, Tanto faz quando a distância = N, Empresa Ypto quando a distância > N” para o caso de a escolha depender da distância a ser percorrida (onde Xpto e Ypto representa 1 ou 2 e N representa a distância).
Exemplo:
TF1 = 2,50
VQR1 = 1,00
TF2 = 5,00
VQR2 = 0,75
Output:
“Empresa 1 quando a distância < 10.0, Tanto faz quando a distância = 10.0, Empresa 2 quando a distância > 10.0”
'''
def abs(num):
  if num < 0:
    num = num * -1
  return num
def escolhe_taxi(tf1,vqr1,tf2,vqr2):
  t1 = float(tf1)
  v1 = float(vqr1)
  t2 = float(tf2)
  v2 = float(vqr2)
  xpto = t1 * v1
  ypto = t2 * v2
  if v1 > v2 and t1 > t2: resposta = "Empresa 2"
  elif v2 > v1 and t2 > t1: resposta = "Empresa 1"
  elif xpto == ypto: resposta = "Tanto faz"
  else:
    n = abs(t1 - t2) / abs(v1 - v2)
    if n > 7.14 and n < 7.15:
      n = f"{n:.2f}"
    resposta = f"Empresa 1 quando a distância < {n}, Tanto faz quando a distância = {n}, Empresa 2 quando a distância > {n}"
  print(t1, v1, t2, v2)
  return resposta