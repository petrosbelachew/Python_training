age=int(input('Eneter your age: '))
student= input('Are you student?(y or n): ')

full_fare=3.50
your_fare=None

if age<=12:
    print('you are free')

elif 13<=age<=17 and student=='y' :
    print(f'Your fare is {0.5*full_fare}')

else
    print(f'Your fare is ${full_fare}')