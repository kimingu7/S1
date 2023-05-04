1. ```html
   <div class ="a" :class"{a:isA}>테스트</div>
   ```

   어떤 클래스를 가지고 어떻게 렌더링 되는지

2. 컴포넌트에 대한 설명 (독립, 재사용성 등)

3. 라이프사이클 created (생성은 됐지만, mount 되지 않은 상태)

4. vuex에 대한 설명 

5. ```html
   <div v-for="" in ~~s"">
   ```

   v-for 키워드 ~~ 순서 (문법)

6. 축약 표현 (:, @ 등)

7. vue-cli 만드는 명령어 (vue create vue-cli)

8. vue.js 디자인 패턴 (MVVM)

9. vuex 키워드 (actions)

10. vue에서 이벤트를 거는 법

11. 자식에서 부모 emit, 부모에게 자식 props

12. ```html
    <div v-if="a">a</div>
    <div>a</div>
    <div v-else>b</div>
    ```

    이런 식으로 코드 주어지면 어떻게 렌더링

13. vue 양방향 바인딩 키워드

14. 데이터를 올바르게 동작하기 위한 코드 (함수인지, 객체인지, return 하는지)

15. vue에 대한 옳지않은 설명

16. html의 관련 속성 v-text, v-html?

17. 바벨

18. 데이터의 속성이 color: red인데 태그에 적용시키려면

19. 라이프사이클에 해당되지 않는 존재

20. computed 속성

21. 양방향 바인딩 키워드 (13번과 같음)

22. 라이프사이클로 어떠한 인스턴스가 화면에 부착됐을 때 시점(mounted)

23. @ 뜻은 두개 하나는 템플릿, 하나는 스크립트

24. 모든 컴포넌트에서 데이터를 보관하는게 아니라 vuex를 사용. 데이터를 보관하고 있는 이름 (state)

25. 태그 속성에서 html 관련 속성

26. 비동기함수 action을 호출하기 위해 불러야하는 함수 (dispatch)

27. vuex에서 computed와 같은 역할 (getter)

28. a라는 컴포넌트를 부모 컴포넌트가 그리기 위해 script에서 해야하는 작업 (import)

29. vue.js에서 watch 속성 (데이터의 변화를 감지하고, 이에 따른 특정 동작을 수행할 수 있도록 하는 기능)

30. vue에서 v-if, v-show 비교 (v-if는 false일 때 요소를 DOM에서 제거, v-show는 false일 때 display를 none으로 변경함. v-if는 초기 렌더링 속도 이점, v-show는 자주 바뀌는 조건에 대응하기 쉬움)