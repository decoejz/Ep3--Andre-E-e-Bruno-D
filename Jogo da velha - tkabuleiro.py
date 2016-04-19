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
        self.botao1 = tk.Button(self.window, borderwidth=3)
        #self.botao1.configure(text='1')
        self.botao1.grid(row=0,column=0, sticky='nsew')
        
        self.botao2 = tk.Button(self.window)
        #self.botao2.configure(text='2')
        self.botao2.grid(row=0,column=1, sticky='nsew')
        
        self.botao3 = tk.Button(self.window)
        #self.botao3.configure(text='3')
        self.botao3.grid(row=0,column=2, sticky='nsew')

        self.botao4 = tk.Button(self.window)
        #self.botao4.configure(text='4')
        self.botao4.grid(row=1,column=0, sticky='nsew')

        self.botao5 = tk.Button(self.window)
        #self.botao5.configure(text='5')
        self.botao5.grid(row=1,column=1, sticky='nsew')

        self.botao6 = tk.Button(self.window)
        #self.botao6.configure(text='6')
        self.botao6.grid(row=1,column=2, sticky='nsew')

        self.botao7 = tk.Button(self.window)
        #self.botao7.configure(text='7')
        self.botao7.grid(row=2,column=0, sticky='nsew')
        
        self.botao8 = tk.Button(self.window)
        #self.botao8.configure(text='8')
        self.botao8.grid(row=2,column=1, sticky='nsew')

        self.botao9 = tk.Button(self.window)
        #self.botao9.configure(text='9')
        self.botao9.grid(row=2,column=2, sticky='nsew')

        #Criando a caixa de texto que mostrará a próxima jogada
        self.proximo_jogador = tk.StringVar()        
        jogador = tk.Label(self.window)
        jogador.configure(textvariable = self.proximo_jogador)
        jogador.grid(row=3, sticky='w', columnspan = 3)
        
        #Fazendo a jogada:
        self.botao1.bind(self.clicar_botao('<Button-1>',self.botao1))
        self.botao2.bind(self.clicar_botao('<Button-1>',self.botao2))
        self.botao3.bind(self.clicar_botao('<Button-1>',self.botao3))
        self.botao4.bind(self.clicar_botao('<Button-1>',self.botao4))
        self.botao5.bind(self.clicar_botao('<Button-1>',self.botao5))
        self.botao6.bind(self.clicar_botao('<Button-1>',self.botao6))
        self.botao7.bind(self.clicar_botao('<Button-1>',self.botao7))
        self.botao8.bind(self.clicar_botao('<Button-1>',self.botao8))
        self.botao9.bind(self.clicar_botao('<Button-1>',self.botao9))

        #O número 1 equivale ao jogador x
        #O número 2 equivale ao jogador O
        self.jogador = 1

    def iniciar(self):
        self.window.mainloop()
        self.jogador = 1
        #self.proxima_jogada(self.jogador)
        
    def proxima_jogada(self):
        self.jogador = 1
        if self.jogador == 1:
            self.proximo_jogador.set('Próxima jogada: X'.format(self.jogador))
            self.jogador += 1
        elif self.jogador == 2:
            self.proximo_jogador.set('Próxima jogada: O'.format(self.jogador))
            self.jogador -= 1

    def clicar_botao(self, event, botao):
        self.transforma_botao_label(botao)
        self.proxima_jogada()
        #self.transforma_botao_label(self.botao)
        
        
    def transforma_botao_label(self,botao):
        self.botao = tk.Label(self.window)
        self.botao.configure(text='hhh')
    
    #Muitas coisas para serem alteradas!!!!
    #Descobrir como alterar o texto do botão e como transformar um botão em label
    #Descobrir como colocar bordas!
    
    

jogo = jogo_da_velha()
jogo.iniciar()