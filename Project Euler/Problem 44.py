# P44 - Pentagon Numbers
import math

def is_pentagonal(x):
    val = 24 * x + 1
    sq_root = math.isqrt(val)
    return (sq_root * sq_root == val) and ((sq_root + 1) % 6 == 0)

pentagonals_set = set()
n = 1
found = False

while not found:
    Pk = (n * (3 * n - 1)) // 2
    
    for Pj in pentagonals_set:
        p_diff = Pk - Pj
        p_sum = Pk + Pj
        
        if p_diff in pentagonals_set and is_pentagonal(p_sum):
            print(f"Found Pair: Pj={Pj}, Pk={Pk}")
            print(f"Minimum Difference (D): {p_diff}")
            found = True
            break
            
    pentagonals_set.add(Pk)
    n += 1
