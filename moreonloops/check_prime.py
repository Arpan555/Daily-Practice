def checkprime(num):
    count=0
    for i in range(2,num):
        if num%i == 0:
            count+=1
            break
    if count:
        print('not prime')
    else:
        print('prime')
checkprime(29)