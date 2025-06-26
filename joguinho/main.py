from partida import Partida


if __name__ == "__main__":
    partida = Partida()
    partida.criar_cartas()
    partida.distribuir_cartas_iniciais()
    partida.inicio_de_partida()