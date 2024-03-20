class A_Estrela:
    def __init__(self):
        self.cidades = {
            "Araçatuba": {"Votuporanga": 127, "Novo Horizonte": 183, "Marília": 170},
            "Votuporanga": {"Araçatuba": 127, "Barretos": 179},
            "Barretos": {"Votuporanga": 179, "Araraquara": 152, "Marília": 161},
            "Marília": {"Barretos": 161, "Araçatuba": 170, "Novo Horizonte": 141},
            "Novo Horizonte": {"Araçatuba": 183, "Bauru": 105, "Marília": 141},
            "Bauru": {"Novo Horizonte": 105, "Rio Claro": 181, "Araraquara": 129},
            "Araraquara": {"Barretos": 152, "Bauru": 129, "Rio Claro": 105},
            "Rio Claro": {
                "Araraquara": 105,
                "Limeira": 26,
                "Piracicaba": 40,
                "Bauru": 181,
            },
            "Piracicaba": {"Rio Claro": 40, "Limeira": 35},
            "Limeira": {
                "Rio Claro": 26,
                "Piracicaba": 35,
                "Sorocaba": 138,
                "Campinas": 56,
            },
            "Sorocaba": {"Limeira": 138, "Campinas": 90, "Santos": 104},
            "Campinas": {"Limeira": 56, "Sorocaba": 90, "Jundiaí": 41},
            "Jundiaí": {"Campinas": 41, "São Paulo": 59},
            "São Paulo": {"Jundiaí": 59, "Santos": 81},
            "Santos": {"Sorocaba": 104, "São Paulo": 81},
        }

        self.heuristica = {
            "São Paulo": 0,
            "Santos": 50,
            "Jundiaí": 50,
            "Campinas": 85,
            "Sorocaba": 86,
            "Limeira": 134,
            "Piracicaba": 137,
            "Rio Claro": 157,
            "Araraquara": 255,
            "Bauru": 284,
            "Novo Horizonte": 352,
            "Marília": 370,
            "Barretos": 386,
            "Votuporanga": 471,
            "Araçatuba": 490,
        }

    def a_estrela(self, inicio, destino):
        pass
