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
        
        self.window.rowconfigure(0, minsize=100, weight=1)
        self.window.rowconfigure(1, minsize=100, weight=1)
        self.window.rowconfigure(2, minsize=100, weight=1)
        self.window.rowconfigure(3, minsize=50, weight=1)
        
        self.window.columnconfigure(0, minsize=100, weight=1)
        self.window.columnconfigure(1, minsize=100, weight=1)
        self.window.columnconfigure(2, minsize=100, weight=1)
        
        
        botao1 = tk.Button(self.window)
        botao1.configure(text='1')
        botao1.grid(row=0,column=0)
        
        botao2 = tk.Button(self.window)
        botao2.configure(text='2')
        botao2.grid(row=0,column=1)
        
        botao3 = tk.Button(self.window)
        botao3.configure(text='3')
        botao3.grid(row=0,column=2)


        botao4 = tk.Button(self.window)
        botao4.configure(text='4')
        botao4.grid(row=1,column=0)

        botao5 = tk.Button(self.window)
        botao5.configure(text='5')
        botao5.grid(row=1,column=1)

        botao6 = tk.Button(self.window)
        botao6.configure(text='6')
        botao6.grid(row=1,column=2)

        botao7 = tk.Button(self.window)
        botao7.configure(text='7')
        botao7.grid(row=2,column=0)
        
        botao8 = tk.Button(self.window)
        botao8.configure(text='8')
        botao8.grid(row=2,column=1)

        botao9 = tk.Button(self.window)
        botao9.configure(text='9')
        botao9.grid(row=2,column=2)

        botao10 = tk.Button(self.window)
        botao10.configure(text='10')
        botao10.grid(row=3)


    def iniciar(self):
        self.window.mainloop()
        
    

jogo = jogo_da_velha()
jogo.iniciar()
