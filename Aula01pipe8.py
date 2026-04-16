"""
Docstring para Aula01PIPE8

"""

"""
Para imprimir  o poema Python:

import this

A ideia da PIP8, é que possamos escrever códigos em Ptython, de forma Pythonica, visivélmente agradavél

[1] - Indentação: 4 espaços por nível de indentação
[2] - Linhas em branco: Separar funções e classes com duas linhas em branco e métodos dentro de uma classe com uma linha em branco
[3] - Comprimento máximo da linha: 79 caracteres            
[4] - Quebras de linha: Quebrar linhas longas usando parênteses, colchetes ou chaves
[5] - Espaços em branco: Evitar espaços em branco desnecessários em expressões e instruções
[6] - Nomes de variáveis: Usar nomes de variáveis descritivos e seguir a convenção de nomenclatura (snake_case para variáveis e funções, CamelCase para classes)                
[7] - Comentários: Escrever comentários claros e concisos para explicar o código        
[8] - Docstrings: Usar docstrings para documentar funções, classes e módulos    
[9] - Importações: Importar módulos em linhas separadas e seguir a ordem de importação (bibliotecas padrão, bibliotecas de terceiros, módulos locais)
[10] - Evitar código redundante: Evitar duplicação de código e usar funções para reutilizar código quando necessário    
[11] - Evitar o uso de caracteres especiais: Evitar o uso de caracteres especiais em nomes de variáveis e funções, como acentos, cedilhas e outros caracteres não ASCII
[12] - Evitar o uso de palavras reservadas: Evitar o uso de palavras reservadas do Python como nomes de variáveis ou funções
[13] - Evitar o uso de variáveis globais: Evitar o uso de variáveis globais e preferir o uso de parâmetros e retornos de funções para compartilhar dados entre diferentes partes do código      
[14] - Evitar o uso de funções aninhadas: Evitar o uso de funções aninhadas, a menos que seja necessário para encapsular uma funcionalidade específica  
[15] - Evitar o uso de variáveis mutáveis como valores padrão: Evitar o uso de variáveis mutáveis, como listas ou dicionários, como valores padrão em funções, pois isso pode levar a comportamentos inesperados
[16] - Evitar o uso de expressões lambda complexas: Evitar o uso de expressões lambda complexas e preferir a definição de funções nomeadas para melhorar a legibilidade do código
[17] - Evitar o uso de loops aninhados: Evitar o uso de loops aninhados, a menos que seja necessário para resolver um problema específico, pois isso pode tornar o código difícil de ler e entender
[18] - Evitar o uso de variáveis temporárias desnecessárias: Evitar o uso de variáveis temporárias desnecessárias e preferir a utilização de expressões diretas para melhorar a clareza do código
[19] - Evitar o uso de funções com muitos parâmetros: Evitar o uso de funções com muitos parâmetros e preferir a utilização de objetos ou dicionários para agrupar dados relacionados
[20] - Evitar o uso de funções com muitos níveis de indentação: Evitar o uso de funções com muitos níveis de indentação e preferir a divisão do código em funções menores para melhorar a legibilidade e a manutenção do código
[21] - Evitar o uso de variáveis com nomes genéricos: Evitar o uso de variáveis com nomes genéricos, como "data" ou "info", e preferir nomes mais específicos que descrevam claramente o propósito da variável
[22] - Em caso de muitos imports, de um mesmo pacote, recomenda-se fazer:

from types import (
    FunctionType,
    LambdaType,
    GeneratorType,
    CoroutineType,
    AsyncGeneratorType
)

[23] - Imports devem ser colocados no topo do arquivo, logo após quaisquer comentários ou docstrings e antes de constantes ou variáveis globais

"""

print("Senhor venha nos socorrer !!!")

if 'a' in 'banana':
    print("Tem a letra a")  
else:
    print("Não tem a letra a")


if 'p' in 'python':
    print("Tem a letra p")  
else:
    print("Não tem a letra p")


if 'm' in 'Thamires':
    print("Tem a letra m")  
else:
    print("Não tem a letra m")

if 'g' in 'gargulho':
    print("Tem a letra g") 
else:
    print("Não tem a letra g")  


# Refatorando o código acima, usando a função def verificar_letra(letra, palavra):

def verificar_letra(letra, palavra):
    if letra in palavra:
        print(f"Tem a letra {letra}")  
    else:
        print(f"Não tem a letra {letra}")   
verificar_letra('a', 'banana')
verificar_letra('p', 'python')          
verificar_letra ('m', 'Thamires')
verificar_letra('g', 'gargulho')    
verificar_letra('j', 'jesus')


def verifica_idade(idade):
    if idade >= 18:
        print("Você é maior de idade")  
    else:
        print("Você é menor de idade")

verifica_idade(2)






