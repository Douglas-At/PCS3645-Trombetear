from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QPushButton, QComboBox
from PyQt6.QtCore import Qt

class Interface(QWidget):
    def __init__(self, engine, partitura, callback_teclado):
        super().__init__()
        self.engine = engine
        self.partitura = partitura
        self.on_key = callback_teclado


        self.setWindowTitle("Jogo Musical")

        self.lblPontos = QLabel("Pontos: 0")
        self.lblPontos.setStyleSheet("font-size: 24px;")

        self.btnSil = QPushButton("Silencioso: OFF")
        self.btnSil.clicked.connect(self.toggle_sil)

        self.btnDif = QPushButton("Dificuldade: 1")
        self.btnDif.clicked.connect(self.toggle_dif)

        self.cmbMusicas = QComboBox()
        self.cmbMusicas.addItem("Asa Branca", 1)
        self.cmbMusicas.addItem("Solfejo", 2)
        self.cmbMusicas.addItem("Carinhoso", 3)
        self.cmbMusicas.addItem("Música 4", 4)
        self.cmbMusicas.currentIndexChanged.connect(self.trocar_musica)

        self.btnStart = QPushButton("Start")
        self.btnStart.clicked.connect(self.start_musica)

        self.btnReset = QPushButton("Reset")
        self.btnReset.clicked.connect(self.reset_musica)


        painel = QVBoxLayout()
        painel.addWidget(self.lblPontos)
        painel.addWidget(self.btnSil)
        painel.addWidget(self.btnDif)
        painel.addWidget(self.cmbMusicas)
        painel.addStretch()

        layout = QHBoxLayout()
        layout.addLayout(painel)
        layout.addWidget(self.partitura, stretch=1)
        painel.addWidget(self.btnStart)
        painel.addWidget(self.btnReset)


        self.setLayout(layout)

    def toggle_sil(self):
        self.engine.silencioso = not self.engine.silencioso
        self.btnSil.setText("Silencioso: " + ("ON" if self.engine.silencioso else "OFF"))

    def toggle_dif(self):
        self.engine.dificuldade += 1
        if self.engine.dificuldade > 3:
            self.engine.dificuldade = 1
        self.btnDif.setText(f"Dificuldade: {self.engine.dificuldade}")

    def atualizar_pontos(self):
        self.lblPontos.setText(f"Pontos: {self.engine.points}")
    
    def trocar_musica(self):
        musica_id = self.cmbMusicas.currentData()
        self.engine.trocar_musica(musica_id)
        self.partitura.set_target(self.engine.target)
        self.atualizar_pontos()

    def keyPressEvent(self, event):
        tecla = event.text()
        if tecla in "1234567":
            nota = int(tecla)
            self.on_key(nota)

    def start_musica(self):
        self.engine.ativo = True  # agora pode tocar
        self.engine.index = 0
        self.engine.target = self.engine.musica[0]
        self.partitura.historico.clear()
        self.partitura.set_target(self.engine.target)

    def reset_musica(self):
        self.engine.ativo = False  # impede tocar notas
        self.engine.points = 0
        self.engine.index = 0
        self.engine.target = self.engine.musica[0]
        self.partitura.historico.clear()
        self.partitura.set_target(self.engine.target)
        self.atualizar_pontos()


