# Projeto AI-102 – Análise de Cartão de Crédito

Aplicação desenvolvida em Python utilizando Streamlit e Azure AI Document Intelligence para realizar a análise automática de cartões de crédito a partir de imagens.

## Funcionalidades
- Upload de imagem de cartão de crédito
- Armazenamento no Azure Blob Storage
- Análise do cartão utilizando o modelo prebuilt-creditCard
- Exibição das informações extraídas

## Tecnologias Utilizadas
- Python
- Streamlit
- Azure Blob Storage
- Azure AI Document Intelligence

## Como Executar o Projeto

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run src/app.py
