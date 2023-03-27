import json
from pprint import pprint


def movie_info(movie, genres):
    movie_data = {
        'id': movie.get('id'),
        'overview': movie.get('overview'),
        'poster_path': movie.get('poster_path'),
        'title' : movie.get('title'),
        'vote_average' : movie.get('vote_average')
    }
    genre_ids = movie['genre_ids']
    genre_names = []
    for ids in genre_ids:
        for i in genres:
            if ids == i['id']:
                ids = 0
                genre_names.append(i['name'])
    movie_data['genre_names'] = genre_names
    return movie_data 
    # 여기에 코드를 작성합니다.


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))