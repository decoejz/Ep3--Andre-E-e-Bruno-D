# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 07:07:47 2016

@author: Bruno Dratcu
"""

#EP3

class Jogo:
    """Classe que representa o gerenciamento do jogo"""
    
    def __init__(self, recebe_jogada, verifica_ganhador, limpa_jogadas, off):
        self.recebe_jogada = recebe_jogada
        self.verifica_ganhador = verifica_ganhador
        self.limpa_jogadas = limpa_jogadas
        self.off = off