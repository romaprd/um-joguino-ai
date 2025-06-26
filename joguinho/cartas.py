from enum import Enum
import random
import os

class Tipo_Aumento(Enum):
    aumento_vida_max = 1
    aumento_energia_max = 2
    aumento_defesa = 3
    aumento_ataque = 4


class Carta:
    def __init__(self, nome, energia_gasta, descricao):
        self.nome = nome
        self.energia_gasta = energia_gasta
        self.descricao = descricao

    def limpar():
        os.system('cls' if os.name == 'nt' else 'clear')

class Carta_aumento(Carta):
    def __init__(self, nome, energia_gasta, descricao, tipo_aumento: Tipo_Aumento, pontos_aumentados):
        super().__init__(nome, energia_gasta, descricao)
        self.tipo_aumento = tipo_aumento
        self.pontos_aumentados = pontos_aumentados

    Carta.limpar()
    def usar_carta(self, beneficiado):
        if self.tipo_aumento == Tipo_Aumento.aumento_vida_max:
            beneficiado.pontos_de_vida_maxima += self.pontos_aumentados
            
            return f"{beneficiado.nome} aumentou sua vida máxima em {self.pontos_aumentados}!"
        elif self.tipo_aumento == Tipo_Aumento.aumento_energia_max:
            beneficiado.energia_maxima += self.pontos_aumentados
            
            return f"{beneficiado.nome} aumentou sua energia máxima em {self.pontos_aumentados}!"
        elif self.tipo_aumento == Tipo_Aumento.aumento_defesa:
            beneficiado.pontos_de_defesa += self.pontos_aumentados
            
            return f"{beneficiado.nome} aumentou sua defesa em {self.pontos_aumentados}!"
        else:
            beneficiado.pontos_de_ataque += self.pontos_aumentados
            
            return f"{beneficiado.nome} aumentou seu ataque em {self.pontos_aumentados}!"


class Carta_roubo(Carta):
    Carta.limpar()
    def usar_carta(self, ladrao, vitima):
        if vitima.deck:
            carta_roubada = random.choice(vitima.deck)
            vitima.deck.remove(carta_roubada)
            ladrao.deck.append(carta_roubada)
            return f"{ladrao.nome} roubou a carta '{carta_roubada.nome}' de {vitima.nome}!"
        return f"{vitima.nome} não tem cartas para serem roubadas."


class Carta_atordoamento(Carta):
    Carta.limpar()
    def usar_carta(self, prejudicado):
        return f"{prejudicado.nome} foi atordoado e perdeu toda sua energia no turno!"


class Carta_dano(Carta):
    def __init__(self, nome, energia_gasta, descricao, dano_causado):
        super().__init__(nome, energia_gasta, descricao)
        self.dano_causado = dano_causado

    Carta.limpar()
    def usar_carta(self, atacante, atacado):
        dano_total = self.dano_causado + \
            atacante.pontos_de_ataque - atacado.pontos_de_defesa
        dano_real = max(dano_total, 0)
        atacado.vida_atual -= dano_real
        return f"{atacante.nome} causou {dano_real} de dano em {atacado.nome}!"


class Carta_cura(Carta):
    def __init__(self, nome, energia_gasta, descricao, vida_curada):
        super().__init__(nome, energia_gasta, descricao)
        self.vida_curada = vida_curada
    Carta.limpar()
    def usar_carta(self, beneficiado):
        beneficiado.vida_atual = min(
            beneficiado.pontos_de_vida_maxima, beneficiado.vida_atual + self.vida_curada)
        return f"{beneficiado.nome} recuperou {self.vida_curada} de vida!"
