import socket
from PyQt5.QtCore import QThread,pyqtSignal


class connectClient(QThread):
    finishSignal =pyqtSignal(str)

    def __init__(self,IP, Port):
        super(connectClient, self).__init__()
        self.IP = IP
        self.Port = Port
        self.message = []
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(self.IP, self.Port)
        self.client.connect((self.IP, int(self.Port)))
        print(self.IP, self.Port)

    def run(self):
        while True:
            rec = self.client.recv(1024).decode()
            # connect_, address = self.client.accept()
            # print('client:run')
            # rec = connect_.recv(1024).decode()
            if rec != '' or None:
                print("In",rec)
                self.message.append(rec)
            self.finishSignal.emit(rec)