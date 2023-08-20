
while True:
    try:
        print ('===============Welcome To The Calculator Program===============')
        print ('===============Enter The Starting Number To Start==============')
        print ('Enter 0 Exit ')
        start = int(input('Enter Start :'))
        if start == 0:
            break
        end = int(input ('Enter End : '))

        for i in range(start,end+1):
            for x in range(1,13):
                print(i,' x ',x,' = ',i*x)
            print ('='*15)
    except :
        print ('error')