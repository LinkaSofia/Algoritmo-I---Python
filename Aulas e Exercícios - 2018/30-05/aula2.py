def lstr (s):
    r=[]
    str=''
    for i in range (len(s)):
        if s[i]!=' ':
            str+=s[i]

        if s[i]== ' ' or i == len(s)-1:
            r.append(str)
            str=''
    return r

s=input('Digite a frase: ')
r=lstr(s)
print (r)
