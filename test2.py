import sys

def shortest_distance(N, n_portals, p1, p2, res):

    for i in range(N):
        curr_portal = n_portals[i]
        p1_dist = abs(curr_portal - p1)
        p2_dist = abs(curr_portal - p2)
        shortest_start = min(p1_dist, p2_dist)
        adjacent_dist_list = [sys.maxsize] * N
        
        for j in range(N):
            if i == j:
                continue

            adjacent_portal = n_portals[j]
            adjacent_dist = abs(adjacent_portal - curr_portal)
            adjacent_dist_list[j] = adjacent_dist
        
        adj_shortest = min(adjacent_dist_list)
        shortest = min(shortest_start, adj_shortest)
        
        if shortest == shortest_start:
            res[i] = shortest
        else:
            for j in range(len(adjacent_dist_list)):
                new_n_portals = n_portals.copy()
                adjacent_dist_list[j] = max(adjacent_dist_list[j], shortest_distance(N, n_portals.copy(), p1, p2, res)[j])
            
            minnest = min(adjacent_dist_list)
            res[i] = minnest          
        
    return res
        
if __name__ == '__main__':
    T_data = []
    T = int(input())
    
    # input
    for _ in range(T):
        N, p1, p2 = input().strip().split(" ")
        N = int(N)
        p1 = int(p1)
        p2 = int(p2)

        n_portals_str = input().strip().split(" ")
        n_portals = [int(num) for num in n_portals_str]
        
        lib = {
            "N": N,
            "p1": p1,
            "p2": p2,
            "n_portals": n_portals
        }
        T_data.append(lib)


    for i in range(T):
        dat = T_data[i]

        N = dat['N']
        n_portals = dat['n_portals']
        p1 = dat['p1']
        p2 = dat['p2']
        res = [sys.maxsize] * N
        res = shortest_distance(N, n_portals, p1, p2, res)
        print(' '.join(str(x) for x in res))
