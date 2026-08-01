# Aplicação baseada em RAG (powered by Python)

## Setup

```bash
# criando virtual
python -m venv .venv

# ativando ambiente virutal

## No Windows (CMD):
.venv\Scripts\activate
## No Windows (PowerShell):
.venv\Scripts\Activate.ps1
## Nos sistemas macOS/Linux:
source .venv/bin/activate

# instlando dependências versionadas
pip install -r requirements.txt
```

## Adicionando novas dependências

```bash
# é só ativar o virtualenve e instalar o pacote com o comando pip
pip install requests pandas  # replace with whatever packages you need

# depois é só gerar o requiments.txt de novo, ainda dentro do virtualenv
pip freeze > requirements.txt
```

## Rodando server

```bash
# rodando em modo dev
cd app && uv run fastapi dev

# outra forma de rodar
fastapi dev app/main.py

# ou para rodar em modo "reload on code change"
uvicorn app.main:app --reload

# ou para simular produção
fastapi run app.main.py
```

