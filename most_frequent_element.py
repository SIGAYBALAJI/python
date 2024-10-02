from collections import Counter
li=[1,2,2,3,3,3,4]
frequency=Counter(li).most_common(1)[0][0]
print(frequency)
