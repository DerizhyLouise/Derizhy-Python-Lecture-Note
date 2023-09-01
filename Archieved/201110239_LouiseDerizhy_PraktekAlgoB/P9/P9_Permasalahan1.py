def ubah(x):
    for i in range(len(x)):
        x[i] = int(x[i])

    h = ""
    for i in range(len(x)):
        for j in range(len(arr)):
            if(x[i]==arr[j]):
                h += huruf[j] 
    return h
                
arr = [2,22,222,3,33,333,4,44,444,5,55,555,6,66,666,7,77,777,7777,8,88,888,9,99,999,9999,0]
huruf = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
x = input().split()

print(ubah(x))