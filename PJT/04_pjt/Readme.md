django 기간 동안 배운 것들을 종합적으로 이용하는 프로젝트였습니다.



어려웠던 부분은 

1. actor_image를 ImageField로 받아와서 detail에서 보여주는 부분
2. score 필드를 설정하는 부분

이렇게 크게 두 부분이 있었습니다.



1. actor_image를 detail에서 보여주기

MEDIA_ROOT와 MEDIA_URL에 대한 부분을 진도 상 교안으로만 보고, 직접 활용해보는 것은 이번이 처음이었기에 헤맸던 부분이 있습니다.

mypjt의 urls.py에서 urlpatterns 뒤에  \+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)를 붙이지 않으면 사진을 제대로 가져오지 못하는 오류가 발생하는 것을 확인할 수 있었습니다.



2. score 필드를 설정하는 부분

forms.py에서 widgets에서 score에 해당하는 부분을 입력해주면 가능한 문제였습니다. 마찬가지로 release_date도 'type' : 'date'로 입력하게 되면 달력을 출력해서 직접 날짜를 입력하는 것이 아닌 달력에서 선택하는 방식으로 입력할 수 있도록 할 수 있었습니다.



3. 기타

genre를 코미디, 공포, 로맨스 중 하나로 선택하는 부분을 genre_choice라는 이중 튜플을 생성해 choices라는 변수에 넣어준다는 방식을 처음 접했는데, 매우 유용하게 사용했습니다.



이번 관통 프로젝트를 거치며 django에 여러가지 편리한 기능들이 있다는 것을 알게 되었습니다. 이번 django에서 배운 기초적으로 활용할 수 있는 부분에 더해 원하는 더 많은 기능들을 사용할 수 있기 위해서 많은 공부를 해야겠다는 생각을 했습니다.