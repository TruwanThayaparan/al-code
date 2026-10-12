max_product = 0
largest_pair = (0, 0)

for i in range(100, 1000):
    for j in range(i, 1000):
        product = i * j
        
        if str(product) == str(product)[::-1]:
            if product > max_product:
                max_product = product
                largest_pair = (i, j)

print(f"Largest pair: {largest_pair} with a product of {max_product}")
