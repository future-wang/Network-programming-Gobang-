import socket
from PyQt5.QtCore import QThread,pyqtSignal

class connectServer(QThread):
    finishSignal = pyqtSignal(str)
    def __init__(self, IP, Port):
        super(connectServer, self).__init__()
        self.IP = IP
        self.Port = int(Port)
        self.message = []

    def run(self):
        self.server = socket.socket()
        print(self.IP, self.Port)
        self.server.bind((self.IP, int(self.Port)))
        print(self.IP, self.Port)
        self.server.listen(5)
        while True:
            self.conobject, self.address = self.server.accept()
            print("Connect ",self.address)
            while True:
                rec = self.conobject.recv(1024)
                if not rec:break
                self.finishSignal.emit(rec.decode())
