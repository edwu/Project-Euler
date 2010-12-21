#problem 24
import itertools
lexicographic = list(itertools.permutations([0,1,2,3,4,5,6,7,8,9]))
lexicographic.sort()
print lexicographic[999999]
