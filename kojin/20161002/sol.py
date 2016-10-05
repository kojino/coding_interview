def longestEvenSubstr(string):
    n = len(string)
    N = [[0 for i in range(n)] for j in range(n)]
    N[0][0] = string[0]
    for i in range(n):
        el = int(string[i])
        for j in range(i):
            N[j][i] += N[j][i-1] + el
        N[i][i] = el
    current_max = 0
    for j in range(n):
        i = j
        while 2*i+1-j < n:
            if N[j][i] == N[i+1][2*i+1-j]:
                current_max = max(i-j+1,current_max)
            i += 1
    return current_max*2

print longestEvenSubstr("123123")
print longestEvenSubstr("1538023")
