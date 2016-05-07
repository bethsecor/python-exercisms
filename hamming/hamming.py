def distance(sequence_1, sequence_2):
    return sum(map(lambda x: x[0] != x[1], zip(sequence_1, sequence_2)))
