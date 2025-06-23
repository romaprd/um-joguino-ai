from enum import Enum
from personagem import Personagem
import random

class Tipo_Aumento (Enum):
    aumento_vida_max = 1
    aumento_energia_max = 2
    aumento_defesa = 3
    aumento_ataque = 4

class Tipo_Artodoamento (Enum):
    
    pass

class Carta:
    def __init__ (self, nome, energia_gasta, descricao): 
        self.nome = nome
        self.energia_gasta = energia_gasta
        self.descricao = descricao
        
  
class Carta_aumento (Carta):
    
    def __init__ (self,  nome, energia_gasta: int, descricao, tipo_aumento: Tipo_Aumento, pontos_aumentados: int):
        super ().__init__ (nome, energia_gasta, descricao)
        self.tipo_aumento = tipo_aumento
        self.pontos_aumentados = pontos_aumentados
    
    def usar_carta (self, beneficiado: Personagem):
    
        sorteado = random.randint(1,4)
        
        if sorteado == 1:
                Tipo_Aumento.aumento_vida_max
                beneficiado.pontos_de_vida_maxima += self.pontos_aumentados
                return (f"O {beneficiado} usou uma carta de Aumento de Vida Máxima")
            
        elif sorteado == 2: 
                Tipo_Aumento.aumento_energia_max
                beneficiado.energia_maxima += self.pontos_aumentados
                return (f"O {beneficiado} usou uma carta de Aumento de Energia Máxima")
                
        elif sorteado == 3: 
                Tipo_Aumento.aumento_defesa
                beneficiado.pontos_de_defesa += self.pontos_aumentados
                return (f"O {beneficiado} usou uma carta de Aumento de Defesa")
                
        else:
                Tipo_Aumento.aumento_ataque
                beneficiado.pontos_de_ataque += self.pontos_aumentados
                return (f"O {beneficiado} usou uma carta de Aumento de Ataque")
                
class Carta_roubo (Carta):
    def __init__ (self, nome, energia_gasta: int, descricao):
        super ().__init__ (nome, energia_gasta, descricao)
        
    def usar_carta (self, ladrao: Personagem, vitima: Personagem):
        sorteio_carta_roubada = random.randint (0, len (vitima.deck) - 1)
        carta_roubada = vitima.deck.pop (sorteio_carta_roubada)
        ladrao.deck.append (carta_roubada)
        return (f"O {ladrao} roubou a carta {carta_roubada} do {vitima}")
    
class Carta_atordoamento (Carta):
    def __init__ (self, nome, energia_gasta: int, descricao):
        super ().__init__ (nome, energia_gasta, descricao)
        
    def usar_carta (self, prejudicado: Personagem):
        prejudicado.energia = 0
        return (f"O {prejudicado} foi atordoado")
    
class Carta_dano (Carta):
    def __init__ (self, nome, energia_gasta: int, descricao, dano_causado: int):
        super ().__init__ (nome, energia_gasta, descricao)
        self.dano_causado = dano_causado
        
    def usar_carta (self, atacante: Personagem, atacado: Personagem):
        atacado.pontos_vida_atual -= self.dano_causado
        return (f"O {atacante} causou {self.dano_causado} de dano ao {atacado}")
    
class Carta_cura (Carta):
    def __init__ (self, nome, energia_gasta: int, descricao, vida_curada: int):
        super ().__init__ (nome, energia_gasta, descricao)
        self.vida_curada = vida_curada
        
    def usar_carta (self, beneficiado: Personagem):
        beneficiado.pontos_vida_atual += self.vida_curada
        return (f"O {beneficiado} curou {self.vida_curada} de vida") 
    