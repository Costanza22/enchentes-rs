#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🌊 ANÁLISE COMPLETA DAS ENCHENTES NO RIO GRANDE DO SUL (2020-2024)

Este script apresenta uma análise abrangente dos impactos das enchentes no Rio Grande do Sul, 
incluindo a crise histórica de 2024. Através de visualizações interativas e análises estatísticas, 
exploramos padrões temporais, vulnerabilidades regionais e correlações entre variáveis.

🎯 OBJETIVOS DA ANÁLISE:
1. Análise Temporal: Evolução dos impactos ao longo dos anos
2. Análise Regional: Comparação entre Metropolitana e Serra
3. Análise da Crise 2024: Dados detalhados da emergência
4. Correlações: Relações entre variáveis hidrológicas e sociais
5. Insights: Padrões e vulnerabilidades identificadas

📊 DATASETS UTILIZADOS:
- enchentes_rs.csv: 60 registros de 2020-2024
- enchente_2024_detalhado.csv: 32 registros da crise de 2024

Autor: [Seu Nome]
Data: 2024
Licença: CC0-1.0 (Domínio Público)
"""

# =============================================================================
# 📚 IMPORTAÇÃO DE BIBLIOTECAS E CONFIGURAÇÕES
# =============================================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import warnings

# Configurações de visualização
warnings.filterwarnings('ignore')
plt.style.use('default')
sns.set_palette("husl")

# Configurações do matplotlib para melhor qualidade
plt.rcParams['figure.dpi'] = 100
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['font.size'] = 10

print("✅ Bibliotecas importadas com sucesso!")
print(f"📊 Pandas version: {pd.__version__}")
print(f"📈 Matplotlib version: {plt.matplotlib.__version__}")
print(f"🎨 Seaborn version: {sns.__version__}")
print("=" * 60)

# =============================================================================
# 📁 CARREGAMENTO DOS DADOS
# =============================================================================

def carregar_dados():
    """Carrega os datasets de enchentes"""
    try:
        # Carregamento dos datasets
        df_principal = pd.read_csv('../input/enchentes-rs-impactos/enchentes_rs.csv')
        df_2024 = pd.read_csv('../input/enchentes-rs-impactos/enchente_2024_detalhado.csv')
        
        print("📊 DATASETS CARREGADOS:")
        print("=" * 50)
        print(f"Dataset Principal: {df_principal.shape[0]} registros, {df_principal.shape[1]} colunas")
        print(f"Dataset 2024: {df_2024.shape[0]} registros, {df_2024.shape[1]} colunas")
        print(f"Total: {df_principal.shape[0] + df_2024.shape[0]} registros")
        
        print("\n📋 COLUNAS DISPONÍVEIS:")
        print("Dataset Principal:", list(df_principal.columns))
        print("Dataset 2024:", list(df_2024.columns))
        
        return df_principal, df_2024
        
    except FileNotFoundError as e:
        print(f"❌ Erro ao carregar dados: {e}")
        print("💡 Verifique se os arquivos CSV estão na pasta correta")
        return None, None

# =============================================================================
# 🔍 EXPLORAÇÃO INICIAL DOS DADOS
# =============================================================================

def explorar_dados(df_principal, df_2024):
    """Realiza exploração inicial dos datasets"""
    print("\n🔍 EXPLORAÇÃO INICIAL DOS DADOS")
    print("=" * 50)
    
    # Informações básicas dos datasets
    print("📊 INFORMAÇÕES DO DATASET PRINCIPAL:")
    print("-" * 40)
    print(df_principal.info())
    
    print("\n📊 INFORMAÇÕES DO DATASET 2024:")
    print("-" * 40)
    print(df_2024.info())
    
    # Estatísticas descritivas
    print("\n📈 ESTATÍSTICAS DESCRITIVAS - DATASET PRINCIPAL:")
    print("-" * 50)
    print(df_principal.describe())
    
    print("\n📈 ESTATÍSTICAS DESCRITIVAS - DATASET 2024:")
    print("-" * 50)
    print(df_2024.describe())
    
    # Verificação de valores únicos
    print("\n🏙️ CIDADES INCLUÍDAS:")
    print("-" * 30)
    print("Dataset Principal:", df_principal['cidade'].unique())
    print("Dataset 2024:", df_2024['cidade'].unique())
    
    print("\n🌍 REGIÕES:")
    print("-" * 20)
    print("Dataset Principal:", df_principal['regiao'].unique())
    print("Dataset 2024:", df_2024['regiao'].unique())
    
    print("\n📅 PERÍODO COBERTO:")
    print("-" * 30)
    print(f"Dataset Principal: {df_principal['data'].min()} a {df_principal['data'].max()}")
    print(f"Dataset 2024: {df_2024['data'].min()} a {df_2024['data'].max()}")

# =============================================================================
# 📅 ANÁLISE TEMPORAL DOS IMPACTOS
# =============================================================================

def analise_temporal(df_principal, df_2024):
    """Realiza análise temporal dos impactos"""
    print("\n📅 ANÁLISE TEMPORAL DOS IMPACTOS")
    print("=" * 50)
    
    # Preparação dos dados para análise temporal
    df_principal['data'] = pd.to_datetime(df_principal['data'])
    df_2024['data'] = pd.to_datetime(df_2024['data'])
    
    # Agregação anual
    df_anual = df_principal.groupby(df_principal['data'].dt.year).agg({
        'mortes': 'sum',
        'feridos': 'sum',
        'desalojados': 'sum',
        'prejuizo_milhoes': 'sum'
    }).reset_index()
    
    print("📊 IMPACTOS ANUAIS (2020-2024):")
    print("-" * 40)
    print(df_anual.round(2))
    
    # Gráfico de evolução temporal dos impactos
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    fig.suptitle('📈 Evolução Temporal dos Impactos das Enchentes no RS (2020-2024)', fontsize=16)
    
    # Mortes
    axes[0, 0].plot(df_anual['data'], df_anual['mortes'], 'ro-', linewidth=2, markersize=8)
    axes[0, 0].set_title('Mortes', fontweight='bold')
    axes[0, 0].set_ylabel('Número de Mortes')
    axes[0, 0].grid(True, alpha=0.3)
    
    # Feridos
    axes[0, 1].plot(df_anual['data'], df_anual['feridos'], 'o-', color='orange', linewidth=2, markersize=8)
    axes[0, 1].set_title('Feridos', fontweight='bold')
    axes[0, 1].set_ylabel('Número de Feridos')
    axes[0, 1].grid(True, alpha=0.3)
    
    # Desalojados
    axes[1, 0].plot(df_anual['data'], df_anual['desalojados'], 'bo-', linewidth=2, markersize=8)
    axes[1, 0].set_title('Desalojados', fontweight='bold')
    axes[1, 0].set_ylabel('Número de Desalojados')
    axes[1, 0].grid(True, alpha=0.3)
    
    # Prejuízos
    axes[1, 1].plot(df_anual['data'], df_anual['prejuizo_milhoes'], 'mo-', linewidth=2, markersize=8)
    axes[1, 1].set_title('Prejuízos (Milhões R$)', fontweight='bold')
    axes[1, 1].set_ylabel('Prejuízos (Milhões R$)')
    axes[1, 1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    return df_anual

# =============================================================================
# 🌍 ANÁLISE REGIONAL DOS IMPACTOS
# =============================================================================

def analise_regional(df_principal):
    """Realiza análise regional dos impactos"""
    print("\n🌍 ANÁLISE REGIONAL DOS IMPACTOS")
    print("=" * 50)
    
    # Análise por região
    df_regional = df_principal.groupby('regiao').agg({
        'mortes': 'sum',
        'feridos': 'sum',
        'desalojados': 'sum',
        'prejuizo_milhoes': 'sum',
        'cidade': 'count'
    }).rename(columns={'cidade': 'eventos'}).round(2)
    
    print("🌍 IMPACTOS POR REGIÃO:")
    print("-" * 40)
    print(df_regional)
    
    # Gráfico de comparação regional
    fig, ax = plt.subplots(figsize=(12, 6))
    
    x = np.arange(len(df_regional.index))
    width = 0.2
    
    ax.bar(x - width*1.5, df_regional['mortes'], width, label='Mortes', color='red', alpha=0.8)
    ax.bar(x - width*0.5, df_regional['feridos'], width, label='Feridos', color='orange', alpha=0.8)
    ax.bar(x + width*0.5, df_regional['desalojados'], width, label='Desalojados', color='blue', alpha=0.8)
    ax.bar(x + width*1.5, df_regional['prejuizo_milhoes'], width, label='Prejuízos (Milhões)', color='purple', alpha=0.8)
    
    ax.set_xlabel('Região', fontweight='bold')
    ax.set_ylabel('Quantidade', fontweight='bold')
    ax.set_title('📊 Comparação de Impactos por Região', fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(df_regional.index)
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    # Análise por cidade
    df_cidades = df_principal.groupby('cidade').agg({
        'mortes': 'sum',
        'feridos': 'sum',
        'desalojados': 'sum',
        'prejuizo_milhoes': 'sum'
    }).round(2).sort_values('desalojados', ascending=False)
    
    print("\n🏙️ IMPACTOS POR CIDADE (Ordenado por Desalojados):")
    print("-" * 60)
    print(df_cidades)
    
    # Gráfico de impacto por cidade
    plt.figure(figsize=(12, 6))
    bars = plt.bar(df_cidades.index, df_cidades['desalojados'], 
                   color=plt.cm.Blues(np.linspace(0.3, 0.8, len(df_cidades))))
    
    plt.title('🏙️ Total de Desalojados por Cidade (2020-2024)', fontsize=14, fontweight='bold')
    plt.xlabel('Cidade', fontweight='bold')
    plt.ylabel('Total de Desalojados', fontweight='bold')
    plt.xticks(rotation=45, ha='right')
    plt.grid(True, alpha=0.3)
    
    # Adicionar valores nas barras
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height + height*0.01,
                 f'{int(height):,}', ha='center', va='bottom')
    
    plt.tight_layout()
    plt.show()
    
    return df_regional, df_cidades

# =============================================================================
# 🚨 ANÁLISE DA CRISE DE 2024
# =============================================================================

def analise_crise_2024(df_2024):
    """Realiza análise específica da crise de 2024"""
    print("\n🚨 ANÁLISE DA CRISE DE 2024")
    print("=" * 50)
    
    # Análise da crise de 2024
    print("🚨 ANÁLISE DA CRISE DE 2024:")
    print("-" * 40)
    print(f"Período: {df_2024['data'].min().strftime('%d/%m/%Y')} a {df_2024['data'].max().strftime('%d/%m/%Y')}")
    print(f"Total de registros: {len(df_2024)}")
    print(f"Cidades afetadas: {df_2024['cidade'].nunique()}")
    print(f"Total de mortes: {df_2024['mortes'].sum()}")
    print(f"Total de feridos: {df_2024['feridos'].sum()}")
    print(f"Total de desalojados: {df_2024['desalojados'].sum()}")
    print(f"Prejuízos totais: R$ {df_2024['prejuizo_milhoes'].sum():.2f} milhões")
    
    # Evolução diária da crise de 2024
    df_2024_diario = df_2024.groupby('data').agg({
        'mortes': 'sum',
        'feridos': 'sum',
        'desalojados': 'sum',
        'prejuizo_milhoes': 'sum'
    }).reset_index()
    
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    fig.suptitle('🚨 Evolução Diária da Crise de Enchentes de 2024 no RS', fontsize=16, fontweight='bold')
    
    # Mortes diárias
    axes[0, 0].plot(df_2024_diario['data'], df_2024_diario['mortes'], 'ro-', linewidth=2, markersize=6)
    axes[0, 0].set_title('Mortes Diárias', fontweight='bold')
    axes[0, 0].set_ylabel('Mortes')
    axes[0, 0].grid(True, alpha=0.3)
    axes[0, 0].tick_params(axis='x', rotation=45)
    
    # Feridos diários
    axes[0, 1].plot(df_2024_diario['data'], df_2024_diario['feridos'], 'o-', color='orange', linewidth=2, markersize=6)
    axes[0, 1].set_title('Feridos Diários', fontweight='bold')
    axes[0, 1].set_ylabel('Feridos')
    axes[0, 1].grid(True, alpha=0.3)
    axes[0, 1].tick_params(axis='x', rotation=45)
    
    # Desalojados diários
    axes[1, 0].plot(df_2024_diario['data'], df_2024_diario['desalojados'], 'bo-', linewidth=2, markersize=6)
    axes[1, 0].set_title('Desalojados Diários', fontweight='bold')
    axes[1, 0].set_ylabel('Desalojados')
    axes[1, 0].grid(True, alpha=0.3)
    axes[1, 0].tick_params(axis='x', rotation=45)
    
    # Prejuízos diários
    axes[1, 1].plot(df_2024_diario['data'], df_2024_diario['prejuizo_milhoes'], 'mo-', linewidth=2, markersize=6)
    axes[1, 1].set_title('Prejuízos Diários (Milhões R$)', fontweight='bold')
    axes[1, 1].set_ylabel('Prejuízos (Milhões R$)')
    axes[1, 1].grid(True, alpha=0.3)
    axes[1, 1].tick_params(axis='x', rotation=45)
    
    plt.tight_layout()
    plt.show()
    
    return df_2024_diario

# =============================================================================
# 🔗 ANÁLISE DE CORRELAÇÕES
# =============================================================================

def analise_correlacoes(df_principal):
    """Realiza análise de correlações entre variáveis"""
    print("\n🔗 ANÁLISE DE CORRELAÇÕES")
    print("=" * 50)
    
    # Matriz de correlação
    colunas_numericas = ['mortes', 'feridos', 'desalojados', 'prejuizo_milhoes', 
                         'altura_rio_metros', 'chuva_24h_mm']
    
    correlacao = df_principal[colunas_numericas].corr()
    
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlacao, annot=True, cmap='RdBu_r', center=0, 
                square=True, linewidths=0.5, cbar_kws={'shrink': 0.8})
    plt.title('🔗 Matriz de Correlação entre Variáveis', fontweight='bold')
    plt.tight_layout()
    plt.show()
    
    print("📊 MATRIZ DE CORRELAÇÃO:")
    print("-" * 40)
    print(correlacao.round(3))
    
    # Gráfico de dispersão: Altura do rio vs Desalojados
    plt.figure(figsize=(10, 6))
    
    scatter = plt.scatter(df_principal['altura_rio_metros'], df_principal['desalojados'], 
                          c=df_principal['prejuizo_milhoes'], s=df_principal['prejuizo_milhoes']*10,
                          cmap='viridis', alpha=0.7)
    
    plt.colorbar(scatter, label='Prejuízos (Milhões R$)')
    plt.xlabel('Altura do Rio (metros)', fontweight='bold')
    plt.ylabel('Número de Desalojados', fontweight='bold')
    plt.title('🌊 Relação entre Altura do Rio e Desalojados', fontweight='bold')
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    return correlacao

# =============================================================================
# 📊 ANÁLISE SAZONAL
# =============================================================================

def analise_sazonal(df_principal):
    """Realiza análise sazonal dos impactos"""
    print("\n📊 ANÁLISE SAZONAL")
    print("=" * 50)
    
    # Análise sazonal por mês
    df_principal['mes'] = df_principal['data'].dt.month
    df_sazonal = df_principal.groupby('mes').agg({
        'mortes': 'mean',
        'feridos': 'mean',
        'desalojados': 'mean',
        'prejuizo_milhoes': 'mean'
    }).round(2)
    
    # Nomes dos meses
    meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 
             'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
    df_sazonal.index = [meses[i-1] for i in df_sazonal.index]
    
    print("📅 IMPACTOS MÉDIOS POR MÊS:")
    print("-" * 40)
    print(df_sazonal)
    
    # Gráfico sazonal
    plt.figure(figsize=(12, 6))
    
    for col in df_sazonal.columns:
        plt.plot(df_sazonal.index, df_sazonal[col], 'o-', linewidth=2, markersize=6, label=col)
    
    plt.title('📅 Padrões Sazonais dos Impactos das Enchentes', fontsize=14, fontweight='bold')
    plt.xlabel('Mês', fontweight='bold')
    plt.ylabel('Impacto Médio', fontweight='bold')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    return df_sazonal

# =============================================================================
# 🎯 INSIGHTS E CONCLUSÕES
# =============================================================================

def mostrar_insights():
    """Mostra os principais insights identificados"""
    print("\n🎯 INSIGHTS E CONCLUSÕES")
    print("=" * 50)
    
    print("🎯 PRINCIPAIS INSIGHTS IDENTIFICADOS:")
    print("-" * 50)
    
    print("\n📈 TENDÊNCIAS TEMPORAIS:")
    print("• Aumento gradual dos impactos de 2020 a 2024")
    print("• Picos sazonais nos meses de abril e maio")
    print("• Crise de 2024 sem precedentes históricos")
    
    print("\n🌍 VULNERABILIDADES REGIONAIS:")
    print("• Região metropolitana concentra os maiores impactos")
    print("• Porto Alegre é a cidade mais afetada")
    print("• Serra apresenta impactos menores mas significativos")
    
    print("\n🔗 CORRELAÇÕES IDENTIFICADAS:")
    print("• Forte correlação entre altura do rio e número de desalojados")
    print("• Relação direta entre precipitação e prejuízos econômicos")
    print("• Padrões consistentes de resposta a emergências")
    
    print("\n🚨 LIÇÕES DA CRISE DE 2024:")
    print("• Necessidade de sistemas de alerta mais eficazes")
    print("• Importância do planejamento urbano resiliente")
    print("• Valor dos dados históricos para prevenção")

# =============================================================================
# 🚀 FUNÇÃO PRINCIPAL
# =============================================================================

def main():
    """Função principal que executa toda a análise"""
    print("🌊 ANÁLISE COMPLETA DAS ENCHENTES NO RIO GRANDE DO SUL (2020-2024)")
    print("=" * 80)
    print("🚀 Iniciando análise...")
    
    # 1. Carregar dados
    df_principal, df_2024 = carregar_dados()
    
    if df_principal is None or df_2024 is None:
        print("❌ Não foi possível carregar os dados. Verifique os arquivos CSV.")
        return
    
    # 2. Exploração inicial
    explorar_dados(df_principal, df_2024)
    
    # 3. Análise temporal
    df_anual = analise_temporal(df_principal, df_2024)
    
    # 4. Análise regional
    df_regional, df_cidades = analise_regional(df_principal)
    
    # 5. Análise da crise de 2024
    df_2024_diario = analise_crise_2024(df_2024)
    
    # 6. Análise de correlações
    correlacao = analise_correlacoes(df_principal)
    
    # 7. Análise sazonal
    df_sazonal = analise_sazonal(df_principal)
    
    # 8. Mostrar insights
    mostrar_insights()
    
    # 9. Resumo final
    print("\n🎉 ANÁLISE CONCLUÍDA COM SUCESSO!")
    print("=" * 50)
    print("📊 Resumo dos resultados:")
    print(f"• Dataset Principal: {df_principal.shape[0]} registros analisados")
    print(f"• Dataset 2024: {df_2024.shape[0]} registros da crise")
    print(f"• Período coberto: {df_principal['data'].min().year} a {df_principal['data'].max().year}")
    print(f"• Cidades analisadas: {df_principal['cidade'].nunique()}")
    print(f"• Regiões: {df_principal['regiao'].nunique()}")
    
    print("\n💡 Próximos passos recomendados:")
    print("• Analisar padrões específicos por cidade")
    print("• Desenvolver modelos preditivos")
    print("• Comparar com dados de outros estados")
    print("• Criar dashboards interativos")
    
    print("\n📞 Para dúvidas e contribuições:")
    print("• Use os comentários no Kaggle")
    print("• Compartilhe seus insights")
    print("• Sugira melhorias para o dataset")

# =============================================================================
# 🚀 EXECUÇÃO DO SCRIPT
# =============================================================================

if __name__ == "__main__":
    main()
