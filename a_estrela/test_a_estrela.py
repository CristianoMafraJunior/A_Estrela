import unittest
from a_estrela import A_Estrela


class TestAEstrela(unittest.TestCase):
    def setUp(self):
        self.estrela = A_Estrela()

    def test_caminho_e_custo_para_destino_conhecido(self):
        inicio = "Araçatuba"
        destino = "São Paulo"
        custo_total, caminho = self.estrela.a_estrela(inicio, destino)
        self.assertEqual(custo_total, 651)
        self.assertEqual(
            caminho,
            [
                ("Araçatuba", 0, 490, 490),
                ("Novo Horizonte", 183, 352, 535),
                ("Bauru", 288, 284, 572),
                ("Rio Claro", 469, 157, 626),
                ("Limeira", 495, 134, 629),
                ("Campinas", 551, 85, 636),
                ("Jundiaí", 592, 50, 642),
                ("São Paulo", 651, 0, 651),
            ],
        )

    def test_destino_inalcancavel(self):
        inicio = "Araçatuba"
        destino = "CidadeInexistente"
        custo_total, caminho = self.estrela.a_estrela(inicio, destino)
        self.assertEqual(custo_total, float("inf"))
        self.assertEqual(caminho, [])


if __name__ == "__main__":
    unittest.main()
