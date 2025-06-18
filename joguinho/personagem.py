from __future__ import annotations
from random import randint, sample


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
        pontos de vida maxima: {self.pontos_de_vida_maxima}
        vida atual: {self.vida_atual}
        pontos de ataque: {self.pontos_de_ataque}
        pontos de defesa: {self.pontos_de_defesa}
        energia usada: {self.energia_usada}
        energia maxima: {self.energia_maxima}
        '''
        return personagem
    
    
    # def atacar(self, inimigo: Personagem):
        
    #     eficiencia = randint(70, 110) / 100
    #     dano = (self.pontos_de_ataque - inimigo.pontos_de_defesa) * eficiencia
    #     dano = max(0, round)
        
    #     adicionar_jogadores (player1: Personagem,player2: Personagem)