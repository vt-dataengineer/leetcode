if __name__=='__main__':

    def water(v):
        if v.__contains__('on') or v.__contains__('up'):
            return 1
        else:
            return 0

    objects = ['fan','light','door','water','volume']
    val = ['on','off','up','down']
    cmd = 'sakjdha'
    z = ''
    for x in cmd.split():
        #print(x)
        if x in objects:
            z = z + x +' '
        elif x in val:
            z = z + x
    final = z
    for y in final:
        if y not in cmd:
            print("Invalid Command")
        else:
            cm = final.split()
            print('Command is: '+final)
            print(str(z)+' '+str(water(cm)))



