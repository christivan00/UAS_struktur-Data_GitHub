def A_star(graph, heuristic, start, goal):                  # fungsi
    open_list = [(start, 0)]                                # daftar node yang akan di periksa
    came_from = {}                                          # dictionari
    g_score = {node: float('inf') for node in graph}        # menyimpan jarak akatual terpendek  dari n strar ke n lainya
    g_score[start] = 0
    f_score = {node: float('inf') for node in graph}        # menyimpan nilai total 
    f_score[start] = heuristic[start] 

    while open_list:                                        # akan berjalann jika masih ada node
        
        current, _ = min(open_list, key=lambda x: f_score[x[0]])        # memilih node dengan nilai f_scorce terendah      
        open_list = [item for item in open_list if item[0] != current]  # menghapus node yang sudah di periksa

        if current == goal:                                 # memeriksa apakah node yang sedang di periksa adalah 
            
            path = []                                       # menginisialisasi list kosong untuk menyimpan jalur
            while current in came_from:                     # untuk menelusuri kembali jalur dari goal ke start
                path.append(current)                        # menambahkan node saat ini ke jalur
                current = came_from[current]                # mengupdate current ke node asal
            path.append(start)                              # menambahkan node start ke jalur
            return path[::-1]                               # mengembalikan jalur yang dibalik agar memulai dari start ke goal

        for neighbor, weight in graph[current]:             # iterasi memulai semua tetangga dari node current.
            # setiap tetangga memiliki:
            tentative_g_score = g_score[current] + weight   # bobot tepi dari current ke neighbor.
            if tentative_g_score < g_score[neighbor]:       # nama node tetangga
                g_score[neighbor] = tentative_g_score       # memperbarui skor g untuk tetangga
                f_score[neighbor] = tentative_g_score + heuristic[neighbor] # memperbarui skor f untuk tetangga
                open_list.append((neighbor, f_score[neighbor])) # menambahkan tetangga ke open_list untuk selanjutnya
                came_from[neighbor] = current               # menyimpan node asal dari tetangga

    return None                                             # mengembalkan nilai

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
    print("Jalur ditemukan:", path)
else:
    print("Tidak ada jalur.")
