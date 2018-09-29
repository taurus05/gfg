def prefix_fun(s):
    n = len(s)
    pf = [0]*(n)
    k = 0
    for q in range(2,n):
        while k>0 and s[k+1] != s[q]:
            k = pf[k]
        if s[k+1] == s[q]:
            k += 1
        pf[q] = k
    return pf

def KMP_Matcher(t,s):
    m = len(t)
    n = len(s)
    t = '-' + t
    s = '-' + s
    pf = prefix_fun(s)
    q = 0
    for i in range(1,m+1):
        while q>0 and s[q+1] != t[i]:
            q = pf[q]
        if s[q+1] == t[i]:
            q += 1
        if q == n:
            print("Pattern occours with shift",i-n)
            q = pf[q]

KMP_Matcher('aabaacaadaabaaba','aaba')


    
