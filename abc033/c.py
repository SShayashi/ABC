def m():
    s = str(input())
    if len(s) == 1:
        if s == "0":
            return 0
        else:
            return 1

    ans = 0
    nums = s[::2]
    sign = s[1::2]
    zero = 0
    for i in range(len(nums)-1):
        if sign[i] == "*":
            if nums[i] == 0:
                zero = 1
            continue
        if zero:
            zero = 0
            continue
        if sign[i] == "+" and nums[i] != "0":
            ans += 1

    if sign[-1] == "+":
        if nums[-1] == "0":
            return ans
        else:
            return ans +1

    if zero:
        return ans
    else:
        if nums[-1] == "0":
            return ans
        else:
            return ans+1


print(m())