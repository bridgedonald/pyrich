# crafty usage collections:

# swap
a, b = b, a    
# concise assignment using tuple
a, b, c = 1, "222", [3,33,333]  

addr = 'monty@python.org'
uname, domain = addr.split('@')

s = 'abc'
t = [0, 1, 2]
for pair in zip(s, t):
    print(pair)
ll = list(zip(s,t))

for index, element in enumerate('abc'):
    print(index, element)
