# Largest palindrome product
# Problem 4
#
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

def find_palindrome():

    lst_palindromes = []
    lower_bound = 100
    upper_bound = 1000

    for a in range(lower_bound, upper_bound, 1):
        for b in range(lower_bound, upper_bound, 1):
            item = a * b
            temp = list(str(item))[::-1]
            item_reversed = ""
            for each in temp:
                item_reversed += each
            if item == int(item_reversed):
                lst_palindromes.append(item)

    return lst_palindromes
print("Searching for palindromes...")
lst_final = find_palindrome()
print(max(lst_final))
