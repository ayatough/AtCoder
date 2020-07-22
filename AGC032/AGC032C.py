# input
n, m = (int(i) for i in input().split())
edges = set()
for i in range(m):
    edges.add(tuple(int(i) for i in input().split()))





# def contain(path: list, vtx: tuple):
#     ''' whether path contain vtx
#     '''
#     for edge in path:
#         if vtx in edge:
#             return True
#     return False


# def extract_closed_path(edges: list):
#     path = []
#     vtx_history = []
#     # start
#     cur_vtx = edges[0][0]

#     while True:
#         vtx_history.append(cur_vtx)
#         con_edge, cur_vtx = get_connected_edge_vtx(edges, cur_vtx)
#         if con_edge is None:
#             # no connected edge has been found
#             break
#         path.append(con_edge)
#         edges.remove(con_edge)
#         if cur_vtx in vtx_history:
#             # closed path found, but it may be imperfect (like 9 or 6, not 0)
#             return path
#     # in this code, no closed path has been found
#     return None


# def find_junction(closed_path: list):
#     ''' find junction or loop start point from closed path
#     '''
#     cand = closed_path[-1]
#     return cand[0] if cand[0] not in closed_path[-2] else cand[1]


# def extract_loop(closed_path: list):
#     junction = find_junction(closed_path)
#     circuit = set()
#     count = 0
#     for edge in reversed(closed_path):
#         if junction in edge:
#             count += 1
#             if count > 2:
#                 break
#         circuit.add(edge)
#     return circuit


# def get_connected_edge_vtx(edges, vertex):
#     for edge in edges:
#         if vertex in edge:
#             counter = edge[0] if edge[0] != vertex else edge[1]
#             return edge, counter
#     return None, None

# # circuit = []

# def extract_circuit(edges):

#     unexplors = list(edges - walks)
#     closed_path = extract_closed_path(unexplors)
#     if closed_path is None:
#         return None, None
#     circuit = extract_loop(closed_path)
#     return circuit, edges - circuit

# circuits = []

# for i in range(3):
#     try:
#         circuit, edges = extract_circuit(edges)
#         circuits.append(circuit)
#     except:
#         break

# print('Yes' if len(circuits) == 3 else 'No')
