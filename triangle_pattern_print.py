n = 10

#Solution 1
for i in range(1,n,2):
    print("{:^{n}}".format("*"*i,n=n))

#Solution 2
[print("{:^{n}}".format("*"*i,n=n)) for i in range(1,n,2)]