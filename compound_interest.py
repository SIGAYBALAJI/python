def compound(p,r,t):
    a=p*(pow((1+r/100),t))
    ci=a-p
    print(ci)
compound(10000, 10.25, 5)
