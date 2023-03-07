import json


def en_movies(movies):
    title = []
    language = []
    for i in movies:
        id = i.get('id')
        movie = open(f'data/movies/{id}.json', encoding='utf-8')
        movie_list = json.load(movie)
        language = movie_list['original_language']
        if language == 'en':
            title.append(movie_list['title'])
    return title

    # 여기에 코드를 작성합니다.  
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(en_movies(movies_list))
