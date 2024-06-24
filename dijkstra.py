from dis import dis
import sys


def dijkstra(adj_matrix, spt_set, dist, src):
    dist[src] = 0
    
    for _ in range(len(spt_set)):
        # find from smallest distance vertex from dist array that spt set is not true (not optimal dist)
        x = dijkstra_shortest_distance_vertex_not_in_spt_set(spt_set, dist)
        
        # set current vertex to visited & already optimal distance
        spt_set[x] = True
        
        # map all adjacent distance from x to dist array, only replace shorter total dist & not optimal distance (spt_set true)
        # -1 is not valid distance
        for i in range(len(spt_set)):
            curr_dist = adj_matrix[x][i]
            
            if spt_set[i] == False and dist[i] > curr_dist + dist[x] and curr_dist > -1:
                dist[i] = curr_dist + dist[x]
    
    return dist

def dijkstra_shortest_distance_vertex_not_in_spt_set(spt_set, dist):
    min = sys.maxsize
    
    for i in range(len(spt_set)):
        curr_dist = dist[i]
        curr_spt = spt_set[i]
        
        if curr_dist < min and curr_spt == False:
            min = curr_dist
            min_index = i
    
    return min_index

if __name__ == '__main__':
    v = int(input())
    e = int(input())

    edges = []

    adj_matrix = [[-1 for _ in range(v)] for _ in range(v)]
    for i in range(e):
        lst = list(map(int, input().rstrip().split()))
        edges.append(lst)
        
        adj_matrix[lst[0]][lst[1]] = lst[2]
        adj_matrix[lst[1]][lst[0]] = lst[2]
    

    shortest_dst = [sys.maxsize for _ in range(v)]
    spt_set = [False] * v
        
    
    dijkstra(adj_matrix, spt_set, shortest_dst, 2)
    print(shortest_dst)
    
    
    

