import random
import matplotlib.pyplot as plt


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

def bubble_sort(values):
    values = values[:]
    p = len(values)

    plt.ion()
    plt.show()

    for i in range(p):
        swapped = False

        for j in range(0, p - i -1):

            index_highlight1 = j
            index_highlight2 = j + 1
            colors = ["steelblue"] * len(values)
            colors[index_highlight1] = "tomato"
            colors[index_highlight2] = "tomato"
            plt.clf()
            plt.bar(range(len(values)), values, color=colors)
            plt.title("Bubble Sort")
            plt.pause(0.1)

            if values[j] > values[j + 1]:
                values[j], values[j + 1] = values[j + 1], values[j]
                swapped = True

                if not swapped:
                    break
    plt.ioff()
    plt.show()

    return values



def main():
    values = random_numbers(100)
    values1 = random_numbers(10)
    sorted_by_piece = selection_sort(values)
    print(sorted_by_piece)

    bubbles = bubble_sort(values1)
    print(bubbles)


if __name__ == "__main__":
    main()


