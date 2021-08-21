'''
Lefties and righties 'position' lists created from enumerated 'hallway' string.
Salutes solution solved by summing 2 salutes for each leftie with a high position than a rightie.
'''

def solution(hallway):
    lefties = [i for i, c in enumerate(hallway) if c=="<"]
    righties = [i for i, c in enumerate(hallway) if c==">"]
    salutes = sum([2 for l in lefties for r in righties if l > r])
    return salutes
