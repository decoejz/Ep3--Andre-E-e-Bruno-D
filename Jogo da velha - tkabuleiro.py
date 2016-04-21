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
        self.window.geometry("300x350+600+55")
        
        #Criando as linhas e colunas do jogo
        self.window.rowconfigure(0, minsize=100, weight=1)
        self.window.rowconfigure(1, minsize=100, weight=1)
        self.window.rowconfigure(2, minsize=100, weight=1)
        self.window.rowconfigure(3, minsize=50, weight=1)
        
        self.window.columnconfigure(0, minsize=100, weight=1)
        self.window.columnconfigure(1, minsize=100, weight=1)
        self.window.columnconfigure(2, minsize=100, weight=1)
        
        
        self.jogod = EP3.Jogo()
        

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

        #Criando a caixa de texto que mostrará o próximo jogador
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
    
    #Como ao ler a função recebe_jogada o computador troca o jogador,
    #para fazer com que de certo o número do jogador com o simbolo,
    #os valores devem ser invertidos. Portanto, X passa a ter no momento em
    #que apertarmos o botão o valor de 2, e O terá o valor de 1.
    def clicar_botao_1(self, event):
        self.jogod.recebe_jogada(0,0)
        if self.jogod.jogador == 1:
            self.botao1.configure(text='O')
            self.label_proximo_jogador('X')
        elif self.jogod.jogador == 2:
            self.botao1.configure(text='X')
            self.label_proximo_jogador('O')
        
        if self.jogod.verifica_ganhador() == 1:
            print('X venceu')
        elif self.jogod.verifica_ganhador() == 2:
            print('O venceu')
        elif self.jogod.verifica_ganhador() == 0:
            print('O jogo empatou')
        
        self.botao1.configure(state='disabled')
        
        
        
    def clicar_botao_2(self, event):
        self.jogod.recebe_jogada(0,1)
        if self.jogod.jogador == 1:
            self.botao2.configure(text='O')
            self.label_proximo_jogador('X')
        elif self.jogod.jogador == 2:
            self.botao2.configure(text='X')
            self.label_proximo_jogador('O')
        
        if self.jogod.verifica_ganhador() == 1:
            print('X venceu')
        elif self.jogod.verifica_ganhador() == 2:
            print('O venceu')
        elif self.jogod.verifica_ganhador() == 0:
            print('O jogo empatou')
        
        self.botao2.configure(state='disabled')
        
    def clicar_botao_3(self, event):
        self.jogod.recebe_jogada(0,2)
        if self.jogod.jogador == 1:
            self.botao3.configure(text='O')
            self.label_proximo_jogador('X')
        elif self.jogod.jogador == 2:
            self.botao3.configure(text='X')
            self.label_proximo_jogador('O')
       
        if self.jogod.verifica_ganhador() == 1:
            print('X venceu')
        elif self.jogod.verifica_ganhador() == 2:
            print('O venceu')
        elif self.jogod.verifica_ganhador() == 0:
            print('O jogo empatou')
        
        self.botao3.configure(state='disabled')
                
    def clicar_botao_4(self, event):
        self.jogod.recebe_jogada(1,0)
        if self.jogod.jogador == 1:
            self.botao4.configure(text='O')
            self.label_proximo_jogador('X')
        elif self.jogod.jogador == 2:
            self.botao4.configure(text='X')
            self.label_proximo_jogador('O')
        
        if self.jogod.verifica_ganhador() == 1:
            print('X venceu')
        elif self.jogod.verifica_ganhador() == 2:
            print('O venceu')
        elif self.jogod.verifica_ganhador() == 0:
            print('O jogo empatou')
        
        self.botao4.configure(state='disabled')
                
    def clicar_botao_5(self, event):
        self.jogod.recebe_jogada(1,1)
        if self.jogod.jogador == 1:
            self.botao5.configure(text='O')
            self.label_proximo_jogador('X')
        elif self.jogod.jogador == 2:
            self.botao5.configure(text='X')
            self.label_proximo_jogador('O')
        
        if self.jogod.verifica_ganhador() == 1:
            print('X venceu')
        elif self.jogod.verifica_ganhador() == 2:
            print('O venceu')
        elif self.jogod.verifica_ganhador() == 0:
            print('O jogo empatou')
        
        self.botao5.configure(state='disabled')
                
    def clicar_botao_6(self, event):
        self.jogod.recebe_jogada(1,2)
        if self.jogod.jogador == 1:
            self.botao6.configure(text='O')
            self.label_proximo_jogador('X')
        elif self.jogod.jogador == 2:
            self.botao6.configure(text='X')
            self.label_proximo_jogador('O')
        
        if self.jogod.verifica_ganhador() == 1:
            print('X venceu')
        elif self.jogod.verifica_ganhador() == 2:
            print('O venceu')
        elif self.jogod.verifica_ganhador() == 0:
            print('O jogo empatou')
        
        self.botao6.configure(state='disabled')
        
    def clicar_botao_7(self, event):
        self.jogod.recebe_jogada(2,0)
        if self.jogod.jogador == 1:
            self.botao7.configure(text='O')
            self.label_proximo_jogador('X')
        elif self.jogod.jogador == 2:
            self.botao7.configure(text='X')
            self.label_proximo_jogador('O')
        
        if self.jogod.verifica_ganhador() == 1:
            print('X venceu')
        elif self.jogod.verifica_ganhador() == 2:
            print('O venceu')
        elif self.jogod.verifica_ganhador() == 0:
            print('O jogo empatou')
        
        self.botao7.configure(state='disabled')
                
    def clicar_botao_8(self, event):
        self.jogod.recebe_jogada(2,1)
        if self.jogod.jogador == 1:
            self.botao8.configure(text='O')
            self.label_proximo_jogador('X')
        elif self.jogod.jogador == 2:
            self.botao8.configure(text='X')
            self.label_proximo_jogador('O')
        
        if self.jogod.verifica_ganhador() == 1:
            print('X venceu')
        elif self.jogod.verifica_ganhador() == 2:
            print('O venceu')
        elif self.jogod.verifica_ganhador() == 0:
            print('O jogo empatou')
        
        self.botao8.configure(state='disabled')
        
    def clicar_botao_9(self, event):
        self.jogod.recebe_jogada(2,2)
        if self.jogod.jogador == 1:
            self.botao9.configure(text='O')
            self.label_proximo_jogador('X')
        elif self.jogod.jogador == 2:
            self.botao9.configure(text='X')
            self.label_proximo_jogador('O')
        
        if self.jogod.verifica_ganhador() == 1:
            print('X venceu')
        elif self.jogod.verifica_ganhador() == 2:
            print('O venceu')
        elif self.jogod.verifica_ganhador() == 0:
            print('O jogo empatou')
        
        self.botao9.configure(state='disabled')
        
    def label_proximo_jogador(self,jogada_de):
        self.proximo_jogador.set('Próxima jogada: {0}'.format(jogada_de))

jogo = jogo_da_velha()
jogo.iniciar()