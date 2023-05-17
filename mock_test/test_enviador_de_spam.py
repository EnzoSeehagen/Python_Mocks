from mock_test.enviador_de_spam import EnviadorDeSpam


def test_enviador_de_span():
    assert EnviadorDeSpam() is not None


def test_enviador_possui_destinatarios():
    enviador = EnviadorDeSpam(["enzo@gmail.com"])
    assert enviador.destinatarios == ['enzo@gmail.com']

    enviador.adicionar_destinatarios("messias@gmail.com")
    assert enviador.destinatarios == ["enzo@gmail.com", "messias@gmail.com"]

