"""
https://www.codewars.com/kata/56f78a42f749ba513b00037f

Probabilities for Sums in Rolling Cubic Dice
"""
def ans(sum_all, n): #次数
    if n == 1:
        if 1 <= sum_all <= 6:
            return 1
        else:
            return 0
    else:
        return sum([ans(sum_all - i, n - 1) for i in range(1, 7)])

def rolldice_sum_prob(x, n):
    return ans(x, n) / (6 ** n)

print(rolldice_sum_prob(8,2))