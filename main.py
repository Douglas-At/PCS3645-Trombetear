import sys
from PyQt6.QtWidgets import QApplication

from serial_reader import SerialReader
from audio import play_note
from engine import GameEngine
from partitura import PartituraWidget
from interface import Interface
import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtCore import QObject, QEvent, Qt
import time

ultimo_tempo = time.time()
intervalo_batida = 60 / 60   # 0.666s
    
def main():
    app = QApplication(sys.argv)

    engine = GameEngine()
    partitura = PartituraWidget()
    partitura.engine = engine

    def on_serial(dist):
        global ultima_leitura, ultimo_tempo
        if not engine.ativo:
            return

        # sempre salva o valor mais recente
        ultima_leitura = int(dist)

        agora = time.time()
        if agora - ultimo_tempo < intervalo_batida:
            return 

        ultimo_tempo = agora  

        
        nota = ultima_leitura
        partitura.set_nota(nota)

        acerto = engine.registrar_nota(nota)
        partitura.set_target(engine.target)

        if not engine.silencioso:
            play_note(nota)

        ui.atualizar_pontos()

    ui = Interface(engine, partitura, on_serial)
    ui.resize(900, 400)
    ui.show()

    # keyboard = KeyboardInput(on_serial)
    # ui.installEventFilter(keyboard)

    # iniciar leitura serial
    SerialReader("COM9", on_serial)

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
