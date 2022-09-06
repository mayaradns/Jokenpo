import os
from jogo import *

while True:
    print()
    boas_vindas()
    sleep(0.8)
    print('\nJogando contra o computador!')
    sleep(1.0)
    cpu = cpu_escolha()
    sleep(1.0)
    print('....')
    sleep(1.0)
    resposta = pergunta()
    jogador = humano(resposta)
    sleep(1.0)
    jokenpo()
    ganhador = verifica(cpu, jogador)
    sleep(1.0)
    print(f'\033[41mComputador: {cpu}\033[m')
    print(f'\033[41mVocê: {jogador}\033[m')
    sleep(0.8)
    print(f'\n####    \033[34;44m{ganhador}\033[m    #####\n')
    novamente = input('Jogar novamente s, n? ').lower().strip()
    if novamente == 's':
        os.system('cls' if os.name == 'nt' else 'clear') # limpa a tela
        continue
    else:
        print('** FIM DE JOGO!!! **')
        break
