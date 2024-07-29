from itertools import chain, combinations

def add_element(s, element):
    """Add an element to a set. No error if the element is already present."""
    s.add(element)

def remove_element(s, element):
    """Remove an element from a set. No error if the element is not present."""
    s.discard(element)

def union_and_intersection(s1, s2):
    """Return the union and intersection of two sets."""
    union = s1.union(s2)
    intersection = s1.intersection(s2)
    return union, intersection

def difference(s1, s2):
    """Return the difference S1 - S2."""
    return s1.difference(s2)

def is_subset(s1, s2):
    """Check if set S1 is a subset of set S2."""
    return s1.issubset(s2)

def set_length(s):
    """Find the length of a set without using len()."""
    count = 0
    for _ in s:
        count += 1
    return count

def symmetric_difference(s1, s2):
    """Compute the symmetric difference of two sets."""
    return s1.symmetric_difference(s2)

def power_set(s):
    """Compute the power set of a given set."""
    return set(frozenset(subset) for subset in chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))

def unique_subsets(s):
    """Get all unique subsets of a given set."""
    return power_set(s)


