#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Setup script for RS Impacto - Análise de Enchentes no Rio Grande do Sul
"""

from setuptools import setup, find_packages
import os

# Read the README file
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Read requirements
def read_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        return [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="rs-impacto",
    version="1.0.0",
    author="Seu Nome",
    author_email="seu-email@exemplo.com",
    description="Análise completa dos impactos das enchentes no Rio Grande do Sul (2020-2024)",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/seu-usuario/rs-impacto",
    project_urls={
        "Bug Reports": "https://github.com/seu-usuario/rs-impacto/issues",
        "Source": "https://github.com/seu-usuario/rs-impacto",
        "Documentation": "https://github.com/seu-usuario/rs-impacto#readme",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Education",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Scientific/Engineering :: Visualization",
        "License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Natural Language :: Portuguese",
        "Natural Language :: English",
    ],
    python_requires=">=3.8",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.8",
            "mypy>=0.800",
        ],
        "docs": [
            "sphinx>=4.0",
            "sphinx-rtd-theme>=1.0",
            "myst-parser>=0.15",
        ],
    },
    entry_points={
        "console_scripts": [
            "rs-impacto=src.analise_enchentes:main",
            "rs-impacto-rapido=src.analise_rapida:main",
            "rs-impacto-kaggle=src.preparar_kaggle:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.csv", "*.md", "*.txt", "*.json"],
    },
    keywords=[
        "enchentes",
        "rio-grande-sul",
        "brasil",
        "desastres-naturais",
        "análise-dados",
        "ciência-dados",
        "hidrologia",
        "impactos-sociais",
        "prejuizos-economicos",
        "crise-2024",
        "data-science",
        "flood-analysis",
        "natural-disasters",
        "social-impact",
        "economic-losses",
    ],
    zip_safe=False,
)
