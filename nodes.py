#!/usr/bin/env python3

def main():
    response = input("Enter a comma-separated set of skills:\n")
    skills = [x.strip() for x in response.split(',')]

main()