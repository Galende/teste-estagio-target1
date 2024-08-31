faturamento = {
    'sp': 67836.43,
    'rj': 36678.66,
    'mg': 29229.88,
    'es': 27165.48,
    'outros': 19849.53
}

total = sum(faturamento.values())

percentuais = {}
for estado, valor in faturamento.items():
    percentual = (valor / total) * 100
    percentuais[estado] = round(percentual, 2)

print("percentual de representação de cada estado:")
for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual}%")