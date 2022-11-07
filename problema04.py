'''
Dada um texto qualquer e um lista de termos de pesquisa (sequencia de caracteres), retorne os primeiros K termos mais recorrentes na string, onde K é um parâmetro configurável.

Exemplo:

String: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua"

Lista de termos: ["a", "em", "i", "el"]

K: 2

Resultado: ["i", "a"]

Explicação:

Ocorrências de cada termo,"i": 11, "a": 7, "em": 2, "el": 1, com K = 2, retornamos "i" e "a" ordenados conforme a quantidade de ocorrências de cada termo.

Obs: Quando houver termos com quantidades iguais, priorizar o retorno de acordo com a ordem de ocorrência do termo na string.
'''
def calcula_top_ocorrencias_de_queries(texto,queries,k):
    lista = []
    dados = []
    for i in range(len(queries)):
      dados.append([])
      for j in range(len(texto)):
        if texto[j:len(queries[i])+j] == queries[i]:
          dados[i].append(j)
          break
      dados[i].append(texto.count(queries[i]))
      dados[i].append(queries[i])
    dados.sort()
    for i in range(len(dados)):
      del dados[i][0]
      print(dados[i])
    dados.sort(reverse = True)
    for i in range(k):
      lista.append(dados[i][1])
    return lista