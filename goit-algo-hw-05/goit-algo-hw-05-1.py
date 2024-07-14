def caching_fibonacci():
    cache = {}

    def fibonacci(n):
        if n in cache:
            return cache[n]
        if n <= 1:
            return n
        result = fibonacci(n - 1) + fibonacci(n - 2)
        cache[n] = result
        return result

    return fibonacci

fibonacci = caching_fibonacci()
print(fibonacci(10))