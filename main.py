def sort_list(numbers):
    return sorted(numbers)


def find_max(numbers):
    if not numbers:
        return None
    return max(numbers)


if __name__ == "__main__":
    numbers = [5, 2, 8, 1, 3]

    print("Отсортированный список:", sort_list(numbers))
    print("Максимальный элемент:", find_max(numbers))