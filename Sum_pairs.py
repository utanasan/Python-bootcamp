"""Write a function called sum_pairs which accepts a list and a number and
returns the first pair of numbers that sum to the number passed to the function."""

def sum_pairs(accepted_list,num):
    for i in range(len(accepted_list)):
        if accepted_list[i]+accepted_list[i+1]==num:
            return accepted_list[i], accepted_list[i+1]


print(sum_pairs([1,2,3,5,10,15],8))

