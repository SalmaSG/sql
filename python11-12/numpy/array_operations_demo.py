"""Array operations demo:
- join
- split
- search
- sort
- filter
"""


def demo_join_split():
    print("=== JOIN and SPLIT ===")
    items = ["apple", "banana", "cherry", "date"]
    joined = ", ".join(items)
    print(f"Joined string: {joined}")
    split_back = joined.split(", ")
    print(f"Split back into list: {split_back}")
    print()


def demo_search():
    print("=== SEARCH ===")
    numbers = [10, 25, 30, 45, 50]
    target = 30
    found = target in numbers
    print(f"Numbers: {numbers}")
    print(f"Is {target} in the list? {found}")
    if found:
        index = numbers.index(target)
        print(f"Found at index: {index}")

    text = "hello world"
    search_char = "o"
    print(f"Text: '{text}'")
    print(f"First occurrence of '{search_char}': {text.find(search_char)}")
    print(f"Count of '{search_char}': {text.count(search_char)}")
    print()


def demo_sort():
    print("=== SORT ===")
    values = [42, 7, 19, 3, 100, 54]
    print(f"Original: {values}")
    sorted_values = sorted(values)
    print(f"Sorted ascending: {sorted_values}")
    sorted_descending = sorted(values, reverse=True)
    print(f"Sorted descending: {sorted_descending}")
    values.sort()
    print(f"In-place sort: {values}")
    print()


def demo_filter():
    print("=== FILTER ===")
    values = [12, 5, 8, 33, 21, 14, 7]
    even_values = [n for n in values if n % 2 == 0]
    greater_than_twenty = [n for n in values if n > 20]
    print(f"Original: {values}")
    print(f"Even values: {even_values}")
    print(f"Values > 20: {greater_than_twenty}")
    print()


def main():
    demo_join_split()
    demo_search()
    demo_sort()
    demo_filter()


if __name__ == "__main__":
    main()
