def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:
        value = func(int_list)
        results[func.__name__] = value
    return results


lst = [6, 20, 15, 9]

print(apply_all_func(lst, max, min), end=' ')
print(apply_all_func(lst, len, sum, sorted))
