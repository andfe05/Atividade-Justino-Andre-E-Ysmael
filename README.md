<img width="1186" height="900" alt="95b64458-c36f-40a6-92ac-6e185408e738" src="https://github.com/user-attachments/assets/d121cdc8-4a41-4902-8e16-0dfd6e272e9f" /># A* em Floriano 🗺️

Implementação do algoritmo A* (A estrela) pra achar o menor caminho entre dois pontos de Floriano-PI, saindo da Rua Godofredo Messias, 186 (Catumbi) até o Mix Atacarejo.

A ideia foi pegar um pedaço do mapa da cidade, marcar os cruzamentos como pontos (nós), ligar os pontos vizinhos com a distância pela rua e deixar o A* descobrir o melhor caminho.

## O mapa

Primeiro tirei o print no Google Maps com a rota de carro entre os dois lugares. Ele mostrou duas opções, de 1,1 km e 1,3 km:

<img width="593" height="450" alt="mapa_rota_maps" src="https://github.com/user-attachments/assets/ebc022b6-01da-48dd-96f2-39785c364bb4" />

Depois marquei 13 pontos e as distâncias de cada trecho. Os pontos em vermelho ficam em cima das rotas do Maps, e os azuis são cruzamentos de ruas que ligam uma rota na outra, pra dar mais caminhos pro A* comparar:
<img width="1186" height="900" alt="95b64458-c36f-40a6-92ac-6e185408e738" src="https://github.com/user-attachments/assets/70f65715-9f1a-4876-a47b-d59bd01836f4" />

## Como o A* funciona

Pra cada ponto ele calcula:

- **g(n)**: quanto já andei até chegar nesse ponto (distância real pela rua)
- **h(n)**: quanto acho que ainda falta até o destino (distância em linha reta)
- **f(n) = g(n) + h(n)**

A cada passo ele pega o ponto com o menor `f` e continua dali, até chegar no destino.

O `h(n)` é a distância euclidiana calculada a partir da latitude e longitude, já convertida pra metros. Como a linha reta nunca é maior que o caminho pela rua, o A* sempre acha o menor caminho.

## Arquivos

- `algoritmo.py`: as funções do A* (`h`, `estrela` e `carregar_grafo`)
- `aestrela.py`: os pontos do mapa, a origem, o destino e a parte que roda tudo

## Como rodar

Só precisa do Python 3, sem instalar nada. Com os dois arquivos na mesma pasta:

```bash
python aestrela.py
```

Pra testar outra origem ou outro destino, é só trocar as variáveis `inicio` e `destino` no `aestrela.py`.

## Resultado

```
Caminho: 0 -> 1 -> 11 -> 10 -> 12 -> 7 -> 8
Distância pela rua: 1045.6 m
Distância em linha reta: 808.4 m
```

Ou seja: sai da Godofredo Messias, pega a Av. Bucar Neto, corta pela R. Heitor Leão até a BR-230 e chega no Mix.

Dos 13 pontos marcados, o algoritmo só precisou analisar 9. Os outros ficaram de fora porque já dava pra ver que não compensava ir por eles.

## E o Google Maps?

O caminho do A* ficou uns 136 m mais curto que a rota principal do Maps (1.182 m). Isso acontece porque o A* procura a **menor distância**, enquanto o Maps procura o **menor tempo** e prefere ir pelas avenidas em vez de cortar por dentro do bairro.

Uma limitação: o grafo considera que todas as ruas são mão dupla. Se alguma for mão única, é só tirar a ligação no sentido proibido na lista `PONTOS`.
