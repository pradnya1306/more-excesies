# harshad number

def is_harshad_number(num):
    z=num
    i=1
    sum=0
    while i <num:
        s=num%10
        sum=sum+s
        num=num//10
    if z%sum==0:
        return(bool(z%sum==0))
    else:
        return(bool(z%sum==0))


num=int(input("enter the number"))
m=is_harshad_number(num)
print(m)


# def is_harshad_number(num):
# num=int(input("enter the number"))
# j=1
# while j<=1000:
#     z=j
#     i=1
#     sum=0
#     while i <=j:
#         s=j%10
#         sum=sum+s
#         j=j//10
#     if z%sum==0:
#         print(z)
#     else:
#         print(z,"is not harshad number")


# num=int(input("enter the number"))
# m=is_harshad_number(num)
# print(m)