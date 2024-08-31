import json

with open('faturamento.json') as arquivo:
    dados = json.load(arquivo)

faturamento = [dia['valor'] for dia in dados['faturamento'] if dia['valor'] > 0]

menor_valor = min(faturamento)

maior_valor = max(faturamento)

media_mensal = sum(faturamento) / len(faturamento)

dias_superior_media = len([dia for dia in faturamento if dia > media_mensal])

print("menor valor de faturamento: {:.2f}".format(menor_valor))
print("maior valor de faturamento:", maior_valor)
print("número de dias com faturamento superior à média mensal:", dias_superior_media)