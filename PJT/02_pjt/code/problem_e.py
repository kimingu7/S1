import requests
from pprint import pprint


def credits(title):
    URL = f'https://api.themoviedb.org/3/search/movie?api_key=b1050a42afaab2565b52746c192c77a4&language=en-US&page=1&include_adult=false&query={title}'
    response = requests.get(URL).json()
    results = response.get('results')
    try :
        movie_id = results[0]['id']
    except IndexError :
        return None
    URL_ = f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key=b1050a42afaab2565b52746c192c77a4&language=en-US'
    response_ = requests.get(URL_).json()
    cast = response_.get('cast')
    crew = response_.get('crew')
    main_cast = []
    directors = []
    for item in cast:
      if item['cast_id'] < 10:
        main_cast.append(item['name'])
    for item in crew:
      if item['department'] == 'Directing':
        directors.append(item['name'])
    dic = {'cast' : main_cast, 'directing' : directors}
    return dic
    # 여기에 코드를 작성합니다.  


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None