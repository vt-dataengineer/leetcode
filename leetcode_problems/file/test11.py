if __name__ == '__main__':
    def isPerfectSquare(num):
        for i in range(1,num):
            if num/i == i:
                return True
        else:
             return False



print(isPerfectSquare(122))
