import csv

# Definição das regiões e seus estados
regioes = {
    'Norte': ['AC', 'AP', 'AM', 'PA', 'RO', 'RR', 'TO'],
    'Nordeste': ['AL', 'BA', 'CE', 'MA', 'PB', 'PE', 'PI', 'RN', 'SE'],
    'Centro-Oeste': ['DF', 'GO', 'MT', 'MS'],
    'Sudeste': ['ES', 'MG', 'RJ', 'SP'],
    'Sul': ['PR', 'RS', 'SC']
}

# Função para determinar a região com base no estado
def obter_regiao(estado):
    for regiao, estados in regioes.items():
        if estado in estados:
            return regiao
    return None

# Dicionário para acumular a quantidade de pessoas por região
pessoas_por_regiao = {regiao: 0 for regiao in regioes}

# Função processar_linha modificada para contar pessoas por região
def processar_linha(estado, valor):
    global pessoas_por_regiao
    regiao = obter_regiao(estado)
    if regiao is None:
        print(f"Estado não encontrado: {estado}")
        return
    
    # Incrementa a contagem de pessoas para a região do estado atual
    pessoas_por_regiao[regiao] += 1

# Leitura e processamento do arquivo CSV
with open('./202101_BolsaFamilia_Pagamentos.csv', encoding='latin1') as csvfile:
    dialect = csv.Sniffer().sniff(csvfile.read(65536))
    csvfile.seek(0)
    reader = csv.reader(csvfile, dialect)
    
    print("Carregando dados...")
    iniciarEstado = 0
    for row in reader:
        if (row[8] != 'VALOR PARCELA'):  # Excluir cabeçalho ou outras linhas indesejadas
            if (iniciarEstado == 0):
                estadoAnt = row[2]
                iniciarEstado += 1
            processar_linha(row[2], row[8])
    print("*********************")
    print("Quantidade de pessoas que recebem bolsa familia por região:")
    print("\n")
    # Imprime a quantidade de pessoas por região
    for regiao, quantidade in pessoas_por_regiao.items():
        print(f"{regiao}: {quantidade:,} pessoas")
    
    # Calcula e imprime a soma total de pessoas
    total_pessoas = sum(pessoas_por_regiao.values())
    print("\n")
    print(f"Total de pessoas: {total_pessoas:,}")

    print("*********************")


# Grafico
# Importação
import matplotlib.pyplot as plt

# Extrair dados para o gráfico
regioes_grafico = list(pessoas_por_regiao.keys())
quantidade_pessoas = list(pessoas_por_regiao.values())

# Configurar o gráfico
plt.figure(figsize=(10, 6))
plt.bar(regioes_grafico, quantidade_pessoas, color='skyblue')
plt.title('Quantidade de pessoas que recebem Bolsa Família por região')
plt.xlabel('Região')
plt.ylabel('Quantidade de Pessoas')
plt.xticks(rotation=45)  # Rotaciona os rótulos do eixo x para melhor legibilidade

# Adicionar rótulos com valores acima das barras
for i, v in enumerate(quantidade_pessoas):
    plt.text(i, v + 1000, f"{v:,}", ha='center', va='bottom', fontsize=9)

# Exibir o gráfico
plt.tight_layout()
plt.show()
