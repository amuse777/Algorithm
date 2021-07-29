# https://www.acmicpc.net/problem/1157
# 단어 공부, Bronze1 (정답 비율 : 39%)

word = input().upper()
list_w = list(set(word))

cnt = []

for i in list_w:
   count = word.count(i)
   cnt.append(count)

if cnt.count(max(cnt)) >= 2:
    print('?')
else:
    print(list_w[cnt.index(max(cnt))])

    print()