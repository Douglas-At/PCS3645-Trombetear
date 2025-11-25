import serial
import threading

class SerialReader:
    def __init__(self, porta, callback):
        self.porta = serial.Serial(
                        port=porta,
                        baudrate=115200,
                        parity=serial.PARITY_EVEN,
                        stopbits=serial.STOPBITS_ONE,
                        bytesize=serial.SEVENBITS
                    )
        self.callback = callback
        self.loop = True

        self.thread = threading.Thread(target=self.run)
        self.thread.daemon = True
        self.thread.start()

    def run(self):
        buffer = ""
        while self.loop:
            raw_data = self.porta.read_until(b'#') 
            data_string = raw_data.decode('ascii').strip('#')
            dist = data_string.split(",")[-1]
            self.callback(dist)
