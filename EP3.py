# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 07:07:47 2016

@author: Bruno Dratcu
"""

#EP3

import numpy as np

#Legenda:
#0 = Espaço Vazio
#1 = X
#2 = O

class Jogo:
    
    def __init__(self):
        #Criando o tabuleiro
        self.tabuleiro = np.zeros([3,3])
        #Criando o jogador e iniando com X
        self.jogador = 1
        
    def recebe_jogada(self,linha,coluna):
        #Igualando a jogada ao local do tabuleiro
        self.tabuleiro[linha][coluna] = self.jogador
        #Alternando o jogador
        if self.tabuleiro[linha][coluna] == 1:
            self.jogador = 2
        elif self.tabuleiro[linha][coluna] == 2:
            self.jogador = 1
    
    def verifica_ganhador(self):
        #Todas as possibilidades de vencer o jogo
        if self.tabuleiro[0][0] == self.tabuleiro[0][1] and self.tabuleiro[0][1] == self.tabuleiro[0][2]:
            if self.tabuleiro[0][0] == 1:
                return 1
            elif self.tabuleiro[0][0] == 2:
                return 2
    
        elif self.tabuleiro[1][0] == self.tabuleiro[1][1] and self.tabuleiro[1][1] == self.tabuleiro[1][2]:
            if self.tabuleiro[1][0] == 1:
                return 1
            elif self.tabuleiro[1][0] == 2:
                return 2
                
        elif self.tabuleiro[2][0] == self.tabuleiro[2][1] and self.tabuleiro[2][1] == self.tabuleiro[2][2]:
            if self.tabuleiro[2][0] == 1:
                return 1
            elif self.tabuleiro[2][0] == 2:
                return 2
                
        elif self.tabuleiro[0][0] == self.tabuleiro[1][0] and self.tabuleiro[1][0] == self.tabuleiro[2][0]:
            if self.tabuleiro[0][0] == 1:
                return 1
            elif self.tabuleiro[0][0] == 2:
                return 2
                
        elif self.tabuleiro[0][1] == self.tabuleiro[1][1] and self.tabuleiro[1][1] == self.tabuleiro[2][1]:
            if self.tabuleiro[0][1] == 1:
                return 1
            elif self.tabuleiro[0][1] == 2:
                return 2
                
        elif self.tabuleiro[0][2] == self.tabuleiro[1][2] and self.tabuleiro[1][2] == self.tabuleiro[2][2]:
            if self.tabuleiro[1][2] == 1:
                return 1
            elif self.tabuleiro[1][2] == 2:
                return 2
                
        elif self.tabuleiro[0][0] == self.tabuleiro[1][1] and self.tabuleiro[1][1] == self.tabuleiro[2][2]:
            if self.tabuleiro[1][1] == 1:
                return 1
            elif self.tabuleiro[1][1] == 2:
                return 2
        
        elif self.tabuleiro[0][2] == self.tabuleiro[1][1] and self.tabuleiro[1][1] == self.tabuleiro[2][0]:
            if self.tabuleiro[1][1] == 1:
                return 1
            elif self.tabuleiro[1][1] == 2:
                return 2
                
        for linha in range(self.tabuleiro.shape[0]):
            for coluna in range(self.tabuleiro.shape[1]):
                if self.tabuleiro[linha,coluna] == 0:
                    return -1
        return 0
    
    def limpa_jogadas(self):
        #Reinicio o tabuleiro e define o primeiro jogador.
        self.tabuleiro = np.zeros([3,3])
        self.jogador = 1