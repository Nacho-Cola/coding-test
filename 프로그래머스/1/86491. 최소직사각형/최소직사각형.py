import numpy as np
def solution(sizes):
    sizes = np.array(list(map(sorted,sizes))).T.tolist()
    return max(sizes[0]) *  max(sizes[1])