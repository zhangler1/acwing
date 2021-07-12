def shortest_path_algorithm():
    n,m,k=input()
    dp=[[float("inf")*n]for _ in range(n)]
    for s,d,weight in range(m):
        dp[s][d]=weight



