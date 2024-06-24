# bfs
from collections import deque
from dis import dis
import queue
import sys

def print_subsequence(input, output):
    if len(input) == 0:
        print(output, end=' ')
        return
        
    print_subsequence(input[1:], output + input[0])
    print_subsequence(input[1:], output)
        

def lcs(str1, str2, m, n, dp):
    if m == 0 or n == 0:
        return 0
    
    if dp[m - 1][n - 1] != -1:
        return dp[m - 1][n - 1]
    
    if str1[m - 1] == str2[n - 1]:
        dp[m - 1][n - 1] = 1 + lcs(str1, str2, m - 1, n - 1, dp)
        return dp[m - 1][n - 1]
    else:
        dp[m - 1][n - 1] = max(lcs(str1, str2, m - 1, n, dp), lcs(str1, str2, m, n - 1, dp))
        return dp[m - 1][n - 1]

def bfs(adjList, start_node, visited):
    queue = []
    
    visited[start_node] = True
    queue.append(start_node)
    
    while queue:
        curr_node = queue.pop(0)
        print(curr_node)
        
        for adj in adjList[curr_node]:
            if not visited[adj]:
                visited[adj] = True
                queue.append(adj)

def dfs(adjList, start_node, visited):
    stack_array = []
    
    visited[start_node] = True
    stack_array.append(start_node)
    
    while stack_array:
        curr_node = stack_array.pop()
        print(curr_node)
        
        for adj in adjList[curr_node]:
            if not visited[adj]:
                visited[adj] = True
                stack_array.append(adj)

def dijkstra_aux_min_distance(shortest_portals, spt_set):
    min = sys.maxsize
    
    for u in range(len((spt_set))):
        if shortest_portals[u] < min and spt_set[u] == False:
            min = shortest_portals[u]
            min_index = u
    
    return min_index

def dijkstra(dist_data, shortest_portals, spt_set):
    
    for c in range(len(spt_set)):
        x = dijkstra_aux_min_distance(shortest_portals, spt_set)
        
        spt_set[x] = True
        
        for y in range(len(spt_set)):
            if dist_data[x][y] > -1 and spt_set[y] == False and shortest_portals[y] > dist_data[x][y]:
                shortest_portals[y] = max(shortest_portals[x], dist_data[x][y])

def addEdge(adjList, u, v):
    adjList[u].append(v)

if __name__ == '__main__':
    # v = 5
    
    # adjList = [[] for _ in range(v)]
    # addEdge(adjList, 0, 1)
    # addEdge(adjList, 0, 2)
    # addEdge(adjList, 1, 3)
    # addEdge(adjList, 1, 4)
    # addEdge(adjList, 2, 4)
    
    # visited = [False] * v
    # print("BFS TRAVERSAL: ")
    # bfs(adjList, 0, visited)
    
    # visited = [False] * v
    # print("DFS TRAVERSAL: ")
    # dfs(adjList, 0, visited)

    # a = 'AGGTAB'
    # b = 'GXTXAYB'
    # dp = [[-1 for _ in range(len(b))] for _ in range(len(a))]
    # print(lcs(a, b, len(a), len(b), dp))
    
    n = 12
    p1 = 5
    p2 = 15
    n_portals = [16, 18, 4, 9, 5, 10, 6, 13, 1, 0, 19, 1]
    
    # set distance data p1
    n_portals.insert(0, p1)
    len_p1 = len(n_portals)
    distance_data_p1 = [[0 for _ in range(len_p1)] for _ in range(len_p1)]
    shortest_portals_p1 = [sys.maxsize for _ in range(len_p1)]
    spanning_tree_set_p1 = [False] * len_p1
    
    shortest_portals_p1[0] = 0
    
    for i in range(len_p1):
        for j in range(i, len_p1):
            if i == j:
                distance_data_p1[i][j] = -1
                continue
                
            dist = abs(n_portals[i] - n_portals[j])
            distance_data_p1[i][j] = dist
            distance_data_p1[j][i] = dist
    
    dijkstra(distance_data_p1, shortest_portals_p1, spanning_tree_set_p1)
    n_portals.pop(0)
    
    # set distance data p1
    n_portals.insert(0, p2)
    len_p2 = len(n_portals)
    distance_data_p2 = [[0 for _ in range(len_p2)] for _ in range(len_p2)]
    shortest_portals_p2 = [sys.maxsize for _ in range(len_p2)]
    spanning_tree_set_p2 = [False] * len_p2
    
    shortest_portals_p2[0] = 0
    
    for i in range(len_p2):
        for j in range(i, len_p2):
            if i == j:
                distance_data_p1[i][j] = -1
                continue

            dist = abs(n_portals[i] - n_portals[j])
            distance_data_p2[i][j] = dist
            distance_data_p2[j][i] = dist
    
    dijkstra(distance_data_p2, shortest_portals_p2, spanning_tree_set_p2)
    n_portals.pop(0)

    #
    for i in range(n):
        if shortest_portals_p1[i + 1] > shortest_portals_p2[i + 1]:
            print(shortest_portals_p2[i + 1], end=" ")
        else:
            print(shortest_portals_p1[i + 1], end=" ")