def solve(a, b):
    counter = 0
    markers = ['2', '3', '4', '5', '7',]
    for i in range(a, b + 1):
        res = []
        var = list(str(i))
        for j in var:
            if j in markers:
                break
            elif j == '6':
                res.append('9')
            elif j == '9':
                res.append('6')
            else:
                res.append(j)
        if var == res[::-1]:
            counter+=1
        res.clear()
    return counter


print(solve(60000, 130000))