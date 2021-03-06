#!/usr/bin/env python3

from collections import Counter
from itertools import permutations

def main():
    response = input("Enter a comma-separated set of skills:\n")
    skills = [x.strip() for x in response.split(',')]
    num_skills = len(skills)

    print("Enter each boost node as comma-separated list of an p, primary skill; o's, other skill on node; and n's, skill not on node")
    print("Press ENTER to submit a boost node to your collection")
    print("Enter 'x' to exit")
    nodes = []
    # TODO: consider using a library like https://github.com/CITGuru/PyInquirer for a more intuitive UI
    # TODO: consider making nodes / skills / sets different classes
    while True:
        response = input()
        if response.lower() == 'x':
            break
        node = [y.strip() for y in response.split(',')]
        if len(node) != num_skills:
            print("Error: incorrect number of references to skills")
            continue
        counter = Counter(node)
        if counter['p'] != 1:
            print("Error: node must include one primary skill")
            continue
        if counter['o'] != 2:
            print("Error: node must include two other skills")
            continue
        # TODO: check for any input besides p, o, n
        nodes.append(node)

    # Remove nodes that are just translations of secondary nodes
    nodes = ["".join(x) for x in nodes] # concatenate the chars in a node
    nodes = list(set(nodes))    # remove duplicates; order is not preserved
    nodes = [list(x) for x in nodes]    # break concatenated strings

    '''
    The set of nodes we are looking for is as follows:
        1) The primary skills of all nodes in the set must be unique to be a valid set
        2) To be maxed, a skill must appear on at least 2 boost nodes
        3) To use the minimum number of boost nodes, a skill will apear on exactly 2 nodes
    '''
    # Determine whether or not the user has a suitable set of nodes
    # Trivial brute force all permutations
    # TODO: optimize this terrible algorithm
    sets = []
    for node_set in permutations(nodes):
        # Check validity of set
        invalid = False
        for i, nodei in enumerate(node_set):
            for s, skill in enumerate(nodei):
                if skill == 'p':
                    break
            for nodeii in node_set(node_set[i+1:]):
                if nodeii[s] == 'p':    # two nodes have the same primary skill
                    invalid = True
                    break
            if invalid:
                break

        # Check optimality
        # TODO: see above

        sets.append(node_set)



def test():
    pass


# test()
main()