def binomial(N, K):
    C = [[0 for x in range(K + 1)] for x in range(N + 1)]
    for i in range(N + 1):
        for j in range(min(i, K) + 1):
            if j == 0 or j == i:
                C[i][j] = 1
            else:
                C[i][j] = C[i - 1][j - 1] + C[i - 1][j]

    return C[N][K] 