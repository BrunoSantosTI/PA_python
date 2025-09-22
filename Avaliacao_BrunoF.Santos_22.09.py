#!/usr/bin/env python
# coding: utf-8

# Coloque seu nome aqui:

# **Atividade Avaliativa **
# 
# Enunciado:
# 
# Crie um programa em Python para avaliar uma competição de bandas de música. O programa deve:
# 
# Perguntar a quantidade de bandas participantes (mínimo 3).
# 
# Perguntar o nome de cada banda.
# 
# Para cada banda, receber as notas de 5 jurados (valores de 0 a 10).
# 
# Calcular a média das notas de cada banda e armazenar o resultado em um dicionário, onde a chave será o nome da banda e o valor será a média das notas.
# 
# Ao final, mostrar:
# 
# A média de cada banda.
# 
# O nome da banda vencedora (a que tiver maior média).

# In[4]:


# Digite sua resposta

quantidade = int(input('Digite a quantidade de bandas participantes: '))
notas_bandas = {}

for i in range(quantidade):
    nome = input(f'\nDigite o nome da {i+1}ª banda: ')
    media = 0
    for j in range(5):
        nota = float(input(f'Digite a nota do {j+1}º jurado para {nome}: '))
        media += nota/5    
    notas_bandas[nome] = media

print('\nPontuações:')
for banda, pontos in notas_bandas.items():
    print(f'{banda}: {pontos}')

vencedora = max(notas_bandas, key = notas_bandas.get)
print(f'vecedora:{vencedora}\ncom {notas_bandas[vencedora]} pontos')


# Enunciado:
# 
# Crie um programa que conte quantas vezes cada palavra aparece em uma frase.
# 
# Pedir ao usuário para digitar uma frase
# 
# Imprimir a palavra e quantas vezes ela aparece

# In[38]:


# Digite sua resposta

frase = str(input('Digite uma frase: '))
palavras = frase.split()
contagem = {}

for palavra in palavras:
    palavra = palavra.lower()
    palavra = palavra.replace(",", "")
    palavra = palavra.replace(".", "")
    if palavra in contagem:
        contagem[palavra] += 1
        
    else:
        contagem[palavra]= 1
print(f'\nContagem de palavras:')
for palavra, qtd in contagem.items():
    print(f'{palavra}: {qtd}')


# Enunciado:
# 
# Crie um programa em python que imprima números pares
# 
# Pedir o usuário para digitar uma lista com mínimo 10 números
# 
# Criar uma nova somente com numeros pares
# 
# Imprimir números pares
# 
# 

# In[13]:


# Digite sua resposta

pares = 0
impares = 0

for i in range(0, 10):
    num = int(input(f'\nDigite o {i+1}º número: '))

    if num %2 == 0:
        print('É par')
        pares += 1
    else:
        print('Não é par')
        impares += 1
        
print(f'\nA quantidade de números pares é: ',pares)
print(f'\nA quantidade de números ímpares é: ',impares)

