t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    prior = list(map(int, input().split()))
    prior_ = [0 for _ in range(n)]
    prior_[m] = 1
    cnt = 0
    while True:
        if prior[0] == max(prior):
            cnt += 1
            if prior_[0] == 1:
                print(cnt)
                break
            else:
                del prior[0]
                del prior_[0]
        else:
            prior.append(prior[0])
            del prior[0]
            prior_.append(prior_[0])
            del prior_[0]