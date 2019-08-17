# Este programa busca e monta uma lista de filmes recebida do usuário.

# Imports.
from imdb import IMDb
import youtube_api as ytapi
import argparse
import fresh_tomatoes
import media

# Recebendo uma lista de filmes do usuário.
movies_list = [movie for movie in input(
        "Enter your favorites movies names, separated by comma: ").split(',')]

# Atribuíndo uma instância IMDb.
ia = IMDb()

# Criando uma lista vazia [do tipo Movie].
movies = []
print("\nPreparing your movies list... \n")

# Iterando sobre cada filme em movieslist.
for movie in movies_list:
    print("Searching for {} data in IMDb...".format(movie))
    # Buscando por este filme no IMDb.
    s_result_list = ia.search_movie(movie)

    # Criando ambas variáveis que terão os respectivos filmes IMDb e a URL do
    # YouTube.
    imdb_movie = ''
    yt_trailer_url = ''

    # Para cada resultado encontrado na result_list.
    for s_result in s_result_list:
        # Se o resultado for um filme, pega o objeto movie e encerra a iteração
        if s_result['kind'] == 'movie':
            imdb_movie = ia.get_movie(s_result.movieID)
            break

    # Caso este filme exista, continua. Do contrário, imprime "movie not found"
    # e continua o resto da iteração.
    if imdb_movie:
        print("Searching movie trailer on youtube...")

        # Pega a URL do trailer do filme no YouTube.
        yt_trailer_url = ytapi.get_trailer_url(imdb_movie['long imdb title'])

        # Caso encontre a URL do trailer, continua.
        # Do contrário, o keyboard cat vai tocar!
        if yt_trailer_url:
            print("{} - OK \n".format(imdb_movie['long imdb title']))
        else:
            print("No official trailer found on Youtube for {}, so... "
                  "Play him off, keyboard cat!! \n".format(movie))
            yt_trailer_url = "https://www.youtube.com/watch?v=DK7CVqbtW0A"

        # Tenta criar uma instância da classe movie, então inclui esta
        # instância na lista de objetos movie.
        # Caso não consiga, trata e imprime a exceção na tela.
        try:
            movie_obj = media.Movie(imdb_movie['long imdb title'],
                                    imdb_movie['plot outline'],
                                    imdb_movie['full-size cover url'],
                                    yt_trailer_url)
            movies.append(movie_obj)
        except:
            print("Exception found when trying to access {} movie data: "
                  "'long imdb title', 'plot outline' or "
                  "'full-size cover url' \n".format(movie))
    else:
        print("No information found on IMDb for {}... \n".format(movie))
        continue

# Abre uma página na web com os filmes encontrados.
fresh_tomatoes.open_movies_page(movies)
