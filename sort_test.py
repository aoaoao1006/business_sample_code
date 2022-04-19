

def sort_priority(vaules, group):
    xx = True
    def helper(x):
        if x in group:
            xx = False
            return (0, x)
        return (1, x)
    print(xx)
    vaules.sort(key=helper)


numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {2, 3, 5, 7}
sort_priority(numbers, group)
print(numbers)