import requests, random, string, os, socket, sys, urllib
from secrets import randbelow

domains = ['@accountant.com', '@engineer.com', '@columnist.com', '@musician.org', '@bartender.net', '@yandex.com', '@yandex.ru', '@pornhub.com', '@winxclub.com', '@gmail.com', '@aol.com', '@outlook.com', '@hotmail.com', '@zohomail.com', '@mail.com', '@yahoo.com', '@protonmail.com','@protonmail.ch','@pm.me','@icloud.com','@gmx.com']
UserAgents = [
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
]

def ImportProxy(): # Imports proxy from website
    tp = 0
    f = open("proxies.txt", "a+")
    r = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=1500&ssl=yes')
    r = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=1500&ssl=no')
    proxies = []
    for proxy in r.text.split('\n'):
        proxy = proxy.strip()
        if proxy != None:
            proxies.append(proxy)
    for p in proxies:
        tp = tp + 1 
        f.write((p)+"\n")
    f.close()
    print("[#] Total Proxies: "+str(tp)+"")

def ProxyConfiguration():
    p = open(f"proxies.txt", encoding="UTF-8")
    rproxy = p.read().split('\n')
    for i in rproxy:
        if i == "" or i == " ":
            index = rproxy.index(i)
            del rproxy[index]
    try:
        if not rproxy[0]:
            print("[#] All proxies are invalid, Please check proxies.txt.")
            return
    except:
        print("[#] All proxies are invalid, Please check proxies.txt.")
        return
    randomproxy = random.choice(rproxy)
    try:
        r1 = requests.get("http://google.com", proxies = {"http" : randomproxy})
        protocol = "http"
    except:
        protocol = "https"
    proxy = {
    str(protocol): randomproxy
    }
    return proxy

def ProxyConnection(rproxy, proxy, protocol):
    try:
        r1 = requests.get("http://google.com", proxies = {protocol : randomproxy})
    except:
        randomproxy = random.choice(rproxy)
        try:
            r1 = requests.get("http://google.com", proxies = {"http" : randomproxy})
            protocol = "http"
        except:
            protocol = "https"
        ProxyConnection(rproxy, randomproxy, protocol)

def HeaderConfiguration(url):
    headers = {
        "User-Agent": random.choice(UserAgents),
        "Referer": str(url),
        "Accept-Language":"en",
        "Connection":"keep-alive",
        "Accept-Encoding":"gzip, deflate, br"
    }
    return headers

def EmailGenerator():
    length = randbelow(27)
    if length < 5: length = 5
    username = ''.join(random.sample((string.ascii_uppercase+string.ascii_lowercase+string.digits), length))
    domain = random.choice(domains)
    return username + domain

def PasswordGenerator():
    length = randbelow(27)
    if length < 7: length = 7
    return ''.join(random.sample((string.ascii_uppercase+string.ascii_lowercase+string.punctuation+string.digits), length))

def PhoneGenerator():
    phone = str(random.randint(1,10**9-1))
    if random.getrandbits(1): #payphone:
        phone = "089"+phone[2:]
    return phone

def ProtocolFixer(url):
    if url[0:7] == "http://": return 1 # The HTTP Protocol is right
    elif url[0:8] == "https://":
        url = url.replace("https://", "http://")
        return 2 # Replaced HTTPS with HTTP

def Main():
    os.system("cls")
    os.system('color 1a')
    print('[=======================================================================]')
    print('[                           Phishing Flooder                            ]')
    print('[                                                                       ]')
    print('[                                                                       ]')
    print('[                                                                       ]')
    print('[                                    By Paranormal Activity, Mirco Soft ]')
    print('[=======================================================================]')
    #ImportProxy()
    link = str(input("[#] URL: "))
    if ProtocolFixer(link) == 1 or ProtocolFixer(link) == 2:
        try:
            requests.get(link, proxies = ProxyConfiguration(), headers = HeaderConfiguration(link))
            #requests.get(link, headers = HeaderConfiguration(link))
        except:
            print("[#] The url or proxy is invalid.")
            exit()
    else:
        print("[#] The url's protocol must be http:// or https://.")
        exit()
    amount = int(input("[#] Threats: "))
    configure = str(input("[#] Do you want configure the data (Y / N): "))
    if configure == "Y":
        email = str(input("[#] Email: "))
        password = str(input("[#] Password: "))
    else:
        email = "email"
        password == "pass"
    
    for i in range(1, amount + 1):
        email1 = EmailGenerator()
        password1 = PasswordGenerator()
        data = {email: email1, password: password1}
        r1 = requests.post(link, data=data, headers = HeaderConfiguration(link))
        if r1.status_code == 200:
            print("[#] Email: "+email+" --> "+password+"")

Main()