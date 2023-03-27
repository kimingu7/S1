import requests

URL = 'https://api.themoviedb.org/3/movie/popular?api_key=b1050a42afaab2565b52746c192c77a4&language=en-US&page=1'

def popular_count():
    response = requests.get(URL).json()
    results = response.get('results')
    return len(results)
    # 여기에 코드를 작성합니다.  

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
