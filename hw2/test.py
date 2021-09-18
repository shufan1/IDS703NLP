from LevenshteinDistance import find_min_cost,make_distance_matrix,find_min_distance

assert make_distance_matrix("intention","execution",1,1,2)[3,2] == 5
assert find_min_distance("intention","execution",1,1,2)==8