from collections import deque, defaultdict

class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        queue = deque() # node, depth, path weight
        flight_dict = defaultdict(list)
        cost = [float('inf')] * n

        # check each flight to see if source is correct
        for s, d, num in flights:
            flight_dict[s].append((d, num))
            if s == src:
                queue.append((d, 0, num))

        # bfs from src to dst with k at most iterations
        def bfs(node):
            nonlocal cheapest
            while queue:
                next_node, depth, w = queue.popleft()
                cost[next_node] = min(cost[next_node], w)

                # if node = dst, update cheapest price
                if depth >= k + 1:
                    break
                elif next_node == dst:
                    cheapest = min(cheapest, w)
                
                for d, num in flight_dict[next_node]:
                    if w + num < cost[d]:
                        queue.append((d, depth + 1, w + num))

        cheapest = float('inf')
        bfs(src)
        return cheapest if cheapest != float('inf') else -1