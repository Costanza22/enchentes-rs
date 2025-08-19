# 📖 Instruções de Uso - RS Impacto

Este documento fornece instruções detalhadas para usar o projeto RS Impacto - Análise de Enchentes no Rio Grande do Sul.

## 🚀 Início Rápido

### 1. Instalação

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/rs-impacto.git
cd rs-impacto

# Instale as dependências
pip install -r requirements.txt
```

### 2. Execução Rápida

```bash
# Análise rápida (recomendado para iniciantes)
python src/analise_rapida.py

# Análise completa
python src/analise_enchentes.py
```

### 3. Uso com Jupyter

```bash
# Inicie o Jupyter
jupyter notebook

# Abra o notebook em notebooks/analise_enchentes.ipynb
```

## 📊 Estrutura dos Dados

### Dataset Principal: `enchentes_rs.csv`

**Colunas disponíveis:**
- `data`: Data da ocorrência (formato: YYYY-MM-DD)
- `regiao`: Região (Metropolitana ou Serra)
- `cidade`: Nome da cidade
- `mortes`: Número de vítimas fatais
- `feridos`: Número de pessoas feridas
- `desalojados`: Número de pessoas desalojadas
- `prejuizo_milhoes`: Prejuízo econômico em milhões de reais
- `altura_rio_metros`: Altura do rio em metros
- `chuva_24h_mm`: Precipitação em 24 horas (mm)

**Exemplo de dados:**
```csv
data,regiao,cidade,mortes,feridos,desalojados,prejuizo_milhoes,altura_rio_metros,chuva_24h_mm
2020-01-15,Metropolitana,Porto Alegre,2,15,120,5.2,3.8,45.2
2020-02-20,Serra,Caxias do Sul,1,8,85,3.1,2.9,38.7
```

### Dataset Crise 2024: `enchente_2024_detalhado.csv`

**Colunas disponíveis:**
- Mesmas colunas do dataset principal
- **Período específico**: 28/04/2024 a 05/05/2024
- **Dados diários** da crise histórica

## 🔬 Funcionalidades Disponíveis

### 1. Análise Temporal

**O que faz:**
- Mostra evolução dos impactos ao longo dos anos
- Identifica tendências e padrões temporais
- Compara diferentes períodos

**Como usar:**
```python
from src.analise_enchentes import analise_temporal

# Execute a análise temporal
df_anual = analise_temporal(df_principal, df_2024)
```

**Resultados:**
- Gráficos de linha mostrando evolução
- Tabelas com agregações anuais
- Estatísticas de tendência

### 2. Análise Regional

**O que faz:**
- Compara impactos entre regiões
- Analisa vulnerabilidades por cidade
- Identifica padrões geográficos

**Como usar:**
```python
from src.analise_enchentes import analise_regional

# Execute a análise regional
df_regional, df_cidades = analise_regional(df_principal)
```

**Resultados:**
- Gráficos de barras comparativos
- Rankings de cidades por impacto
- Análise de concentração regional

### 3. Análise da Crise 2024

**O que faz:**
- Foco específico na crise histórica
- Evolução diária dos impactos
- Comparação com períodos anteriores

**Como usar:**
```python
from src.analise_enchentes import analise_crise_2024

# Execute a análise da crise
df_2024_diario = analise_crise_2024(df_2024)
```

**Resultados:**
- Gráficos de evolução diária
- Estatísticas da crise
- Comparações temporais

### 4. Análise de Correlações

**O que faz:**
- Identifica relações entre variáveis
- Mostra padrões de associação
- Ajuda na compreensão de causas

**Como usar:**
```python
from src.analise_enchentes import analise_correlacoes

# Execute a análise de correlações
correlacao = analise_correlacoes(df_principal)
```

**Resultados:**
- Matriz de correlação
- Gráficos de dispersão
- Análise de relações

### 5. Análise Sazonal

**O que faz:**
- Identifica padrões mensais
- Mostra sazonalidade dos impactos
- Ajuda no planejamento preventivo

**Como usar:**
```python
from src.analise_enchentes import analise_sazonal

