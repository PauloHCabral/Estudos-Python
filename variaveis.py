media = 0
n1 = n2 = n3 = n4 = 0.0
nome, idade = 'Paulo Henrique', 32
print(nome,idade)
estado = True


# Função type() # a função type mostra que tipo ela é, soma, inteiro, string
print(type(media))
print(type(n1))
print(type(nome))
print(type(idade))
print(type(estado))
print(type(1+2j))


# Função isinstance() É uma ocorrência de terminado tipo ou classe, ela retorna verdadeiro se o valor for verdadeiro, ou falso.

a = 10
b = 'sol'
print(isinstance(a, int))
print(isinstance(b, int)) # Aqui ele fala que o valor é Falso, porque na variavel b, o valor não é um número inteiro, mas sim uma string #

d = 'vida'
print(isinstance(d, (int, float))) # Aqui, podemos verificar com duas operações se o valor corresponde a inteiro ou float, ele retornou falso, porque dentro da variavel d, está uma string chamada 'vida'


