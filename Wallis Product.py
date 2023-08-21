def wallis(n):
    pi = 0.0   
    for i in range(1, n):
        x = 4 * (i ** 2)
        y = x - 1
        z = float(x) / float(y)
        if (i == 1):
            pi = z
        else:
            pi *= z
        print(pi*2)
    pi *= 2
    return pi

wallis(int(input("Please give nth term(try something like 100000): ")))

#n is accuracy to the nth term in the product
# for more details on wallis product and mathematical perspective you can watch this video:
# https://www.youtube.com/watch?v=EZSiQv_G9HM
