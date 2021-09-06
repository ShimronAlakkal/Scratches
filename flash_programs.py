def scroller():
    lis = eval(input('enter list here '))
    print(lis)
    lis_f = [lis[len(lis)-1]]
    print(lis_f)
    lis.remove(lis_f[0])
    print(lis)
    for i in range(len(lis)):
        lis_f.append(lis[i])

    print(lis_f)

scroller()
