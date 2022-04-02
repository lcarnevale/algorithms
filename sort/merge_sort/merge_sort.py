def merge(s1,s2,s):
    i = j = 0
    while i+j < len(s):
        if j==len(s2) or (i<len(s1) and s1[i]<s2[j]):
            #print("IF: ",i,'\t',j,'\t')
            s[i+j] = s1[i]
            i += 1
        else:
            #print("ELSE: ",i,'\t',j,'\t')
            s[i+j] = s2[j]
            j += 1
    return s

def merge_sort(s):
    n = len(s)
    if n < 2:
        return
    mid = n // 2
    s1 = s[0:mid]
    s2 = s[mid:n]
    #print("Prima: ",s1,s2,s)
    merge_sort(s1)
    merge_sort(s2)
    merge(s1,s2,s)
    #print(s1,s2,s)
    return s

def main():
    unsorted_numbers = [87,24,63,45,17,31,96,50]
    print( merge_sort(unsorted_numbers) )

if __name__ == '__main__':
    main()
