from collections import deque
T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    cheese = deque(list(map(int, input().split())))
    pizzas = deque([i+1 for i in range(m)])
    oven = deque(maxlen=n)
    pizza_num = deque(maxlen=n)
    for i in range(n):
        oven.append(cheese.popleft())
        pizza_num.append(pizzas.popleft())
    while oven:
        if len(pizza_num) == 1:
            ans = pizza_num[0]
            break
        pizza = oven.popleft()
        num = pizza_num.popleft()
        if pizza > 1:
            oven.append(pizza//2)
            pizza_num.append(num)
        else :
            pass
        if len(oven) < n and cheese:
            oven.append(cheese.popleft())
            pizza_num.append(pizzas.popleft())
    print(f'#{tc}',ans)

# 크기가 한정된 deque에 순차적으로 과정을 실행한 뒤 새로운 원소를 추가해주는 문제
# deque의 크기는 n으로 한정됨(화덕의 크기가 n)
# oven은 실제로 피자가 들어가는 deque
# pizza_num은 피자의 순서를 알기 위한 deque
# n만큼 oven과 pizza_num에 append 시키고 시작
# line 14-16 oven 또는 pizza_num의 원소의 개수가 하나(남은 피자가 하나)일 때 pizza_num[0]을 ans에 할당
# line 17-20 oven의 제일 앞 피자를 꺼내 1보다 크다면 //2해 다시 오븐의 맨뒤로 넣음
# 이 때 순서를 기억하기 위해 pizza_num 또한 맨 뒤로 넣어줌
# 0보다 작을 경우 다시 들어오지 않기 때문에 oven의 크기가 n보다 작아짐
# line 24-26 따라서 oven의 크기가 n보다 작으며 cheese에 남은 피자가 있을 때 새로운 피자를 추가해줌