#Author ------> Magic Man
#Author's Email -----> magicmangit@gmail.com
import hashlib
import os
import sys

class password:
    
    def pas1(self):

        text = open('password list.text','w')    #for enter password in notpad
        pas = []                           #for input password
        has = []                            # for input hash's password
        try:
            count = int(raw_input('how many do you have information  about target(only enter number) ? '))  # enter how do you have information
        except ValueError:
            print('only you should enter number')   # for Instead eroor
            sys.exit()
            
        ma = 0
        for i in range(0,count):         #  count number information 
            ma += 1
            b=raw_input('enter {} information : ' . format(ma)).replace(' ','')     # input you'r password
            pas.append(b)                # full list pas
            hasmd5 = hashlib.md5(b'%s' % (b)).hexdigest()  # Convert password to hash(md5)
            hassha224 = hashlib.sha224(b'%s' % (b)).hexdigest() # Convert password to hash(sha224)
            has.append(hassha224)                    #full list has
            has.append(hasmd5)
        
        print('this is your pas ---> {}' . format(pas))
        print("hash's you'r password ----> {}" . format(has))

        mypas = raw_input("i change you'r password and add to you'r password (Y/N) ? ")

        if mypas == 'y' or mypas == 'Y':
            pasnew = []
            pasa = []
            for newpas in pas:
                mym = newpas.replace('a','@')  #change a to @
                pasa.append(mym)
                hoo = newpas.replace('s','$') # change s to $
                pasa.append(hoo)
                end = newpas.replace('a','@') 
                end = end.replace('s','$')    # change s to $ and a to @
                end = end.replace('i','!')   # change i to !
                pasnew.append(end)

            print("this is change you'r password -----> {} " . format(pasnew))
            pasnew = pasnew+pasa
            pas = pasnew + pas           #add edite you'r password whith orginal password
        elif mypas == 'n' or mypas == 'N':
            pass
        else:
            print('you should only enter N or Y')
                    

        ted = len(pas)
        ted2 = len(has)
                                                  # make password list
        for d in range(0,ted):
            text.write("{}\n".format(pas[d]))

        for haas in range(0,ted2):
            text.write("{}\n".format(has[haas]))

        for n in range(0,ted):
            for m in range(0,ted):
                text.write("{}{}\n". format(pas[n],pas[m]))
                text.write("{}{}@\n". format(pas[n],pas[m]))
                text.write("{}_{}\n". format(pas[n],pas[m]))

        for t in range(0,ted):
            for k in range(0,ted):
                for h in range(0,ted):
                    text.write("{}{}{}\n". format(pas[t],pas[k],pas[h]))
                    text.write("{}{}{}@\n". format(pas[t],pas[k],pas[h]))

        for u in range(0,ted):
            for y in range(0,ted):
                for o in range(0,ted):
                    for q in range(0,ted):
                        text.write("{}{}{}{}\n". format(pas[u],pas[y],pas[o],pas[q]))
                        text.write("{}{}{}{}@\n". format(pas[u],pas[y],pas[o],pas[q]))

        for l in range(0,ted):
            for p in range(0,ted):
                for t in range(0,ted):
                    for c in range(0,ted):
                        for he in range(0,ted):
                            text.write("{}{}{}{}{}\n". format(pas[l],pas[p],pas[t],pas[c],pas[he]))
                            text.write("{}{}{}{}{}@\n". format(pas[l],pas[p],pas[t],pas[c],pas[he]))




        text.close()


os.system('clear')

print("""
                    
    
                 010101010101                                                                                                                010101010101                                                          
                 010      010          01010101010                                                                        010101010101       010      010        
                 101      101        01010     101010       1010                   0101 1010                   0101       10101              101      101          
                 010101010010      01010         101010       0101                1010    0101                1010        01010              010101010101                   
                 101               10101          101010        1010            1010        1010            1010          010101010101       101 0101                                            
                 010               01010        010101            0101         1010           0101         1010           10101              010   0101                                            
                 101                 01010    10101                 1010     0101                1010     0101            10101              101    0101              
                 010                     0101010                       0101010                      0101010               010101010101       010      0101                
                                                                                                                                           

                                        Author ------> Magic Man
                                        Author's Email -----> magicmangit@gmail.com
                                                  
                
                """)


me=password()
me.pas1()


