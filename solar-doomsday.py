'''
Find largest square root whole number and subtract its square from total area.
Rinse and repeat until no remaining area available to put squares into.
'''

from math import sqrt as sqrt
from math import floor as floor


def solution(area):
    panels = []
    panel = floor(sqrt(area)) ** 2
    remainder = area - panel
    panels.append(panel)
    while remainder:
        panel = floor(sqrt(remainder)) ** 2
        panels.append(panel)
        remainder = remainder - panel
    return panels
