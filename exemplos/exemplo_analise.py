#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exemplo de Análise de Dados de Enchentes no Rio Grande do Sul
Demonstra como usar os datasets criados para análises específicas
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def exemplo_analise_basica():
    """Exemplo de análise básica dos dados"""
    print("🔍 EXEMPLO DE ANÁLISE BÁSICA")
    print("=" * 40)
    
    # Carregar dados
    df = pd.read_csv('../data/enchentes_rs.csv')
    df['data'] = pd.to_datetime(df['data'])
    
    # 1. Análise de tendências temporais
    print("\n1. 📈 ANÁLISE DE TENDÊNCIAS TEMPORAIS")
    
    # Agrupamento por ano
    df_anual = df.groupby(df['data'].dt.year).agg({
        'desalojados': 'sum',
        'prejuizo_milhoes': 'sum',
        'feridos': 'sum'
    }).reset_index()
    
    print("Evolução anual dos impactos:")
    print(df_anual.to_string(index=False))
    
    # 2. Análise regional
    print("\n2. 🗺️ ANÁLISE REGIONAL")
    
    df_regional = df.groupby('regiao').agg({
        'desalojados': 'sum',
        'prejuizo_milhoes': 'sum',
        'feridos': 'sum'
    }).round(2)
    
    print("Impactos por região:")
    print(df_regional)
    
    # 3. Análise sazonal
    print("\n3. 📅 ANÁLISE SAZONAL")
    
    df_sazonal = df.groupby(df['data'].dt.month).agg({
        'desalojados': 'mean',
        'prejuizo_milhoes': 'mean'
    }).round(2)
    
    meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 
             'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
    
    df_sazonal.index = [meses[i-1] for i in df_sazonal.index]
    print("Médias mensais:")
    print(df_sazonal)
    
    return df, df_anual, df_regional, df_sazonal

def exemplo_visualizacoes():
    """Exemplo de criação de visualizações"""
    print("\n🎨 EXEMPLO DE VISUALIZAÇÕES")
    print("=" * 40)
    
    df, df_anual, df_regional, df_sazonal = exemplo_analise_basica()
    
    # Configurações de estilo
    plt.style.use('seaborn-v0_8')
    sns.set_palette("husl")
    
    # 1. Gráfico de linha temporal
    plt.figure(figsize=(12, 8))
    
    plt.subplot(2, 2, 1)
    plt.plot(df_anual['data'], df_anual['desalojados'], marker='o', linewidth=2, color='blue')
    plt.title('Evolução dos Desalojados por Ano')
    plt.ylabel('Número de Desalojados')
    plt.grid(True, alpha=0.3)
    
    plt.subplot(2, 2, 2)
    plt.plot(df_anual['data'], df_anual['prejuizo_milhoes'], marker='s', linewidth=2, color='red')
    plt.title('Evolução dos Prejuízos por Ano')
    plt.ylabel('Prejuízo (R$ milhões)')
    plt.grid(True, alpha=0.3)
    
    plt.subplot(2, 2, 3)
    plt.bar(df_regional.index, df_regional['desalojados'], color=['#FF6B6B', '#4ECDC4'])
    plt.title('Total de Desalojados por Região')
    plt.ylabel('Número de Desalojados')
    plt.xticks(rotation=45)
    
    plt.subplot(2, 2, 4)
    plt.bar(df_sazonal.index, df_sazonal['desalojados'], color='skyblue')
    plt.title('Média de Desalojados por Mês')
    plt.ylabel('Média de Desalojados')
    plt.xticks(rotation=45)
    
    plt.tight_layout()
    plt.show()
    
    print("✅ Visualizações criadas com sucesso!")

