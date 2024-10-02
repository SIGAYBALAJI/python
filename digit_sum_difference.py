def digit_sum_differernce(m,n):
    digit_sum_of_4=0
    digit_sum_of_7=0
    for i in range(m,n+1):
        if i%4==0:
            num=i
            while num>0:
                digit_sum_of_4+=num%10
                num//=10
        elif i%7==0:
           num=i
           while num>0:
               digit_sum_of_7+=num%10
               num//=10
        return abs(digit_sum_of_4 - digit_sum_of_7)
m,n=50,120
result=digit_sum_differernce(m,n)
print(result)
               
    
