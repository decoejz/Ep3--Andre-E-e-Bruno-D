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
        
#    def tabuleiro(self):
#        self.tabuleiro = np.zeros([3,3])
#        for i in range(1,10):
#            self.X
#        
#         
#    def verifica_ganhador(self):
#        if self.tabuleiro == self.vazio:
#            print("Empate!")
#        elif self.X == [0,1,2] or self.X == [3,4,5] or self.X == [6,7,8] or self.X == [0,3,6] or self.X == [1,4,7] or self.X == [2,5,8] or self.X == [0,4,8] or self.X == [2,4,6]:
#            print("O jogador X venceu!")
#        elif self.O == [0,1,2] or self.O == [3,4,5] or self.O == [6,7,8] or self.O == [0,3,6] or self.O == [1,4,7] or self.O == [2,5,8] or self.O == [0,4,8] or self.O == [2,4,6]:
#            print("O jogador O venceu!")
#        
#    def troca_usuario(self):
#        while True:
#            if self.X == 
#        self.X = True
#        
#    def recebe_jogada(self):
#        while True:
#            jogada = 1
#            while 1 <= 10:
#                self.X.append(self.tabuleiro)
#                self.O.append(self.tabuleiro)
#                self.X += 1
#                self.O += 1
#        break
        
    def limpa_jogada(self):
        self.tabuleiro = np.zeros([3,3])
        #k e l estão com valores genéricos para poder entrar na função
        #Quando entrarem na função seus valores serão alterados        
        k=0
        l=0
        self.recebe_jogada(k,l)
        
    def pergunta_jogada(self):
        j = int(input("Onde deseja jogar? ")) #onde deseja colocar X ou O
        if j == 1:
            k = 0             #k = linhas
            l = 0             #l = colunas
            return (k, l)

        elif j == 2:
            k = 0
            l = 1
            return (k, l)
        elif j == 3:
            k = 0
            l = 2
            return (k, l)
        elif j == 4:
            k = 1
            l = 0
            return (k, l)
            
        elif j == 5:
            k = 1
            l = 1
            return (k, l)
        elif j == 6:
            k = 1
            l = 2
            return (k, l)
        elif j == 7:
            k = 2
            l = 0
            return (k, l)
        elif j == 8:
            k = 2
            l = 1
            return (k, l)
        elif j == 9:
            k = 2
            l = 2
            return (k, l)
        else:
            print("Escolha um numero de 1 a 9!")
            

    def recebe_jogada(self, k, l):
        a = 1
        for i in range(10):
            if a == 1: 
                k, l = self.pergunta_jogada()
                self.tabuleiro[k,l] = 1
                continuacao = self.verifica_ganhador()
                if not continuacao == -1:
                    break
                a += 1
            elif a == 2:
                k, l = self.pergunta_jogada()
                self.tabuleiro[k,l] = 2
                continuacao = self.verifica_ganhador()
                if not continuacao == -1:
                    break
                a -= 1
                
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
#        ..............
        for k in range(self.tabuleiro.shape[0]):
            for l in range(self.tabuleiro.shape[1]):
                if self.tabuleiro[k,l] == 0:
                    return -1
        return 0
                
    
    
    
velha = Jogo()
velha.limpa_jogo()
#          