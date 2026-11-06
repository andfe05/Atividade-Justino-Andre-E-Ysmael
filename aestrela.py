from algoritmo import carregar_grafo, estrela, h

# pontos marcados no mapa: id, nome, latitude, longitude, destinos (vizinhos)
# e a distância pela rua (em metros) até cada destino
PONTOS = [
    {'id': 0, 'nome': 'Rua Godofredo Messias, 186 (origem)', 'latitude': -6.77222468402999, 'longitude': -43.01354527475154, 'destinos': [1, 4], 'distancias': [186.4, 225.4]},
    {'id': 1, 'nome': 'Godofredo Messias x Av. Bucar Neto', 'latitude': -6.771905064568758, 'longitude': -43.011893034003016, 'destinos': [0, 11], 'distancias': [186.4, 191.9]},
    {'id': 2, 'nome': 'Hotel Rio Parnaíba', 'latitude': -6.7737375466067355, 'longitude': -43.00970435145302, 'destinos': [3, 11], 'distancias': [244.5, 128.5]},
    {'id': 3, 'nome': 'Av. Bucar Neto x BR-343', 'latitude': -6.775229096614921, 'longitude': -43.00811648372066, 'destinos': [2, 7], 'distancias': [244.5, 350.5]},
    {'id': 4, 'nome': 'Desvio p/ R. Júlio Guimarães', 'latitude': -6.77066920065127, 'longitude': -43.01223635673917, 'destinos': [0, 9], 'distancias': [225.4, 237.9]},
    {'id': 5, 'nome': 'R. Júlio Guimarães x BR-230', 'latitude': -6.767941765654126, 'longitude': -43.008781671537704, 'destinos': [6, 9], 'distancias': [357.7, 249.4]},
    {'id': 6, 'nome': 'Jorge Batista (BR-230)', 'latitude': -6.770946204906026, 'longitude': -43.007622957246525, 'destinos': [5, 12], 'distancias': [357.7, 34.2]},
    {'id': 7, 'nome': 'BR-230 x acesso ao Mix', 'latitude': -6.772714766783916, 'longitude': -43.00691485406858, 'destinos': [3, 8, 12], 'distancias': [350.5, 80.2, 178.3]},
    {'id': 8, 'nome': 'Mix Atacarejo (destino)', 'latitude': -6.772480379437803, 'longitude': -43.006228208562696, 'destinos': [7], 'distancias': [80.2]},
    {'id': 9, 'nome': 'R. David Caldas x R. Júlio Guimarães', 'latitude': -6.769348101255239, 'longitude': -43.01054120064482, 'destinos': [4, 5, 10], 'distancias': [237.9, 249.4, 327.9]},
    {'id': 10, 'nome': 'R. David Caldas x R. Heitor Leão', 'latitude': -6.77208909098716, 'longitude': -43.009444847151464, 'destinos': [9, 11, 12], 'distancias': [327.9, 167.6, 241.2]},
    {'id': 11, 'nome': 'R. Heitor Leão x Av. Bucar Neto', 'latitude': -6.773034385714948, 'longitude': -43.010627031333065, 'destinos': [1, 2, 10], 'distancias': [191.9, 128.5, 167.6]},
    {'id': 12, 'nome': 'R. Heitor Leão x BR-230', 'latitude': -6.7712019010062585, 'longitude': -43.007451295868364, 'destinos': [6, 7, 10], 'distancias': [34.2, 178.3, 241.2]},
]


grafo = carregar_grafo(PONTOS)

inicio = 0   # Rua Godofredo Messias, 186
destino = 8  # Mix Atacarejo

caminho, distancia, expandidos = estrela(grafo, inicio, destino)

# mostra a ordem em que o A* analisou os pontos
print(f"{'Passo':>5}  {'Ponto':<45} {'g(n)':>8} {'h(n)':>8} {'f(n)':>8}")
for passo, (ponto, g_p, h_p, f_p) in enumerate(expandidos, start=1):
    nome = f"{ponto} - {grafo[ponto]['nome']}"
    print(f"{passo:>5}  {nome:<45} {g_p:>8.1f} {h_p:>8.1f} {f_p:>8.1f}")

print()
print("Caminho:", " -> ".join(str(p) for p in caminho))
print(f"Distância pela rua: {distancia:.1f} m")
print(f"Distância em linha reta: {h(grafo, inicio, destino):.1f} m")
