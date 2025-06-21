def sum_avg(nums):
    return sum(nums), sum(nums)/len(nums)

# Example
numbers = [9, 11]
s, a = sum_avg(numbers)
print("Sum:", s)
print("Average:", a)