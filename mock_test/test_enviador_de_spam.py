from unittest.mock import Mock

from mock_test.enviador_de_spam import EnviadorDeSpam, CanalEmail


def test_enviador_de_span():
    assert EnviadorDeSpam() is not None


def test_enviador_possui_destinatarios():
    enviador = EnviadorDeSpam(["enzo@gmail.com"])
    assert enviador.destinatarios == ['enzo@gmail.com']

    enviador.adicionar_destinatarios("messias@gmail.com")
    assert enviador.destinatarios == ["enzo@gmail.com", "messias@gmail.com"]


def test_envio_de_spam():
    enviador = EnviadorDeSpam(["enzo@gmail.com"])
    canal = Mock()
    canal.enviar.return_value=("enzo@gmail.com", "Spam enviado para Enzo")
    enviador.canais_de_envio=[canal]

    assert list(enviador.enviar_spam("Spam enviado")) == [
        ("enzo@gmail.com", "Spam enviado para Enzo")
    ]

def test_canal_foi_executado():
    enviador = EnviadorDeSpam(["enzo@gmail.com"])
    canal = Mock()
    enviador.canais_de_envio = [canal]
    list(enviador.enviar_spam("Spam enviado"))

    canal.enviar.assert_called_once_with("enzo@gmail.com", "Spam enviado")