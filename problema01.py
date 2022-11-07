'''
Você e seu time estão desenvolvendo um sistema de indicações de postos de gasolina que ficam próximos da localização atual do veículo. No modo de direção “viagem”, a funcionalidade a ser desenvolvida é de indicar ao condutor o posto mais distante possível dentro do limite atual de combustível. E caso não exista posto de gasolina, retornar -1

A pessoa responsável por fazer a especificação do sistema informou que você terá as seguintes informações: consumo médio de combustível, quantidade de combustível restante no veículo e um array contendo distâncias dos postos de gasolinas.

Exemplo:
Combustivel (em litros): 2
Consumo médio (km/l): 8
Postos de Gasolina (km): [2, 15, 22, 10.2]
'''
def ultima_parada(combustivel,consumo,postos_de_gasolina):
  pass
  alcance = combustivel * consumo
  posto = -1
  postos_de_gasolina.sort()
  if postos_de_gasolina[-1] <= alcance:
    posto = postos_de_gasolina[-1]
  elif postos_de_gasolina[0] > alcance:
    posto = -1
  else:
    for i in range(len(postos_de_gasolina)):
      if postos_de_gasolina[i] > alcance:
        posto = postos_de_gasolina[i-1]
        break
  return posto