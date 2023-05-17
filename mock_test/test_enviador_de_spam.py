from mock_test.enviador_de_spam import EnviadorDeSpam, CanalEmail, CanalMock


def test_enviador_de_span():
    assert EnviadorDeSpam() is not None


def test_enviador_possui_destinatarios():
    enviador = EnviadorDeSpam(["enzo@gmail.com"])
    assert enviador.destinatarios == ['enzo@gmail.com']

    enviador.adicionar_destinatarios("messias@gmail.com")
    assert enviador.destinatarios == ["enzo@gmail.com", "messias@gmail.com"]


def test_envio_de_spam():
    enviador = EnviadorDeSpam(["enzo@gmail.com"])
    enviador.canais_de_envio=[CanalMock()]

    assert list(enviador.enviar_spam("Spam enviado")) == [
        ("enzo@gmail.com", "Spam enviado para Enzo")
    ]

def test_canal_foi_executado():
    enviador = EnviadorDeSpam(["enzo@gmail.com"])
    canal = CanalMock
    enviador.canais_de_envio = [canal]
    list(enviador.enviar_spam("Spam enviado"))

    assert canal.enviar_foi_chamado
    assert canal.enviar_argumento == ["enzo@gmail.com', "Spam enviado"]