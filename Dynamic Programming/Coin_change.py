def minCoins(coins, m, V):
    table = [0 for i in range(V + 1)]
    for i in range(1, V + 1):
        table[i] = float('inf')
    for i in range(1, V + 1):
        for j in range(m):
            if (coins[j] <= i):
                sub_res = table[i - coins[j]]
                if (sub_res != float('inf') and
                        sub_res + 1 < table[i]):
                    table[i] = sub_res + 1
    return table[V]


arr = [9, 6, 5, 1]
m = len(arr)
n = 11
x = minCoins(arr, m , n)
print (x)