def exemplo_analise_avancada():
    """Exemplo de análise avançada"""
    print("\n🚀 EXEMPLO DE ANÁLISE AVANÇADA")
    print("=" * 40)
    
    df = pd.read_csv('../data/enchentes_rs.csv')
    df['data'] = pd.to_datetime(df['data'])
    
    # 1. Correlação entre variáveis
    print("1. 🔗 ANÁLISE DE CORRELAÇÕES")
    
    colunas_numericas = ['mortes', 'feridos', 'desalojados', 'prejuizo_milhoes', 
                         'altura_rio_metros', 'chuva_24h_mm']
    
    correlacoes = df[colunas_numericas].corr()
    
    print("Matriz de correlação:")
    print(correlacoes.round(3))
    
    # 2. Análise de outliers
    print("\n2. 📊 ANÁLISE DE OUTLIERS")
    
    # Usar IQR para identificar outliers
    Q1 = df['desalojados'].quantile(0.25)
    Q3 = df['desalojados'].quantile(0.75)
    IQR = Q3 - Q1
    
    outliers = df[(df['desalojados'] < (Q1 - 1.5 * IQR)) | 
                  (df['desalojados'] > (Q3 + 1.5 * IQR))]
    
    print(f"Outliers encontrados: {len(outliers)}")
    if len(outliers) > 0:
        print("Registros com outliers:")
        print(outliers[['data', 'cidade', 'desalojados']].head())
    
    # 3. Análise de clusters por cidade
    print("\n3. 🏙️ ANÁLISE DE CLUSTERS POR CIDADE")
    
    df_cidades = df.groupby('cidade').agg({
        'desalojados': 'mean',
        'prejuizo_milhoes': 'mean',
        'feridos': 'mean'
    }).round(2)
    
    # Normalizar dados para análise
    from sklearn.preprocessing import StandardScaler
    
    scaler = StandardScaler()
    df_normalizado = pd.DataFrame(
        scaler.fit_transform(df_cidades),
        columns=df_cidades.columns,
        index=df_cidades.index
    )
    
    print("Cidades com maior impacto médio:")
    print(df_cidades.nlargest(5, 'desalojados'))
    
    return df, correlacoes, outliers, df_cidades

def exemplo_enchente_2024():
    """Exemplo específico da análise da enchente de 2024"""
    print("\n🚨 EXEMPLO DA ENCHENTE DE 2024")
    print("=" * 40)
    
    try:
        df_2024 = pd.read_csv('../data/enchente_2024_detalhado.csv')
        df_2024['data'] = pd.to_datetime(df_2024['data'])
        
        print(f"📅 Período da crise: {df_2024['data'].min().strftime('%d/%m/%Y')} a {df_2024['data'].max().strftime('%d/%m/%Y')}")
        print(f"🏙️ Cidades afetadas: {df_2024['cidade'].nunique()}")
        
        # Análise da evolução da crise
        print("\n📈 EVOLUÇÃO DA CRISE:")
        
        df_evolucao = df_2024.groupby('data').agg({
            'desalojados': 'sum',
            'feridos': 'sum',
            'prejuizo_milhoes': 'sum'
        }).reset_index()
        
        print("Evolução diária dos impactos:")
        print(df_evolucao.to_string(index=False))
        
        # Gráfico da evolução
        plt.figure(figsize=(12, 8))
        
        plt.subplot(2, 2, 1)
        plt.plot(df_evolucao['data'], df_evolucao['desalojados'], marker='o', linewidth=2, color='red')
        plt.title('Evolução dos Desalojados - Crise 2024')
        plt.ylabel('Número de Desalojados')
        plt.xticks(rotation=45)
        plt.grid(True, alpha=0.3)
        
        plt.subplot(2, 2, 2)
        plt.plot(df_evolucao['data'], df_evolucao['prejuizo_milhoes'], marker='s', linewidth=2, color='orange')
        plt.title('Evolução dos Prejuízos - Crise 2024')
        plt.ylabel('Prejuízo (R$ milhões)')
        plt.xticks(rotation=45)
        plt.grid(True, alpha=0.3)
        
        plt.subplot(2, 2, 3)
        plt.plot(df_evolucao['data'], df_evolucao['feridos'], marker='^', linewidth=2, color='purple')
        plt.title('Evolução dos Feridos - Crise 2024')
        plt.ylabel('Número de Feridos')
        plt.xticks(rotation=45)
        plt.grid(True, alpha=0.3)
        
        # Análise por cidade
        plt.subplot(2, 2, 4)
        df_cidades_crise = df_2024.groupby('cidade')['desalojados'].max().sort_values(ascending=False)
        plt.bar(df_cidades_crise.index, df_cidades_crise.values, color='lightcoral')
        plt.title('Máximo de Desalojados por Cidade - Crise 2024')
        plt.ylabel('Máximo de Desalojados')
        plt.xticks(rotation=45)
        
        plt.tight_layout()
        plt.show()
        
        print("✅ Análise da enchente de 2024 concluída!")
        
    except FileNotFoundError:
        print("❌ Dataset de 2024 não encontrado. Verifique se o arquivo existe.")

def main():
    """Função principal que executa todos os exemplos"""
    print("🎯 EXEMPLOS DE ANÁLISE DE DADOS DE ENCHENTES NO RS")
    print("=" * 60)
    
    try:
        # Executar exemplos
        exemplo_analise_basica()
        exemplo_visualizacoes()
        exemplo_analise_avancada()
        exemplo_enchente_2024()
        
        print("\n🎉 TODOS OS EXEMPLOS EXECUTADOS COM SUCESSO!")
        print("📁 Verifique os gráficos gerados e use os códigos como base para suas análises.")
        
    except Exception as e:
        print(f"❌ Erro durante a execução: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
