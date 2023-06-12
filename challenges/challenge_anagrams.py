def merge_sort(strings):
    if len(strings) <= 1:
        return strings
    mid = len(strings) // 2
    left = strings[:mid]
    right = strings[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    strings_sorted = ""
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            strings_sorted += right[right_index]
            right_index += 1
        else:
            strings_sorted += left[left_index]
            left_index += 1

    while left_index < len(left):
        strings_sorted += left[left_index]
        left_index += 1

    while right_index < len(right):
        strings_sorted += right[right_index]
        right_index += 1

    return strings_sorted


def is_anagram(first_string, second_string):
    if (
        (first_string == "" and second_string == "")
        or type(first_string) != str
        or type(second_string) != str
    ):
        return (first_string, second_string, False)
    first_sorted = merge_sort(first_string.lower())
    second_sorted = merge_sort(second_string.lower())
    return (
        first_sorted, second_sorted,
        first_sorted.lower() == second_sorted.lower()
    )
