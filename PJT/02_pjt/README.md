# OVERVIEW

첫 관통 프로젝트에서 json을 사용해 딕셔너리 형의 파일을 다루는 법을 연습했고

이번 주에는 url을 통해 웹에서 데이터를 읽어오는 법을 연습했다

## Problem_A

results에 results 안 데이터를 리스트 형태로 저장하고, 길이를 출력하면 끝나는 문제

## Problem_B

A와 기본적 뼈대는 같음

movie라는 빈 리스트를 만들어 results에서 vote_average 값이 8 이상일 때

movie.append()를 통해 리스트에 할당

## Problem_C

B와 기본적 뼈대는 같음

results를 sorted 함수와 lambda를 활용해 vote_average 기준으로 정렬

* sorted의 경우 기본 오름차순이기 때문에 내림차순으로 정렬하기 위해 reverse = True를 입력

이후에 4번 index까지 movies라는 빈 리스트에 할당

## Problem_D

사이트에서 긁어온 url에 &query={title}를 붙여주지않으면 안되는걸 몰랐음

f string을 활용해 고정된 title이 아닌 입력값에 따라 url이 바뀌도록 했으며

처음 url에서 받아온 데이터에서 movie_id를 추출한 후

새로운 url에 movie_id 값을 이용해 원하는 값을 받아옴

입력값이 없을 때 try except 구문을 활용해 None과 []를 출력하도록 함

## Problem_E

D와 거의 같은 논리로 풀이했으며

cast, crew 두개의 딕셔너리를 분리해 저장한 뒤

cast_id가 10 미만인 cast의 name을 main_cast라는 새 리스트에,

department가 Directing인 crew의 name을 directors라는 새 리스트에 할당한 뒤

새 딕셔너리에 {'cast' : main_cast, 'directing' : directors}로 할당 후 출력

## Problem_F

크게 3가지 과정으로 작성했음

1. 입력한 title에서 처음으로 검색되는 movie_id 저장
2. movie_id를 통해 찾은 데이터에서 처음으로 나오는 배우의 person_id 저장
3. person_id를 통해 찾은 데이터에서 배우가 출연한 영화 title을 출력