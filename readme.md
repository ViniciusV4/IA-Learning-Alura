# Exercícios de GPT e Python com a API da OpenAI

Repositório de exercícios práticos desenvolvidos durante o curso [GPT e Python: criando ferramentas com a API](https://cursos.alura.com.br/course/gpt-python-criando-ferramentas-com-api), da formação de [Inteligência Artificial da Alura](https://cursos.alura.com.br/search?query=inteligencia-artificial&categoryFilters=inteligencia-artificial).

Os exemplos exploram chamadas à API da OpenAI, engenharia de prompt, templates, contagem de tokens, seleção de modelos, processamento de arquivos, tratamento de erros e análise de transações. O código tem finalidade educacional e serve como ponto de partida para experimentos com aplicações de IA generativa em Python.

## Conteúdos praticados

- Integração com a API de chat da OpenAI.
- Carregamento da chave da API por variável de ambiente.
- Definição de mensagens `system` e `user`.
- Engenharia de prompt com persona, contexto, regras e formato de saída.
- Categorização de produtos a partir de categorias informadas pelo usuário.
- Contagem de tokens com `tiktoken`.
- Estimativa simples de custos entre modelos.
- Escolha dinâmica de modelo conforme o tamanho da entrada.
- Processamento de avaliações de produtos e análise de sentimentos.
- Classificação de transações como aprovadas ou possíveis fraudes.
- Geração de pareceres e recomendações para transações suspeitas.
- Leitura e gravação de arquivos de texto, CSV e JSON.

## Estrutura do repositório

| Arquivo ou diretório | Descrição |
| --- | --- |
| [`main.py`](./main.py) | Exemplo introdutório de chamada à API, solicitando uma lista de produtos sustentáveis. |
| [`categorizador.py`](./categorizador.py) | Categoriza produtos com base na lista de categorias fornecida no terminal. |
| [`contador_token.py`](./contador_token.py) | Codifica um prompt, conta tokens e calcula uma estimativa de custo para dois modelos. |
| [`selecao_de_modelo.py`](./selecao_de_modelo.py) | Lê a lista de compras de clientes, calcula o tamanho da entrada e seleciona um modelo. |
| [`analisador_de_sentimentos.py`](./analisador_de_sentimentos.py) | Resume avaliações de produtos, identifica o sentimento geral e registra pontos fortes e fracos. |
| [`analisador_de_transacoes.py`](./analisador_de_transacoes.py) | Analisa transações, gera pareceres para possíveis fraudes e produz recomendações. |
| [`prompts/`](./prompts/) | Prompts reutilizáveis e catálogo de produtos usados nos exercícios. |
| [`data/`](./data/) | Avaliações, análises geradas, lista de compras e transações de exemplo. |
| [`.env`](./.env) | Arquivo local para a chave da API; não deve ser compartilhado nem versionado. |
| [`.gitignore`](./.gitignore) | Ignora ambientes virtuais, arquivos `.env` e artefatos gerados pelo Python. |

## Pré-requisitos

- Python 3.10 ou superior.
- Uma chave válida da API da OpenAI.
- Acesso à internet para realizar as chamadas à API.

As versões dos modelos e os preços da OpenAI podem mudar. Os valores exibidos por `contador_token.py` são exemplos didáticos e não substituem a tabela de preços atual.

## Configuração do ambiente

No PowerShell, a partir da raiz do projeto:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install openai python-dotenv tiktoken
```

Crie um arquivo `.env` na raiz do projeto com a sua própria chave:

```env
OPENAI_API_KEY=sua_chave_da_openai
```

Nunca publique a chave no Git, em screenshots ou em mensagens. Se uma chave real tiver sido exposta, revogue-a no painel da OpenAI e gere outra.

## Como executar

Ative o ambiente virtual antes de executar os exemplos:

```powershell
.\.venv\Scripts\Activate.ps1
```

### Exemplo básico

```powershell
python .\main.py
```

### Categorizador de produtos

O programa solicita primeiro as categorias válidas e depois continua solicitando nomes de produtos:

```powershell
python .\categorizador.py
```

Para encerrar o loop interativo, use `Ctrl+C`.

### Tokens e custos

Este exercício não faz chamada à API:

```powershell
python .\contador_token.py
```

### Seleção de modelo

O script utiliza [`data/lista_de_compras_100_clientes.csv`](./data/lista_de_compras_100_clientes.csv) como entrada:

```powershell
python .\selecao_de_modelo.py
```

### Análise de sentimentos

As avaliações de três produtos são lidas de `data/avaliacoes-*.txt`. As análises são salvas em `data/analise-*.txt`:

```powershell
python .\analisador_de_sentimentos.py
```

### Análise de transações

O script lê [`data/transacoes.csv`](./data/transacoes.csv), identifica possíveis fraudes e salva as recomendações em arquivos dentro de `data/transacoes/`. Crie o diretório de saída antes da primeira execução:

```powershell
New-Item -ItemType Directory -Force .\data\transacoes
python .\analisador_de_transacoes.py
```

## Observações sobre os exemplos

- Os scripts são independentes e executam chamadas reais à API; cada execução pode gerar custo.
- Os arquivos `analisador_de_sentimentos.py` e `analisador_de_transacoes.py` definem um modelo de exemplo no código. Antes de executar, confira se esse identificador corresponde a um modelo disponível na sua conta e substitua-o, se necessário.
- As respostas de modelos generativos podem variar. Para aplicações reais, valide o conteúdo retornado antes de persistir ou utilizar os dados.
- A análise de transações é apenas um exercício de classificação com dados de exemplo; não deve ser usada como mecanismo de decisão financeira ou antifraude em produção.
- O processamento depende do diretório de execução. Execute os comandos a partir da raiz do repositório para que os caminhos `./data` sejam encontrados.
- O uso de `json.loads` pressupõe que o modelo retorne JSON válido. Em uma aplicação real, é recomendável validar o schema e tratar respostas incompletas ou inválidas.

## Relação com o curso

Os exercícios acompanham os principais módulos do curso:

1. **Playground e API da OpenAI** — integração em Python, mensagens e proteção da API key.
2. **Prompt engineering e prompt template** — persona, contexto, formato de saída e categorização.
3. **Custos, modelos e contagem de tokens** — `tiktoken`, estimativas e escolha de modelo.
4. **Batch e controle de erros** — análise de sentimentos, leitura de arquivos e tratamento de erros.
5. **Praticando: análise de fraudes** — classificação, pareceres e recomendações sobre transações.

## Créditos

Material desenvolvido como parte dos estudos do curso da [Alura](https://www.alura.com.br/). Consulte a [página do curso](https://cursos.alura.com.br/course/gpt-python-criando-ferramentas-com-api) para a sequência completa das aulas e os conceitos apresentados.
