r = lambda x, func : x + func(x)
res = r(2, lambda x : x*x)
print(res)