# 🌊 Enchentes no Rio Grande do Sul - Impactos e Análises (2020-2024)

## 📋 Sobre este Dataset

Este dataset contém informações completas sobre os impactos das enchentes no Rio Grande do Sul, Brasil, incluindo a crise histórica de 2024. Os dados incluem estatísticas sobre vítimas, desalojados, prejuízos econômicos e indicadores hidrológicos.

## 🚨 Contexto Histórico

O Rio Grande do Sul enfrentou uma das maiores crises de enchentes de sua história em abril-maio de 2024, com impactos devastadores em toda a região metropolitana e serra. Este dataset permite analisar a evolução dos impactos ao longo dos anos e compreender os padrões de vulnerabilidade regional.

## 📊 Estrutura dos Dados

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

**Colunas adicionais:**
- `status_emergencia`: Status da emergência (Declarada)

## 🏙️ Cidades Monitoradas

### Região Metropolitana:
- **Porto Alegre**: Capital do estado
- **Canoas**: Cidade vizinha à capital
- **São Leopoldo**: Importante centro industrial

### Região Serra:
- **Santa Maria**: Maior cidade do interior
- **Caxias do Sul**: Principal cidade da serra
- **Bento Gonçalves**: Capital do vinho

## 📈 Principais Insights dos Dados

### 1. **Tendências Temporais**
- Aumento gradual dos impactos de 2020 a 2024
- Picos sazonais nos meses de abril e maio
- Crise de 2024 sem precedentes históricos

### 2. **Vulnerabilidades Regionais**
- Região metropolitana concentra os maiores impactos
- Porto Alegre é a cidade mais afetada
- Serra apresenta impactos menores mas significativos

### 3. **Correlações Identificadas**
- Forte correlação entre altura do rio e número de desalojados
- Relação direta entre precipitação e prejuízos econômicos
- Padrões consistentes de resposta a emergências

## 🎯 Possibilidades de Análise

### **Análises Temporais**
- Evolução dos impactos ao longo dos anos
- Padrões sazonais e tendências
- Comparação entre diferentes períodos

### **Análises Regionais**
- Comparação entre Metropolitana e Serra
- Vulnerabilidades específicas por cidade
- Capacidade de resposta regional

### **Análises de Impacto**
- Correlação entre variáveis hidrológicas e sociais
- Análise de custos e prejuízos
- Eficiência dos sistemas de alerta

### **Análises de Crise**
- Evolução da crise de 2024
- Comparação com eventos anteriores
- Lições aprendidas e recomendações

## 🔬 Exemplos de Uso

### **1. Análise de Vulnerabilidade**
```python
# Identificar cidades mais vulneráveis
df_vulnerabilidade = df.groupby('cidade').agg({
    'desalojados': 'mean',
    'prejuizo_milhoes': 'mean'
}).sort_values('desalojados', ascending=False)
```

### **2. Análise Sazonal**
```python
# Padrões mensais de enchentes
df_sazonal = df.groupby(df['data'].dt.month).agg({
    'desalojados': 'sum',
    'prejuizo_milhoes': 'sum'
})
```

### **3. Análise de Correlação**
```python
# Correlação entre altura do rio e impactos
correlacao = df[['altura_rio_metros', 'desalojados', 'prejuizo_milhoes']].corr()
```

## 📚 Fontes dos Dados

- **Defesa Civil do RS**: Registros oficiais de emergências
- **IBGE**: Dados demográficos e socioeconômicos
- **CEPED**: Estudos sobre desastres naturais
- **ANA**: Dados hidrológicos e meteorológicos
- **Governo do RS**: Relatórios oficiais e declarações

## 🚀 Como Usar

1. **Download** dos arquivos CSV
2. **Carregamento** em Python com pandas
3. **Análise** usando as variáveis disponíveis
4. **Visualização** com matplotlib, seaborn ou plotly
5. **Modelagem** para previsões futuras

## 📊 Estatísticas Rápidas

- **Total de registros**: 92 (60 + 32)
- **Período coberto**: 4 anos e 4 meses
- **Cidades monitoradas**: 6
- **Regiões**: 2
- **Variáveis**: 8-9 por registro

## 🔗 Notebooks Relacionados

- **Análise Completa**: Notebook com análise completa dos dados
- **Visualizações**: Gráficos e dashboards interativos
- **Modelos**: Análises preditivas e estatísticas avançadas

## 📞 Contribuições e Dúvidas

Este dataset é parte de um projeto maior de análise de desastres naturais. Contribuições, sugestões e dúvidas são bem-vindas através dos comentários no Kaggle.

## 📄 Licença

Este dataset está disponível sob licença CC0-1.0 (domínio público), permitindo uso livre para pesquisa, educação e aplicações comerciais.

---

**🎉 Use este dataset para entender melhor os impactos das enchentes no RS e contribuir para soluções futuras!**
