# Créditos e Fontes de Dados

Todos os livros presentes nesta pasta foram obtidos do [Project Gutenberg](https://www.gutenberg.org/) no formato **HTML**.

## Livros Catalogados

| ID Gutenberg | Arquivo | Título | Autor | Idioma | Link do Gutenberg |
|---|---|---|---|---|---|
| **55682** | `55682-h.htm` | Quincas Borba | Machado de Assis | Português | [Gutenberg #55682](https://www.gutenberg.org/ebooks/55682) |
| **55752** | `55752-h.htm` | Dom Casmurro | Machado de Assis | Português | [Gutenberg #55752](https://www.gutenberg.org/ebooks/55752) |

---

## Detalhes dos Créditos e Digitalização

- **Quincas Borba (#55682):** Digitalizado e preparado por *Laura Natal Rodriguez & Marc D'Hooghe* (Free Literature / Internet Archive).
- **Dom Casmurro (#55752):** Digitalizado e preparado por *Laura Natal Rodriguez & Marc D'Hooghe* (Free Literature / Internet Archive).

---

## Observações de Licença e Uso no RAG (Arquivos HTML)

1. **Licença:** Ambas as obras estão em **Domínio Público** nos Estados Unidos e em grande parte do mundo.
2. **Parsing de HTML:** Como os arquivos estão em HTML, utilize parsers adequados (como `BS4HTMLLoader` do LangChain ou `BeautifulSoup` nativo) para extrair o texto limpo mantendo a estrutura dos parágrafos/capítulos (`<p>`, `<h1>`, `<h2>`).
3. **Limpeza de Cabeçalhos e Rodapés:** Remova as tags ou divs de aviso de licença do Project Gutenberg localizadas no início e no fim do documento HTML antes de realizar o *chunking* para os embeddings.