# 소수찾기 (정답률 48%)

num = int(input())
num_list = list(map(int, input().split()))
prime = 0

if num == len(num_list):
    for i in num_list:
        cnt = 0
        for j in range(1, i+1):
            if i % j == 0:
                cnt += 1
        if cnt == 2:        # 소수가 아니라면 카운트가 3이상이 된다. ex) 4의 나머지가 0인 수 : 1, 2, 4
            prime += 1

print(prime)