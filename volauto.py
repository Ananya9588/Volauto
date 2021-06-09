import os
import argparse
import time
from pyfiglet import Figlet
from termcolor import colored
import string
import random




parser = argparse.ArgumentParser()
parser.add_argument('-f','--filename', type=str,help="Give us the file to evaluate")
args = parser.parse_args()

#os.system('cd volatility/')
def vols(filename):
    
    banner()
    fi = filename.split('/')
    print(filename)
    l = fi[-1].split('.')
    
    p = "grep -v 'Failed' "
    q = "awk '/Profile/{print $4}' "
    os.system('mkdir output)
    if os.path.exists('output/{}'.format(l[0])) == True:
        #print("File Does not exists")
        letters = string.ascii_lowercase
        s = ''.join(random.choice(letters) for i in range(5))
        l[0] = s
        #print(l[0])
        print(colored(("Your Output will be saved in output/{}".format(l[0])),"yellow"))
        os.makedirs('output/{}'.format(l[0]))
        
    
    else:
        print(colored("Your output will be saved in: output/{}".format(l[0]),"yellow"))
        os.system('mkdir output/{}'.format(l[0]))    
    
    
    
    os.system('mkdir output/{}/dumpfiles/'.format(l[0]))
    os.system('mkdir output/{}/dumpfiles/processdump'.format(l[0]))
    
    print(colored("......................................ImageInfo Scan is started......................",'magenta'))
    os.system('python2 volatility/vol.py -f ' + filename + ' imageinfo'+' > '+'output/{}'.format(l[0]) + "/imageinfo_output.txt")
    os.system('grep -v "Failed" '+'output/{}'.format(l[0]) + "/imageinfo_output.txt")
    pro = os.popen(p+'output/{}'.format(l[0]) + "/imageinfo_output.txt | "+q+'output/{}'.format(l[0]) + "/imageinfo_output.txt" + " | cut -d ',' -f1").read()
    profile = pro.rstrip("\n")
    #print(type(profile))
    cmd = 'python2 volatility/vol.py -f ' + filename + ' --profile={}'.format(profile) 
    #print(cmd)
    #s = os.system(q+'output/{}'.format(l[0]) + "/imageinfo_output.txt")
    print(colored("\n ----------------------------------------DONE--------------------------------------",'red'))
    print("\n")
    
    print(colored("......................................Process list scan is started......................",'green'))
    phuss = cmd + ' pslist'+' > '+'output/{}'.format(l[0]) + "/process_list_output.txt" + " | uniq -u " + 'output/{}'.format(l[0]) + "/process_list_output.txt"
    os.system(phuss)
    #print(phuss)
    os.system(p+'output/{}'.format(l[0]) + "/process_list_output.txt")
    print(colored("\n --------------------------------------DONE---------------------------------",'red'))
    
    print(colored(".........................................Command Line scan is started......................",'yellow'))
    cmdline = " | awk '/Command/' "
    os.system(cmd + ' cmdline'+' > '+'output/{}'.format(l[0]) + "/cmdline_output.txt" )
    os.system(p+'output/{}'.format(l[0]) + "/cmdline_output.txt" + cmdline + 'output/{}'.format(l[0]) + "/cmdline_output.txt")
    print(colored("\n ----------------------------------------------DONE-------------------------------------------",'red'))
    print("\n")
    
    print(colored("...................................Process Tree scan is started......................",'cyan'))
    os.system(cmd + ' pstree'+' > '+'output/{}'.format(l[0]) + "/Process_Tree_output.txt" )
    os.system(p+'output/{}'.format(l[0]) + "/Process_Tree_output.txt")
    print(colored("\n ------------------------------------------DONE----------------------------",'red'))
    print("\n")
    
    print(colored("........................................Console scan is started......................",'magenta'))
    os.system(cmd + ' consoles'+' > '+'output/{}'.format(l[0]) + "/consoles_output.txt" )
    os.system(p+'output/{}'.format(l[0]) + "/consoles_output.txt")
    print(colored("\n ----------------------------------------DONE--------------------------------------",'red'))
    print("\n")
    
    print(colored("........................................Environment Variable scan is started......................",'yellow'))
    os.system(cmd + ' envars'+' > '+'output/{}'.format(l[0]) + "/envars_output.txt" )
    os.system(p+'output/{}'.format(l[0]) + "/envars_output.txt")
    print(colored("\n ----------------------------------------DONE----------------------------------------",'red'))
    print("\n")
    
    print(colored(".........................Hash Dump scan is started......................",'cyan'))
    os.system(cmd + ' hashdump'+' > '+'output/{}'.format(l[0]) + "/hashdump_output.txt" )
    os.system(p+'output/{}'.format(l[0]) + "/hashdump_output.txt")
    print(colored("\n ----------------------------------------DONE-----------------------------------------",'red'))
    print("\n")
    
    print(colored("..........................MFT Parser is started......................",'blue'))
    os.system(cmd + ' mftparser'+ ' > '+'output/{}'.format(l[0]) + "/mftparser_output.txt" )
    #os.system(p+'output/{}'.format(l[0]) + "/mftparser_output.txt")
    print(colored("You can see this in the output folder",'yellow'))
    print(colored("\n -----------------------------------------DONE-----------------------------------------",'red'))
    print("\n")
    
    print(colored("---------------------------------------------File scan is running..........................",'cyan'))
    os.system(cmd + ' filescan'+ ' > ' + 'output/{}'.format(l[0]) + "/filescan_output.txt")
    #os.system(p+'output/{}'.format(l[0]) + "/filescan_output.txt")
    print(colored("File Scan is Completed Shortning the results for you",'blue'))
    print(colored('\n ------------------------------------Done------------------------------------------------','red'))
    print("\n")
    
    print(colored("---------------------------------------------Desktop Files scan is running..........................",'cyan'))
    time.sleep(5)
    Desk = "grep -v 'Failed' "
    Desk_awk = "awk '/Desktop/{print $1,$5,$6}' "
    os.system(Desk+'output/{}'.format(l[0]) + "/filescan_output.txt"+ "|" + Desk_awk + 'output/{}'.format(l[0]) + "/filescan_output.txt")
    print(colored('\n ------------------------------------Done------------------------------------------------','red'))
    print("\n") 
    
    print(colored("---------------------------------------------Downloads File scan is running..........................",'cyan'))
    time.sleep(5)
    Down = "grep -v 'Failed' "
    Down_awk = "awk '/Download/{print $1,$5,$6}' "
    os.system(Down+'output/{}'.format(l[0]) + "/filescan_output.txt"+ "|" + Down_awk + 'output/{}'.format(l[0]) + "/filescan_output.txt")
    print(colored('\n ------------------------------------Done------------------------------------------------','red'))
    print("\n")
    
    print(colored("---------------------------------------------Users File scan is running..........................",'cyan'))
    time.sleep(5)   
    User = "grep -v 'Failed' "
    User_awk = "awk '/Users/{print $1,$5,$6}' "
    os.system(User+'output/{}'.format(l[0]) + "/filescan_output.txt" + "|" + User_awk + 'output/{}'.format(l[0]) + "/filescan_output.txt")
    print(colored('\n ------------------------------------Done------------------------------------------------','red'))
    print("\n")
    
    print(colored("---------------------------------------------IEHistory scan is running..........................",'magenta'))
    os.system(cmd + ' iehistory'+ ' > ' + 'output/{}'.format(l[0]) + "/iehistory_output.txt")
    os.system(p+'output/{}'.format(l[0]) + "/iehistory_output.txt")
    print(colored('\n ------------------------------------Done------------------------------------------------','red'))
    print("\n")
    
    print(colored(".........................Clipboard scan is started......................",'cyan'))
    os.system(cmd + ' clipboard'+' > '+'output/{}'.format(l[0]) + "/clipboard_output.txt" )
    os.system(p+'output/{}'.format(l[0]) + "/clipboard_output.txt")
    print(colored("\n ----------------------------------------DONE-----------------------------------------",'red'))
    print("\n")
    
    print(colored(".........................Notepad scan is started......................",'cyan'))
    os.system(cmd + ' notepad'+' > '+'output/{}'.format(l[0]) + "/notepad_output.txt" )
    os.system(p+'output/{}'.format(l[0]) + "/notepad_output.txt")
    print(colored("\n ----------------------------------------DONE-----------------------------------------",'red'))
    print("\n")
    
#------------------------------------------Plugins----------------------------------------------------------------------------------------------    
    initial = "python2 volatility/vol.py --plugins=volatility/volatility-plugins/ -f " + filename + " --profile={} ".format(profile)  
    chrome_sed = "grep -v 'Failed' "
    
    print(colored("---------------------------------------------ChromeHistory Scan is running..........................",'yellow'))
    thuss = initial + ' chromehistory'+ ' > ' + 'output/{}'.format(l[0]) + "/chromehistory_output.txt"
    os.system(thuss) 
    os.system(chrome_sed+'output/{}'.format(l[0]) + "/chromehistory_output.txt")
    print(colored('\n ------------------------------------Done------------------------------------------------','red'))
    print("\n")
    
    
    print(colored("---------------------------------------------Firefoxhistory Scan is running..........................",'yellow'))
    phurr = initial + ' firefoxhistory'+ ' > ' + 'output/{}'.format(l[0]) + "/firefoxhistory_output.txt"
    os.system(phurr) 
    os.system(chrome_sed+'output/{}'.format(l[0]) + "/firefoxhistory_output.txt")
    print(colored('\n ------------------------------------Done------------------------------------------------','red'))
    print("\n")
    
    #--------------_-----------------------------------------------Dumping files---------------------------

    print(colored("---------------File Dump is started-----------------------------------","magenta"))
    li= []
    i = []
    inp = [".txt",".png",".jpg",".pdf",".zip",".rar"]
    with open ("output/{}/filescan_output.txt".format(l[0]), 'r') as f :
	    for line in f :
		    for a in inp :
			    if ( a in line):
				    li = str(line)
				    offset  = li.split(" ")
				    i = i + [(offset[0])]

    
    for off in i:
        dump = cmd + " dumpfiles -Q " + off + " -D output/{}/dumpfiles/".format(l[0])
        bump = os.popen(dump).read()   
        print(colored("Dumping files for you of extentions txt,jpg,png,pdf,zip,rar with offsets as: {} ".format(off),"yellow" ))
    print(colored('\n ------------------------------------Done------------------------------------------------','red'))
    print("\n")

#--------------------------------------------------------------Process files Dump-----------------------------------------
    
    print(colored("------------Process File Dumping Started-------------------------","magenta"))
    process_awk = "awk '/.exe/{print$3}' "
    pro_awk = process_awk + "output/{}/process_list_output.txt".format(l[0]) + " > " + "output/{}/awkprocess.txt".format(l[0])
    os.system(pro_awk)
    
    with open ("output/{}/awkprocess.txt".format(l[0]), 'r') as f :
        for line in f :
            q=[x.strip() for x in f.readlines()]
        for dup in q:
            qw = cmd + " procdump -D " + "output/{}/dumpfiles/processdump ".format(l[0]) + "-p " + str(dup)
            sw = os.popen(qw).read()
            print(colored("Process File dumped with PID as: {}".format(dup),"blue"))
        print(colored('\n ------------------------------------Done------------------------------------------------','red'))
    os.system("rm " + "output/{}/awkprocess.txt".format(l[0]))    
            

def banner():
    banner1 = Figlet(font='slant')
    print(colored(banner1.renderText("   VOLAUTO"),"green"))
    banner2 = Figlet(font='digital')
    print(colored(banner2.renderText("      Let's Automate Volatility"),"yellow"))


if __name__=='__main__':
    vols(args.filename)
