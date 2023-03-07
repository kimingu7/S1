import json
from pprint import pprint


def movie_info(movies, genres):
    movies_data=[]
    for i in movies:
            movie_data={
                'id': i.get('id'),
                'overview': i.get('overview'),
                'poster_path': i.get('poster_path') ,
                'title' : i.get('title'),
                'vote_average' : i.get('vote_average'),
            }
            movies_data.append(movie_data) 
            genre_ids = i['genre_ids']
            genre_names = []
            for ids in genre_ids:
                for i in genres:
                    if ids == i['id']:
                        ids = 0
                        genre_names.append(i['name'])
            movie_data['genre_names'] = genre_names 
    return movies_data 
    # 여기에 코드를 작성합니다.  
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))
