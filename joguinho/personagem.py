from random import sample

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
        Vida atual: {self.vida_atual}/{self.pontos_de_vida_maxima}
        Pontos de ataque: {self.pontos_de_ataque}
        Pontos de defesa: {self.pontos_de_defesa}
        Energia usada: {self.energia_usada}/{self.energia_maxima}
        '''
        return personagem

    def receber_cartas_iniciais(self, todas_as_cartas: list):
        self.deck = sample(todas_as_cartas, 3)
        print(f"\nCartas iniciais de {self.nome}:")
        for carta in self.deck:
            print(f"- {carta.nome} | Energia: {carta.energia_gasta} | {carta.descricao}")

    def comprar_carta(self, todas_as_cartas: list):
        nova_carta = sample(todas_as_cartas, 1)[0]
        self.deck.append(nova_carta)
        print(f"\n{self.nome} comprou uma carta:")
        print(f"- {nova_carta.nome} | Energia: {nova_carta.energia_gasta} | {nova_carta.descricao}")
