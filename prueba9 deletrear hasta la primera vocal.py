def deletrear():

    i = 0

    s = input ('texto para deletrear' + '\n' + '\n')

   

    while i < len(s) and not(s[i] in 'aeiouAEIOU'):
        print (s[i])
        i = i+1
        
def deletrear_string():

    i = 0

    s = input ('texto para deletrear' + '\n' + '\n')

    sbs =''

    while i < len(s) and not(s[i] in 'aeiouAEIOU'):
        sbs = sbs + (s[i])
        i = i+1

    return sbs


