# 🌊 Enchentes no Rio Grande do Sul - Análise de Impactos (2020-2024)

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-CC0%201.0-green.svg)](https://creativecommons.org/publicdomain/zero/1.0/)
[![Kaggle](https://img.shields.io/badge/Kaggle-Dataset-orange.svg)](https://www.kaggle.com/)

Análise completa dos impactos das enchentes no Rio Grande do Sul, incluindo a crise histórica de 2024. Este projeto fornece dados, análises e visualizações para compreender padrões temporais, vulnerabilidades regionais e correlações entre variáveis.

## 📋 Sobre o Projeto

Este projeto foi desenvolvido para analisar os impactos das enchentes no Rio Grande do Sul entre 2020 e 2024, com foco especial na crise histórica de abril-maio de 2024. Os dados incluem estatísticas sobre vítimas, desalojados, prejuízos econômicos e indicadores hidrológicos.

## 🎯 Objetivos

- **Análise Temporal**: Evolução dos impactos ao longo dos anos
- **Análise Regional**: Comparação entre Metropolitana e Serra
- **Análise da Crise 2024**: Dados detalhados da emergência
- **Correlações**: Relações entre variáveis hidrológicas e sociais
- **Insights**: Padrões e vulnerabilidades identificadas

## 📊 Estrutura do Projeto

```
RS Impacto/
├── 📁 data/                          # Datasets CSV
│   ├── enchentes_rs.csv             # 60 registros (2020-2024)
│   └── enchente_2024_detalhado.csv  # 32 registros da crise 2024
├── 📁 src/                           # Scripts de análise
│   ├── analise_enchentes.py         # Análise completa
│   ├── analise_rapida.py            # Análise rápida
│   └── preparar_kaggle.py           # Script para Kaggle
├── 📁 notebooks/                     # Jupyter notebooks
│   ├── analise_enchentes.ipynb      # Notebook principal
│   └── analise_enchentes_kaggle.py  # Script para Kaggle
├── 📁 docs/                          # Documentação
│   └── fontes_dados.md              # Fontes dos dados
├── 📁 exemplos/                      # Exemplos de uso
│   └── exemplo_analise.py           # Exemplos práticos
├── 📁 outputs/                       # Resultados e relatórios
├── 📄 README.md                      # Este arquivo
├── 📄 requirements.txt               # Dependências Python
├── 📄 INSTRUCOES.md                  # Instruções de uso
└── 📄 .gitignore                     # Arquivos ignorados pelo Git
```

## 🚀 Como Usar

### Pré-requisitos

- Python 3.8+
- pip (gerenciador de pacotes Python)

### Instalação

1. **Clone o repositório**
```bash
git clone https://github.com/seu-usuario/rs-impacto.git
cd rs-impacto
```

2. **Instale as dependências**
```bash
pip install -r requirements.txt
```

3. **Execute a análise**
```bash
# Análise rápida
python src/analise_rapida.py

# Análise completa
python src/analise_enchentes.py

# Preparar para Kaggle
python src/preparar_kaggle.py
```

### Uso com Jupyter

```bash
# Inicie o Jupyter
jupyter notebook

# Abra o notebook em notebooks/analise_enchentes.ipynb
```

## 📊 Datasets

### Dataset Principal: `enchentes_rs.csv`
- **Período**: 2020-2024
- **Registros**: 60
- **Cidades**: 6 principais cidades do RS
- **Regiões**: Metropolitana e Serra

**Colunas:**
- `data`: Data da ocorrência
- `regiao`: Região (Metropolitana/Serra)
- `cidade`: Nome da cidade
- `mortes`: Número de vítimas fatais
- `feridos`: Número de pessoas feridas
- `desalojados`: Número de pessoas desalojadas
- `prejuizo_milhoes`: Prejuízo econômico em milhões de reais
- `altura_rio_metros`: Altura do rio em metros
- `chuva_24h_mm`: Precipitação em 24 horas (mm)

### Dataset Crise 2024: `enchente_2024_detalhado.csv`
- **Período**: 28/04/2024 - 05/05/2024
- **Registros**: 32
- **Cidades**: 4 cidades mais afetadas
- **Dados**: Evolução diária da crise

## 🔬 Funcionalidades

### Análises Disponíveis

- **📅 Análise Temporal**: Evolução dos impactos ao longo dos anos
- **🌍 Análise Regional**: Comparação entre regiões e cidades
- **🚨 Análise da Crise 2024**: Dados detalhados da emergência
- **🔗 Correlações**: Relações entre variáveis hidrológicas e sociais
- **📊 Análise Sazonal**: Padrões mensais dos impactos
- **🎯 Insights**: Padrões e vulnerabilidades identificadas

### Visualizações

- Gráficos de linha para evolução temporal
- Gráficos de barras para comparações regionais
- Heatmaps para correlações
- Gráficos de dispersão para relações entre variáveis
- Gráficos sazonais para padrões mensais

## 📚 Documentação

- **[INSTRUCOES.md](INSTRUCOES.md)**: Instruções detalhadas de uso
- **[docs/fontes_dados.md](docs/fontes_dados.md)**: Fontes e metodologia dos dados
- **[exemplos/exemplo_analise.py](exemplos/exemplo_analise.py)**: Exemplos práticos de uso

## 🌟 Exemplos de Uso

### Análise Básica
```python
import pandas as pd
from src.analise_enchentes import AnalisadorEnchentes

# Carregar e analisar dados
analisador = AnalisadorEnchentes()
analisador.executar_analise_completa()
```

### Análise Personalizada
```python
# Carregar dados
df = pd.read_csv('data/enchentes_rs.csv')

# Análise por região
impactos_regionais = df.groupby('regiao').agg({
    'desalojados': 'sum',
    'prejuizo_milhoes': 'sum'
})
```

## 🚀 Deploy no Kaggle

Para usar este projeto no Kaggle:

1. **Execute o script de preparação**
```bash
python src/preparar_kaggle.py
```

2. **Faça upload da pasta `enchentes-rs-kaggle/` no Kaggle**
3. **Crie um notebook conectado ao dataset**
4. **Cole o código de análise**

## 🤝 Contribuições

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está licenciado sob a licença CC0-1.0 (Domínio Público) - veja o arquivo [LICENSE](LICENSE) para detalhes.

