# Input: [1,1,1,3,3,4,3,2,4,2]
# Output: true
if __name__=='__main__':
    l =[1,2,3,4,1]
    if len(set(l))==len(l):
        print('False')
    else:
         print('True')
