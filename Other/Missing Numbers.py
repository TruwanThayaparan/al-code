# Find the Missing Numbers
'''
You have a bag containing tiles with numbers [1, 2, 3, …, n] 
written on them. Each number appears exactly once, so there are n tiles and n numbers. 
Now, without looking, k number tiles are randomly picked out of the bag and discarded. 
Create a missing_nos() function that takes in a list and k, and returns the missing 
numbers in ascending order (from smallest to greatest).

For example, missing_nos([1, 2, 4, 5, 6, 7, 8, 10], 2) should return [3, 9].
'''

def missing_nos(bag, k):
    q = 0
    expected = 1
    mod = []
    
    while len(mod) < k:
        if q >= len(bag):
            mod.append(expected)
        elif expected != bag[q]:
            mod.append(expected)
        else:
            q += 1
            
        expected += 1
            
    return mod

bag = [10, 8, 7, 6, 5, 4, 2, 1]
k = 2
print(missing_nos(sorted(bag), k))

#################################################################################
def missing_nos(bag, k):
    bag_set = set(bag)
    mod = []
    expected = 1
    
    while len(mod) < k:
        if expected not in bag_set:
            mod.append(expected)
        expected += 1
            
    return mod

bag = [10, 8, 7, 6, 5, 4, 2, 1]
k = 2
print(missing_nos(bag, k))
