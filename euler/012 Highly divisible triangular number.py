def triangle_factors(a):
    count = 0
    tri = sum(range(1, a+1))
    for i in range(1, int(tri**.5)):
        if tri%i == 0:
            count += 2
    return tri, count

n = 1
while True:
    tri, count = triangle_factors(n)
    if count > 500:
        print('Triangular number:', tri)
        print('Factors:', count)
        break
    n += 1