titulos = {
    "Flamengo": [3,4,2,2,0],
    "Palmeiras": [0,0,0,2,3],
    "Palmeiras": [0,3,1,3,3],
    "Corinthians": [1,0,0,0,0],
    "Atlético Pr": [3,1,1,0,1],
    "São Paulo": [0,0,1,0,1],
    "Grêmio": [1,0,1,1,1]
}

classificacao = sorted(titulos.items(),key=lambda x: sum(x[1]),reverse=True)

for posicao, (time,_) in enumerate(classificacao):
    print(f"{posicao + 1 }ºlugar: {time}")