import heapq


def merge_k_lists(lists: list[list[int]]) -> list[int]:
    """Merge k sorted lists into one sorted list.

    :param lists: List of sorted lists
    :return: Merged sorted list
    """
    return list(heapq.merge(*lists))


if __name__ == "__main__":
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    merged_list = merge_k_lists(lists)
    assert merged_list == [1, 1, 2, 3, 4, 4, 5, 6]
    print("Відсортований список:", merged_list)
