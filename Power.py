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
        year = []
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
        print(80 * '-')
        print('this is your pas ---> {}' . format(pas))
        print(80 * '-')
        print("hash's you'r password ----> {}" . format(has))
        print(80 * '-')
	print('')
        print("warning : if you think the target doesnt have a strong password , don't enter (y) . because it will result in a longer password")
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
            print(80 * '-')
            print("this is change you'r password -----> {} " . format(pasnew))
            print(80 * '-')
            pasnew = pasnew+pasa
            pas = pasnew + pas           #add edite you'r password whith orginal password
        elif mypas == 'n' or mypas == 'N':
            pass
        else:
            print('you should only enter N or Y')

        ted = len(pas)
	print('')
        questionyear = raw_input("if you don't know the target date of birth . do you want me to find it for you (Y/N) ? ")
        if questionyear == 'y' or questionyear == 'Y':
            try:
                print("hint : it will calculate in a range between the first year and second year , then it will add the reswt to the password list")
                year1 = int(raw_input('enter first year : '))
                year2 = int(raw_input('enter secound year : '))
            except ValueError:
                print('you should enter year')
                sys.exit()

            year1 -= 1		
            while(year1 < year2):
                year1 += 1
                year.append(year1)
            print(80 * '-')
            print('this is years ----> {}' . format(year))
            print(80 * '-')

            count_year = len(year)

            for pas_year1 in range(0,count_year):
                for pas2_year in range(0,ted):
                    text.write("{}{}\n". format(pas[pas2_year],year[pas_year1]))
                    text.write("{}{}\n". format(year[pas_year1],pas[pas2_year]))
                    
            for pas_year2 in range(0,count_year):
                for pas3_year in range(0,ted):
                    for pas4_year in range(0,ted):
                        text.write("{}{}{}\n" . format(pas[pas3_year] , pas[pas4_year] , year[pas_year2]))
                        text.write("{}{}{}\n" . format(year[pas_year2] , pas[pas4_year] , pas[pas3_year]))
                        text.write("{}{}{}\n" . format(pas[pas3_year] , year[pas_year2] , pas[pas4_year]))

            for pas_year3 in range(0,count_year):
                for pas5_year in range(0,ted):
                    for pas6_year in range(0,ted):
                        for pas7_year in range(0,ted):
                            text.write("{}{}{}{}\n" . format(pas[pas5_year] , pas[pas6_year] , pas[pas7_year] , year[pas_year3]))
                            text.write("{}{}{}{}\n" . format(pas[pas5_year] , pas[pas6_year] , year[pas_year3] , pas[pas7_year]))
                            text.write("{}{}{}{}\n" . format(pas[pas5_year] , year[pas_year3] , pas[pas6_year] , pas[pas7_year]))
                            text.write("{}{}{}{}\n" . format(year[pas_year3] , pas[pas5_year] , pas[pas6_year] , pas[pas7_year]))

        elif question_year == 'n' or question_year == 'N':
                pass
        else:
            print('you should enter Y or N')
            sys.exit()



        
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
try:
    if sys.argv[1] == '-h' or sys.argv[1] == 'H':
        print("""                  -r ----> run script  
                  -v ----> Version of the program""")
        sys.exit()

    elif sys.argv[1] == '-r' or sys.argv[1] == 'R':
        me=password()
        me.pas1()

    elif sys.argv[1] == '-v':
        print('verssion 1.3')
    else:
        print("""              -h ----> Help 
              -r ----> run script
              -v ----> Version of the program  """)
        
except IndexError:
    print("""              -h ----> Help 
              -r ----> run script
              -v ----> Version of the program  """)




