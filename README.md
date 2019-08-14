# finding_movies
finding_movies é um aplicativo _server-side_ que busca filmes através de nomes informados pelo usuário no site de filmes [IMDb](https://www.imdb.com/) e, quando os encontra, busca seu trailer oficial no [YouTube](https://www.youtube.com/). Ao final, monta uma página em seu navegador _web_ contendo a capa de cada filme encontrado e seu respectivo trailer.

# Começo rápido

Este projeto ainda não encontra-se disponibilizado na _internet_. Para obter o código deste projeto, envie um e-mail para **kassem.zaher@outlook.com** com o assunto **finding_movies code**.

## Instalação

Baixe e instale o python em seu computador de acordo com o seu sistema operacional:
* [Windows](https://www.python.org/downloads/windows/)
* [Mac OS X](https://www.python.org/downloads/mac-osx/)
* [Linux/UNIX](https://www.python.org/downloads/source/)
* [Outros](https://www.python.org/download/other/)

Abra o prompt de comando e instale, respectivamente, as APIs do IMDb e Google:
`$ pip install IMDbPY`

`$ pip install --upgrade google-api-python-client`
`$ pip install --upgrade google-auth google-auth-oauthlib google-auth-httplib2`

Para usar a API do Google, você precisará de uma conta Google e obter uma chave de desenvolvedor. Você pode seguir o passo-a-passo para obter a chave neste [link](https://developers.google.com/youtube/v3/quickstart/python).
Após finalizar o passo-a-passo acima, localize o código abaixo no programa *youtube_api.py* e preencha com a sua chave de desenvolvedor da API Google:
```
DEVELOPER_KEY = 'SUA CHAVE AQUI'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'
```
Isto permitirá que o programa faça buscas no YouTube.
Para mais informações sobre as API's, visite as páginas [IMBbpy](https://imdbpy.sourceforge.io/index.html) e [Google API](https://developers.google.com/youtube/v3/getting-started).

## Como usar

1. Extraia todos os arquivos no mesmo diretório.
2. Abra o prompt de comando.
3. Localize o diretório com o arquivo `entertainment_center.py`.
4. Execute o arquivo com o comando `$ python entertainment_center.py`.
5. Digite o(s) nome(s) do(s) filme(s) que deseja buscar.
    + Após finalizar a busca, o programa exibirá uma página com a capa do filme.
    + Para ver o trailer oficial encontrado, basta clicar na capa do filme desejado.

# Problemas

As limitações de busca deste programa estão atreladas as limitações do algoritmo de busca do IMDb. Em alguns casos como filmes com várias continuações, o algoritmo pode se confundir se o nome do filme não for especificado com detalhes.
Por exemplo, se você deseja ver o trailer do filme "Star Wars I", ele terá dificuldade em identificar qual Star Wars está sendo buscado (_Star Wars Epidode I The Phantom Menace_ ou _Star Wars IV A New Hope_). Nestes casos, você pode escrever o nome do filme completo ou a data em que foi lançado (_Star Wars 1999_).
**Prefira sempre buscar os nomes dos filmes em inglês. Buscas em outros idiomas podem gerar confusões nos resultados encontrados pelo algoritmo do IMDb.**

Alguns trailers podem não ser exibidos na página. Isto varia de acordo com a disponibilidade daquele trailer para o país de onde foi realizado a busca ou mesmo limitações impostas pelo próprio canal, de acordo com termos de exibição.
Em casos de refilmagens de filmes antigos, pode ocorrer da busca retornar o filme mais atual. Filmes antigos podem não conter um "trailer oficial" no YouTube.

# Referências

Para o desenvolvimento deste projeto, foram realizadas pesquisas em sites como:
* [Stack Overflow](https://stackoverflow.com/) - Dúvidas e dicas de utilização das APIs
* [Developers Google](https://developers.google.com/youtube/v3/) - Como usar a Google API para buscar no YouTube
* [IMDbpy Sourceforge](https://imdbpy.sourceforge.io/index.html) - Como usar a API do IMDb para buscar filmes
* [Udacity](https://br.udacity.com/) - Motivação do projeto e disponibilização do código *fresh_tomatoes.py*

O arquivo *youtube_api.py* foi criado a partir do exemplo usado neste [link](https://developers.google.com/youtube/v3/code_samples/python#search_by_keyword).

# Licença

finding_movies é _Copyright_ © 2018 Kassem Zaher Filho. É um software livre, e pode ser redistribuído sob os termos especificados no arquivo [LICENSE](\LICENSE.txt).
