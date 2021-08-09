# https://www.acmicpc.net/problem/20546
# 기적의 매매법, Bronze1 (정답 비율 : 56%)


money = int(input())
stock = list(map(int, input().split()))
#
# J_wallet = money
# J_stock = 0
#
# S_wallet = money
# S_stock = 0
#
# for i in stock:
#     if J_wallet >= i:
#         J_stock += J_wallet // i
#         J_wallet %= i
#     elif J_wallet == 0: break
#
# J_result = J_wallet + (J_stock * stock[-1])
#
# for i in range(len(stock)-4):
#     if stock[i] > stock[i+1] > stock[i+2] > stock[i+3]:
#         S_stock += S_wallet // stock[i+3]
#         S_wallet %= stock[i+3]
#
#     if stock[i] < stock[i+1] < stock[i+2] < stock[i+3]:
#         S_wallet += S_stock * stock[i+3]
#         S_stock = 0
#
# S_result = S_wallet + (S_stock * stock[-1])
#
# if J_result > S_result: print('BNP')
# elif J_result < S_result: print('TIMING')
# elif J_result == S_result: print('SAMESAME')


#==================================================================


def BNP():
    J_wallet = money
    J_stock = 0
    for i in stock:
        if J_wallet >= i:
            J_stock += J_wallet // i
            J_wallet %= i

    return J_wallet, J_stock


def TIMING():
    S_wallet = money
    S_stock = 0
    for i in range(len(stock)-4):
        if stock[i] > stock[i+1] > stock[i+2] > stock[i+3]:
            S_stock += S_wallet // stock[i+3]
            S_wallet  %= stock [i+3]
        elif stock[i] < stock[i+1] < stock[i+2] < stock[i+3]:
            S_wallet += S_stock * stock[i+3]
            S_stock = 0

    return S_wallet, S_stock

BNP_wallet, BNP_count = BNP()
BNP_result = BNP_wallet + (BNP_count * stock[-1])

TIMING_wallet, TIMING_count = TIMING()
TIMING_result = TIMING_wallet + (TIMING_count * stock[-1])

if BNP_result > TIMING_result: print('BNP')
elif BNP_result < TIMING_result: print('TIMING')
else: print("SAMESAME")
