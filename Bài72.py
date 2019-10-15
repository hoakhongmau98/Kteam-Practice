def bin_search(a,b):
    ln_lst = 0
    c = []
    for i in range(len(a)):
        if a[i]==b:
            c.append(str(i))
        else:
            ln_lst +=1
            if ln_lst == len(a):
                c.append('-1')
    return c
li=[2,5,7,9,11,17,11,222]
print(','.join(bin_search(li,11)))
print(','.join(bin_search(li,12)))
