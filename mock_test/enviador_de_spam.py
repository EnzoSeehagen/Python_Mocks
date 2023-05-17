class EnviadorDeSpam :
    def __init__(self, destinatarios = None):
        self.destinatarios = destinatarios if destinatarios else []

    def adicionar_destinatarios(self, destinatario):
        self.destinatarios.append(destinatario)

