'''
    This file is part of DeviantArtWatcher.

    DeviantArtWatcher is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    DeviantArtWatcher is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with  WhatsApp Dragon.  If not, see <http://www.gnu.org/licenses/>.
    
    @author DangerBlack
    @version 0.1
    
    
    BUGFIX 
    In order to make this work you need to install RoboBrowser and edit
    # geany /usr/local/lib/python2.7/dist-packages/robobrowser/helpers.py
    and adding at line 111
    
    mdelay=3
    multiplier=2

'''
import re
import time
from robobrowser import RoboBrowser
from requests import session as req_session
import json
import os
import requests

OUTPUT_FILE='results.html'
USERNAME='USERNAME'
PSWD='pswd'
HOSTING='http://www.miosito.com/folder/devwatch.php'
PERSONAL_KEY='some random character'


def sendContent(browser,code,body):
    payload = {'code': code, 'body': body}
    r = requests.post(HOSTING, data=payload) 
    #browser.open('http://www.danielebaschieri.eu/devwatch/devwatch.php?code='+code+"&body="+body)
    if r.text=="done":
        print('Posted online')
    if r.text=="403":
        print('Unautorised 403')
    


USERAGENTS ='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:37.0) Gecko/20100101 Firefox/37.0'
session = req_session()
session.headers.update({'Referer': 'https://www.deviantart.com'})

browser = RoboBrowser(history=False, session=session, tries=2, user_agent=USERAGENTS)

print("Attempting to log in to deviantArt...")

browser.open('https://www.deviantart.com/users/login?ref=https%3A%2F%2Fwww.deviantart.com%2F&remember_me=1')
form = browser.get_forms()[1]
form['username'] = USERNAME
form['password'] = PSWD
#print(form)
if browser.find(text=re.compile("Login")):
    print('Compiled login fields form...')

browser.submit_form(form)

if browser.find(text=re.compile("The password you entered was incorrect")):
        print("Wrong password or username. Attempting to download anyway.")
        exit();
elif browser.find(text=re.compile("\"loggedIn\":true")):
        print("Logged in!")
else:
        print("Login unsuccessful. Attempting to download anyway.")
        exit();
browser.open('https://www.deviantart.com/messages/#view=deviantwatch')
page=browser.select('body')

script=browser.select('script')
for s in script:
    st=s.text
    json_start= st.find('{"api":"scmc","preload":')
    if json_start!=-1:
        json_end= st.find('}}}}) }',json_start)
        print('Analising the json')
        #print(str(json_start)+" "+str(json_end))
        js=st[json_start:json_end+4]
        out_file = open("source.txt","w")
        out_file.write(js)
        out_file.close()
        #REPLACE ALL THE SINGLE QUOTE
        #REPLACE ALL THE \ WITH \\
        #js=json.dumps(js)
        in_file = open("source.txt","r")
        js=in_file.read()
        in_file.close();        
        d=json.loads(js)
        devianWatch=d['preload']['14612091,oq:devwatch:0:20:f:tg=deviations']['result']['hits']
        ris_file=open(OUTPUT_FILE,"w")
        bodys="";
        for dev in devianWatch:
            print(dev['username'])
            print(dev['url'])#urlpagina
            ris_file.write(dev['hugeview'])
            bodys=bodys+dev['hugeview']
        ris_file.close()
        os.remove("source.txt")
        sendContent(browser,PERSONAL_KEY,bodys)
        

        
