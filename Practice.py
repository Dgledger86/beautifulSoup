data = '2 3 7 0'
count = 1  # int(input())


def round(x):
    y = 0
    if x < 0:
        y = int(x - 0.5)
    else:
        y = int(x + 0.5)
    print(y)


def avg_sum(nums):
    total = 0
    range = len(nums)
    for num in nums:
        num = int(num)
        total += num
        if num == 0:
            range -= 1
    total = total/range
    round(total)



for _ in range(0, count):
    nums = data.split()  # input().split()
    amount = len(nums)
    avg_sum(nums)



