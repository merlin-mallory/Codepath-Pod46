def create_matrix
len_related = len(related)
    this_row = []
    for i in range(len_related):
        this_row = [] * len_related
    matrix = [this_row * len_related]
    print(matrix)