import heapq


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
        fila_prioridade = []
        heapq.heappush(fila_prioridade, (0, inicio))
        visitados = set()
        caminho_percorrido = {inicio: None}
        custo_total = {cidade: float("inf") for cidade in self.cidades}
        custo_total[inicio] = 0

        while fila_prioridade:
            custo_atual, cidade_atual = heapq.heappop(fila_prioridade)

            if cidade_atual == destino:
                caminho = self.reconstruir_caminho(
                    caminho_percorrido, destino, custo_total
                )
                return custo_total[destino], caminho

            if cidade_atual in visitados:
                continue

            visitados.add(cidade_atual)

            for vizinho, custo in self.cidades[cidade_atual].items():
                novo_custo = custo_total[cidade_atual] + custo
                custo_heuristica = self.heuristica[vizinho]
                if novo_custo < custo_total[vizinho]:
                    custo_total[vizinho] = novo_custo
                    heapq.heappush(
                        fila_prioridade, (novo_custo + custo_heuristica, vizinho)
                    )
                    caminho_percorrido[vizinho] = cidade_atual

        return float("inf"), []

    def reconstruir_caminho(self, caminho_percorrido, destino, custo_total):
        caminho = []
        cidade = destino
        while cidade is not None:
            caminho.append(
                (
                    cidade,
                    custo_total[cidade],
                    self.heuristica[cidade],
                    custo_total[cidade] + self.heuristica[cidade],
                )
            )
            cidade = caminho_percorrido[cidade]
        return list(reversed(caminho))


# Exemplo de uso
estrela = A_Estrela()
inicio = "Araçatuba"
destino = "São Paulo"
custo_total, caminho = estrela.a_estrela(inicio, destino)
print(f"Custo total de {inicio} a {destino}: {custo_total}")
print("Caminho percorrido:")
for cidade, custo_atual, heuristica, total in caminho:
    print(
        f" - {cidade}: Custo atual: {custo_atual}, Heurística: {heuristica}, Total: {total}"
    )
