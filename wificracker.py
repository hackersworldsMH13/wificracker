#!/usr/bin/python
# -*- coding: utf8 -*-
'''imports'''
'''imports'''
import os
import sys
from pathlib import Path
import time

class bcolor:
    GREEN = '\033[92m'
    YELLOW= '\033[93m'
    RED= '\033[91m'
    
def banner():
    print(bcolor.GREEN + '''
    ⠀
    ⠀⠀⠀⠀⠀      
                                   :^!?YPGGBBBBBBBBBBBBBBGG5Y?!^:                                   
                             .^7YPGGP5Y?!~^::....  ....::^~!?Y5GGGPY7^.                             
                         .!YGBG5?~:.                            .:~?5GBPJ~.                         
                      ^JGBGJ~:                                        :!JGBG?^                      
                   ^JBB5!.                                                :!5BBJ^                   
                .7G#5~.                                                      .!P#G7.                
              :Y#B7.                                                            .?B#J:              
            :5&G~                       .......      .......                       !G&Y:            
          .J&G~         ::         ...                        ...         ::         ~G&J.          
         !##!       ^7PG?:     ..                                  ..     :?G57^       7##~         
       .5@Y.   .:.7B@@P:    ..                                        ..    ^P@@G7 :.   .5@Y        
      ^#&~   ~PJ~G@@#!    .                  WIFI-CRACKER                .    7#@@P^Y5~   !&B:      
     !@B:  .P@5.B@BJ77  .                  -----------------               .  7!J#@G.P@5   :#&~     
    !@P  :.P@@:JP77PB: .                  AUTHO : MH-13-CYBER                  ^BP77G?^@@5.: .G@~    
   ~@G  JJ~@@5.?5#@P:                    ---------------------                ^G@#57 P@@^Y? .B@^   
  :&#. Y@!!@#?B@#5^ .                                                           .~5#@B?#@~7@J :&#.  
  G@^ ~@@7^@#&P!7! .                                                            . !7!P&#@:?@@^ ~@P  
 7@J  Y@@Y:&Y~7BB:.                                                              .^#G7!5&:P@@J  5@! 
 B&.  5@@G:7J&@#:.                                                                .^#@#J7:B@@J  :@G 
!@Y :~!@@P~#@@5. .                                                                 .:P@@#^G@@~~. 5@~
5@~ YY P@P#@B~!.. ...  ... ..  ..   .:   .::    ::.  :.  .:...::.  ..:::. ..::.    .:!~B@BP@5 5? !@Y
#&. B&..&#@? ?B .                                                                  ..#7 J@&#.:&G :@B
@B  G@P !@!.P@Y .	░▒█▀▄▀█░▒█░▒█░▄█░░█▀▀█░▒█▀▀▄░▒█░░▒█░▒█▀▀▄░▒█▀▀▀░▒█▀▀▄      . 5@5 7@~ G@P .#&
@B  J@@P.7:#@@^ . 	░▒█▒█▒█░▒█▀▀█░░█▒░░▒▀▄░▒█░░░░▒▀▄▄▄▀░▒█▀▀▄░▒█▀▀▀░▒█▄▄▀      . ^@@B:7.G@@7 .#@
@B  :&@@5 G@@J 		░▒█░░▒█░▒█░▒█░▄█▄░█▄▄█░▒█▄▄▀░░░▒█░░░▒█▄▄█░▒█▄▄▄░▒█░▒█      . 5@@P P@@#. .#&  
#&. ^~&@@7&@G ?...                                                                 ..?.B@#7@@&^^ :@B
5@~ G^:G@G#@^.&? . ...  ... ..  ..   .:   .::    ::.  :.  .:...::.  ..:::. ..::.  . Y& !@#B@P.~P !@Y
!@Y 5@? 7#@B ?@B ..                                                               ..#@! #@B! ?@Y P@~
 B&.:#@B!:YP B@@^ .                                                              . ~@@P GJ:7#@B.:@G 
 !@Y :G@@B7^.&@@~^^                                                              ~^!@@#.^?#@@G: 5@~ 
  P@~  ?&@@G^5@@7.#?.                                                          .JB.?@@Y~B@@#7  !@5  
  :&#. ~~J#@@5#@5 5@Y.                                                        .P@Y P@B5@@B?~^ :&#.  
   ~@G :G?:~YB#@@:!@@5 .                                                     .P@@^^@@#BJ^:?P..B&^   
    !@G :B&5~:^?G5.#@@J :                                                  : Y@@B.5P7^:!5&G..B@~    
     ~&B: ?#@@GY77:~&@@!7P!.                                            .!P!7@@#^:77YB@@#7 :#&^     
      ^B&!  !P&@@@#5JG@#:?@G?P?:                                    .!Y?B@7^&@G?5#@@@&P!  !@B:      
       .5@Y.  ~?YG#@@##@&~7@@@@&GJ~.                            .^?P#@@@@!~&@##@@#GY7^  .5@Y        
         !##!  7J7~~~!7?Y5~^5#@@@@@&B5?~^.                .:~7YG#@@@@@#Y^!5Y?7!~~~7J7  7&B~         
          .J&G~ :JG##BGGPPG5Y5G#&@@@@@@@@&BGP5YJJ???JY5PGB#&@@@@@@@&BG5YPGPPGGB##GJ: !B&?           
            :Y&G~  :!YPB#&&&&#BG5J7!Y@@@@@@@@@@@@@@@@@@@@@@@@@@J!7J5GB&&&&&#BPY!:  !B&J.            
              :J#B?.  ^7!~~^^^^^!?P#@@@@@@@@@@@@@@@@@@@@@@@@@@@@#P?!^^^^^~~!7^  .?B#J.              
                .7G#P!.:75B#&&@@@@@&&@@@@@@@@@@@@@@@@@@@@@@@@@@&@@@@@@&&#G57..!P#G!                 
                   ^JB#5!..:^!777!^.P@@@@@@@@@@@@@@@@@@@@@@@@@@5.~!77!!^. :!P#G?:                   
                      ^?PBGJ~.      B@@@@@@@@@@@@@@@@@@@@@@@@@@G      :!YGBP?:                      
                         .~JPBG5J!::&@@@@@@@@@@@@@@@@@@@@@@@@@@#:^!JPGBPJ~.                         
                             .^7JPGB&@@@@@@@@@@@@@@@@@@@@@@@@@@&GGPJ!^.                             
                                   .^~7JYPGB##&&@@@@&&##BGPYJ7~:.                                                       
    ''')
