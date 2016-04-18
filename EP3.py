# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 07:07:47 2016

@author: Bruno Dratcu
"""

#EP3

import numpy as np

class Jogo:
    """Classe que representa o gerenciamento do jogo"""
    
    def __init__(self, X, O, vazio, tabuleiro, turn):
        self.X = X
        self.O = O
        self.vazio = vazio
        self.tabuleiro = tabuleiro
        self.turn = turn
        
    def tabuleiro(self):
        self.tabuleiro = np.zeros([3,3])
        for i in range(1,10):
            self.X
        
         
    def verifica_ganhador(self):
        if self.tabuleiro == self.vazio:
            print("Empate!")
        elif self.X == [0,1,2] or self.X == [3,4,5] or self.X == [6,7,8] or self.X == [0,3,6] or self.X == [1,4,7] or self.X == [2,5,8] or self.X == [0,4,8] or self.X == [2,4,6]:
            print("O jogador X venceu!")
        elif self.O == [0,1,2] or self.O == [3,4,5] or self.O == [6,7,8] or self.O == [0,3,6] or self.O == [1,4,7] or self.O == [2,5,8] or self.O == [0,4,8] or self.O == [2,4,6]:
            print("O jogador O venceu!")
        
    def troca_usuario(self):
        while True:
#            if self.X == 
#        self.X = True
        
#    def recebe_jogada(self):
#        while True:
#            jogada = 1
#            while 1 <= 10:
#                self.X.append(self.tabuleiro)
#                self.O.append(self.tabuleiro)
#                self.X += 1
#                self.O += 1
#        break
#        