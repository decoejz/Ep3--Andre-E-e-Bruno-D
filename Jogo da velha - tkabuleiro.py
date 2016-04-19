# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 17:19:32 2016

@author: Andre
"""

import tkinter as tk
#Importando o código do jogo
import EP3

class jogo_da_velha:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Jogo da Velha')
        self.window.geometry("300x350+550+70")
        
        #Criando as linhas e colunas do jogo
        self.window.rowconfigure(0, minsize=100, weight=1)
        self.window.rowconfigure(1, minsize=100, weight=1)
        self.window.rowconfigure(2, minsize=100, weight=1)
        self.window.rowconfigure(3, minsize=50, weight=1)
        
        self.window.columnconfigure(0, minsize=100, weight=1)
        self.window.columnconfigure(1, minsize=100, weight=1)
        self.window.columnconfigure(2, minsize=100, weight=1)
        
        
        self.jogod = EP3.Jogo(self.iniciar)
        
        
        #Criando os nove botões do jogo
        self.botao1 = tk.Button(self.window, borderwidth=3)
        self.botao1.grid(row=0,column=0, sticky='nsew')
        
        self.botao2 = tk.Button(self.window)
        self.botao2.grid(row=0,column=1, sticky='nsew')
        
        self.botao3 = tk.Button(self.window)
        self.botao3.grid(row=0,column=2, sticky='nsew')

        self.botao4 = tk.Button(self.window)
        self.botao4.grid(row=1,column=0, sticky='nsew')

        self.botao5 = tk.Button(self.window)
        self.botao5.grid(row=1,column=1, sticky='nsew')

        self.botao6 = tk.Button(self.window)
        self.botao6.grid(row=1,column=2, sticky='nsew')

        self.botao7 = tk.Button(self.window)
        self.botao7.grid(row=2,column=0, sticky='nsew')
        
        self.botao8 = tk.Button(self.window)
        self.botao8.grid(row=2,column=1, sticky='nsew')

        self.botao9 = tk.Button(self.window)
        self.botao9.grid(row=2,column=2, sticky='nsew')

        #Criando a caixa de texto que mostrará a próxima jogada
        self.proximo_jogador = tk.StringVar()        
        jogador = tk.Label(self.window)
        jogador.configure(textvariable = self.proximo_jogador)
        jogador.grid(row=3, sticky='w', columnspan = 3)
        
                
        #Fazendo a jogada:
        self.botao1.bind('<Button-1>',self.clicar_botao_1)
        self.botao2.bind('<Button-1>',self.clicar_botao_2)
        self.botao3.bind('<Button-1>',self.clicar_botao_3)
        self.botao4.bind('<Button-1>',self.clicar_botao_4)
        self.botao5.bind('<Button-1>',self.clicar_botao_5)
        self.botao6.bind('<Button-1>',self.clicar_botao_6)
        self.botao7.bind('<Button-1>',self.clicar_botao_7)
        self.botao8.bind('<Button-1>',self.clicar_botao_8)
        self.botao9.bind('<Button-1>',self.clicar_botao_9)


    def iniciar(self):
        self.window.mainloop()
        self.proxima_jogada(1)
        
#    def proxima_jogada(self,jogador):
#        self.jogod.verifica_ganhador()

    def clicar_botao_1(self, event):
        self.botao1 = tk.Label(self.window)
        self.jogada_feita = self.jogod.recebe_jogada(0,0)
        if self.jogada_feita == 1:
            self.botao1.configure(text = 'X')
        elif self.jogada_feita == 2:
            self.botao1.configure(text='O')
        print ('oi')
        
    def clicar_botao_2(self, event):
        self.botao2 = tk.Label(self.window)
        self.botao2.config(text='X')
        self.jogada_feita = self.jogod.recebe_jogada(0,1)
        if self.jogada_feita == 1:
            self.botao1.configure(text = 'X')
        elif self.jogada_feita == 2:
            self.botao1.configure(text='O')

        self.proxima_jogada()
        print ('oi')
        
        
    def clicar_botao_3(self, event):
        self.botao3 = tk.Label(self.window)
        self.botao3.configure(text='X')
        self.jogada_feita = self.jogod.recebe_jogada(0,2)
        if self.jogada_feita == 1:
            self.botao1.configure(text = 'X')
        elif self.jogada_feita == 2:
            self.botao1.configure(text='O')

        self.proxima_jogada()
        print ('oi')
        
    def clicar_botao_4(self, event):
        self.botao4 = tk.Label(self.window)
        self.botao4.configure(text='X')
        self.jogada_feita = self.jogod.recebe_jogada(1,0)
        if self.jogada_feita == 1:
            self.botao1.configure(text = 'X')
        elif self.jogada_feita == 2:
            self.botao1.configure(text='O')

        self.proxima_jogada()
        print ('oi')
        
    def clicar_botao_5(self, event):
        self.botao5 = tk.Label(self.window)
        self.botao5.configure(text='X')
        self.jogada_feita = self.jogod.recebe_jogada(1,1)
        if self.jogada_feita == 1:
            self.botao1.configure(text = 'X')
        elif self.jogada_feita == 2:
            self.botao1.configure(text='O')

        self.proxima_jogada()
        print ('oi')
        
    def clicar_botao_6(self, event):
        self.botao6 = tk.Label(self.window)
        self.botao6.configure(text='X')
        self.jogada_feita = self.jogod.recebe_jogada(1,2)
        if self.jogada_feita == 1:
            self.botao1.configure(text = 'X')
        elif self.jogada_feita == 2:
            self.botao1.configure(text='O')

        self.proxima_jogada()
        print ('oi')
        
    def clicar_botao_7(self, event):
        self.botao7 = tk.Label(self.window)
        self.botao7.configure(text='X')
        self.jogada_feita = self.jogod.recebe_jogada(2,0)
        if self.jogada_feita == 1:
            self.botao1.configure(text = 'X')
        elif self.jogada_feita == 2:
            self.botao1.configure(text='O')

        self.proxima_jogada()
        print ('oi')
        
    def clicar_botao_8(self, event):
        self.botao8 = tk.Label(self.window)
        self.botao8.configure(text='X')
        self.jogada_feita = self.jogod.recebe_jogada(2,1)
        if self.jogada_feita == 1:
            self.botao1.configure(text = 'X')
        elif self.jogada_feita == 2:
            self.botao1.configure(text='O')

        #self.proxima_jogada()
        print ('oi')
        
    def clicar_botao_9(self, event):
        self.botao9 = tk.Label(self.window)
        self.botao9.configure(text='X')
        self.jogada_feita = self.jogod.recebe_jogada(2,2)
        if self.jogada_feita == 1:
            self.botao1.configure(text = 'X')
        elif self.jogada_feita == 2:
            self.botao1.configure(text='O')
        self.proxima_jogada()
        print ('oi')
    
    #Muitas coisas para serem alteradas!!!!
    #Descobrir como alterar o texto do botão e como transformar um botão em label
    #Descobrir como colocar bordas!
    

jogo = jogo_da_velha()
jogo.iniciar()