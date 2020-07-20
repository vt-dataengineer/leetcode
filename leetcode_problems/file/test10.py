if __name__ == '__main__':

# Input: [1,2,3]
# Output: [1,2,4]
    #l = [4,3,2,1]
    def plusone(digits):

        if digits[0]==0 and len(digits)==1:
            digits = digits[0]+1
            return digits
        elif digits[0]==0 and len(digits)>1:
            print('Not a number')
        else:
            digits[-1]=digits[-1]+1
            return digits


plusone([1,2,3])
