# Uses python3
def edit_distance(s, t):
    #write your code here
    if (len(s) == 0):
        return len(t)
    if (len(t) == 0):
        return len(s)    

    result = [[i for i in range(len(s)+1)]]
    for i in range(1, len(t)+1): # 列
        tmp = [i]
        for j in range(1, len(s)+1): # 行
            if (t[i-1] == s[j-1]):
                tmp.append(min(tmp[j-1]+1, result[i-1][j]+1, result[i-1][j-1]))
            else:
                tmp.append(min(tmp[j-1]+1, result[i-1][j]+1, result[i-1][j-1]+1))
        result.append(tmp)
    # print(result)
    return tmp[-1]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
    # print(edit_distance("short", "ports"))