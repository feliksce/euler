# Multiples of 3 and 5
# Problem 1
#
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.

# create temporary variable for summing all numbers fulfilling conditions
temp_sum = 0

print("List of all numbers in test condition:")
for each in range(1, 10):
    # condition
    if each % 3 == 0 or each % 5 == 0:
        print(each)
        temp_sum += each

print("Sum of all: {}".format(temp_sum))
temp = sum([item for item in range(1, 1000) if item % 3 == 0 or item % 5 == 0])
print("Sum for all multiples below 1000: {}".format(temp))
