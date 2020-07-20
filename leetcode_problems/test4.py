if __name__ == "__main__":
    l = (1,0,1,0,0)
    z=0
    m =0
    last_index = -1
    while True:
        try:
            last_index = l.index(z, last_index + 1)
            print(last_index)
            if last_index> l.index(1):
                m = m +1
            print("Max = "+str(m))
        except ValueError:
            break


