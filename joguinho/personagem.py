class Personagem:
    def personagem(self, vida_personagem, vida_atual, dano_sofrido, pontos_de_ataque, pontos_de_defesa, nome, energia_usada):
        self.vida_personagem = vida_personagem
        self.vida_atual = vida_atual
        self.dano_sofrido = dano_sofrido
        self.pontos_de_ataque = pontos_de_ataque
        self.pontos_de_defesa = pontos_de_defesa
        self.nome = nome
        self.energia_usada = energia_usada
        
    def criar_personagem():
        arqueiro = Personagem(100, 100, 0, 15, 15, "Arqueiro", 0)
        return print(arqueiro[5])