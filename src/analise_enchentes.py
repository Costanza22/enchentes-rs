#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Análise de Impactos das Enchentes do Rio Grande do Sul
Análise de dados sobre mortes, impactos e consequências das enchentes
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

# Configurações de estilo
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 10

class AnalisadorEnchentes:
    def __init__(self):
        self.df_geral = None
        self.df_2024 = None
        self.carregar_dados()
    
    def carregar_dados(self):
        """Carrega os datasets de enchentes"""
        try:
            self.df_geral = pd.read_csv('data/enchentes_rs.csv')
            self.df_2024 = pd.read_csv('data/enchente_2024_detalhado.csv')
            
            # Converter coluna de data
            self.df_geral['data'] = pd.to_datetime(self.df_geral['data'])
            self.df_2024['data'] = pd.to_datetime(self.df_2024['data'])
            
            print("✅ Dados carregados com sucesso!")
            print(f"📊 Dataset geral: {len(self.df_geral)} registros")
            print(f"📊 Dataset 2024: {len(self.df_2024)} registros")
            
        except Exception as e:
            print(f"❌ Erro ao carregar dados: {e}")
    
    def estatisticas_gerais(self):
        """Exibe estatísticas gerais dos dados"""
        print("\n" + "="*60)
        print("📈 ESTATÍSTICAS GERAIS DAS ENCHENTES NO RS")
        print("="*60)
        
        print(f"\n📅 Período analisado: {self.df_geral['data'].min().strftime('%d/%m/%Y')} a {self.df_geral['data'].max().strftime('%d/%m/%Y')}")
        print(f"🏙️ Cidades monitoradas: {self.df_geral['cidade'].nunique()}")
        print(f"🗺️ Regiões: {', '.join(self.df_geral['regiao'].unique())}")
        
        print(f"\n💀 Total de mortes: {self.df_geral['mortes'].sum()}")
        print(f"🤕 Total de feridos: {self.df_geral['feridos'].sum()}")
        print(f"🏠 Total de desalojados: {self.df_geral['desalojados'].sum():,}")
        print(f"💰 Prejuízo total: R$ {self.df_geral['prejuizo_milhoes'].sum():.1f} milhões")
        
        print(f"\n🌊 Altura máxima do rio: {self.df_geral['altura_rio_metros'].max():.1f}m")
        print(f"🌧️ Chuva máxima em 24h: {self.df_geral['chuva_24h_mm'].max():.1f}mm")
    
    def analise_temporal(self):
        """Análise temporal das enchentes"""
        print("\n" + "="*60)
        print("⏰ ANÁLISE TEMPORAL DAS ENCHENTES")
        print("="*60)
        
        # Agrupamento por ano
        df_anual = self.df_geral.groupby(self.df_geral['data'].dt.year).agg({
            'mortes': 'sum',
            'feridos': 'sum',
            'desalojados': 'sum',
            'prejuizo_milhoes': 'sum',
            'altura_rio_metros': 'max',
            'chuva_24h_mm': 'max'
        }).reset_index()
        
        df_anual.columns = ['Ano', 'Mortes', 'Feridos', 'Desalojados', 'Prejuízo (R$ milhões)', 
                           'Altura Máxima (m)', 'Chuva Máxima (mm)']
        
        print("\n📊 Evolução anual dos impactos:")
        print(df_anual.to_string(index=False))
        
        return df_anual
    
    def analise_regional(self):
        """Análise por região"""
        print("\n" + "="*60)
        print("🗺️ ANÁLISE REGIONAL DOS IMPACTOS")
        print("="*60)
        
        df_regional = self.df_geral.groupby('regiao').agg({
            'mortes': 'sum',
            'feridos': 'sum',
            'desalojados': 'sum',
            'prejuizo_milhoes': 'sum',
            'altura_rio_metros': 'mean',
            'chuva_24h_mm': 'mean'
        }).round(2)
        
        df_regional.columns = ['Mortes', 'Feridos', 'Desalojados', 'Prejuízo (R$ milhões)', 
                              'Altura Média (m)', 'Chuva Média (mm)']
        
        print("\n📊 Impactos por região:")
        print(df_regional.to_string())
        
        return df_regional
    
    def analise_cidades(self):
        """Análise por cidade"""
        print("\n" + "="*60)
        print("🏙️ ANÁLISE POR CIDADE")
        print("="*60)
        
        df_cidades = self.df_geral.groupby('cidade').agg({
            'mortes': 'sum',
            'feridos': 'sum',
            'desalojados': 'sum',
            'prejuizo_milhoes': 'sum',
            'altura_rio_metros': 'max',
            'chuva_24h_mm': 'max'
        }).sort_values('prejuizo_milhoes', ascending=False).round(2)
        
        df_cidades.columns = ['Mortes', 'Feridos', 'Desalojados', 'Prejuízo (R$ milhões)', 
                             'Altura Máxima (m)', 'Chuva Máxima (mm)']
        
        print("\n📊 Ranking de cidades por prejuízo:")
        print(df_cidades.to_string())
        
        return df_cidades
    
    def analise_enchente_2024(self):
        """Análise específica da enchente de 2024"""
        print("\n" + "="*60)
        print("🚨 ANÁLISE DA ENCHENTE DE 2024")
        print("="*60)
        
        if self.df_2024 is not None:
            print(f"\n📅 Período da crise: {self.df_2024['data'].min().strftime('%d/%m/%Y')} a {self.df_2024['data'].max().strftime('%d/%m/%Y')}")
            
            # Estatísticas por cidade
            df_crise = self.df_2024.groupby('cidade').agg({
                'feridos': 'sum',
                'desalojados': 'max',
                'prejuizo_milhoes': 'max',
                'altura_rio_metros': 'max',
                'chuva_24h_mm': 'max'
            }).sort_values('desalojados', ascending=False).round(2)
            
            df_crise.columns = ['Feridos', 'Desalojados Máximo', 'Prejuízo Máximo (R$ milhões)', 
                               'Altura Máxima (m)', 'Chuva Máxima (mm)']
            
            print("\n📊 Impactos por cidade durante a crise:")
            print(df_crise.to_string())
            
            return df_crise
        else:
            print("❌ Dataset de 2024 não disponível")
            return None
    
    def criar_graficos(self):
        """Cria gráficos de análise"""
        print("\n" + "="*60)
        print("📊 GERANDO GRÁFICOS DE ANÁLISE")
        print("="*60)
        
        # 1. Evolução temporal dos impactos
        self.grafico_evolucao_temporal()
        
        # 2. Comparação regional
        self.grafico_comparacao_regional()
        
        # 3. Análise sazonal
        self.grafico_analise_sazonal()
        
        # 4. Correlação entre variáveis
        self.grafico_correlacao()
        
        # 5. Enchente de 2024 (se disponível)
        if self.df_2024 is not None:
            self.grafico_enchente_2024()
        
        print("\n✅ Gráficos gerados e salvos na pasta 'outputs/'")
    
    def grafico_evolucao_temporal(self):
        """Gráfico de evolução temporal dos impactos"""
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        fig.suptitle('Evolução Temporal dos Impactos das Enchentes no RS (2020-2024)', fontsize=16, fontweight='bold')
        
        # Agrupamento por mês
        df_mensal = self.df_geral.groupby([self.df_geral['data'].dt.year, self.df_geral['data'].dt.month]).agg({
            'desalojados': 'sum',
            'prejuizo_milhoes': 'sum',
            'altura_rio_metros': 'mean',
            'chuva_24h_mm': 'mean'
        }).reset_index()
        
        df_mensal['data_completa'] = pd.to_datetime(df_mensal[['data_0', 'data_1']].assign(day=1))
        
        # Desalojados
        axes[0,0].plot(df_mensal['data_completa'], df_mensal['desalojados'], marker='o', linewidth=2)
        axes[0,0].set_title('Evolução dos Desalojados')
        axes[0,0].set_ylabel('Número de Desalojados')
        axes[0,0].tick_params(axis='x', rotation=45)
        
        # Prejuízos
        axes[0,1].plot(df_mensal['data_completa'], df_mensal['prejuizo_milhoes'], marker='s', color='red', linewidth=2)
        axes[0,1].set_title('Evolução dos Prejuízos')
        axes[0,1].set_ylabel('Prejuízo (R$ milhões)')
        axes[0,1].tick_params(axis='x', rotation=45)
        
        # Altura do rio
        axes[1,0].plot(df_mensal['data_completa'], df_mensal['altura_rio_metros'], marker='^', color='blue', linewidth=2)
        axes[1,0].set_title('Evolução da Altura do Rio')
        axes[1,0].set_ylabel('Altura (metros)')
        axes[1,0].tick_params(axis='x', rotation=45)
        
        # Chuva
        axes[1,1].plot(df_mensal['data_completa'], df_mensal['chuva_24h_mm'], marker='d', color='green', linewidth=2)
        axes[1,1].set_title('Evolução da Chuva em 24h')
        axes[1,1].set_ylabel('Chuva (mm)')
        axes[1,1].tick_params(axis='x', rotation=45)
        
        plt.tight_layout()
        plt.savefig('outputs/evolucao_temporal.png', dpi=300, bbox_inches='tight')
        plt.show()
    
    def grafico_comparacao_regional(self):
        """Gráfico de comparação regional"""
        df_regional = self.df_geral.groupby('regiao').agg({
            'desalojados': 'sum',
            'prejuizo_milhoes': 'sum',
            'feridos': 'sum'
        }).reset_index()
        
        fig, axes = plt.subplots(1, 3, figsize=(18, 6))
        fig.suptitle('Comparação Regional dos Impactos das Enchentes no RS', fontsize=16, fontweight='bold')
        
        # Desalojados
        axes[0].bar(df_regional['regiao'], df_regional['desalojados'], color=['#FF6B6B', '#4ECDC4'])
        axes[0].set_title('Total de Desalojados por Região')
        axes[0].set_ylabel('Número de Desalojados')
        axes[0].tick_params(axis='x', rotation=45)
        
        # Prejuízos
        axes[1].bar(df_regional['regiao'], df_regional['prejuizo_milhoes'], color=['#45B7D1', '#96CEB4'])
        axes[1].set_title('Total de Prejuízos por Região')
        axes[1].set_ylabel('Prejuízo (R$ milhões)')
        axes[1].tick_params(axis='x', rotation=45)
        
        # Feridos
        axes[2].bar(df_regional['regiao'], df_regional['feridos'], color=['#FFEAA7', '#DDA0DD'])
        axes[2].set_title('Total de Feridos por Região')
        axes[2].set_ylabel('Número de Feridos')
        axes[2].tick_params(axis='x', rotation=45)
        
        plt.tight_layout()
        plt.savefig('outputs/comparacao_regional.png', dpi=300, bbox_inches='tight')
        plt.show()
    
    def grafico_analise_sazonal(self):
        """Gráfico de análise sazonal"""
        df_sazonal = self.df_geral.groupby(self.df_geral['data'].dt.month).agg({
            'desalojados': 'mean',
            'prejuizo_milhoes': 'mean',
            'altura_rio_metros': 'mean'
        }).reset_index()
        
        meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 
                'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
        
        fig, axes = plt.subplots(1, 3, figsize=(18, 6))
        fig.suptitle('Análise Sazonal das Enchentes no RS', fontsize=16, fontweight='bold')
        
        # Desalojados por mês
        axes[0].bar(range(1, 13), df_sazonal['desalojados'], color='skyblue')
        axes[0].set_title('Média de Desalojados por Mês')
        axes[0].set_ylabel('Média de Desalojados')
        axes[0].set_xticks(range(1, 13))
        axes[0].set_xticklabels(meses, rotation=45)
        
        # Prejuízos por mês
        axes[1].bar(range(1, 13), df_sazonal['prejuizo_milhoes'], color='lightcoral')
        axes[1].set_title('Média de Prejuízos por Mês')
        axes[1].set_ylabel('Média de Prejuízos (R$ milhões)')
        axes[1].set_xticks(range(1, 13))
        axes[1].set_xticklabels(meses, rotation=45)
        
        # Altura do rio por mês
        axes[2].bar(range(1, 13), df_sazonal['altura_rio_metros'], color='lightgreen')
        axes[2].set_title('Média da Altura do Rio por Mês')
        axes[2].set_ylabel('Altura Média (metros)')
        axes[2].set_xticks(range(1, 13))
        axes[2].set_xticklabels(meses, rotation=45)
        
        plt.tight_layout()
        plt.savefig('outputs/analise_sazonal.png', dpi=300, bbox_inches='tight')
        plt.show()
    
    def grafico_correlacao(self):
        """Gráfico de correlação entre variáveis"""
        # Selecionar apenas colunas numéricas
        colunas_numericas = ['mortes', 'feridos', 'desalojados', 'prejuizo_milhoes', 
                             'altura_rio_metros', 'chuva_24h_mm']
        
        df_corr = self.df_geral[colunas_numericas].corr()
        
        plt.figure(figsize=(10, 8))
        sns.heatmap(df_corr, annot=True, cmap='coolwarm', center=0, 
                    square=True, linewidths=0.5, cbar_kws={'shrink': 0.8})
        plt.title('Matriz de Correlação entre Variáveis das Enchentes', fontsize=16, fontweight='bold')
        plt.tight_layout()
        plt.savefig('outputs/correlacao.png', dpi=300, bbox_inches='tight')
        plt.show()
    
    def grafico_enchente_2024(self):
        """Gráfico específico da enchente de 2024"""
        if self.df_2024 is None:
            return
        
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        fig.suptitle('Análise Detalhada da Enchente de 2024 no RS', fontsize=16, fontweight='bold')
        
        # Evolução dos desalojados por cidade
        for cidade in self.df_2024['cidade'].unique():
            df_cidade = self.df_2024[self.df_2024['cidade'] == cidade]
            axes[0,0].plot(df_cidade['data'], df_cidade['desalojados'], marker='o', label=cidade, linewidth=2)
        
        axes[0,0].set_title('Evolução dos Desalojados por Cidade')
        axes[0,0].set_ylabel('Número de Desalojados')
        axes[0,0].legend()
        axes[0,0].tick_params(axis='x', rotation=45)
        
        # Evolução dos prejuízos por cidade
        for cidade in self.df_2024['cidade'].unique():
            df_cidade = self.df_2024[self.df_2024['cidade'] == cidade]
            axes[0,1].plot(df_cidade['data'], df_cidade['prejuizo_milhoes'], marker='s', label=cidade, linewidth=2)
        
        axes[0,1].set_title('Evolução dos Prejuízos por Cidade')
        axes[0,1].set_ylabel('Prejuízo (R$ milhões)')
        axes[0,1].legend()
        axes[0,1].tick_params(axis='x', rotation=45)
        
        # Altura do rio por cidade
        for cidade in self.df_2024['cidade'].unique():
            df_cidade = self.df_2024[self.df_2024['cidade'] == cidade]
            axes[1,0].plot(df_cidade['data'], df_cidade['altura_rio_metros'], marker='^', label=cidade, linewidth=2)
        
        axes[1,0].set_title('Evolução da Altura do Rio por Cidade')
        axes[1,0].set_ylabel('Altura (metros)')
        axes[1,0].legend()
        axes[1,0].tick_params(axis='x', rotation=45)
        
        # Chuva por cidade
        for cidade in self.df_2024['cidade'].unique():
            df_cidade = self.df_2024[self.df_2024['cidade'] == cidade]
            axes[1,1].plot(df_cidade['data'], df_cidade['chuva_24h_mm'], marker='d', label=cidade, linewidth=2)
        
        axes[1,1].set_title('Evolução da Chuva em 24h por Cidade')
        axes[1,1].set_ylabel('Chuva (mm)')
        axes[1,1].legend()
        axes[1,1].tick_params(axis='x', rotation=45)
        
        plt.tight_layout()
        plt.savefig('outputs/enchente_2024.png', dpi=300, bbox_inches='tight')
        plt.show()
    
    def gerar_relatorio(self):
        """Gera relatório completo em texto"""
        print("\n" + "="*60)
        print("📋 GERANDO RELATÓRIO COMPLETO")
        print("="*60)
        
        # Criar pasta outputs se não existir
        import os
        os.makedirs('outputs', exist_ok=True)
        
        with open('outputs/relatorio_enchentes.txt', 'w', encoding='utf-8') as f:
            f.write("RELATÓRIO DE ANÁLISE DAS ENCHENTES NO RIO GRANDE DO SUL\n")
            f.write("="*60 + "\n\n")
            
            f.write("1. RESUMO EXECUTIVO\n")
            f.write("-" * 30 + "\n")
            f.write(f"Período analisado: {self.df_geral['data'].min().strftime('%d/%m/%Y')} a {self.df_geral['data'].max().strftime('%d/%m/%Y')}\n")
            f.write(f"Total de registros: {len(self.df_geral)}\n")
            f.write(f"Cidades monitoradas: {self.df_geral['cidade'].nunique()}\n")
            f.write(f"Regiões: {', '.join(self.df_geral['regiao'].unique())}\n\n")
            
            f.write("2. IMPACTOS TOTAIS\n")
            f.write("-" * 30 + "\n")
            f.write(f"Mortes: {self.df_geral['mortes'].sum()}\n")
            f.write(f"Feridos: {self.df_geral['feridos'].sum()}\n")
            f.write(f"Desalojados: {self.df_geral['desalojados'].sum():,}\n")
            f.write(f"Prejuízo total: R$ {self.df_geral['prejuizo_milhoes'].sum():.1f} milhões\n\n")
            
            f.write("3. ANÁLISE TEMPORAL\n")
            f.write("-" * 30 + "\n")
            df_anual = self.analise_temporal()
            f.write(df_anual.to_string())
            f.write("\n\n")
            
            f.write("4. ANÁLISE REGIONAL\n")
            f.write("-" * 30 + "\n")
            df_regional = self.analise_regional()
            f.write(df_regional.to_string())
            f.write("\n\n")
            
            f.write("5. ANÁLISE POR CIDADE\n")
            f.write("-" * 30 + "\n")
            df_cidades = self.analise_cidades()
            f.write(df_cidades.to_string())
            f.write("\n\n")
            
            if self.df_2024 is not None:
                f.write("6. ANÁLISE DA ENCHENTE DE 2024\n")
                f.write("-" * 30 + "\n")
                df_crise = self.analise_enchente_2024()
                if df_crise is not None:
                    f.write(df_crise.to_string())
                f.write("\n\n")
            
            f.write("7. RECOMENDAÇÕES\n")
            f.write("-" * 30 + "\n")
            f.write("- Implementar sistema de alerta precoce\n")
            f.write("- Melhorar infraestrutura de drenagem\n")
            f.write("- Desenvolver planos de contingência regionais\n")
            f.write("- Investir em monitoramento hidrológico\n")
            f.write("- Capacitar equipes de resposta a emergências\n")
        
        print("✅ Relatório salvo em 'outputs/relatorio_enchentes.txt'")
    
    def executar_analise_completa(self):
        """Executa análise completa"""
        print("🚀 INICIANDO ANÁLISE COMPLETA DAS ENCHENTES NO RS")
        print("="*60)
        
        # Estatísticas gerais
        self.estatisticas_gerais()
        
        # Análises específicas
        self.analise_temporal()
        self.analise_regional()
        self.analise_cidades()
        self.analise_enchente_2024()
        
        # Gráficos
        self.criar_graficos()
        
        # Relatório
        self.gerar_relatorio()
        
        print("\n🎉 ANÁLISE COMPLETA FINALIZADA!")
        print("📁 Verifique a pasta 'outputs/' para gráficos e relatórios")

def main():
    """Função principal"""
    try:
        # Criar instância do analisador
        analisador = AnalisadorEnchentes()
        
        # Executar análise completa
        analisador.executar_analise_completa()
        
    except Exception as e:
        print(f"❌ Erro durante a execução: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
