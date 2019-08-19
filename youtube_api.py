#!/usr/bin/python

# Este programa realiza uma requisição de busca no youtube pelo termo recebido
# por parâmetro.

# NOTE: É necessário informar uma chave de desenvolvedor obtida no console da
#       Google API.
#       Procure por 'SUA_DEVELOPER_KEY_AQUI' e substitua com sua Developer Key.
#       Para mais informações de como obter essa chave, veja o README.md deste
#       projeto.

# Imports.
import argparse
import re
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Atribui os parâmetros necessários para realizar a requisição.
# 'SUA_DEVELOPER_KEY_AQUI'
DEVELOPER_KEY = 'ADD_YOUR_DEVELOPER_KEY_HERE'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'


def youtube_search(options):
    # Cria um objeto de comunicação com youtube,
    # passando as chaves necessárias.
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    # Chama o método search.list para obter os resultados que correspondem ao
    # termo da consulta especificada.
    search_response = youtube.search().list(q=options.q, part='id,snippet',
                                            type=options.type,
                                            maxResults=options.max_results,
                                            videoEmbeddable=options.embeddable,
                                            videoSyndicated=options.syndicated
                                            ).execute()

    # Lê cada resultado da lista de resultados obtidas.
    for search_result in search_response.get('items', []):
        # Obtém o título do resultado.
        video_title = search_result['snippet']['title']
        # Verifica se existe a palavra "Official" e "Trailer" no título.
        is_official = re.search(r'([Oo]+[FfIiCcAa]+[Ll]+)', video_title,
                                re.IGNORECASE)
        is_trailer = re.search(r'([Tt]+[RrAaIiLlEe]+[Rr]+)', video_title,
                               re.IGNORECASE)
        # Caso as duas palavras estejam contidas no título,
        # retorna a URL do vídeo.
        if is_official and is_trailer:
            return "https://www.youtube.com/watch?v={}".format(
                    search_result['id']['videoId'])
    # Caso não encontre nada, retorna vazio
    return ""


def get_trailer_url(movie):
    # Monta os argumentos necessários para realizar a busca,
    # através de um objeto parser.
    trailer_to_search = movie + " official trailer"
    parser = argparse.ArgumentParser()
    # Termo para busca, sendo o nome do filme + "official trailer".
    parser.add_argument('--q', help='Search term', default=trailer_to_search)
    # Apenas resultados do tipo vídeo.
    parser.add_argument('--type', help='Type', default='video')
    # Busca com máximo de 10 resultados.
    parser.add_argument('--max-results', help='Max results', default=10)
    # Apenas vídeos que possam ser incorporados a uma página.
    parser.add_argument('--embeddable', help='Video embeddable',
                        default='true')
    # Apenas vídeos que possam ser reproduzidos fora do youtube.
    parser.add_argument('--syndicated', help='Video syndicated',
                        default='true')
    args = parser.parse_args()

    try:
        return youtube_search(args)
    except HttpError as e:
        print("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))
