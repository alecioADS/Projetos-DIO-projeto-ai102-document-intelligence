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

## Configuração de Variáveis de Ambiente

Este projeto utiliza serviços do Azure e requer a criação de um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```env
ENDPOINT=<SEU_ENDPOINT_DO_AZURE_DOCUMENT_INTELLIGENCE>
SUBSCRIPTION_KEY=<SUA_SUBSCRIPTION_KEY_DO_AZURE>
AZURE_STORAGE_CONNECTION_STRING=<SUA_CONNECTION_STRING_DO_BLOB_STORAGE>
CONTAINER_NAME=<NOME_DO_CONTAINER>
