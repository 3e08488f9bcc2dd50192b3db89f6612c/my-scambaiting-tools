import os
import random
import string
import json
import requests

os.system("cls")
os.system('color 1a')
print('[===========================================================================================]')
print('[                                   Discord Invite Generator                                ]')
print('[                                                                                           ]')
print('[                                                                                           ]')
print('[                                                                                           ]')
print('[                                                                     By Paranormal Activity]')
print('[===========================================================================================]')
os.system('color 0')
try:
    amount = int(input('\33[1m'+'\33[37m'+"["+'\33[33m'+"+"+'\33[37m'+"] How much invites will be generated?: "))
except ValueError:
    print('\33[1m'+'\33[37m'+"["+'\33[33m'+"-"+'\33[37m'+"] The amount need be integer, not string.")
    exit()
    
try:
    timeout = int(input('\33[1m'+'\33[37m'+"["+'\33[33m'+"+"+'\33[37m'+"] Timeout?: "))
except ValueError:
    print('\33[1m'+'\33[37m'+"["+'\33[33m'+"-"+'\33[37m'+"] The timeout need be integer, not string.")
    exit()
    
auto = input('\33[1m'+'\33[37m'+"["+'\33[33m'+"+"+'\33[37m'+"] Automaticaly scrape the proxies. (If no, every check will be on random proxy). [YES/NO]: ")
mult = input('\33[1m'+'\33[37m'+"["+'\33[33m'+"+"+'\33[37m'+"] Multiple checks for proxy [YES/NO]: ")

def scrape():
    scraped = 0
    f = open("proxies.txt", "a+")
    f.truncate(0)
    r = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=1500&ssl=yes')
    r = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=1500&ssl=no')
    proxies = []
    for proxy in r.text.split('\n'):
        proxy = proxy.strip()
        if proxy:
            proxies.append(proxy)
    for p in proxies:
        scraped = scraped + 1 
        f.write((p)+"\n")
    f.close()
    print('\33[1m'+'\33[37m'+"["+'\33[33m'+"+"+'\33[37m'+"] Total Scraped Proxies: "+"\33[35m"+str(scraped)+"\33[37m.")


if auto == "YES":
    scrape()

if auto == "NO":
    pass

print('\33[1m'+'\33[37m'+"["+'\33[33m'+"+"+'\33[37m'+"] Total Generated Invites: "+"\33[35m"+str(amount)+"\33[37m")

fulla = amount


p = open(f"proxies.txt", encoding="UTF-8")


rproxy = p.read().split('\n')
for i in rproxy:
    if i == "" or i == " ":
        index = rproxy.index(i)
        del rproxy[index]


while amount > 0:
    f = open(f"invites.txt","a", encoding="UTF-8")
    try:
        if not rproxy[0]:
            print('\33[1m'+'\33[37m'+"["+'\33[33m'+"-"+'\33[37m'+"] All proxies are invalid, Please check proxies.txt.")
            exit()
    except:
        print('\33[1m'+'\33[37m'+"["+'\33[33m'+"-"+'\33[37m'+"] All proxies are invalid, Please check proxies.txt.")
        exit()
    if mult == "yes":
        proxy = rproxy[0]
    else:
        proxy = random.choice(rproxy)
    proxies = {
        "https": proxy
    }
    amount = amount - 1
    code = ''.join([random.choice(string.ascii_letters + string.digits) for i in range(6)])
    try:
        url = requests.get(f"https://canary.discord.com/api/v6/invite/{code}?with_counts=true", proxies=proxies, timeout=timeout)
        if url.status_code == 200:
            jurl = url.json()
            ginfo = jurl["guild"]
            gname = ginfo["name"] # guild name
            members = jurl["approximate_member_count"]
            owner = ginfo["username"]
            print('\33[1m'+'\33[37m'+"["+'\33[33m'+"+"+'\33[37m'+"] New Invite (Work): Code: "+str(code)+" | Name: "+str(gname)+" | Total Members: "+str(members)+" | Invite Owner: "+str(owner))
            f.write(f"\ndiscord.gg/{code}     |     {members}     |     {gname}")
            f.close()
        elif url.status_code == 404:
            fulla = fulla - 1
            print('\33[1m'+'\33[37m'+"["+'\33[33m'+"-"+'\33[37m'+"] Invalid Invite: "+"\33[35m"+str(code)+"\33[37m")
        elif url.status_code == 403:
            fulla = fulla - 1
            print('\33[1m'+'\33[37m'+"["+'\33[33m'+"-"+'\33[37m'+"] Forbidden Invite: "+"\33[35m"+str(code)+"\33[37m")
        elif url.status_code == 429:
            fulla = fulla - 1
            if mult == "yes":
                    print('\33[1m'+'\33[37m'+"["+'\33[33m'+"-"+'\33[37m'+"] The Proxy "+"\33[31m"+str(proxy)+""+"\33[37m is ratelimited! | Switching proxy")
            else:
                print('\33[1m'+'\33[37m'+"["+'\33[33m'+"-"+'\33[37m'+"] The Proxy "+"\33[31m"+str(proxy)+""+"\33[37m is ratelimited!")
            index = rproxy.index(proxy)
            del rproxy[index]
        else:
            fulla = fulla - 1
            print('\33[1m'+'\33[37m'+"["+'\33[33m'+"-"+'\33[37m'+"] HTTP Error! | Status code "+"'\33[31m'"+str(url.status_code)+"\33[37m")
    except:
        index = rproxy.index(proxy)
        del rproxy[index]
        pw = open(f"proxies.txt","w", encoding="UTF-8")
        for i in rproxy:
            pw.write(i + "\n")
        pw.close()
        fulla = fulla - 1
        print('\33[1m'+'\33[37m'+"["+'\33[33m'+"-"+'\33[37m'+"] Failed connecting to proxy "+"\33[31m"+str(proxy)+""+"\33[37m | Removed from list!")
        pass