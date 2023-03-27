import requests
from pprint import pprint



def recommendation(title):
    URL = f'https://api.themoviedb.org/3/search/movie?api_key=b1050a42afaab2565b52746c192c77a4&language=en-US&page=1&include_adult=false&query={title}'
    response = requests.get(URL).json()
    results = response.get('results')
    try :
        movie_id = results[0]['id']
    except IndexError :
        return None
    URL_ = f'https://api.themoviedb.org/3/movie/{movie_id}/recommendations?api_key=b1050a42afaab2565b52746c192c77a4&language=en-US&page=1'
    response_ = requests.get(URL_).json()
    results_ = response_.get('results')
    try :
        title = results_[0]['title']
        return title
    except IndexError:
        return []
    # 여기에 코드를 작성합니다.  


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
