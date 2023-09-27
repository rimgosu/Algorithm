while True:
    a = int(input())
    lst = []
    for i in range(1, a):
        if a % i ==0 :
            lst.append(i)

    # print(lst, sum(lst))

    if sum(lst) == a:
        print(f'{a} = ', end = "")
        for i in range(len(lst)-1):
            print(f'{lst[i]} + ' , end = '')
        
        print(lst[-1])

    elif a == -1 :
        break

    else : 
        print(f'{a} is NOT perfect.' )



