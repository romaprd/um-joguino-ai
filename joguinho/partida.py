import random
from personagem import Personagem
from cartas import (
    Carta_aumento, Carta_cura, Carta_dano, Carta_roubo,
    Carta_atordoamento, Tipo_Aumento
)

players = []

class Partida:
    def __init__(self):
        self.nome1 = input("Jogador 1! Informe seu nome: ")
        self.player1 = Personagem(self.nome1)
        print(self.player1.criar_personagem())

        self.nome2 = input("Jogador 2! Informe seu nome: ")
        self.player2 = Personagem(self.nome2)
        print(self.player2.criar_personagem())

        while True:
            input("Pressione Enter para jogar o dado!")
            dado1 = random.randint(1, 6)
            print(f"{self.nome1} tirou: {dado1}")

            input("Pressione Enter para jogar o dado!")
            dado2 = random.randint(1, 6)
            print(f"{self.nome2} tirou: {dado2}")

            if dado1 > dado2:
                print(f"{self.nome1} começa!")
                self.ordem = 0
                break
            elif dado2 > dado1:
                print(f"{self.nome2} começa!")
                self.ordem = 1
                break
            else:
                print("Empate! Tentem novamente.")

    def criar_cartas(self):
        self.lista_de_cartas = [
            Carta_aumento("Aumento Vida Máx", 10, "Aumenta vida máx", Tipo_Aumento.aumento_vida_max, 20),
            Carta_aumento("Aumento Energia Máx", 10, "Aumenta energia máx", Tipo_Aumento.aumento_energia_max, 15),
            Carta_aumento("Aumento Defesa", 10, "Aumenta defesa", Tipo_Aumento.aumento_defesa, 10),
            Carta_aumento("Aumento Ataque", 10, "Aumenta ataque", Tipo_Aumento.aumento_ataque, 10),
            Carta_roubo("Roubo", 15, "Rouba uma carta"),
            Carta_atordoamento("Atordoamento", 15, "Zera a energia do oponente"),
            Carta_dano("Dano", 15, "Causa dano", 25),
            Carta_cura("Cura", 15, "Cura vida", 30)
        ]

    def distribuir_cartas_iniciais(self):
        self.player1.receber_cartas_iniciais(self.lista_de_cartas)
        self.player2.receber_cartas_iniciais(self.lista_de_cartas)

    def get_jogador_obj(self, nome):
        return self.player1 if self.player1.nome == nome else self.player2

    def exibir_status(self, jogador):
        print(f"\n{jogador.nome}:")
        print(f"Vida: {jogador.vida_atual}/{jogador.pontos_de_vida_maxima}")
        print(f"Ataque: {jogador.pontos_de_ataque}")
        print(f"Defesa: {jogador.pontos_de_defesa}")
        print(f"Energia: {jogador.energia_usada}/{jogador.energia_maxima}")
        print(f"Cartas na mão: {[c.nome for c in jogador.deck]}")

    def comprar_carta_turno(self):
        jogador = self.get_jogador_obj(self.jogador_atual)
        jogador.comprar_carta(self.lista_de_cartas)

    def passar_turno(self):
        self.jogador_atual, self.jogador_inimigo = self.jogador_inimigo, self.jogador_atual
        print(f"\n🎯 Agora é a vez de {self.jogador_atual}")

    def usar_carta(self):
        jogador = self.get_jogador_obj(self.jogador_atual)
        inimigo = self.get_jogador_obj(self.jogador_inimigo)

        if not jogador.deck:
            print("Você não tem cartas para usar.")
            return

        print("\nCartas disponíveis:")
        for i, carta in enumerate(jogador.deck):
            print(f"{i + 1} - {carta.nome} | Energia: {carta.energia_gasta} | {carta.descricao}")

        escolha = int(input("Escolha o número da carta para usar: ")) - 1
        if escolha < 0 or escolha >= len(jogador.deck):
            print("Escolha inválida.")
            return

        carta = jogador.deck.pop(escolha)

        if jogador.energia_usada + carta.energia_gasta > jogador.energia_maxima:
            print("Energia insuficiente.")
            jogador.deck.insert(escolha, carta)
            return

        jogador.energia_usada += carta.energia_gasta

        # Executa o efeito
        if hasattr(carta, 'usar_carta'):
            if isinstance(carta, (Carta_dano, Carta_roubo)):
                resultado = carta.usar_carta(jogador, inimigo)
            elif isinstance(carta, Carta_atordoamento):
                resultado = carta.usar_carta(inimigo)
            else:
                resultado = carta.usar_carta(jogador)
            print("🃏", resultado)

        self.exibir_status(jogador)
        self.exibir_status(inimigo)

    def inicio_de_partida(self):
        players = [self.nome1, self.nome2] if self.ordem == 0 else [self.nome2, self.nome1]
        self.jogador_atual, self.jogador_inimigo = players[0], players[1]

        while True:
            print(f"\n🎮 Turno de {self.jogador_atual}")
            print("1 - Usar carta\n2 - Comprar carta\n3 - Passar turno")
            acao = input("Escolha: ")

            match acao:
                case "1":
                    self.usar_carta()
                    self.passar_turno()
                case "2":
                    self.comprar_carta_turno()
                    self.passar_turno()
                case "3":
                    self.passar_turno()



if __name__ == "__main__":
    partida = Partida()
    partida.criar_cartas()
    partida.distribuir_cartas_iniciais()
    partida.inicio_de_partida()
