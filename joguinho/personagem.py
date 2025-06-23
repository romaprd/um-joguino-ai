from __future__ import annotations
from random import randint, sample
import random
# from cartas import Carta_atordoamento, Carta_aumento, Carta_cura, Carta_dano, Carta_roubo

class Personagem:
    def __init__(self, nome):
        self.nome = nome
        self.pontos_de_vida_maxima = 100
        self.vida_atual = 100
        self.pontos_de_ataque = 15
        self.pontos_de_defesa = 15
        self.energia_usada = 0
        self.energia_maxima = 100
        self.deck = []
    def criar_personagem(self):
        personagem = f'''
        {self.nome}
        vida atual: {self.vida_atual}\{self.pontos_de_vida_maxima}
        pontos de ataque: {self.pontos_de_ataque}
        pontos de defesa: {self.pontos_de_defesa}
        energia usada: {self.energia_usada}\{self.energia_maxima}
        '''
        return personagem
    
    def comprar_carta(self):
        
        pass
    
    def levar_dano(self):
    
        pass
    
    def ver_mao_de_cartas(self):
        
        pass
    
    def curar_se(self):
        
        pass
    
    # def sorteio_cartas(self):
    #     for i in range(4):
    #         carta_sorteada = random.randint(1,5)
            
    #         if carta_sorteada == 1:
    #             carta1 = Carta_aumento.usar_carta
    
    