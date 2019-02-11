from heapq import heappush, heappop


class Solution:
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        path = {'0000': None}
        heap = [(0, '0000')]
        visited = set(deadends) | {'0000'}
        while len(heap) > 0:
            turns, state = heappop(heap)
            if state == target:
                return turns, self.construct_path(path, state)
            if state in deadends:
                continue
            for i in range(len(state)):
                right_turn = str((int(state[i]) + 1) % 10)
                left_turn = str((int(state[i]) - 1) % 10)
                successors = [state[:i] + right_turn + state[i+1:], state[:i] + left_turn + state[i+1:]]
                for successor in successors:
                    if successor not in visited:
                        heappush(heap, (turns+1, successor))
                        visited.add(successor)
                        path[successor] = state
        return -1

    def construct_path(self, path, state):
        res = []
        while state:
            res.insert(0, state)
            state = path[state]
        return res


s = Solution()
deadends, target = ['0000'], '8888'
print (s.openLock(deadends, target))