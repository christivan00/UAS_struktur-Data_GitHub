def A_star(graph, heuristic, start, goal):
    open_list = [(start, 0)]  # Daftar node yang akan diperiksa
    came_from = {}  # Menyimpan asal node
    g_score = {node: float('inf') for node in graph}  # Jarak aktual terpendek dari start ke node
    g_score[start] = 0
    f_score = {node: float('inf') for node in graph}  # g_score + heuristic
    f_score[start] = heuristic[start] 

    iteration = 0  # Counter untuk iterasi
    while open_list:
        iteration += 1
        print(f"\nIterasi {iteration}")
        print(f"Open list: {[node[0] for node in open_list]}")
        
        # Pilih node dengan f_score terendah
        current, _ = min(open_list, key=lambda x: f_score[x[0]])
        print(f"Memeriksa node: {current}")

        open_list = [item for item in open_list if item[0] != current]  # Hapus node yang sedang diperiksa

        # Jika tujuan ditemukan
        if current == goal:
            print("Tujuan ditemukan!")
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        # Periksa setiap tetangga dari node saat ini
        for neighbor, weight in graph[current]:
            print(f"  Memeriksa tetangga: {neighbor}")
            tentative_g_score = g_score[current] + weight
            if tentative_g_score < g_score[neighbor]:
                # Update jarak dan f_score
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + heuristic[neighbor]
                open_list.append((neighbor, f_score[neighbor]))
                came_from[neighbor] = current
                print(f"  Update {neighbor}: g={g_score[neighbor]}, f={f_score[neighbor]}")

    return None  # Jika tidak ada jalur

grafik = {
    'UNP_2': [('A', 0.4)],
    'A': [('UNP_2', 0.4), ('B', 3.5), ('E', 18.1)],
    'B': [('A', 3.5), ('C', 25.8), ('D', 36.9)],
    'C': [('B', 25.8), ('D', 19.2), ('F', 15.3)],
    'D': [('B', 36.9), ('E', 7.5), ('L', 20.2)],
    'E': [('A', 18.1), ('D', 7.5), ('F', 14.5), ('H', 7.8)],
    'F': [('E', 14.5), ('C', 15.3), ('G', 10.8), ('J', 9.6)],
    'G': [('C', 19.2), ('F', 10.8), ('I', 10.0)],
    'H': [('E', 7.8), ('J', 13.6), ('M', 11.5)],
    'I': [('G', 13.0), ('J', 17.2), ('N', 10.4)],
    'J': [('F', 9.6), ('I', 17.2), ('M', 13.6), ('K', 9.1)],
    'K': [('J', 9.1), ('M', 14.0), ('O', 8.5)],
    'L': [('M', 2.9), ('D', 20.2), ('O', 14.6)],
    'M': [('L', 2.9), ('K', 14.0), ('H', 11.5)],
    'N': [('I', 10.4), ('UNP_1', 3.1), ('O', 23.3)],
    'O': [('N', 23.3), ('K', 8.5), ('L', 14.6)],
    'UNP_1': [('N', 3.1)]
}

heuristic = {
    'UNP_2': 0,   
    'A': 3,       
    'B': 4,
    'C': 6,
    'D': 5,
    'E': 4,
    'F': 7,
    'G': 8,
    'H': 6,
    'I': 7,
    'J': 9,
    'K': 10,
    'L': 8,
    'M': 6,
    'N': 3,
    'O': 4,
    'UNP_1': 0  
}

start = 'UNP_2'
goal = 'UNP_1'
path = A_star(grafik, heuristic, start, goal)

if path:
    print("\nJalur ditemukan:", path)
else:
    print("\nTidak ada jalur.")
