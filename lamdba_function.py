#lambda_function
#varialble_name=lambda arguments:expression
add=lambda a,b:a+b
print(add(10,20))
sub=lambda a,b:a-b
print(sub(10,20))
mul=lambda a,b:a*b
print(mul(10,20))
div=lambda a,b:a/b
print(div(10,20))
sqt=lambda num:num*num
print(sqt(4))
bigger=lambda x,y: x if x>y else y
print(bigger(5,6))
reverse=lambda st:st[::-1]
print(reverse("hello"))
even=lambda num: "even" if num%2==0 else "odd" 
print(even(2))
lst1=[1,2,3,4,5,6,7]
even=list(filter(lambda a:a%2==0,lst1))
print(even)
lst2=[1,2,3,4,5]
multiply=list(map(lambda a:a*5,lst2))
print(multiply)
from functools import*
lst3=[1,2,3,4,5,6]
product=reduce(lambda a,b:a*b,lst3)
print(product)


