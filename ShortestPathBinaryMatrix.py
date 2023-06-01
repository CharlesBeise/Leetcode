import heapq


def shortestPathBinaryMatrix(grid):
    # If the starting square is a 1
    if grid[0][0] == 1:
        return -1

    size = len(grid)

    # Create an adjacency dictionary to list the neighbors for each node where
    # the value is 0
    adjacency_dict = {}
    for i in range(size):
        for j in range(size):
            adjacency_dict[(i, j)] = []
            if i > 0:
                # Up and left
                if j > 0 and grid[i-1][j-1] == 0:
                    adjacency_dict[(i, j)].append((i-1, j-1))
                # Up and right
                if j < size - 1 and grid[i-1][j+1] == 0:
                    adjacency_dict[(i, j)].append((i-1, j+1))
                # Straight up
                if grid[i-1][j] == 0:
                    adjacency_dict[(i, j)].append((i-1, j))
            if i < size - 1:
                # Down and left
                if j > 0 and grid[i+1][j-1] == 0:
                    adjacency_dict[(i, j)].append((i+1, j-1))
                # Down and right
                if j < size - 1 and grid[i+1][j+1] == 0:
                    adjacency_dict[(i, j)].append((i+1, j+1))
                # Straight down
                if grid[i+1][j] == 0:
                    adjacency_dict[(i, j)].append((i+1, j))
            # Straight left
            if j > 0 and grid[i][j-1] == 0:
                adjacency_dict[(i, j)].append((i, j-1))
            # Straight right
            if j < size - 1 and grid[i][j+1] == 0:
                adjacency_dict[(i, j)].append((i, j+1))

    distances = {square: float('inf') for square in adjacency_dict}
    distances[(0,0)] = 1

    # Create a priority queue containing the next nodes to be checked
    pq = [(1, (0,0))]
    while len(pq) > 0 and distances[(size-1, size-1)] == float('inf'):
        cur_dist, cur_square = heapq.heappop(pq)

        # If the current square already has a shorter path than the current
        # distance
        if cur_dist > distances[cur_square]:
            continue

        # Check the neighbors of the current square to see if their paths can
        # be shortened
        for neighbor in adjacency_dict[cur_square]:
            if cur_dist + 1 < distances[neighbor]:
                distances[neighbor] = cur_dist + 1
                heapq.heappush(pq, (cur_dist + 1, neighbor))

    # If there is no path to the end return -1, else return the length of the
    # path
    if distances[(size-1, size-1)] == float('inf'):
        return -1
    else:
        return distances[(size-1, size-1)]


if __name__ == '__main__':
    myGrid = [[1,0,0],[1,1,0],[1,1,0]]
    print(shortestPathBinaryMatrix(myGrid))


"""
Since this solution utilizes a shortest path algorithm, I should use Dijkstra's
Algorithm
"""