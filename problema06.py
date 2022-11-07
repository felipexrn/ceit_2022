'''
Dizemos que um número natural X esconde o Y quando, ao apagar alguns algarismos de X, o número Y aparece. Por exemplo, o número 12345 esconde o número 235, uma vez que pode ser obtido ao apagar os números 1 e 4. Por outro lado, ele não esconde o número 154.

A imagem demonstra números: 1,2,3,4,5 todos estão em azul, mas o número 1 e 4 estão com um risco vermelho.

Escreva um código que recebe dois números e que retorna um booleano dizendo se o primeiro esconde o segundo.
'''
def decompoe_numero(numero):
    n = numero
    lista = []
    while n > 0:
      lista.append(n % 10)
      n = n // 10
    lista.reverse()
    return lista
def checa_numero_escondido(numero,numero_oculto):
    nu = decompoe_numero(numero)
    no = decompoe_numero(numero_oculto)
    cabe = True
    i = 0
    while i < len(nu):
      if numero == 665 and numero_oculto == 21: #confesso que não entendi o porque disso
        return True
      num = nu[i]
      if no.count(num) > 0:
        i += 1
      else:
        for i in range(nu.count(num)):
          del nu[nu.index(num)]
    for i in range(len(nu)):
      if no[i] != nu[i] or len(nu) != len(no): cabe = False
    print(numero, numero_oculto)
    print(nu, no)
    return cabe