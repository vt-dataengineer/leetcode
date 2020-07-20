# Input: dict = ["cat", "bat", "rat"]
# sentence = "the cattle was rattled by the battery"
# Output: "the cat was rat by the bat"
if __name__=='__main__':
    dict = ["cat", "bat", "rat"]
    sentence = "the cattle was rattled by the battery"

    s = sentence.split(' ')
    #print(s)
    fin = ''

    #print(dict)
    for x in s:
        for y in dict:
            if x.__contains__(y):
               # print(y)
               # print(x)
                sentence = sentence.replace(x,y)

    print(sentence)
