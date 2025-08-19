#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Análise Rápida das Enchentes no Rio Grande do Sul
Script simples para verificação inicial dos dados
"""

import pandas as pd
import matplotlib.pyplot as plt

def analise_rapida():
    """Executa análise rápida dos dados"""
    print("🚀 ANÁLISE RÁPIDA DAS ENCHENTES NO RS")
    print("=" * 50)
    
    try:
        # Carregar dados
        df = pd.read_csv('data/enchentes_rs.csv')
        df['data'] = pd.to_datetime(df['data'])
        
        print(f"✅ Dados carregados: {len(df)} registros")
        print(f"📅 Período: {df['data'].min().strftime('%d/%m/%Y')} a {df['data'].max().strftime('%d/%Y')}")
        print(f"🏙️ Cidades: {df['cidade'].nunique()}")
        print(f"🗺️ Regiões: {', '.join(df['regiao'].unique())}")
        
        # Estatísticas básicas
        print(f"\n📊 IMPACTOS TOTAIS:")
        print(f"   • Mortes: {df['mortes'].sum()}")
        print(f"   • Feridos: {df['feridos'].sum()}")
        print(f"   • Desalojados: {df['desalojados'].sum():,}")
        print(f"   • Prejuízo: R$ {df['prejuizo_milhoes'].sum():.1f} milhões")
        
        # Análise por região
        print(f"\n🗺️ IMPACTOS POR REGIÃO:")
        df_regional = df.groupby('regiao').agg({
            'desalojados': 'sum',
            'prejuizo_milhoes': 'sum'
        }).round(2)
        
        for regiao, dados in df_regional.iterrows():
            print(f"   • {regiao}: {dados['desalojados']:,.0f} desalojados, R$ {dados['prejuizo_milhoes']:.1f}M")
        
        # Gráfico simples
        plt.figure(figsize=(10, 6))
        df.groupby('regiao')['desalojados'].sum().plot(kind='bar', color=['#FF6B6B', '#4ECDC4'])
        plt.title('Total de Desalojados por Região')
        plt.ylabel('Número de Desalojados')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
        
        print("\n✅ Análise rápida concluída!")
        
    except Exception as e:
        print(f"❌ Erro: {e}")

if __name__ == "__main__":
    analise_rapida()
