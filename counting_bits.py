def countbits(n):
    ans = [0]*(n+1)

    for i in range(1, n+1):
        ans[i] = ans[i >> 1] + (i & 1)

    return ans


if __name__ == "__main__":
    print(countbits(2))
    print(countbits(5))
