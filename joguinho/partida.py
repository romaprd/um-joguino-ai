import random
from personagem import Personagem
class Partida:
    def __init__(self):
        
        self.nome1 = input("Jogador 1! Informe seu nome: ")
        self.player1 = Personagem(self.nome1).criar_personagem()
        print(self.player1)
        self.nome2 = input("Jogador 2! Informe seu nome: ")
        self.player2 = Personagem(self.nome2).criar_personagem()
        print(self.player2)

        op = input(
            "Vocês sabem como funciona o jogo? Se sim, escreva 'sim', se não escreva 'não':  ")

        if op.lower() == "sim":
            while True:
                entrada = input("Pressione Enter para jogar o dado!")
                if entrada == "":
                    dado_jogador_1 = random.randint(1, 6)
                    print("O jogador 1 tirou:", dado_jogador_1)

                    entrada2 = input("Pressione Enter para jogar o dado!")
                    if entrada2 == "":
                        dado_jogador_2 = random.randint(1, 6)
                        print("O jogador 2 tirou:", dado_jogador_2)

                        if dado_jogador_1 > dado_jogador_2:
                            print(
                                f"O jogador {self.nome1} tirou o maior número e começará a jogada!")
                            break
                        elif dado_jogador_2 > dado_jogador_1:
                            print(
                                f"O jogador {self.nome2} tirou o maior número, portanto começará a batalha!")
                            break
                        else:
                            print("Empate! Vamos fazer um desempate.")
        else:
            print("Informações: a gente aprende jogando")

    def adicionar_jogadores(self):
        players = []
        players.append(self.player1)
        players.append(self.player)

    def inicio_de_partida(self):
        print(f"Iniciando partida com {self.nome1} e {self.nome2}!")


if __name__ == "__main__":
    partida = Partida()  
    
    partida.inicio_de_partida()  
