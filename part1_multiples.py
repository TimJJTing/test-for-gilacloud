# part1_multiples.py
# If we list all the natural numbers below 10 that
#  are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def find_multiples_of_3_or_5(below):
    # ans = []
    
    # multiples of 3
    # n = 0
    # while 3*n < below:
    #    ans.append(3*n)
    #    n += 1
    
    # multiples of 5
    # n = 0
    # while 5*n < below:
    #     # if n is not a multiple of 3, 5*n won't be.
    #     if n%3 != 0:
    #         ans.append(5*n)
    #     n += 1
    # return ans
    mult = [i for i in range(below) if i % 3 == 0 or i % 5 == 0]
    return mult

print(sum(find_multiples_of_3_or_5(1000)))
