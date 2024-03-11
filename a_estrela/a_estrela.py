# Lista de cidades
cidades = [
    "São Paulo",
    "Santos",
    "Capivariano",
    "Bauru",
]

# Matriz de distâncias entre as cidades (em quilômetros)
distancias_entre_cidades = [
    [0, 81, 203, 349],
    [81, 0, 164, 290],
    [203, 164, 0, 155],
    [349, 290, 155, 0],
]

distancias_linha_reta = []


cidade1 = input("Ponto Inicial: ")
cidade2 = input("Ponto Final: ")

if cidade1 in cidades and cidade2 in cidades:
    # Obter Índices
    indice_cidade1 = cidades.index(cidade1)
    indice_cidade2 = cidades.index(cidade2)

    quilometragem = distancias_entre_cidades[indice_cidade1][indice_cidade2]

    print(f"Quilometragem entre {cidade1} e {cidade2}: {quilometragem} km")
else:
    print("Cidades não encontradas")