# Execute a análise sazonal
df_sazonal = analise_sazonal(df_principal)
```

**Resultados:**
- Gráficos de padrões mensais
- Estatísticas sazonais
- Identificação de picos

## 🎯 Casos de Uso Comuns

### Para Pesquisadores

```python
# Carregar dados
import pandas as pd
df = pd.read_csv('data/enchentes_rs.csv')

# Análise estatística básica
print(df.describe())

# Análise por região
impactos_regionais = df.groupby('regiao').agg({
    'mortes': ['sum', 'mean', 'std'],
    'prejuizo_milhoes': ['sum', 'mean', 'std']
})
```

### Para Educadores

```python
# Exemplo para aulas de estatística
from src.analise_enchentes import explorar_dados

# Mostrar estrutura dos dados
explorar_dados(df_principal, df_2024)

# Análise de correlações para discussão
correlacao = analise_correlacoes(df_principal)
```

### Para Analistas de Dados

```python
# Análise personalizada
df_metropolitana = df[df['regiao'] == 'Metropolitana']
df_serra = df[df['regiao'] == 'Serra']

# Comparação estatística
from scipy import stats
t_stat, p_value = stats.ttest_ind(
    df_metropolitana['prejuizo_milhoes'],
    df_serra['prejuizo_milhoes']
)
```

## 📈 Personalizando as Análises

### Modificando Gráficos

```python
import matplotlib.pyplot as plt

# Personalizar estilo
plt.style.use('seaborn-v0_8')
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 12

# Criar gráfico personalizado
plt.figure(figsize=(15, 10))
# ... seu código de gráfico ...
plt.title('Meu Gráfico Personalizado', fontsize=16, fontweight='bold')
plt.show()
```

### Adicionando Novas Análises

```python
def minha_analise_personalizada(df):
    """Minha análise personalizada"""
    
    # Sua lógica aqui
    resultado = df.groupby('cidade').agg({
        'mortes': 'sum',
        'prejuizo_milhoes': 'sum'
    }).sort_values('prejuizo_milhoes', ascending=False)
    
    # Visualização
    plt.figure(figsize=(10, 6))
    resultado['prejuizo_milhoes'].plot(kind='bar')
    plt.title('Prejuízos por Cidade')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    
    return resultado

# Use sua análise
minha_analise = minha_analise_personalizada(df_principal)
```

## 🚨 Solução de Problemas

### Erro: "Arquivo não encontrado"

**Problema:** Script não consegue encontrar os arquivos CSV

**Solução:**
```bash
# Verifique se está na pasta correta
pwd  # Linux/Mac
cd   # Windows

# Verifique se os arquivos existem
ls data/  # Linux/Mac
dir data\  # Windows
```

### Erro: "Módulo não encontrado"

**Problema:** Bibliotecas Python não instaladas

**Solução:**
```bash
# Instale as dependências
pip install -r requirements.txt

# Ou instale individualmente
pip install pandas numpy matplotlib seaborn jupyter
```

### Erro: "Dados vazios"

**Problema:** DataFrame está vazio após carregamento

**Solução:**
```python
# Verifique os dados
print(df.shape)
print(df.head())
print(df.columns)

# Verifique o caminho do arquivo
import os
print(os.path.exists('data/enchentes_rs.csv'))
```

### Gráficos não aparecem

**Problema:** Gráficos não são exibidos

**Solução:**
```python
# Para Jupyter
%matplotlib inline

# Para scripts Python
plt.show()

# Para salvar em arquivo
plt.savefig('meu_grafico.png', dpi=300, bbox_inches='tight')
```

## 🔧 Configurações Avançadas

### Configurando Matplotlib

```python
import matplotlib.pyplot as plt
import seaborn as sns

# Configurações globais
plt.rcParams['figure.dpi'] = 100
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['font.size'] = 10
plt.rcParams['axes.titlesize'] = 12
plt.rcParams['axes.labelsize'] = 10

