from musicas import MUSICAS

class GameEngine:
    def __init__(self, musica_id=1):
        self.musica_id = musica_id
        self.musica = MUSICAS[musica_id]  
        self.index = 0                   # posição dentro da música
        self.target = self.musica[self.index]

        self.points = 0
        self.silencioso = False
        self.dificuldade = 1
        self.ativo = False

    def registrar_nota(self, nota):
        acerto = (nota == self.target)

        if acerto:
            self.points += 10
        else:
            self.points -= 3

        # avança índice
        self.index += 1

        # se acabou a música → sinaliza e NÃO tenta acessar self.musica[self.index]
        if self.index >= len(self.musica):
            self.index = len(self.musica)  # trava no final
            return "fim"   # <- SINALIZA ENCERRAMENTO

        # continua normalmente
        self.target = self.musica[self.index]
        return acerto


    def trocar_musica(self, musica_id):
        self.musica_id = musica_id
        self.musica = MUSICAS[musica_id]
        self.index = 0
        self.target = self.musica[0]
