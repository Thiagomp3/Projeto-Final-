# -*- coding: utf-8 -*-
"""
Created on Thu May  9 16:08:22 2019

@author: lucca
"""

mapa= [[0,1,2],
       [0]*10,
       [0]*10,
       [0]*10,
       [0]*10,]

linha=0
for e in mapa:
    for i in mapa[linha]:
        if i == 0:
            print("espaco vazio feature")
        elif i == 1:
            print("chao")
        elif i == 2:
            print("escada")
    linha+=1
    

        
    


       
       
       
    

        
        
        