banner()
print()
def bar():
    total = 1007  # total number to reach
    bar_length = 70  # should be less than 100
    for i in range(total+1):
        percent = 100.0*i/total
        sys.stdout.write('\r')
        sys.stdout.write("Completed: [{:{}}] {:>3}%"
                        .format('~'*int(percent/(100.0/bar_length)),
                                bar_length, int(percent)))
        sys.stdout.flush()
        time.sleep(0.002)

class tool():
    def __init__(self) :
        try:
            bar()
            print()
            print()
            self.set_tool=int(input(bcolor.RED +'''\nSelect The tool :-
1.AIRCRAK 
2.Fluixe
3.Airgeddon \n'''))
            if int(self.set_tool) >int(3) or int(self.set_tool) < int(1):
                print(bcolor.YELLOW,'ERROR : invalid option Goodbye !!!')
                sys.exit(1)
        except Exception as e:
            print(f'ERROR:{e}')
    # def check(self):
    #     self.checker="AIRCRAK"
        
    #     if  self.set_tool == int(1):

        
    def instll(self):
        try:
            if self.set_tool==int(1):
                print(bcolor.RED,banner())
                bar()
                print()
                os.system('git clone https://github.com/aircrack-ng/aircrack-ng && cd aircrack-ng')
#                 os.system('cd aircrack-ng/')
                os.system('autoreconf -i')
                os.system('./configure --with-experimental')
                os.system('make')
                os.system('make install')
                os.system('ldconfig')
                os.system('aircrack-ng -h')
            elif self.set_tool==int(2):
                print(bcolor.RED,banner())
                bar()
                os.system('git clone https://www.github.com/FluxionNetwork/fluxion.git && cd fluxion/ && sudo ./fluxion.sh')
#                 os.system('apt install dhcpd lighttpd php-cgi && isc-dhcp-server')
#                 os.system('cd fluxion/ && sudo ./fluxion.sh')
                
                
            elif self.set_tool==int(3):
                  print(bcolor.RED,banner())
                  bar()
                  print()
                  os.system('git clone --depth 1 https://github.com/v1s1t0r1sh3r3/airgeddon.git && cd airgeddon && bash airgeddon.sh')
                 
               
                
        except Exception as e:
            print(f'The {e}') 
        finally:
            if self.set_tool==int(1):
                os.system('aircrack-ng')
            elif self.set_tool==int(2):
                 os.system('cd fluxion/ && sudo ./fluxion.sh')
                 os.system('1')
            elif self.set_tool==int(3):
                 os.system('cd airgeddon && bash airgeddon.sh')
            else:
                print('Allah HafIz')
                sys.exit('1')
                  

    # def check(self):
    #     try:
    #         os.path
 


           

        
obj=tool()
obj.instll()
#  os.system("pwd")
