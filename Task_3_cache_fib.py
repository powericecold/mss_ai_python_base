def cache_results(func):
    cached_results = {}

    def wrapper(args):
        if args not in cached_results:  # проверка наличия в кэше
            cached_results[args] = func(args)  # добавление элемента в кэш
        return cached_results[args]  # возврат значения из кэша

    return wrapper


@cache_results
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    print(fibonacci(0))  # Результат будет вычислен и сохранен
    print(fibonacci(1))  # Результат будет вычислен и сохранен
    print(fibonacci(5))  # Результат будет вычислен и сохранен
    print(fibonacci(5))  # Результат будет взят из кэша
    print(fibonacci(10))  # Результат будет вычислен и сохранен
