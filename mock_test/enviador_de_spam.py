class CanalEmail:
    def enviar(self, destinatario, mensagem):
        nome = destinatario.split("@")[0].capitalize()
        print("E-mail enviado erroneamente")
        mensagem_final = f'{mensagem} para {nome}'
        return destinatario, mensagem_final


class EnviadorDeSpam:
    def __init__(self, destinatarios=None):
        self.destinatarios = destinatarios if destinatarios else []
        self.canais_de_envio = [CanalEmail()]

    def adicionar_destinatarios(self, destinatario):
        self.destinatarios.append(destinatario)

    def enviar_spam(self, mensagem):
        for destinatario in self.destinatarios:
            for canal in self.canais_de_envio:
                yield canal.enviar(destinatario, mensagem)
