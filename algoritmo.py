import math
from queue import PriorityQueue

RAIO_TERRA = 6_371_000  # metros


def carregar_grafo(pontos):
    '''transforma a lista PONTOS em:
    {id: {"nome", "lat", "lon", "vizinhos": {id_vizinho: distancia_pela_rua}}}'''
    grafo = {}
    for ponto in pontos:
        grafo[ponto["id"]] = {
            "nome": ponto["nome"],
            "lat": ponto["latitude"],
            "lon": ponto["longitude"],
            # destinos [1, 4] + distancias [186.4, 225.4] -> {1: 186.4, 4: 225.4}
            "vizinhos": dict(zip(ponto["destinos"], ponto["distancias"])),
        }
    return grafo


def h(grafo, ponto, destino):
    '''heurística: distância em linha reta (euclidiana) do ponto até o destino, em metros.
    as coordenadas estão em graus, então primeiro converte a diferença para metros
    e depois aplica Pitágoras'''
    p1, p2 = grafo[ponto], grafo[destino]
    lat_media = math.radians((p1["lat"] + p2["lat"]) / 2)
    dx = math.radians(p2["lon"] - p1["lon"]) * math.cos(lat_media) * RAIO_TERRA
    dy = math.radians(p2["lat"] - p1["lat"]) * RAIO_TERRA
    return math.sqrt(dx ** 2 + dy ** 2)


def estrela(grafo, inicio, destino):
    # f = g + h de cada ponto. começa tudo em infinito porque ainda não visitamos nada
    f = {ponto: float("inf") for ponto in grafo}
    g = {ponto: float("inf") for ponto in grafo}

    g[inicio] = 0
    f[inicio] = g[inicio] + h(grafo, inicio, destino)

    # fila de prioridade: sempre sai o ponto com menor f (em empate, o menor h)
    fila = PriorityQueue()
    fila.put((f[inicio], h(grafo, inicio, destino), inicio))

    caminho = {}      # caminho[vizinho] = ponto de onde eu vim
    expandidos = []   # ordem em que os pontos foram analisados (para a tabela)

    while not fila.empty():
        f_item, h_item, ponto_atual = fila.get()

        # se esse ponto já foi achado depois com um f menor, essa entrada está velha
        if f_item > f[ponto_atual]:
            continue

        expandidos.append((ponto_atual, g[ponto_atual], h_item, f_item))

        if ponto_atual == destino:
            break

        # olha cada vizinho do ponto atual (no labirinto eram as direções N, S, L, O)
        for vizinho, distancia_rua in grafo[ponto_atual]["vizinhos"].items():
            novo_g = g[ponto_atual] + distancia_rua
            novo_f = novo_g + h(grafo, vizinho, destino)

            # só atualiza se achou um caminho melhor até esse vizinho
            if novo_f < f[vizinho]:
                g[vizinho] = novo_g
                f[vizinho] = novo_f
                fila.put((novo_f, h(grafo, vizinho, destino), vizinho))
                caminho[vizinho] = ponto_atual

    if g[destino] == float("inf"):
        return [], float("inf"), expandidos

    # monta o caminho de trás pra frente: destino -> ... -> início
    caminho_final = [destino]
    while caminho_final[-1] != inicio:
        caminho_final.append(caminho[caminho_final[-1]])
    caminho_final.reverse()

    return caminho_final, g[destino], expandidos
