def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        pr = True
        for i in range(2, result):
            if result % i == 0:
                pr = False
                break
            else:
                pr = True
        res = 'Простое' if pr else 'Составное'
        print(res)
        return result

    return wrapper


@is_prime
def sum_three(a, b, c):
    return sum([a, b, c])


print(sum_three(2, 3, 6))
