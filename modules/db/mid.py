def generateUserID(counter=0, cuntil=20):
        abc="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        numb=str(1234567891011121314151617181920212223242526)
        numbl=[]
        abcl=[]
        for a in abc: abcl.append(a)
        for n in numb: numbl.append(n)
        l =[]
        while counter < cuntil:
                shuffle(numbl)
                shuffle(abcl)
                l.append(abcl[counter])
                l.append(numbl[counter])
                shuffle(l)
                counter+=1
                #print counter
                if counter == 10: return  ''.join(l) + '==msgid'
