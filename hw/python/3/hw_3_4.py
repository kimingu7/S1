s_triangle = input().split()
s_triangle = list(s_triangle)
s_triangle = list(map(int, s_triangle))
s_triangle.sort()
if s_triangle[0] == s_triangle[1] and s_triangle[0] == s_triangle[2]:
    print('정삼각형')
elif s_triangle[0] == s_triangle[1] and s_triangle[0] != s_triangle[2]:
    print("이등변삼각형")
elif s_triangle[0] == s_triangle[2] and s_triangle[0] != s_triangle[1]:
    print("이등변삼각형")
elif s_triangle[1] == s_triangle[2] and s_triangle[0] != s_triangle[1]:
    print("이등변삼각형")
elif (s_triangle[0] ** 2) + (s_triangle[1] ** 2) == (s_triangle[2] ** 2) :
    print("직각삼각형")
elif s_triangle[0] + s_triangle[1] > s_triangle[2]:
    print("삼각형")
else :
    print("삼각형 아님")