# Configurar Seaborn
sns.set_style("whitegrid")
sns.set_palette("husl")
```

### Configurando Pandas

```python
import pandas as pd

# Configurações de exibição
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', 50)
pd.set_option('display.width', 1000)
pd.set_option('display.precision', 2)
```

### Configurando Logs

```python
import logging

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('rs_impacto.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
logger.info('Iniciando análise...')
```

## 📊 Exportando Resultados

### Salvando Gráficos

```python
# Salvar gráfico atual
plt.savefig('outputs/meu_grafico.png', dpi=300, bbox_inches='tight')

# Salvar múltiplos gráficos
fig, axes = plt.subplots(2, 2, figsize=(15, 10))
# ... criar gráficos ...
plt.savefig('outputs/analise_completa.png', dpi=300, bbox_inches='tight')
```

### Exportando Dados

```python
# Exportar para CSV
df_resultado.to_csv('outputs/resultado_analise.csv', index=False)

# Exportar para Excel
df_resultado.to_excel('outputs/resultado_analise.xlsx', index=False)

# Exportar para JSON
df_resultado.to_json('outputs/resultado_analise.json', orient='records')
```

### Criando Relatórios

```python
# Relatório em texto
with open('outputs/relatorio.txt', 'w', encoding='utf-8') as f:
    f.write("RELATÓRIO DE ANÁLISE\n")
    f.write("=" * 50 + "\n")
    f.write(f"Total de registros: {len(df)}\n")
    f.write(f"Período: {df['data'].min()} a {df['data'].max()}\n")
    # ... mais informações ...
```

## 🌟 Dicas e Truques

### Performance

```python
# Para datasets grandes, use chunks
for chunk in pd.read_csv('data/enchentes_rs.csv', chunksize=1000):
    # Processar cada chunk
    processar_chunk(chunk)

# Use métodos vetorizados do pandas
# ❌ Ruim
for i in range(len(df)):
    df.loc[i, 'nova_coluna'] = df.loc[i, 'coluna'] * 2

# ✅ Bom
df['nova_coluna'] = df['coluna'] * 2
```

### Visualização

```python
# Use cores consistentes
cores = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']

# Adicione anotações úteis
plt.annotate('Pico máximo', xy=(x_max, y_max), 
             xytext=(x_max+1, y_max+10),
             arrowprops=dict(arrowstyle='->', color='red'))

# Use temas consistentes
plt.style.use('seaborn-v0_8-darkgrid')
```

### Debugging

```python
# Verificar dados em cada etapa
def analise_com_debug(df):
    print(f"Shape inicial: {df.shape}")
    print(f"Colunas: {df.columns.tolist()}")
    print(f"Tipos: {df.dtypes}")
    
    # Sua análise aqui
    resultado = df.groupby('regiao').sum()
    
    print(f"Resultado: {resultado.shape}")
    return resultado
```

## 📞 Suporte e Ajuda

### Recursos Adicionais

- **Documentação Python**: [docs.python.org](https://docs.python.org/)
- **Pandas**: [pandas.pydata.org](https://pandas.pydata.org/)
- **Matplotlib**: [matplotlib.org](https://matplotlib.org/)
- **Seaborn**: [seaborn.pydata.org](https://seaborn.pydata.org/)

### Comunidade

- **GitHub Issues**: Para bugs e problemas
- **GitHub Discussions**: Para dúvidas e discussões
- **Stack Overflow**: Para perguntas técnicas

### Contato Direto

- **Email**: [seu-email@exemplo.com](mailto:seu-email@exemplo.com)
- **GitHub**: [@seu-usuario](https://github.com/seu-usuario)

---

## 🎯 Próximos Passos

1. **Execute** a análise rápida para familiarizar-se
2. **Explore** os notebooks interativos
3. **Personalize** as análises para suas necessidades
4. **Contribua** com melhorias e novas funcionalidades
5. **Compartilhe** seus insights e descobertas

**Boa análise! 🌊📊**
