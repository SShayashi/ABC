def main():
    N, M = map(int, input().split())
    field = [0 for _ in range(1000000)]
    info = []
    for i in range(M):
        L, R, D = map(int, input().split())
        info.append([L, R, D])

    for i in info:
        L, R, D = i
        if field[L] != 0 and field[L] != L:
            return print('No')
        if field[L + D] != 0 and field[L + D] != R:
            return print('No')
        field[L] = L
        field[L + D] = R

    return print('Yes')


def ans():
    NOT_VISITED = -99999
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    visited = [NOT_VISITED for _ in range(N + 1)]

    def dps(graph, start, visited):
        if visited[start] != NOT_VISITED:
            return False
        stuck = [start]
        visited[start] = 0
        while stuck:
            label = stuck.pop()
            for nextnode, distance in graph[label]:
                if visited[nextnode] == NOT_VISITED:
                    stuck.append(nextnode)
                    visited[nextnode] = visited[label] + distance
                elif visited[nextnode] != visited[label] + distance:
                    return True

    for _ in range(M):
        L, R, D = map(int, input().split())
        graph[L].append((R, D))
        graph[R].append((L, -D))

    for i in range(1, N + 1):
        if dps(graph, i, visited):
            return print('No')
    return print('Yes')
# main()
ans()
