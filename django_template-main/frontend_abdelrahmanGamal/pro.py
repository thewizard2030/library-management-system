n = 5
def subnum(n):
    nums = []
    nums.append(n)
    while n > 0:
        n -= 1
        if n == 0:
            continue
        else:
            nums.append(str(n))
    for n in nums[::-1]:
        

        print(n, end='')


subnum(n)