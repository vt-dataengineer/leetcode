if __name__=='__main__':
    import itertools
    d ={'1':['a','b','c'], '2':['c','d','e']}
    for x in itertools.product(*[d[k] for k in sorted(d.keys())]):
        print(''.join(x))
