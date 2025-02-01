import heapq


def min_cost_to_connect_cables(cables: list[int]) -> int:
    """Calculate the minimum cost to connect all cables into one.

    :param cables: List of cable lengths
    :return: Total minimum cost to connect all cables
    """
    # Convert the list of cables into a min-heap
    heapq.heapify(cables)
    total_cost = 0

    # While there is more than one cable in the heap
    while len(cables) > 1:
        # Extract the two shortest cables and combine them
        cost = heapq.heappop(cables) + heapq.heappop(cables)
        total_cost += cost
        # Push the new cable back into the heap
        heapq.heappush(cables, cost)

    return total_cost


if __name__ == "__main__":
    cables = [4, 10, 3, 5, 1]
    print("Total cost to connect cables:", min_cost_to_connect_cables(cables))
