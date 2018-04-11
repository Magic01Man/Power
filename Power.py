import hashlib
import os
import sys
class password:
    
    def pas1(self):
        text = open('password list.text','w')
        pas = []
        has = []
        try:
            tedad = int(raw_input('how many do you have information ? :  '))
        except ValueError:
            print('only you should enter number')
            sys.exit()

        for i in range(0,tedad):
            b=raw_input('enter : ')
            pas.append(b)
            hasmd5 = hashlib.md5(b'%s' % (b)).hexdigest()
            hassha224 = hashlib.sha224(b'%s' % (b)).hexdigest()
            has.append(hassha224)
            has.append(hasmd5)
        
        print('this is your pas ---> {}' . format(pas))
        print('this is your hash of password ----> {}' . format(has))

        mypas = raw_input('I edite your password : ')

        if mypas == 'y' or mypas == 'Y':
            pasja = []
            for pasjadid in pas:
                mym = pasjadid.replace('a','@')
                pasja.append(mym)
                hyh = pasjadid.replace('s' , '$')
                pasja.append(hyh)
                nyu = pasjadid.replace('i' , '!')
                pasja.append(nyu)
            pas = pasja + pas
            print('this is edit you password -----> {} ' . format(pasja))
        elif mypas == 'n' or mypas == 'N':
            pass
        else:
            print('you should only enter N or Y')
            

        ted = len(pas)
        ted2 = len(has)

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
                    text.write("{}#{}*{}\n". format(pas[t],pas[k],pas[h]))

        for u in range(0,ted):
            for y in range(0,ted):
                for o in range(0,ted):
                    for q in range(0,ted):
                        text.write("{}{}{}{}\n". format(pas[u],pas[y],pas[o],pas[q]))
                        text.write("{}{}{}{}@\n". format(pas[u],pas[y],pas[o],pas[q]))
                        text.write("{}${}@{}={}\n". format(pas[u],pas[y],pas[o],pas[q]))

        for l in range(0,ted):
            for p in range(0,ted):
                for t in range(0,ted):
                    for c in range(0,ted):
                        for he in range(0,ted):
                            text.write("{}{}{}{}{}\n". format(pas[l],pas[p],pas[t],pas[c],pas[he]))
                            text.write("{}{}{}{}{}@\n". format(pas[l],pas[p],pas[t],pas[c],pas[he]))
                            text.write("{}@{}#{}-{}*{}\n". format(pas[l],pas[p],pas[t],pas[c],pas[he]))




        text.close()


os.system('cls')

print("""
                    
    
                 010101010101                                                                                                                010101010101                                                          
                 010      010          01010101010                                                                                           010      010        
                 101      101        01010     101010       1010                   0101 1010                   0101       010101010101       101      101          
                 010101010010      01010         101010       0101                1010    0101                1010        10101              010101010101                   
                 101               10101          101010        1010            1010        1010            1010          01010              101 0101                                            
                 010               01010        010101            0101         1010           0101         1010           010101010101       010   0101                                            
                 101                 01010    10101                 1010     0101                1010     0101            10101              101    0101              
                 010                     0101010                       0101010                      0101010               01010              010      0101                
                                                                                                                          010101010101                 
                                                                                                                                   
                              
                                       hgghhhjhjsdjfdjfdjkjkksdkjfdjkfdskjfjkdjkfdjksdjk
                                                  
                
                """)

me=password()
me.pas1()

