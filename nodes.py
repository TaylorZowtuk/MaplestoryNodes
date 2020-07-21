#!/usr/bin/env python3

from collections import Counter

def main():
    response = input("Enter a comma-separated set of skills:\n")
    skills = [x.strip() for x in response.split(',')]
    num_skills = len(skills)

    print("Enter each boost node as comma-separated list of an p, primary skill; o's, other skill on node; and n's, skill not on node")
    print("Press ENTER to submit a boost node to your collection")
    print("Enter 'x' to exit")
    nodes = []
    # Consider using a library like https://github.com/CITGuru/PyInquirer for a more intuitive UI
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
        nodes.append(node)

    # Determine whether or not the user has a suitable set of nodes




main()