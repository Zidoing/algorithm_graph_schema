#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by Z Lei on 2019-02-23.


graph = {
    "start": {
        "a": 6,
        "b": 2
    },
    "b": {
        "fin": 5,
        "a": 3
    },
    "a": {
        "fin": 1
    }
}

infinity = float("inf")

costs = {
    "a": 6,
    "b": 2,
    "fin": infinity
}

parents = {
    "a": "start",
    "b": "start",
    "fin": None
}

visit = []


def find_lowest_cost_node(costs):
    low_cost = infinity
    low_cost_node = None

    for node in costs:
        if node not in visit and costs[node] < low_cost and node != "fin":
            low_cost = costs[node]
            low_cost_node = node

    return low_cost_node


node = find_lowest_cost_node(costs)

while node is not None:
    print(node)
    neighbour = graph[node]
    cost = costs[node]

    for node_child in neighbour.keys():
        new_cost = cost + neighbour[node_child]
        if new_cost < costs[node_child]:
            costs[node_child] = new_cost
            parents[node_child] = node

    visit.append(node)

    node = find_lowest_cost_node(costs)

print(costs)
print(parents)