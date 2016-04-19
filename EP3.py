# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 07:07:47 2016

@author: Bruno Dratcu
"""

#EP3

import numpy as np
from sys import exit

class Jogo:
    """Classe que representa o gerenciamento do jogo"""
    
#    def __init__(self, X, O, vazio, tabuleiro, turn):
    def __init__(self, tabuleiro):
#        self.X = X
#        self.O = O
#        self.vazio = vazio
        self.tabuleiro = tabuleiro
#        self.turn = turn
        
        
      #função na qual cria o tabuleiro 'zerado' e ocorre um reset após ultima jogada
    def limpa_jogada(self):
        self.tabuleiro = np.zeros([3,3])
        #k e l estão com valores genéricos para poder entrar na função
        #Quando entrarem na função seus valores serão alterados        
        linha=0
        coluna=0
        self.recebe_jogada(linha, coluna)
        print(self.tabuleiro)
        if self.recebe_jogada:
            pergunta_reset = str(input("Deseja jogar novamente? "))
            if pergunta_reset == "sim" or pergunta_reset == "Sim" or pergunta_reset == "SIM":
                print(velha.limpa_jogada)
            elif pergunta_reset == "nao" or pergunta_reset == "Nao" or pergunta_reset == "não" or pergunta_reset == "Não":
                print("Obrigado por jogar!")
                exit (0)
            else:
                print("Desculpe, não entendi, por isso vou embora...")
                exit (0)
            
        
      #função na qual o jogador escolhe qual posição irá assinalar,
      #sendo que, as posições, de 1 a 9, são as posições de uma matriz
    def pergunta_jogada(self):
        posicao = int(input("Onde deseja jogar? ")) #onde deseja colocar X ou O
        if posicao == 1:
            linha = 0 
            coluna = 0  
            return (linha, coluna)

        elif posicao == 2:
            linha = 0
            coluna = 1
            return (linha, coluna)
        elif posicao == 3:
            linha = 0
            coluna = 2
            return (linha, coluna)
        elif posicao == 4:
            linha = 1
            coluna = 0
            return (linha, coluna)
            
        elif posicao == 5:
            linha = 1
            coluna = 1
            return (linha, coluna)
        elif posicao == 6:
            linha = 1
            coluna = 2
            return (linha, coluna)
        elif posicao == 7:
            linha = 2
            coluna = 0
            return (linha, coluna)
        elif posicao == 8:
            linha = 2
            coluna = 1
            return (linha, coluna)
        elif posicao == 9:
            linha = 2
            coluna = 2
            return (linha, coluna)
        else:
            print("Escolha um numero de 1 a 9!")
            print("Por culpa desse bug, preciso recomeçar...")
            print(velha.limpa_jogada)
            
     #função na qual troca de jogador a cada rodada
    def recebe_jogada(self, linha, coluna):
        Troca_de_jogador = 1
        for i in range(10):
            if Troca_de_jogador == 1: 
                linha, coluna = self.pergunta_jogada()
                self.tabuleiro[linha,coluna] = 1
                continuacao = self.verifica_ganhador()
                if not continuacao == -1:
                    print(self.tabuleiro)
                    break
                Troca_de_jogador += 1
                print(self.tabuleiro)
            elif Troca_de_jogador == 2:
                linha, coluna = self.pergunta_jogada()
                self.tabuleiro[linha,coluna] = 2
                continuacao = self.verifica_ganhador()
                if not continuacao == -1:
                    print(self.tabuleiro)
                    break
                Troca_de_jogador -= 1
                print(self.tabuleiro)
                
     #funçao na qual é verificado caso o jogador venceu, perdeu ou empatou           
    def verifica_ganhador(self):
        if self.tabuleiro[0,0] == self.tabuleiro[0,1] and self.tabuleiro[0,1] == self.tabuleiro[0,2]:
            if self.tabuleiro[0,0] == 1:
                return 1
            elif self.tabuleiro[0,0] == 2:
                return 2
    
        elif self.tabuleiro[1,0] == self.tabuleiro[1,1] and self.tabuleiro[1,1] == self.tabuleiro[1,2]:
            if self.tabuleiro[1,0] == 1:
                return 1
            elif self.tabuleiro[1,0] == 2:
                return 2
                
        elif self.tabuleiro[2,0] == self.tabuleiro[2,1] and self.tabuleiro[2,1] == self.tabuleiro[2,2]:
            if self.tabuleiro[2,0] == 1:
                return 1
            elif self.tabuleiro[2,0] == 2:
                return 2
                
        elif self.tabuleiro[0,0] == self.tabuleiro[1,0] and self.tabuleiro[1,0] == self.tabuleiro[2,0]:
            if self.tabuleiro[0,0] == 1:
                return 1
            elif self.tabuleiro[0,0] == 2:
                return 2
                
        elif self.tabuleiro[0,1] == self.tabuleiro[1,1] and self.tabuleiro[1,1] == self.tabuleiro[2,1]:
            if self.tabuleiro[0,1] == 1:
                return 1
            elif self.tabuleiro[0,1] == 2:
                return 2
                
        elif self.tabuleiro[0,2] == self.tabuleiro[1,2] and self.tabuleiro[1,2] == self.tabuleiro[2,2]:
            if self.tabuleiro[1,2] == 1:
                return 1
            elif self.tabuleiro[1,2] == 2:
                return 2
                
        elif self.tabuleiro[0,0] == self.tabuleiro[1,1] and self.tabuleiro[1,1] == self.tabuleiro[2,2]:
            if self.tabuleiro[1,1] == 1:
                return 1
            elif self.tabuleiro[1,1] == 2:
                return 2
                
        elif self.tabuleiro[0,2] == self.tabuleiro[1,1] and self.tabuleiro[1,1] == self.tabuleiro[2,0]:
            if self.tabuleiro[1,1] == 1:
                return 1
            elif self.tabuleiro[1,1] == 2:
                return 2
                
        for linha in range(self.tabuleiro.shape[0]):
            for coluna in range(self.tabuleiro.shape[1]):
                if self.tabuleiro[linha,coluna] == 0:
                    return -1
        return 0
                
    
    
matriz = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(matriz)
print ('Para jogar escreve o numero onde deseja fazer a jogada!')
velha = Jogo(np.zeros([3,3]))
velha.limpa_jogada()