ip_address="192.168.001.001"
var=ip_address.split('.')
var1=[str(int(i))for i in var]
res='.'.join(var1)
print(res)
