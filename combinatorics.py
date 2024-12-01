import math

N = 26
K = 6
M = 4

def binomial_coef(n, k):
    if k > n or k < 0: return 0
    return math.comb(n, k)

def lottery_probability(N, K, M):
    total_ways = binomial_coef(N, K)
    winning_ways = 0
    
    for x in range(M, K + 1):
        ways_to_choose_x_from_ticket = binomial_coef(K, x)
        ways_to_choose_remaining_from_others = binomial_coef(N - K, K - x)
        winning_ways += ways_to_choose_x_from_ticket * ways_to_choose_remaining_from_others
    
    probability = (winning_ways / total_ways) * 100 if total_ways > 0 else 0
    return round(probability, 4)


result = lottery_probability(N, K, M)
print(f"Вероятность выигрыша: {result}%")