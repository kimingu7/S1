import json


def max_revenue(movies):
    revenues = []
    title = []
    for i in movies:
        id = i.get('id')
        movie = open(f'data/movies/{id}.json', encoding='utf-8')
        movie_list = json.load(movie)
        revenues.append(movie_list['revenue'])
        title.append(movie_list['title'])
    max_title = title[revenues.index(max(revenues))]

    return max_title
    # 여기에 코드를 작성합니다.  
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))
