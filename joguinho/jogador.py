class Jogador:
    def __init__(self, nome_jogador1, nome_jogador2):
        self.nome_jogador1 = nome_jogador1
        self.nome_jogador2 = nome_jogador2

    def jogadores(self):
        return f"jogador 1: {self.nome_jogador1}\njogador 2: {self.nome_jogador2}"
