from random import choice
from time import sleep


def boas_vindas():
    print('=-' * 18)
    print('       \033[32mBem vindo ao jogo!!!\033[m')
    print('          \033[32m** Jokenpô **\033[m')
    print('=-' * 18)


def cpu_escolha():
    '''Escolha da cpu feita aleatoriamente'''
    print('CPU escolhendo...')
    cpu_escolhe = choice(['PEDRA', 'PAPEL', 'TESOURA'])
    return cpu_escolhe


def pergunta():
    '''Pergunta feita ao jogador humano'''
    escolha = int(input('Faça sua escolha, digite o número correspondente:\n1- Pedra, 2 - Papel ou 3 - Tesoura: '))
    return escolha


def humano(escolha):
    '''Escolha do jogador humano'''
    resposta = ''
    if escolha == 1:
        resposta = 'PEDRA'
    elif escolha == 2:
        resposta = 'PAPEL'
    elif escolha == 3:
        resposta = 'TESOURA'
    else:
        print('Opção inválida, escolha novamente.')
        pergunta()
    return resposta


def verifica(cpu_escolhe, human):
    '''Verifica quem venceu a partida'''
    vitoria = ''
    if cpu_escolhe == human:
        vitoria = 'Empate!!!'
    elif cpu_escolhe == 'PEDRA' and human == 'TESOURA':
        vitoria = 'O computador venceu!'
    elif cpu_escolhe == 'PEDRA' and human == 'PAPEL':
        vitoria = 'Aêêê!!! Você venceu!!!'
    elif cpu_escolhe == 'TESOURA' and human == 'PAPEL':
        vitoria = 'O computador venceu!'
    elif cpu_escolhe == 'TESOURA' and human == 'PEDRA':
        vitoria = 'Aêêê!!! Você venceu!!!'
    elif cpu_escolhe == 'PAPEL' and human == 'PEDRA':
        vitoria = 'O computador venceu!'
    elif cpu_escolhe == 'PAPEL' and human == 'TESOURA':
        vitoria = 'Aêêê!!! Você venceu!!!'
    return vitoria


def jokenpo():
    '''Imprime Jokenpô na tela'''
    print('\033[1;34m     JO\033[m\n')
    sleep(1.0)
    print('\033[1;34m     KEN\033[m\n')
    sleep(1.0)
    print('\033[1;34m     PÔ!!!\033[m\n')
    sleep(1.0)
