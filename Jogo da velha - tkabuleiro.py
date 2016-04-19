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
        
    def proxima_jogada(self,jogador):
        #O número 1 equivale ao jogador x
        #O número 2 equivale ao jogador O
        if self.jogador == 1:
            self.proximo_jogador.set('Próxima jogada: X'.format(self.jogador))
            self.jogador += 1
        elif self.jogador == 2:
            self.proximo_jogador.set('Próxima jogada: O'.format(self.jogador))
            self.jogador -= 1

    def clicar_botao_1(self, event):
        self.transforma_botao_label(self.botao1)
        #self.proxima_jogada()
        print ('oi')
        
    def clicar_botao_2(self, event):
        self.transforma_botao_label(self.botao2)
        #self.proxima_jogada()
        print ('oi')
        
        
    def clicar_botao_3(self, event):
        self.transforma_botao_label(self.botao3)
        #self.proxima_jogada()
        print ('oi')
        
    def clicar_botao_4(self, event):
        self.transforma_botao_label(self.botao4)
        #self.proxima_jogada()
        print ('oi')
        
    def clicar_botao_5(self, event):
        self.transforma_botao_label(self.botao5)
        #self.proxima_jogada()
        print ('oi')
        
    def clicar_botao_6(self, event):
        self.transforma_botao_label(self.botao6)
        #self.proxima_jogada()
        print ('oi')
        
    def clicar_botao_7(self, event):
        self.transforma_botao_label(self.botao7)
        #self.proxima_jogada()
        print ('oi')
        
    def clicar_botao_8(self, event):
        self.transforma_botao_label(self.botao8)
        #self.proxima_jogada()
        print ('oi')
        
    def clicar_botao_9(self, event):
        self.transforma_botao_label(self.botao9)
        #self.proxima_jogada()
        print ('oi')
        
    def transforma_botao_label(self,botao):
        self.botao = tk.Label(self.window)
        self.botao.configure(text='X')
    
    #Muitas coisas para serem alteradas!!!!
    #Descobrir como alterar o texto do botão e como transformar um botão em label
    #Descobrir como colocar bordas!
    
    

jogo = jogo_da_velha()
jogo.iniciar()