#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the roadsAndLibraries function below.
def dfs(nodes, node, visited):
    if visited[node]:
        return 0

    visited[node], count = 1, 1
    for neighbor in nodes[node]:
        count += dfs(nodes, neighbor, visited)

    return count


def roadsAndLibraries(n, c_lib, c_road, cities):
    nodes = {i + 1: [] for i in range(n)}
    visited = [0] * (n + 1)

    for u, v in cities:
        nodes[u].append(v)
        nodes[v].append(u)

    cost = 0
    for node in nodes:
        count = dfs(nodes, node, visited)
        if count:
            cost += c_lib + (count - 1) * min(c_lib, c_road)

    return cost


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    q = int(input())

    for q_itr in range(q):
        nmC_libC_road = input().split()

        n = int(nmC_libC_road[0])
        m = int(nmC_libC_road[1])

        c_lib = int(nmC_libC_road[2])
        c_road = int(nmC_libC_road[3])

        cities = []
        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)
        fptr.write(str(result) + '\n')
    fptr.close()
