import json


def dec_movies(movies):
    title = []
    release_date = []
    for i in movies:
        id = i.get('id')
        movie = open(f'data/movies/{id}.json', encoding='utf-8')
        movie_list = json.load(movie)
        release_date = movie_list['release_date']
        if release_date[5] == '1' and release_date[6] == '2':
            title.append(movie_list['title'])
    return title

    # 여기에 코드를 작성합니다.  
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))
