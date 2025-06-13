## Python para Trabalhar com Dados - Guia Simples 

# 1. Trabalhando com Listas


# Uma lista armazena vários valores em uma única variável
nomes_personagens = ["Goku",
                     "Vegeta",
                     "Piccolo",
                     "Mestre Kame",
                     "Bulma",
                     "Gohan",
                     "Freeza",
                     "Mestre Karin",
                     "Androide 16",
                     "Androide 17",
                     "Goten"]

idades_personagens = [33,34,39,71,36,21,55,78,34,35,23]



# Imprimindo a lista com os nomes dos personagens
print(nomes_personagens)



# Acessar valores
print("Lista de nomes:", nomes_personagens[2])



# Adicionando elementos
nomes_personagens.append("Céu")
print(nomes_personagens)
nomes_personagens.append("Rick")
print(nomes_personagens)



# Removendo elementos
nomes_personagens.remove("Rick")
print(nomes_personagens)



