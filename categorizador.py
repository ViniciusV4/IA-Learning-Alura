from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv()

# Diretório do projeto
BASE_DIR = Path(__file__).resolve().parent

# Carregando o System Prompt
prompt_system = (
    BASE_DIR / "prompts" / "system_prompt.md"
).read_text(encoding="utf-8")

# Carregando o catálogo de produtos
produtos = (
    BASE_DIR / "prompts" / "produtos.md"
).read_text(encoding="utf-8")

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

model = "gpt-4o-mini"


def categoriza_produtos (nome_produto, lista_categorias):
    """
        Função para categorizar produtos com base em uma lista de categorias fornecida.
    """
    print(lista_categorias)
    prompt_system = f"""
        Você é um categorizador de produtos.
        Você deve assumir as categorias presentes na lista abaixo.

        # Lista de Categorias Válidas
        {lista_categorias.split(",")}

        # Formato da Saída
        Produto: Nome do Produto
        Categoria: apresente a categoria do produto

        # Exemplo de Saída
        Produto: Escova elétrica com recarga solar
        Categoria: Eletrônicos Verdes
    """


    response = client.chat.completions.create(
        model=model,
        max_tokens=400,
        n=1,
        frequency_penalty=1.0,
        messages=[
            {
                "role": "system",
                "content": prompt_system
            },
            {
                "role": "user",
                "content": (
                    f"Produto:\n{nome_produto}"
                )
            }
        ]
    )

    return response.choices[0].message.content

categorias_validas = input("Digite as categorias válidas: ")

while(True):
    nome_produto = input("Digite o nome de um produto: ")
    print(categoriza_produtos(nome_produto, categorias_validas))