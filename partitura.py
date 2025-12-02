from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPainter, QPen, QColor
from PyQt6.QtCore import Qt, QRectF, QPointF
from PyQt6.QtSvg import QSvgRenderer
import math

class PartituraWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.historico = []
        self.x_inicial = 100
        self.espaco = 50

        #padrao pauta 
        self.esp = 18
        self.y_base = 150  # linha central da pauta

        # Carregar SVGs
        self.clave = QSvgRenderer(r"imagens\clave_de_sol.svg")

        # Controle do alvo
        self.target_nota = 1

        self.n_notas = round((self.x_inicial+self.width()-30)/self.espaco)
        self.nome_notas = {
                            1: "Dó",
                            2: "Ré",
                            3: "Mi",
                            4: "Fá",
                            5: "Sol",
                            6: "Lá",
                            7: "Si"
                        }


    def set_nota(self, nota):
        self.historico.append(nota)
        self.update()

    def set_target(self, t):
        self.target_nota = t
        self.update()

    def nota_to_y(self, nota):
        #pega a nota e joga na pauta
        return self.y_base + (7-nota)*9

    def criar_nota(self, x, y,nota, cor=QColor(0, 0, 0)):
        qp = QPainter(self)
        largura = self.esp * 1.1
        rect = QRectF(x, y - self.esp/2, largura, self.esp)

        qp.setPen(QPen(cor, 2))
        qp.setBrush(cor)
        qp.drawEllipse(rect)

        p1 = QPointF(x + largura, y)
        p2 = QPointF(x + largura, y - self.esp * 3.5)
        qp.drawLine(p1, p2)

        nome = self.nome_notas.get(nota, str(nota))
        qp.setPen(QPen(Qt.GlobalColor.black))
        qp.drawText(int(x), int(y + 1.5*self.esp), nome)

    def paintEvent(self, event):
        qp = QPainter(self)
        qp.setRenderHint(QPainter.RenderHint.Antialiasing)

        #pauta
        qp.setPen(QPen(Qt.GlobalColor.black, 2))
        for i in range(5):
            y = self.y_base - ((i - 2) * self.esp)
            qp.drawLine(50, y, self.width() - 30, y)

        #clave de sol
        clave_rect = QRectF(10, self.y_base - 3 * self.esp, 60, 6 * self.esp)
        self.clave.render(qp, clave_rect)

        centro = (self.x_inicial+self.width()-30)/2
        #lionha vertical estilo guitar hero 
        qp.setPen(QPen(Qt.GlobalColor.red, 2))
        p1 = QPointF(centro, 150-2*self.esp)
        p2 = QPointF(centro, 150+2*self.esp)
        qp.drawLine(p1, p2)
        # qp.drawLine(centro, 20, centro, self.height() - 20)

        #porximas notas
        if hasattr(self, "engine"):
            nota_alvo = self.engine.target
            y = self.nota_to_y(nota_alvo)
            self.criar_nota(centro, y, nota_alvo,QColor(0, 0, 255))  # azul
            musica = self.engine.musica
            idx = self.engine.index

            x = centro + self.espaco
            for i in range(1, 6): 
                proximo = musica[(idx + i) % len(musica)]
                y2 = self.nota_to_y(proximo)
                self.criar_nota(x, y2, proximo,QColor(0, 255, 0))
                x += self.espaco

        #mecanismo de sifht de notas 
        
        # self.criar_nota(centro,self.y_base,QColor(0,0,255))
        # print("+"*30)
        for idx, nota in enumerate(self.historico[-math.floor((self.n_notas-1 )/2):]):
            y = self.nota_to_y(nota)
            x = centro - (len(self.historico[-math.floor((self.n_notas-1 )/2):])- idx)*self.espaco
            self.criar_nota(x,y,nota)
            
