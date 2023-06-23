tc = int(input())

for t in range(tc):
    category = {}
    n = int(input())
    res = 1
    for i in range(n):
        name, cate = input().split()
        if cate not in category: 
            category[cate] = 1
        else:
            category[cate] +=1

    for i in category.items():
        res *= (i[1]+1)

    

    print(res-1)
    
""" 
2 2
3 3
4 4

3 7 15

a b
1 2

1 2
12
3

a b
12 3

1 2 3
13 23
4C3 = 4
5
3C2 +2
2C2
3C3
3C1
a b c
1 2 3 

1 2 3
12 13 23
123

7
4C3 + 
a  b  c
12 3  4

1 2 3 4
13 14 23 24 34
134 234 
11

a b c d
1 2 3 4
12 13 14 23 24 34
123 124 134 234
1234
15


"""
