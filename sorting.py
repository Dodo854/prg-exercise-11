import random

def random_numbers(count, low=0, high=100):
    return [random.randint(low, high) for _ in range(count)]


def selection_sort(values):
    p = 0
    while p < len(values):
        min_index = p
        min_values = values[min_index]
        for i in range(p, len(values)):
            if values[i] < min_values:
                min_index = i
                min_values = values[i]
        values[p], values[min_index] = values[min_index], values[p]
        p += 1
    return values


def main():
    values = random_numbers(10)  # 10 čísel v rozsahu 0–100
    sorted = selection_sort(values)
    print(sorted)
    small = random_numbers(5, low=0, high=20)  # 5 čísel v rozsahu 0–20

if __name__ == "__main__":
    main()


