# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 17:19:32 2016

@author: Andre
"""

import tkinter as tk

class jogo_da_velha:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Jogo da Velha')
        self.window.geometry("300x350+525+220")
        
        #Criando as linhas e colunas do jogo
        self.window.rowconfigure(0, minsize=100, weight=1)
        self.window.rowconfigure(1, minsize=100, weight=1)
        self.window.rowconfigure(2, minsize=100, weight=1)
        self.window.rowconfigure(3, minsize=50, weight=1)
        
        self.window.columnconfigure(0, minsize=100, weight=1)
        self.window.columnconfigure(1, minsize=100, weight=1)
        self.window.columnconfigure(2, minsize=100, weight=1)

#        self.window.frame(borderwidth=10)
        
        #Criando os nove botões do jogo
        self.botao1 = tk.Button(self.window)
        self.botao1.configure(text='')
        self.botao1.grid(row=0,column=0, sticky='nsew')
        
        botao2 = tk.Button(self.window)
        botao2.configure(text='2')
        botao2.grid(row=0,column=1, sticky='nsew')
        
        botao3 = tk.Button(self.window)
        botao3.configure(text='3')
        botao3.grid(row=0,column=2, sticky='nsew')

        botao4 = tk.Button(self.window)
        botao4.configure(text='4')
        botao4.grid(row=1,column=0, sticky='nsew')

        botao5 = tk.Button(self.window)
        botao5.configure(text='5')
        botao5.grid(row=1,column=1, sticky='nsew')

        botao6 = tk.Button(self.window)
        botao6.configure(text='6')
        botao6.grid(row=1,column=2, sticky='nsew')

        botao7 = tk.Button(self.window)
        botao7.configure(text='7')
        botao7.grid(row=2,column=0, sticky='nsew')
        
        botao8 = tk.Button(self.window)
        botao8.configure(text='8')
        botao8.grid(row=2,column=1, sticky='nsew')

        botao9 = tk.Button(self.window)
        botao9.configure(text='9')
        botao9.grid(row=2,column=2, sticky='nsew')

        #Criando a caixa de texto que mostrará a próxima jogada
        self.proximo_jogador = tk.StringVar()        
        jogador = tk.Label(self.window)
        jogador.configure(textvariable = self.proximo_jogador)
        jogador.grid(row=3, sticky='w', columnspan = 3)
        
        #Fazendo a jogada:
        self.botao1.bind("<Button-1>", self.clicar_botao)
        botao2.bind("<Button-1>", self.clicar_botao)
        botao3.bind("<Button-1>", self.clicar_botao)
        botao4.bind("<Button-1>", self.clicar_botao)
        botao5.bind("<Button-1>", self.clicar_botao)
        botao6.bind("<Button-1>", self.clicar_botao)
        botao7.bind("<Button-1>", self.clicar_botao)
        botao8.bind("<Button-1>", self.clicar_botao)
        botao9.bind("<Button-1>", self.clicar_botao)


    def iniciar(self):
        self.window.mainloop()
        self.proximo_jogador.set('Próxima jogada: X')
        
    def proxima_jogada(self):
        self.jogador = 'X'
        self.proximo_jogador.set('Próxima jogada: {0}'.format(self.jogador))
        if '<Button-1>' == True:
            self.jogador = 'O'
            self.proximo_jogador.set('Próxima jogada: {0}'.format(self.jogador))

    def clicar_botao(self, event, botao):
        self.proxima_jogada()
        self.transforma_botao_label(self.botao)
        
    def transforma_botao_label(self,botao):
        self.botao = tk.Label(self.window)
        self.botao.configure(text='hhh')
    

jogo = jogo_da_velha()
jogo.iniciar()
