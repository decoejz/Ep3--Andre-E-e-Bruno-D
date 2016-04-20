# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 07:07:47 2016

@author: Bruno Dratcu
"""

#EP3

import numpy as np


class Jogo:
    """Classe que representa o gerenciamento do jogo"""
    
    def __init__(self, tabuleiro,jogador):
        self.tabuleiro = tabuleiro
        self.jogador = jogador
        self.tabuleiro = np.zeros([3,3])        
        
        
      #função na qual cria o tabuleiro 'zerado' e ocorre um reset após ultima jogada
    def limpa_jogada(self):
        #self.tabuleiro = np.zeros([3,3])
        return (np.zeros([3,3]))

            
     #função na qual troca de jogador a cada rodada
    def recebe_jogada(self, linha, coluna):
#       self.tabuleiro = self.limpa_jogada()
        if self.jogador == 1: 
            self.tabuleiro[linha][coluna]=self.jogador
            continuacao = self.verifica_ganhador()
            if not continuacao == -1:
                self.jogador += 1

        elif self.jogador == 2:
            self.tabuleiro[linha][coluna]=self.jogador
            continuacao = self.verifica_ganhador()
            if not continuacao == -1:
                self.jogador -= 1
        print(self.tabuleiro,'\n')

                
                
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

