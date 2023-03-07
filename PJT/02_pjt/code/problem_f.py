import requests
from pprint import pprint


def credits(title):
    URL = f'https://api.themoviedb.org/3/search/movie?api_key=b1050a42afaab2565b52746c192c77a4&language=ko-KR&page=1&include_adult=false&query={title}'
    response = requests.get(URL).json()
    results = response.get('results')
    movie_id = results[0]['id']
    URL1 = f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key=b1050a42afaab2565b52746c192c77a4&language=ko-KR'
    response1 = requests.get(URL1).json()
    cast = response1.get('cast')
    person_id = cast[0]['id']
    name = cast[0]['name']
    URL2 = f'https://api.themoviedb.org/3/person/{person_id}/movie_credits?api_key=b1050a42afaab2565b52746c192c77a4&language=ko-KR'
    response2 = requests.get(URL2).json()
    casting = response2.get('cast')
    title = []
    for item in casting:
        title.append(item['title'])
    print(f'{name}의 출연작은')
    for name in title:
        print(name, end=', ')
    print('입니다')
    # 여기에 코드를 작성합니다.  


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    credits(input())