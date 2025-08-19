#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para preparar arquivos para upload no Kaggle
Cria a estrutura correta e organiza os arquivos
"""

import os
import shutil
import zipfile
from datetime import datetime

def criar_estrutura_kaggle():
    """Cria a estrutura de pastas para o Kaggle"""
    print("🚀 PREPARANDO ARQUIVOS PARA O KAGGLE")
    print("=" * 50)
    
    # Nome da pasta do Kaggle
    pasta_kaggle = "enchentes-rs-kaggle"
    
    # Criar pasta principal
    if os.path.exists(pasta_kaggle):
        shutil.rmtree(pasta_kaggle)
    
    os.makedirs(pasta_kaggle)
    os.makedirs(f"{pasta_kaggle}/data")
    os.makedirs(f"{pasta_kaggle}/notebooks")
    
    print(f"✅ Pasta '{pasta_kaggle}' criada com sucesso!")
    
    return pasta_kaggle

def copiar_arquivos(pasta_kaggle):
    """Copia os arquivos necessários para o Kaggle"""
    print("\n📁 COPIANDO ARQUIVOS...")
    
    # Copiar CSVs
    arquivos_csv = [
        "data/enchentes_rs.csv",
        "data/enchente_2024_detalhado.csv"
    ]
    
    for arquivo in arquivos_csv:
        if os.path.exists(arquivo):
            destino = f"{pasta_kaggle}/data/{os.path.basename(arquivo)}"
            shutil.copy2(arquivo, destino)
            print(f"   ✅ {arquivo} → {destino}")
        else:
            print(f"   ❌ Arquivo não encontrado: {arquivo}")
    
    # Copiar README
    if os.path.exists("README_KAGGLE.md"):
        shutil.copy2("README_KAGGLE.md", f"{pasta_kaggle}/README.md")
        print("   ✅ README_KAGGLE.md → README.md")
    
    # Copiar notebook
    if os.path.exists("notebooks/analise_enchentes_kaggle.ipynb"):
        shutil.copy2("notebooks/analise_enchentes_kaggle.ipynb", 
                    f"{pasta_kaggle}/notebooks/analise_enchentes_kaggle.ipynb")
        print("   ✅ Notebook copiado")
    
    # Copiar metadados
    if os.path.exists("kaggle_metadata.json"):
        shutil.copy2("kaggle_metadata.json", f"{pasta_kaggle}/metadata.json")
        print("   ✅ Metadados copiados")
    
    print(f"\n✅ Todos os arquivos copiados para '{pasta_kaggle}/'")

def criar_zip(pasta_kaggle):
    """Cria arquivo ZIP para upload no Kaggle"""
    print(f"\n📦 CRIANDO ARQUIVO ZIP...")
    
    nome_zip = f"{pasta_kaggle}.zip"
    
    with zipfile.ZipFile(nome_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(pasta_kaggle):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, pasta_kaggle)
                zipf.write(file_path, arcname)
    
    print(f"✅ Arquivo ZIP criado: {nome_zip}")
    
    # Verificar tamanho
    tamanho = os.path.getsize(nome_zip) / (1024 * 1024)  # MB
    print(f"📏 Tamanho do ZIP: {tamanho:.2f} MB")
    
    return nome_zip

def mostrar_estrutura(pasta_kaggle):
    """Mostra a estrutura final criada"""
    print(f"\n📋 ESTRUTURA FINAL CRIADA:")
    print("=" * 40)
    
    for root, dirs, files in os.walk(pasta_kaggle):
        level = root.replace(pasta_kaggle, '').count(os.sep)
        indent = ' ' * 2 * level
        print(f"{indent}{os.path.basename(root)}/")
        subindent = ' ' * 2 * (level + 1)
        for file in files:
            print(f"{subindent}{file}")

def instrucoes_upload(nome_zip, pasta_kaggle):
    """Mostra instruções para upload no Kaggle"""
    print(f"\n🎯 INSTRUÇÕES PARA UPLOAD NO KAGGLE:")
    print("=" * 50)
    
    print("1. 📱 Acesse kaggle.com e faça login")
    print("2. 📊 Clique em 'Datasets' → 'Create Dataset'")
    print("3. 📁 Arraste o arquivo ZIP ou extraia e arraste a pasta")
    print("4. ✏️ Configure:")
    print("   • Nome: 'Enchentes no RS: Impactos e Análises (2020-2024)'")
    print("   • Descrição: Use o README.md")
    print("   • Tags: enchentes, rio-grande-sul, brasil")
    print("   • Licença: CC0-1.0")
    print("5. 🚀 Clique em 'Create Dataset'")
    print("6. 📝 Depois crie um notebook de análise")
    
    print(f"\n📦 Arquivo pronto para upload: {nome_zip}")
    print(f"📁 Pasta local: {pasta_kaggle}/")

def main():
    """Função principal"""
    try:
        # Criar estrutura
        pasta_kaggle = criar_estrutura_kaggle()
        
        # Copiar arquivos
        copiar_arquivos(pasta_kaggle)
        
        # Mostrar estrutura
        mostrar_estrutura(pasta_kaggle)
        
        # Criar ZIP
        nome_zip = criar_zip(pasta_kaggle)
        
        # Instruções
        instrucoes_upload(nome_zip, pasta_kaggle)
        
        print(f"\n🎉 PREPARAÇÃO CONCLUÍDA COM SUCESSO!")
        print(f"📁 Pasta: {pasta_kaggle}/")
        print(f"📦 ZIP: {nome_zip}")
        print("\n🚀 Agora você pode fazer upload no Kaggle!")
        
    except Exception as e:
        print(f"❌ Erro durante a preparação: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
