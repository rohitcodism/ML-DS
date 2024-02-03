def wordValidator(line):

    words = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'
    nums = [1,2,3,4,5,6,7,8,9]

    charFlag = 0
    intFlag = 0

    for char in line:
        if char in words:
            charFlag+=1
        elif int(char) in nums:
            intFlag+=1

    if charFlag == 0 or intFlag == 0:
        return False
    else:
        return True

print(wordValidator("dkgd5lksjs3lk"))