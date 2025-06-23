import random
from personagem import Personagem
from cartas import Carta, Carta_atordoamento, Carta_aumento,Carta_cura,Carta_dano,Carta_roubo
from cartas import Tipo_Aumento

players_status = []
players = []
class Partida:
    def __init__(self):
        
        self.nome1 = input("Jogador 1! Informe seu nome: ")
        self.player1 = Personagem(self.nome1).criar_personagem()
        print(self.player1)
        players_status.append(self.player1)
        self.nome2 = input("Jogador 2! Informe seu nome: ")
        self.player2 = Personagem(self.nome2).criar_personagem()
        print(self.player2)
        players_status.append(self.player2)

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
                                f"O jogador {self.nome1} tirou o maior número, portanto começará a batalha!")
                            self.ordem = 0
                            break
                        elif dado_jogador_2 > dado_jogador_1:
                            print(
                                f"O jogador {self.nome2} tirou o maior número, portanto começará a batalha!")
                            self.ordem = 1
                            break
                        else:
                            print("Empate! Vamos fazer um desempate.")
        else:
            print("Informações: a gente aprende jogando")
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
                            self.ordem = 0
                            break
                        elif dado_jogador_2 > dado_jogador_1:
                            print(
                                f"O jogador {self.nome2} tirou o maior número, portanto começará a batalha!")
                            self.ordem = 1
                            break
                        else:
                            print("Empate! Vamos fazer um desempate.")
            
    def inicio_de_partida(self):
        if self.ordem == 0:
            players_status.append(self.player1)
            players_status.append(self.player2)
            players.append(self.nome1)
            players.append(self.nome2)  
        else:
            players_status.append(self.player2)
            players_status.append(self.player1)
            players.append(self.nome2)   
            players.append(self.nome1)  
        self.jogador_atual = players[0]
        self.jogador_inimigo = players[1]
        print("o jogador atacante é: ",self.jogador_atual) 
        print("o jogador inimigo é: ",self.jogador_inimigo) 
        
        op = input(self.jogador_atual," o que você deseja fazer?\n\n1 - usar carta\n2 - comprar carta\n3 - passar ")
        
    def criar_cartas (self):
    
        nome = "Carta de Aumento de Vida Maxima"
        energia_gasta = 10
        descricao = "Esta carta aumenta a vida maxima de um jogador!"
        carta_vida_maxima = Carta_aumento(nome, energia_gasta, descricao)
        
        nome = "Carta de Aumento de Energia"
        energia_gasta = 10
        descricao = "Essa carta aumenta a energia maxima de um jogador!"
        carta_energia_maxima = Carta_aumento(nome, energia_gasta, descricao)
        
        nome = "Carta de Aumento de Defesa"
        energia_gasta = 10
        descricao = "Essa carta aumentas os pontos de defesa de um jogador!"
        carta_de_defesa = Carta_aumento(nome, energia_gasta, descricao)
        
        nome = "Carta de Aumento de Pontos de Ataque"
        energia_gasta = 10
        descricao = "Essa carta aumenta os pontos de ataque de um jogador!"
        carta_de_ataque = Carta_aumento(nome, energia_gasta, descricao)
        
        nome = "Presidencia"
        energia_gasta = 15
        descricao = "Essa carta ti permite roubar qual carta do seu oponente!"
        carta_de_roubo = Carta_roubo(nome, energia_gasta, descricao)
        
        nome = "Carta de Atordoamento"
        energia_gasta = 15
        descricao = "Essa carta ti permite atordoar o jogador inimigo!"
        carta_de_atordoamento = Carta_atordoamento(nome, energia_gasta, descricao)
        
        nome = "Carta de Dano"
        energia_gasta = 15
        descricao = "Essa carta ti permite aumentar o dano do seu personagem!"
        carta_de_aumento_de_dano = Carta_dano(nome, energia_gasta, descricao)
        
        nome = "Carta de cura"
        energia_gasta = 15
        descricao = "Essa carta ti permite aumentar a vida do seu personagem!"
        carta_de_cura = Carta_cura(nome, energia_gasta, descricao)
        
        self.lista_de_cartas = []
        self.lista_de_cartas.append(carta_vida_maxima)
        self.lista_de_cartas.append(carta_energia_maxima)
        self.lista_de_cartas.append(carta_de_defesa)
        self.lista_de_cartas.append(carta_de_ataque)
        self.lista_de_cartas.append(carta_de_roubo)
        self.lista_de_cartas.append(carta_de_atordoamento)
        self.lista_de_cartas.append(carta_de_aumento_de_dano)
        self.lista_de_cartas.append(carta_de_cura)
        
    def listar_cartas(self):
        for i in self.lista_de_cartas:
            print(i.nome, i.energia_gasta, i.descricao)  
              
if __name__ == "__main__":
    partida = Partida()  
    partida.criar_cartas()
    partida.lista_de_cartas()
    partida.inicio_de_partida()  
    