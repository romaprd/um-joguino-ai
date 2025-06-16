from __future__ import annotations
from random import randint, sample
from partida import Partida
class Personagem:
    def __init__(self, nome):
        self.nome = nome
        self.pontos_de_vida_maxima = 100
        self.vida_atual = 100
        self.pontos_de_ataque = 15
        self.pontos_de_defesa = 15
        self.energia_usada = 0
        self.energia_maxima = 100
    
    def criar_personagem(self):
        personagem = Personagem(self.nome, self.pontos_de_vida_maxima)
        return personagem
    def atacar(self, inimigo: Personagem):
        
        eficiencia = randint(70, 110) / 100
        dano = (self.pontos_de_ataque - inimigo.pontos_de_defesa) * eficiencia
        dano = max(0, round)
        
        adicionar_jogadores (player1: Personagem,player2: Personagem)
        
        
        