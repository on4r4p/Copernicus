#!/usr/bin/python3
# coding: utf8
from argparse import ArgumentParser
from bs4 import BeautifulSoup
from unidecode import unidecode
from functools import wraps
from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client
from pyfiglet import Figlet
import re
import errno
import imageGwall
import os
import sys
import signal
import urllib.request, urllib.parse, urllib.error
import requests
import random
import itertools
import datetime
import PyPDF2
import time
import json

#some vars

page = 1

timer = "New search at : " ,datetime.datetime.now()

lang = []

listnbr = 0
pageBres = []
pageBacu = []
googleresults = []
variation1= []
variation2= []
variation3= []
variation4= []
variation5= []
variation6= []

ActualImages = []
family = ""
joinvar = []
allcomb = ""

bingtitles =[]
bingurls = []
bingmeta_descs = []

finalres = []

finalink = []

finalinkchance =[]

specialres = []

specialreslink = []

specialreslinkchance = []

pdfinal = []

pdfinalink = []

pdfinalinkchance =[]

pdflink = []

bingpdflink = []

bingfinalink = []

bingfinalinkchance =[]

bingspecialres = []

bingspecialreslink = []

bingspecialreslinkchance = []

bingpdfinal = []

bingpdfinalink = []

bingpdfinalinkchance =[]

yahoores = []

yahoopdflink = []

yahoofinalink = []

yahoofinalinkchance =[]

yahoospecialres = []

yahoospecialreslink = []

yahoospecialreslinkchance = []

yahoopdfinal = []

yahoopdfinalink = []

yahoopdfinalinkchance =[]


searcharglist = []



allcombparsedfinal = []
allcombparsed = []
tmpchance = []
enginelist = ['google','yahoo','bing','pagesblanches']
regionfr = ["Alsace","Aquitaine","Auvergne","Basse-Normandie","Bourgogne","Bretagne","Centre","Champagne-Ardenne","Corse","Franche-Comté","Haute-Normandie","Île-de-France","Languedoc-Roussillon","Limousin","Lorraine","Midi-Pyrénées","Nord-Pas-de-Calais","Pays de la Loire","Picardie","Poitou-Charentes","Provence-Alpes-Côte+d'Azur","Rhône-Alpes","Guadeloupe","Guyane","La+Réunion","Martinique","Mayotte"]
regionnode =["PbMayotte","PbMartinique","PbLaRunion","PbLaRunion","PbGuadeloupe","PbGuyane","PbRhoneAlpes","PbProvenceAlpesCotedAzur","PbPoitouCharentes","PbPicardie","PbPaysdelaLoire","PbNordPasdeCalais","PbMidiPyrnes","PbLorraine","PbLimousin","PbLanguedocRoussillon","PbiledeFrance","PbHauteNormandie","PbFrancheComt","PbCorse","PbChampagneArdenne","PbCentre","PbBretagne","PbBourgogne","PbBasseNormandie","PbAuvergne","PbAquitaine","PbAlsace"]
alllng = ['af','ar','hy','be','bg','ca','zh-CN','hr','cs','da','nl','en','et','tl','fi','fr','de','el','hi','hu','is','id','it','ja','ko','lv','lt','no','fa','pl','pt','ro','ru','sr','sk','sl','es','sv','th','tr','uk','vi']
lng = []


#some def



class TimeoutError(Exception):
    pass

def timeout(seconds=10, error_message=os.strerror(errno.ETIME)):
    def decorator(func):
        def _handle_timeout(signum, frame):
            raise TimeoutError(error_message)

        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.alarm(seconds)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result

        return wraps(func)(wrapper)

    return decorator


def pageblanche(familyname,city):

     global pageBres
     global pageBacu
     print()
     Fig = Figlet(font='cybermedium')
     print(Fig.renderText('Searching family name in pagesblanches.fr'))
     print()
     pbuser_agent_list = ['Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/50.0',
                 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:52.0) Gecko/20100101 Firefox/51.0']

     UserAgent = random.choice(pbuser_agent_list)
     page = 0
     if city != "none":

          try:
                         query = "http://www.pagesjaunes.fr/pagesblanches/recherche?quoiqui="+familyname+"&ou="+city+"&proximite=1"
     
                         opener = urllib.request.build_opener()
                         opener.addheaders = [('User-Agent', str(UserAgent))]

                         send = opener.open(query)
     


                         soup = BeautifulSoup(send,'lxml')
                         #Do a Barrel Roll

                         initial = 0

                         loca = re.findall('" href="#" title="Voir le plan">(.*?)</a></div>', str(soup),re.DOTALL)
                         if len(loca) >0:

                              for item in loca:
                                   item = item.replace("   ","").replace("\n"," ").replace("<br>"," ")
                                   loca[initial] = item
                                   mask = re.compile('\d{5}')
                                   codepostal = mask.search(loca[initial]).group(0)
                                   
                                   time.sleep(10)

                                   query2 = "http://www.pagesjaunes.fr/pagesblanches/recherche?quoiqui="+familyname+"&ou="+str(codepostal)
                                   
                                   opener2 = urllib.request.build_opener()
                                   opener2.addheaders = [('User-Agent', str(UserAgent))]

                                   send2 = opener2.open(query2)



                                   soup2 = BeautifulSoup(send2,'lxml')


                                   i = 0
                                   names = re.findall('<a class="bi-pos-links pj-lb pj-link" data-pjlb=(.*?)<span class="id-bi', str(soup2),re.DOTALL)


                                   if len(names) > 0:

                                        for item in names:

                                             item = item.split('href="#" title=')

                                             item = item[1].replace("   "," ").replace('"','').replace(">","").replace("\n","")
                                             names[i] = item
                                             
                                             i = i + 1
                                   else:
                                             names.append("none")


                                   i = 0

                                   locations = re.findall('" href="#" title="Voir le plan">(.*?)</a></div>', str(soup2),re.DOTALL)
                                   if len(locations) >0:
     
                                        for item in locations:
                                             item = item.replace("   ","").replace("\n"," ").replace("<br>"," ")
                                             locations[i] = item
                                             
                                             i = i + 1
                                   else:
                                             locations.append("none")

                                   i = 0




                                   tels = re.findall('</span><strong class="num" title="(.*?)">', str(soup2),re.DOTALL)

                                   if len(tels) >0:
                                        pass
                                   else:
                                             tels.append("none")



                                   i = 0
                                   for Maow in names:



                                        try:
                                             locations[i]
                                        except:
                                         
                                            locations.append("none")


                                        try:
                                             names[i]
                                        except:
                                             names.append("none")
     
                                        try:
                                             tels[i]
                                        except:
                                             tels.append("none")


                                        if names[i] != "none" and locations[i] != "none" and tels[i] != "none":
                                             print("Autour de "+city+"#***#"+names[i]+"#***#"+locations[i]+"#***#"+tels[i])
                                             pageBacu.append("Autour de "+city+"#***#"+names[i]+"#***#"+locations[i]+"#***#"+tels[i])
                                             i = i + 1 

                                        else:
                                         
                                         
                                             pass







                                   initial = initial + 1
                         else:
                                   pass


                         time.sleep(15)

          except Exception as e:

#             print(e)
             pass





     names = []
     locations = []
     tels =[]

     print()

     for region in regionfr:
          
          
          try:
               query = "http://www.pagesjaunes.fr/pagesblanches/recherche?quoiqui="+familyname+"&ou="+region
     
               opener = urllib.request.build_opener()
               opener.addheaders = [('User-Agent', str(UserAgent))]

               send = opener.open(query)
     


               soup = BeautifulSoup(send,'lxml')


          
               totalpage = re.findall('<span class="pagination-compteur" id="SEL-compteur"><strong>Page 1</strong>(.*?)</span>', str(soup), re.DOTALL)

               if len(totalpage) > 0:

                    totalpage = totalpage[0].replace("  ","").replace("/","")

                    if int(totalpage) == 1:

                         

                         #Do a Barrel Roll
                         tmp = ""
                         i = 0
                         names = re.findall('<a class="bi-pos-links pj-lb pj-link" data-pjlb=(.*?)<span class="id-bi', str(soup),re.DOTALL)
                         
                         
                         if len(names) > 0:

                              for item in names:
                              
                                   item = item.split('href="#" title=')
                                   
                                   item = item[1].replace("   "," ").replace('"','').replace(">","").replace("\n","")
                                   names[i] = item
#                                   print(names[i])
                                   i = i + 1
                         else:
                                   names.append("none")
                         i = 0

                         locations = re.findall('" href="#" title="Voir le plan">(.*?)</a></div>', str(soup),re.DOTALL)
                         if len(locations) >0:

                              for item in locations:
                                   item = item.replace("   ","").replace("\n"," ").replace("<br>"," ")
                                   locations[i] = item
#                                   print(locations[i])
                                   i = i + 1
                         else:
                                   locations.append("none")
                         i = 0

                         tels = re.findall('</span><strong class="num" title="(.*?)">', str(soup),re.DOTALL)

                         if len(tels) >0:
                              pass
                         else:
                                   tels.append("none")
                         i = 0
     
                         for Maow in names:



                                   try:
                                        locations[i]
                                   except:
                                        
                                        locations.append("none")


                                   try:
                                        names[i]
                                   except:
                                        names.append("none")

                                   try:
                                        tels[i]
                                   except:
                                        tels.append("none")

                                   
                                   if names[i] != "none" and locations[i] != "none" and tels[i] != "none":
                                        print(region+"#***#"+names[i]+"#***#"+locations[i]+"#***#"+tels[i])
                                        pageBres.append(region+"#***#"+names[i]+"#***#"+locations[i]+"#***#"+tels[i])
                                        i = i + 1 

                                   else:
                                         i = i + 1
                                         pass
                                   

                         time.sleep(15)


               if int(totalpage) > 1:
                         #print("Total nbr of pages : ",totalpage)

                         #Do a Barrel Roll

                         page = 1
                         while page <= int(totalpage):

                               #print("Page nbr :",page)
                               time.sleep(15)
                               
                               query = "http://www.pagesjaunes.fr/pagesblanches/recherche?quoiqui="+familyname+"&ou="+region+"&page="+str(page)

                               opener = urllib.request.build_opener()
                               opener.addheaders = [('User-Agent', str(UserAgent))]

                               send = opener.open(query)



                               soup = BeautifulSoup(send,'lxml')
                               


                               #print(soup)
                               tmp = ""
                               i = 0
                               
                               names = re.findall('<a class="bi-pos-links pj-lb pj-link" data-pjlb=(.*?)<span class="id-bi', str(soup),re.DOTALL)
                               
                               if len(names) > 0:
     
                                    for item in names:
                                         item = item.split('href="#" title=')
                                         item = item[1].replace("   "," ").replace('"','').replace(">","").replace("\n","")
                                         names[i] = item
                                         i = i + 1
                               else:
                                         names.append("none")
                               i = 0

                               locations = re.findall(' href="#" title="Voir le plan(.*?)</a></div>', str(soup),re.DOTALL)
                               if len(locations) >0:
     
                                    for item in locations:
                                         item = item.replace("   "," ").replace('"','').replace("\n"," ").replace("<br>"," ")
                                         locations[i] = item
                                         i = i + 1
                               else:
                                         locations.append("none")
                               i = 0

                               tels = re.findall('<div class="tel-zone"><span> Tél :</span><strong class="num" title="(.*?)">', str(soup),re.DOTALL)

                               if len(tels) >0:
                                    pass
                               else:
                                         tels.append("none")


                               for maow in names:


                                        try:
                                             locations[i]
                                        except:
                                             locations.append("none")


                                        try:
                                             names[i]
                                        except:
                                             names.append("none")

                                        try:
                                             tels[i]
                                        except:
                                             tels.append("none")

                                        if names[i] != "none" and locations[i] != "none" and tels[i] != "none":
                                             print(region+"#***#"+names[i]+"#***#"+locations[i]+"#***#"+tels[i])
                                             pageBres.append(region+"#***#"+names[i]+"#***#"+locations[i]+"#***#"+tels[i])
                                             i = i + 1 
                                        else:
                                             i = i + 1
                                             pass
                               page = page + 1
               UserAgent = random.choice(pbuser_agent_list)
               
          except Exception as e:

#             print(e)
             pass




def getYahooLinks(link,depth): #from https://github.com/geckogecko
     
     global yahoores
     print()
     Fig = Figlet(font='cybermedium')
     print(Fig.renderText('Getting results from Yahoo'))
     print()
     i = 0
     link = link.replace(" ","+")
     urls2 = []
     results_array = []
     while i<depth: 
          urls2 = []
          results_array = []
          try:
               query = "http://search.yahoo.com/search;_ylt=Agm6_o0evxm18v3oXd_li6bvzx4?p="+str(link)+"&b="+str((i*100)+1)+"&pz=100"
               i = i+1
               print()
               print(query)
               print("Page nbr : ",i)
               print()

               yhuser_agent_list = ['Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/50.0',
                 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:52.0) Gecko/20100101 Firefox/51.0']

               UserAgent = random.choice(yhuser_agent_list)


               opener = urllib.request.build_opener()
               opener.addheaders = [('User-Agent', str(UserAgent))]

               htmltext = opener.open(query)



               soup = BeautifulSoup(htmltext,'lxml')
               search = soup.findAll('div',attrs={'id':'web'})
               searchtext = str(search[0])
               soup1 = BeautifulSoup(searchtext,'lxml')
               list_items = soup1.findAll('li')
               
               time.sleep(random.randint(30,60))
               
               for li in list_items:
                    soup2 = BeautifulSoup(str(li),'lxml')
                    links = soup2.findAll('a')
                    if len(links)>0:
                         results_array.append(links)
               urls2 = (re.findall('www(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',str(results_array)))
               print("Yahoo Link counter : ",len(urls2))
               print()

               for cleanlink in urls2:
                    try:
                         cleanlink = cleanlink.split("/RK")
                         cleanlink[0] = "http://"+urllib.parse.unquote(cleanlink[0])
                         print(cleanlink[0])
                         yahoores.append(cleanlink[0]) 
                    except Exception as e:
                         print(e)
                         pass
               print()
               print()
               print("Yahoo Total : ",len(yahoores))
               if len(yahoores) > 600 :
                    print("ITS OVER 9000 !")
                    print("Need to fix that loop")
                    return

               endofres = re.findall('<span>(.*?)results</span></div></div></li></ol></div>', str(soup),re.DOTALL)
               try:
                    endofres = endofres[0].replace(" ","").replace(",","")
                    if  int(endofres) < i * 100 + 100 - len(yahoores):
                         print()
                         print("That's all falks!")
                         return
               except Exception as e:
                    #print(e)
                    endofres = 1
                    if  int(endofres) < i * 100 + 100 - len(yahoores):
                         print()
                         print("That's all falks")
                         return


          except Exception as e:
                    #print(e)
                    pass
                    if len(yahoores) > 600 :
                         print("Need to fix that loop")
                         return





def random_user_agent_bing():
    binguser_agent_list = ['Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0',
                 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36']

    UserAgent = random.choice(binguser_agent_list)
    UserAgent = {'User-Agent':str(UserAgent)}
    return UserAgent


def make_request_bing(keyword,first):

     
    keyword = keyword.replace(' ','+')
    base_url = 'http://www.bing.com/search?q='
    result_count = '&count=50'
    try:
        r = requests.get('{}{}{}{}'.format(base_url,keyword,result_count,first),headers=random_user_agent_bing())
        #print("\n\n",r)
        return r
    except Exception as e:
        print(e)
        

def parse_soup_bing(keyword,response):
    titles = []
    urls = []
    meta_descs = []
    if response.status_code == 200:
        soup = BeautifulSoup(response.text,'lxml')
        results = soup.find_all('li',attrs={'class':'b_algo'})
        for result in results:
            title = result.find('h2')
            title = title.get_text()
            titles.append(title)
            url = result.find('a')
            url = url['href']
            urls.append(url)
            meta_desc = result.find('p')
            meta_desc = meta_desc.get_text()
            meta_descs.append(meta_desc)
        return titles,urls,meta_descs
        
    else:
        
        return titles, urls, meta_descs



def bing(keyword): #from https://github.com/EdmundMartin

        global bingtitles
        global bingurls
        global bingmeta_desk  
        global page
     	
        respage = []
        print()
        Fig = Figlet(font='cybermedium')
        print(Fig.renderText('Getting results from Bing'))
        print()

        while page < 401:
               print()
               valuepage = "&first=" + str(page)
               print("Results from Bing : ",page)

               respage.append(make_request_bing(keyword,valuepage))
               page = page + 50
               time.sleep(random.randint(30,60))
        

        for response in respage:
               #print(response)
               try:
                   titles, urls, meta_descs = parse_soup_bing(keyword,response)
                   for titres in titles:
                         bingtitles.append(titres)
                   for liens in urls:
                         bingurls.append(liens)
                   for meta in meta_descs:
                         bingmeta_descs.append(meta)

               except:
                         pass



def get_soup(url,header):
	

	
    return BeautifulSoup(urllib.request.urlopen(urllib.request.Request(url,headers=header)),'html.parser')

def google(language,searcharg,cityarg,addarg):

     global googleresults

     for boka in language:
            print()
            inc = "Google Fetching Results in : " + str(boka)
            print() 
            Fig = Figlet(font='cybermedium')
            print(Fig.renderText(str(inc)))
            print()
            if cityarg != "none":
               
               if pbarg.lower() != "true":
                    #cityarg = cityarg
                    print("with cityarg")
                    pass
               if pbarg.lower() == "true":
                    print("without cityarg")
                    cityarg = "none"


            if cityarg != "none":
                #print("without cityarg")
                try:



                         gguseragent = ['Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/50.0',
                                     'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:52.0) Gecko/20100101 Firefox/51.0']

                         UserAgent = random.choice(gguseragent)
                         #print(UserAgent)
                         page = 0
                         stop = 0
                         fuckingstop = 0

                         try:
                                        while stop != 1:
                                             query = "https://www.google.com/search?hl="+boka+"&q="+str(searcharg).replace(" ","+")+"+"+cityarg+"&btnG=Google+Search&start="+str(page)+"&num=100&filter=0"
                                             opener = urllib.request.build_opener()
                                             opener.addheaders = [('User-Agent', str(UserAgent))]
                                             send = opener.open(query)
                                             soup = BeautifulSoup(send,'lxml')
                                             theend = re.findall('id="pnnext"',str(soup))
                                             if len(theend) >0:
                                                  links = re.findall('<h3 class="r"><a href="(.*?)" onmousedown="', str(soup),re.DOTALL)
                                                  for link in links:

                                                       if not link in googleresults:
                                                            #print(link)
                                                            googleresults.append(link)
                                                       else:
                                                                 #print("Already Saved !"),googleresults
                                                                 pass
                                                  print()
                       

                                                  print("Google founds new links:",len(links))
                                                  page = page + 100
                              
                                                  time.sleep(random.randint(42,84))
                                                  
                                             else:
                                                  links = re.findall('<h3 class="r"><a href="(.*?)" onmousedown="', str(soup),re.DOTALL)
                                                  for link in links:
                                                  
                                                       if not link in googleresults:
                                                               #print(link)
                                                               googleresults.append(link)
                                                       else:
                                                                 #print("Already Saved !"),googleresults
                                                                 pass

                                                  print()
                                                  print("Google total Links :",len(googleresults))
                                                  print("End of results")
                              
                                                  stop = 1

                         except Exception as e:
                                   print(e)
                                   fuckingstop =  fuckingstop + 1
                                   if fuckingstop > 3:
                                        stop = 1
                except Exception as e:
                
                    print(("error : ",e))
                    pass
            if cityarg == "none":
                     #print("with cityarg")
                try:



                         gguseragent = ['Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/50.0',
                                     'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:52.0) Gecko/20100101 Firefox/51.0']

                         UserAgent = random.choice(gguseragent)
                         #print(UserAgent)
                         page = 0
                         stop = 0
                         fuckingstop = 0
                         

                         try:
                                        while stop != 1:
                                             query = "https://www.google.com/search?hl="+boka+"&q="+str(searcharg).replace(" ","+")+"&btnG=Google+Search&start="+str(page)+"&num=100&filter=0"
                                             opener = urllib.request.build_opener()
                                             opener.addheaders = [('User-Agent', str(UserAgent))]
                                             send = opener.open(query)
                                             soup = BeautifulSoup(send,'lxml')
                                             theend = re.findall('id="pnnext"',str(soup))
                                             if len(theend) >0:
                                                  links = re.findall('<h3 class="r"><a href="(.*?)" onmousedown="', str(soup),re.DOTALL)
                                                  for link in links:

                                                       if not link in googleresults:
                                                            #print(link)
                                                            googleresults.append(link)
                                                       else:
                                                                 #print("Already Saved !"),googleresults
                                                                 pass
                                                  print()
                       

                                                  print("Google founds new links counter",len(links))
                                                  page = page + 100
                              
                                                  time.sleep(random.randint(42,84))
                              
                                             else:
                                                  links = re.findall('<h3 class="r"><a href="(.*?)" onmousedown="', str(soup),re.DOTALL)
                                                  for link in links:
                                                       
                                                       if not link in googleresults:
                                                               print(link)
                                                               googleresults.append(link)
                                                       else:
                                                                 #print("Already Saved !"),googleresults
                                                                 pass

                                                  print()
                                                  print("Google total Links :",len(googleresults))
                                                  print("End of results")
                              
                                                  stop = 1

                         except Exception as e:
                                   print(e)
                                   fuckingstop =  fuckingstop + 1
                                   if fuckingstop > 3:
                                        stop = 1
                except Exception as e:
                
                    print(("error : ",e))
                    pass


     try:
                                        filelog = open("./Data/Search.log","r")
                                        filelog.close()
     except:
                                        print("==")
                                        print("filelog does not exist Search.log")
                                        print("Creating filelog")
                                        print("==")
                                        filelog = open("./Data/Search.log","w")
                                        filelog.write("")
                                        filelog.close()


     filelog = open("./Data/Search.log","a")
     filelog.write("\n"+str(timer)+"\n"+"For : "+str(searcharg)+"\nIn :"+str(cityarg)+"\nMay Contain :"+str(addarg)+"\n")

     for item in googleresults:

             filelog.write("\n"+str(item))
     filelog.close










def catch(url):

     catch = ["www.amazon.fr","watch?v",".pdf","dailymotion",".asp",".doc",".gz",".zip",".tar",".bz2",".rar",".7zip",".jsp",".ppt"]

     for ext in catch:
          if ext.lower() in url:
               return 1
def getimg(query,cityarg):

    global ActualImages

    if cityarg != "none":
           query = query+ " "+cityarg

    query = unidecode(query)
    image_type="osint"
    query= query.split()
    query='+'.join(query)
    url="https://www.google.co.in/search?q="+query+"&source=lnms&tbm=isch"
    print()
    Fig = Figlet(font='cybermedium')
    print(Fig.renderText('Getting Pictures from Google'))
    print()

    #add the directory for your image here
    DIR="./Data/Pictures/"

    header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
    soup = get_soup(url,header)

    ActualImages=[]# contains the link for Large original images, type of  image
    #print(ActualImages)
    for a in soup.find_all("div",{"class":"rg_meta"}):
        #print(a)
        link , Type =json.loads(a.text)["ou"]  ,json.loads(a.text)["ity"]
        ActualImages.append((link,Type))
    print()
    print("there are total" , len(ActualImages),"images")
    print()
    if not os.path.exists(DIR):
                os.mkdir(DIR)
                #print("pasglop")
    DIR = os.path.join(DIR, query.split()[0])

    if not os.path.exists(DIR):
            os.mkdir(DIR)

    print(DIR)

    ###print images
    for i , (img , Type) in enumerate( ActualImages):
        try:
            req = urllib.request.Request(img, headers={'User-Agent' : str(header)})
            raw_img = urllib.request.urlopen(req).read()
            cntr = len([i for i in os.listdir(DIR) if image_type in i]) + 1
            #print(cntr)
            if len(Type)==0:
                f = open(os.path.join(DIR , image_type + "_"+ str(cntr)+".jpg"), 'wb')
            else :
                f = open(os.path.join(DIR , image_type + "_"+ str(cntr)+"."+Type), 'wb')

            f.write(raw_img)
            f.close()

        except Exception as e:
            pass
            #print()
            #print("could not load : "+img)
            #print(e)



   


    onlyfiles = [f for f in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, f))]

    for imgs in onlyfiles:

                try:
                    print(imageGwall.Image(str(DIR+"/"+imgs)))
                except Exception as e:
                    print(e)


def permutation(searcharg):

     global joinvar
     global searcharglist
     global allcomb
     global allcombparsed


     searcharglist = searcharg.lower()
     searchsave = searcharglist
     asclify = unidecode(searcharglist).split(" ")
     searcharglist = searcharglist.split(" ")

     if all(ord(char) < 128 for char in searchsave) == True:

         for i in range(0,len(searcharglist)):
             variation1.append(searcharglist[i])
             variation2.append(searcharglist[i].title())
             variation3.append(searcharglist[i].upper())

         joinvar = variation1+variation2+variation3

         #print(joinvar)



         allcomb = list(itertools.permutations(joinvar, len(searcharglist)))

         #print("==")
         #print("loading all permutations")
         #print("==")


         for item in allcomb:

             allcombparsed.append(str(item).replace(",","").replace("(","").replace("'","").replace(")",""))
             #print((str(item).replace(",","").replace("(","").replace("'","").replace(")","")))

         #for item in allcombparsed:

            #print(item)

     #sys.exit()
     else:

         for i in range(0,len(searcharglist)):
             variation1.append(searcharglist[i])
             variation2.append(searcharglist[i].title())
             variation3.append(searcharglist[i].upper())
             variation4.append(asclify[i])
             variation5.append(asclify[i].title())
             variation6.append(asclify[i].upper())
         joinvar = variation1+variation2+variation3+variation4+variation5+variation6

         

         #print(joinvar)



         allcomb = list(itertools.permutations(joinvar, len(searcharglist)))

         #print("==")
         #print("loading all permutations")
         #print("==")


         for item in allcomb:

             allcombparsed.append(str(item).replace(",","").replace("(","").replace("'","").replace(")",""))
             #print((str(item).replace(",","").replace("(","").replace("'","").replace(")","")))

         #for item in allcombparsed:

           # print(item)
         



@timeout(121)
def lastchance(res,link,searcharg,addarg,cityarg):
     global tmpchance
     
     tmpchance = []
     min = []

     if type(res) == list:
          res = [chunk.lower() for chunk in res]
     if type(res) == str:
          res = res.lower()


     searcharg = searcharg.lower()
     addarg = addarg.lower()
     cityarg = cityarg.lower()

     for item in searcharg.split(' '):
          if len(item) > 2:
               min.append(item)


     if cityarg != "none":
          min.append(cityarg)






     if len(addarg.split(",")) > 0:
          

          if family != "none" and family.lower() in res:
               #print("Family Name detected",family)
               cnt = 0
               required = 0
               roundmin = int(round(len(min)/3))
               if roundmin < 1:
                    roundmin = 1
               good = len(min)+ roundmin

               for item in min:

                     if item.lower() in res:
                           required = required + 1
                           cnt = cnt + 1
#                           print("Found required word : ",item)
                           tmpchance.append(item)

               for item in addarg.split(","):

                     if item.lower() in res:

                           cnt = cnt + 1
#                           print("Found additional word : ",item)
                           tmpchance.append(item)

               

               if cnt >= good and required >= 1:

#                     if link not in finalink:

#                           if link not in pdflink:
                                        tmpchance = " ".join(tmpchance)
                                        return 1




@timeout(242)
def searchhtml(item,addarg,searcharg,cityarg,listpos,engine):
       global finalres
       global finalink
       global specialres
       global pdflink
     
       global bingfinalink

       global bingfinalinkchance

       global bingspecialres

       global bingpdflink

       global yahoofinalink

       global yahoofinalinkchance

       global yahoospecialres

       global yahoopdflink


       if engine == "google":
          #print(engine)


          if catch(item) != 1:

               try:

                          done = 0
                          agent_list = ['Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/50.0',
                          'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:52.0) Gecko/20100101 Firefox/51.0']

                     
                          opener = urllib.request.build_opener()
                          opener.addheaders = [('User-Agent', str(agent_list))]           
                          html = opener.open(str(item))
                          soup = BeautifulSoup(html,'lxml')
                         
                          titre = str(soup.title.string).replace("\n","")
                          result = soup.get_text()
                          print()
                          print()
                          print("############")
                          print(("Google Scanning  : ",item))
                          print("############")
                          print("title: ",titre)
                          print()
                          print()
                          for comb in allcombparsed:
                               splitemcase = []
                               Dbl = 0
                               splitem = comb.split(' ')
                               for case in splitem:
                                          splitemcase.append(case.lower())
	     
                               for word in splitemcase:
                                  if Dbl == 0:

                                       if splitemcase.count(word.lower()) > 1:
                                                   Dbl = Dbl + 1



                               if Dbl == 0:
     
                                             if comb in result:
                                                     print()
                                                     print()
                                                     print()
                                                     print()
                                                     print("SUCH WOW !")
                                                     print()
                                                     print()
                                                     print(("FOUND : ", comb))
                                                     print()
                                                     print(("In : ", item))


                                                     pos = result.find(comb)
                                                     samplemin = pos - 70
                                                     samplemax = pos + 70

                                                     echantillon = result[samplemin:samplemax]
                                                     print()
                                                     echantillon = str(echantillon).replace("\n"," ")
                                                     print("Description : ",echantillon)
                                                     print()
                                                     finalres.append(item+" "+comb)
                                                     finalink.append(titre+"#***#"+item+"#***#"+echantillon)
                                                     done = 1
                                                     print()
                                                     print()
                                                     print()


     
                               else:
     
     
                                            pass

                          if lastchance(result,item,searcharg,addarg,cityarg) == 1 and addarg != "none":
                              
                              if done == 0:
                                                     print()
                                                     print()
                                                     print()
                                                     print()
                                                     print("May found Something interesting...")
                                                     print()
                                                     print("In : ", item)

                                                     print()
                                                     print("Contains :",tmpchance)


                                                     finalres.append(item+" "+"lastchance")
                                                     finalinkchance.append(titre+"#***#"+item+"#***#"+"Contains : "+tmpchance)
                                                     print()
                                                     print()
                                                     print()
                                                     print()
 


               except Exception as e:
                                     print()
                                     print()
                                     print(("Error : ",e))
                                     print()
                                     print()
                                     pass
          else:
     
                     print()
                     special = "\nFound special item : " + str(item)
                     print()
                     if ".pdf" in item:
     
                             pdflink.append(item)
                     else:
                             specialres.append(str(special))
                             specialreslink.append(str(item))



       if engine == "bing":


          if catch(item) != 1:


               try:

                          done = 0
                          agent_list = ['Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/50.0',
                           'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:52.0) Gecko/20100101 Firefox/51.0']


                          opener = urllib.request.build_opener()
                          opener.addheaders = [('User-Agent', agent_list)]           

                          html = opener.open(item)
                          soup = BeautifulSoup(html,'lxml')
                          print()
                          result = soup.get_text()

                          print()
                          print()
                          print("############")
                          print(("Bing Scanning  : ",item))
                          print("############")
                          print("title: ",bingtitles[listpos])
                          print()
                          print()
                          for comb in allcombparsed:
                               splitemcase = []
                               Dbl = 0
                               splitem = comb.split(' ')
                               for case in splitem:
                                          splitemcase.append(case.lower())
          
                               for word in splitemcase:
                                  if Dbl == 0:

                                       if splitemcase.count(word.lower()) > 1:
                                                   Dbl = Dbl + 1



                               if Dbl == 0:
     
                                             if comb in result:
                                                     print()
                                                     print()
                                                     print()
                                                     print()
                                                     print("SUCH WOW !")
                                                     print()
                                                     print()
                                                     print(("FOUND : ", comb))
                                                     print()
                                                     print(("In : ", item))



                                                     print()
                                                     print("Description : ",bingmeta_descs[listpos])
                                                     print()
                                                     finalres.append(item+" "+comb+ " bing")
                                                     bingfinalink.append(bingtitles[listpos]+"#***#"+item+"#***#"+bingmeta_descs[listpos])
                                                     done = 1
                                                     print()
                                                     print()
                                                     print()


     
                               else:
     
     
                                            pass

                          if lastchance(result,item,searcharg,addarg,cityarg) == 1 and addarg != "none":
                              
                              if done == 0:
                                                     print()
                                                     print()
                                                     print()
                                                     print()
                                                     print("May found Something interesting...")
                                                     print()
                                                     print("In : ", item)

                                                     print()
                                                     print("Contains :",tmpchance)


                                                     finalres.append(item+" "+"lastchance bing")
                                                     bingfinalinkchance.append(bingtitles[listpos]+"#***#"+item+"#***#"+bingmeta_descs[listpos]+" Contains : "+tmpchance)
                                                     print()
                                                     print()
                                                     print()
                                                     print()
 


               except Exception as e:
                                     print()
                                     print()
                                     print("searchtml error")
                                     print(("Error : ",e))
                                     print()
                                     print()
                                     pass
          else:
     
                     print()
                     special = "\n Bing Found special item : " + str(item)
                     print()
                     if ".pdf" in item:
     
                             bingpdflink.append(item)
                     else:
                             specialres.append(str(special))
                             bingspecialreslink.append(str(item))







       if engine == "yahoo":
          #print(engine)


          if catch(item) != 1:

               try:

                          done = 0
                          agent_list = ['Mozilla/5.0 (Windows NT 10.0; WOW64; rv:49.0) Gecko/20100101 Firefox/50.0',
                           'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:52.0) Gecko/20100101 Firefox/51.0']
                     
                     
                          opener = urllib.request.build_opener()
                          opener.addheaders = [('User-Agent', agent_list)]           

                          html = opener.open(item)

                          soup = BeautifulSoup(html,'lxml')
     
                          titre = str(soup.title.string).replace("\n","")
                          result = soup.get_text()
                          print()
                          print()
                          print("############")
                          print(("Scanning  : ",item))
                          print("############")
                          print("title: ",titre)
                          print()
                          print()
                          for comb in allcombparsed:
                               splitemcase = []
                               Dbl = 0
                               splitem = comb.split(' ')
                               for case in splitem:
                                          splitemcase.append(case.lower())
          
                               for word in splitemcase:
                                  if Dbl == 0:

                                       if splitemcase.count(word.lower()) > 1:
                                                   Dbl = Dbl + 1



                               if Dbl == 0:
     
                                             if comb in result:
                                                     print()
                                                     print()
                                                     print()
                                                     print()
                                                     print("SUCH WOW !")
                                                     print()
                                                     print()
                                                     print(("FOUND : ", comb))
                                                     print()
                                                     print(("In : ", item))


                                                     pos = result.find(comb)
                                                     samplemin = pos - 70
                                                     samplemax = pos + 70

                                                     echantillon = result[samplemin:samplemax]
                                                     print()
                                                     echantillon = str(echantillon).replace("\n"," ")
                                                     print("Description : ",echantillon)
                                                     print()
                                                     finalres.append(item+" "+comb+" Yahoo")
                                                     yahoofinalink.append(titre+"#***#"+item+"#***#"+echantillon)
                                                     done = 1
                                                     print()
                                                     print()
                                                     print()


     
                               else:
     
     
                                            pass

                          if lastchance(result,item,searcharg,addarg,cityarg) == 1 and addarg != "none":
                              
                              if done == 0:
                                                     print()
                                                     print()
                                                     print()
                                                     print()
                                                     print("May found Something interesting...")
                                                     print()
                                                     print("In : ", item)

                                                     print()
                                                     print("Contains :",tmpchance)


                                                     finalres.append(item+" "+"lastchance Yahoo")
                                                     yahoofinalinkchance.append(titre+"#***#"+item+"#***#"+"Contains : "+tmpchance)
                                                     print()
                                                     print()
                                                     print()
                                                     print()
 


               except Exception as e:
                                     print()
                                     print()
                                     print(("Error : ",e))
                                     print()
                                     print()
                                     pass
          else:
     
                     print()
                     special = "\nYahoo Found special item : " + str(item)
                     print()
                     if ".pdf" in item:
     
                             yahoopdflink.append(item)
                     else:
                             specialres.append(str(special))
                             yahoospecialreslink.append(str(item))












@timeout(242)
def searchpdf(pdf,addarg,searcharg,cityarg,engine):
    global pdfinal
    global pdfinalink
    global bingpdfinalink
    global yahoopdfinalink

    if engine == "google":
           
             print()
             print(("Google Searching in pdf file : ",pdf))
             print()

             try: 

                     done = 0
                     save = "./Data/Pdf/"+str(pdf.split("/")[-1])
                     urllib.request.urlretrieve (str(pdf), str(save))
                     Pdtxt = getPDFContent(save)

                     for comb in allcombparsed:

                          splitemcase = []
                          Dbl = 0
                          splitem = comb.split(' ')
                          for case in splitem:
                                     splitemcase.append(case.lower())

                          for word in splitemcase:
                             if Dbl == 0:

                                  if splitemcase.count(word.lower()) > 1:
                                             Dbl = Dbl + 1


                          if Dbl == 0:

                             if comb in Pdtxt:


                                     print()
                                     print()
                                     print()
                                     print("SUCH WOW !!!")
                                     print()
                                     print(("Found : ",str(comb)))
                                     print()
                                     print(("In : ", str(pdf)))


                                     pos = Pdtxt.find(comb)
                                     samplemin = pos - 70
                                     samplemax = pos + 70

                                     echantillon = Pdtxt[samplemin:samplemax]
                                     print()
                                     echantillon = str(echantillon).replace("\n"," ")
                                     print("Description : ",echantillon)
                                     print()

                                     pdfinal.append(str(pdf)+" "+"Confirmed Google")
                                     pdfinalink.append(str(pdf)+"#***#"+echantillon)
                                     done = 1
                                     print()
                                     print()
                                     print()


                    
                     if lastchance(Pdtxt,pdf,searcharg,addarg,cityarg) == 1 and addarg != "none":
                         if done == 0:

                                     print()
                                     print()
                                     print()
                                     print("May have found Something interesting...")
                                     print()
                                     print("In : ", str(pdf))
                                     print()
                                     print()
                                     print("Description",tmpchance)
                                     print()

                                     pdfres = "Google Confirmed Last Chance: ",str(pdf)
                                     pdfinal.append(str(pdfres))
                                     pdfinalinkchance.append(str(pdf)+"#***#"+"Contains : "+tmpchance)


             except Exception as e:
                     print(e)
                     pass

    if engine == "yahoo":
           
             print()
             print(("Yahoo Searching in pdf file : ",pdf))
             print()

             try: 

                     done = 0
                     save = "./Data/Pdf/"+str(pdf.split("/")[-1])
                     urllib.request.urlretrieve (str(pdf), str(save))
                     Pdtxt = getPDFContent(save)

                     for comb in allcombparsed:

                          splitemcase = []
                          Dbl = 0
                          splitem = comb.split(' ')
                          for case in splitem:
                                     splitemcase.append(case.lower())

                          for word in splitemcase:
                             if Dbl == 0:

                                  if splitemcase.count(word.lower()) > 1:
                                             Dbl = Dbl + 1


                          if Dbl == 0:

                             if comb in Pdtxt:


                                     print()
                                     print()
                                     print()
                                     print("SUCH WOW !!!")
                                     print()
                                     print(("Found : ",str(comb)))
                                     print()
                                     print(("In : ", str(pdf)))


                                     pos = Pdtxt.find(comb)
                                     samplemin = pos - 70
                                     samplemax = pos + 70

                                     echantillon = Pdtxt[samplemin:samplemax]
                                     print()
                                     echantillon = str(echantillon).replace("\n"," ")
                                     print("Description : ",echantillon)
                                     print()

                                     pdfinal.append(str(pdf)+" "+"Confirmed Yahoo")
                                     yahoopdfinalink.append(str(pdf)+"#***#"+echantillon)
                                     done = 1
                                     print()
                                     print()
                                     print()


                    
                     if lastchance(Pdtxt,pdf,searcharg,addarg,cityarg) == 1 and addarg != "none":
                         if done == 0:

                                     print()
                                     print()
                                     print()
                                     print("May have found Something interesting...")
                                     print()
                                     print("In : ", str(pdf))
                                     print()
                                     print()
                                     print("Description",tmpchance)
                                     print()

                                     pdfres = "Yahoo Confirmed Last Chance: ",str(pdf)
                                     pdfinal.append(str(pdfres))
                                     yahoopdfinalinkchance.append(str(pdf)+"#***#"+"Contains : "+tmpchance)


             except Exception as e:
                     print(e)
                     pass

    if engine == "bing":
           
             print()
             print(("Bing Searching in pdf file : ",pdf))
             print()

             try: 

                     done = 0
                     save = "./Data/Pdf/"+str(pdf.split("/")[-1])
                     urllib.request.urlretrieve (str(pdf), str(save))
                     Pdtxt = getPDFContent(save)

                     for comb in allcombparsed:

                          splitemcase = []
                          Dbl = 0
                          splitem = comb.split(' ')
                          for case in splitem:
                                     splitemcase.append(case.lower())

                          for word in splitemcase:
                             if Dbl == 0:

                                  if splitemcase.count(word.lower()) > 1:
                                             Dbl = Dbl + 1


                          if Dbl == 0:

                             if comb in Pdtxt:


                                     print()
                                     print()
                                     print()
                                     print("SUCH WOW !!!")
                                     print()
                                     print(("Found : ",str(comb)))
                                     print()
                                     print(("In : ", str(pdf)))


                                     pos = Pdtxt.find(comb)
                                     samplemin = pos - 70
                                     samplemax = pos + 70

                                     echantillon = Pdtxt[samplemin:samplemax]
                                     print()
                                     echantillon = str(echantillon).replace("\n"," ")
                                     print("Description : ",echantillon)
                                     print()

                                     pdfinal.append(str(pdf)+" "+"bing Confirmed")
                                     bingpdfinalink.append(str(pdf)+"#***#"+echantillon)
                                     done = 1
                                     print()
                                     print()
                                     print()


                    
                     if lastchance(Pdtxt,pdf,searcharg,addarg,cityarg) == 1 and addarg != "none":
                         if done == 0:

                                     print()
                                     print()
                                     print()
                                     print("May have found Something interesting...")
                                     print()
                                     print("In : ", str(pdf))
                                     print()
                                     print()
                                     print("Description",tmpchance)
                                     print()

                                     pdfres = "Bing Confirmed Last Chance: ",str(pdf)
                                     pdfinal.append(str(pdfres))
                                     bingpdfinalinkchance.append(str(pdf)+"#***#"+"Contains : "+tmpchance)


             except Exception as e:
                     print("searchpdf error")
                     print(e)
                     pass







def getPDFContent(path):
    content = ""
    pdf = PyPDF2.PdfFileReader(path, "rb")
    for i in range(0, pdf.getNumPages()):
        
        content += pdf.getPage(i).extractText() + "\n"
    content = " ".join(content.strip().split())
    return content





### Some code:


parser = ArgumentParser()

parser.add_argument("-e","--engine", dest="engine",default='google,bing,yahoo,pagesblanches',
                    help="Use specific search engine: -e yahoo,bing ", metavar="Engine")

parser.add_argument("-l","--language", dest="lang",default='fr',
                    help="Country : en,zh-CN,es,ar,pt,ja,ru,fr,de...", metavar="LANG")

parser.add_argument("-pb","--pagesblanches", dest="pbarg",default='none',
                    help="-pb true : Only use the city arg with pagesblanches", metavar="TRUE-FALSE")

parser.add_argument("-s","--search", dest="name",default='Marcel Menou',
                    help="Name to Search", metavar="'NAME'")

parser.add_argument("-f","--family", dest="family",default='none',
                    help="Specify Family name if any (needed with -a and to use pageblanche)ex: -s Albert Einstein -f Einstein -a relativity,physics", metavar="FAMILY NAME")

parser.add_argument("-a","--add", dest="add",default='none',
                    help="Additional information to catch more results: \n--add Word1,Word2,Word3", metavar="OPTION")

parser.add_argument("-c","--city", dest="city",default='none',
                    help="Specify city", metavar="CITY")

parser.add_argument("-i","--img", dest="image",default='true',
                    help="-i true Search and download pictures too ", metavar="TRUE-FALSE")


args = parser.parse_args()

argsengine = args.engine

lang = args.lang

argsname = args.name

argscity = args.city

argsfamily = args.family

argsadd = args.add

argsimg = args.image

pbarg = args.pbarg

family = argsfamily

#file = open("arg.txt","w")
#file.write("\n"+argsname+"\n"+argscity+"\n"+argsfamily+"\n"+argsadd)
#file.close

if lang != "none":

     tmpsplit = lang.split(",")
     for split in tmpsplit:
          if split in alllng:
               lng.append(split)
     if len(lng) == 0:
          lng = ['en','fr']
else:

     lng = ['en','fr']

print()

if argsengine.lower() != "none" :
     splitengine = argsengine.split(",")
     for item in splitengine:
          if not item.lower() in enginelist:
               print()
               print("some options are missing")
               print()
               print("-e option must match the following names : google,bing,yahoo,pagesblanches")
               print()
               print("Example: -e google,pagesblanches  -s Albert Einstein -f Einstein -c Berne")
               print()
               print("")
               sys.exit()


if argsadd != "none" and family == "none":
     print()
     print("-f option is missing")
     print()
     print("To use additional information (-a) :")
     print()
     print("Specify Family name (-f) ex: -s Albert Einstein -f Einstein -a relativity,physics")
     print()
     print("")
     sys.exit()

if argsadd == "none" and family != "none":
     print()
     print("-a option is missing")
     print()
     print("The -f option must be used in combination with -a :")
     print()
     print("Specify Additional informations (-a) ex: -s Albert Einstein -f Einstein -a relativity,physics")
     print()
     print("")
     sys.exit()


if pbarg != "none" and family == "none":
     print()
     print("some options are missing")
     print()
     print("-pb option must be used in combination with -c and -f :")
     print()
     print(" -s Albert Einstein -f Einstein -c Berne -pb true")
     print()
     print("")
     sys.exit()

if pbarg != "none" and argscity == "none":
     print()
     print("some options are missing")
     print()
     print("-pb option must be used in combination with -c and -f :")
     print()
     print(" -s Albert Einstein -f Einstein -c Berne -pb true")
     print()
     print("")
     sys.exit()


if pbarg.lower() != "none" :
     if pbarg.lower() != "true" :
          if pbarg.lower() != "false":
               print()
               print("some options are missing")
               print()
               print("-pb option must be True or False")
               print()
               print(" -s Albert Einstein -f Einstein -c Berne -pb true")
               print()
               print("")
               sys.exit()

if argsimg.lower() != "none" :
     if argsimg.lower() != "true" :
          if argsimg.lower() != "false":
               print()
               print("some options are missing")
               print()
               print("-i option must be True or False")
               print()
               print(" -s Albert Einstein -f Einstein -c Berne -i true")
               print()
               print("")
               sys.exit()



print()
print("Using Search Engine :",splitengine)
print()
print("Results Languages : ",lng)
print()
print("Search related pictures :",argsimg)
print()
print("Searching for : ",args.name)
print()
print("Family Name : ",args.family)
print()
print("In city : ",args.city)
print()
print("Which may contain : ",args.add)
print()

permutation(argsname)



for item in splitengine:
     if item.lower() == "pagesblanches":
          if family != "none":
               pageblanche(family,args.city)

for item in splitengine:
     if item.lower() == "yahoo":
          getYahooLinks(argsname,5)

for item in splitengine:
     if item.lower() == "bing":
          bing(argsname)
if argsimg.lower() == "true":
     getimg(argsname,argscity)

for item in splitengine:
     if item.lower() == "google":
          google(lng,argsname,argscity,argsadd)




#searcharglist = searcharg.lower()
#searcharglist = searcharglist.split(" ")
print()
print()
print()
for item in splitengine:
     if item.lower() == "google":

          Fig = Figlet(font='cybermedium')
          print(Fig.renderText('Google Searching in Results'))
          print()
          print()
          for link in googleresults:

               try:
                    searchhtml(link,argsadd,argsname,argscity,"placehold","google")
               except Exception as e:
                    print(e)
                    pass

          print()
          print()
          Fig = Figlet(font='cybermedium')
          print(Fig.renderText('Google Searching in PDF'))
          print()
          print(("Pdf Nbr :",len(pdflink)))
          print()


          for links in pdflink:
               try:
                    searchpdf(links,argsadd,argsname,argscity,"google")
               except Exception as e:
                    print(e)
                    pass


print()
print()
######################################################################
print()
for item in splitengine:
     if item.lower() == "bing":

          Fig = Figlet(font='cybermedium')
          print(Fig.renderText('Bing Searching in Results'))
          print()
          print()
          print()
          for link in bingurls:
     
               try:
                         searchhtml(link,argsadd,argsname,argscity,listnbr,"bing")
                         listnbr = listnbr + 1
               except Exception as e:
                    print(e)
                    listnbr = listnbr + 1
                    pass

          print()
          print()
          print()
          Fig = Figlet(font='cybermedium')
          print(Fig.renderText('Bing Searching in PDF'))
          print()
          print(("Pdf Nbr :",len(bingpdflink)))
          print()
          print()
          print()

          for links in bingpdflink:
               try:
                    searchpdf(links,argsadd,argsname,argscity,"bing")
               except Exception as e:
                    print(e)
                    pass
######################################################################



print()
print()

print()
for item in splitengine:
     if item.lower() == "yahoo":

          Fig = Figlet(font='cybermedium')
          print(Fig.renderText('Yahoo Searching in Results'))
          print()
          print()
          for link in yahoores:

               try:
                    searchhtml(link,argsadd,argsname,argscity,"placehold","yahoo")
               except Exception as e:
                    print(e)
                    pass

          print()
          print()
          print()
          Fig = Figlet(font='cybermedium')
          print(Fig.renderText('Yahoo Searching in PDF'))
          print()
          print()
          print(("Pdf Nbr :",len(yahoopdflink)))
          print()
          print()
          print()


          for links in yahoopdflink:
               try:
                    searchpdf(links,argsadd,argsname,argscity,"yahoo")
               except Exception as e:
                    print(e)
                    pass


print()
print()







proceed = ""

while proceed.lower() != "ok":
     proceed = input('Make sure neo4j is up and running then type ok : ')



print()
print()
print("##############################################")
print()
Fig = Figlet(font='cybermedium')
print(Fig.renderText('Building Graph'))
print()
print("##############################################")
print()
print()

for item in splitengine:
     if item.lower() == "pagesblanches":

          Pb = pageBres

for item in splitengine:
     if item.lower() == "google":

          googlelink = finalink
          googlelinkchance = finalinkchance
          googlepdf = pdfinalink
          googlepdfchance = pdfinalinkchance
          googlespecial = specialreslink
          googleimg = ActualImages

for item in splitengine:
     if item.lower() == "bing":

          binglink = bingfinalink
          binglinkchance = bingfinalinkchance
          bingpdf = bingpdfinalink
          bingpdfchance = bingpdfinalinkchance
          bingspecial = bingspecialreslink
          bingimg = ActualImages

for item in splitengine:
     if item.lower() == "yahoo":

          yahoolink = yahoofinalink
          yahoolinkchance = yahoofinalinkchance
          yahoopdf = yahoopdfinalink
          yahoopdfchance = yahoopdfinalinkchance
          yahoospecial = yahoospecialreslink
          yahooimg = ActualImages



db = GraphDatabase("http://localhost:7474")
 

stitle = db.labels.create("Search")  
s0 = db.nodes.create(Searchname=argsname)
stitle.add(s0)


srcheng = db.labels.create("Engine")
for item in splitengine:
     if item.lower() == "google":

          s1 = db.nodes.create(Enginename="Google")
          srcheng.add(s1)
          s0.relationships.create("Query", s1)
for item in splitengine:
     if item.lower() == "bing":

          s2 = db.nodes.create(Enginename="Bing")
          srcheng.add(s2)
          s0.relationships.create("Query", s2)
for item in splitengine:
     if item.lower() == "yahoo":

          s3 = db.nodes.create(Enginename="Yahoo")
          srcheng.add(s3)
          s0.relationships.create("Query", s3)
for item in splitengine:
     if item.lower() == "pagesblanches":

          s4 = db.nodes.create(Enginename="PagesBlanches")
          srcheng.add(s4)
          s0.relationships.create("Query", s4)


labelwebsite = db.labels.create("Website")
labelFile = db.labels.create("File")
labelIMG = db.labels.create("Image")
labelIMGres = db.labels.create("ImageResults")
labelspecial = db.labels.create("Special")
labelspecialres = db.labels.create("SpecialeResults")
labelsiteverified = db.labels.create("Important")
labelsitechance = db.labels.create("Valid")
labelpdfverified = db.labels.create("Important")
labelpdfchance = db.labels.create("Valid")
labelPbacu = db.labels.create("Accurate")
labelPbres = db.labels.create("National")
labelPbregion = db.labels.create("Regions")
labelPbinfo = db.labels.create("infoPageBlanches")

for item in splitengine:
     if item.lower() == "google":
          GoogleurlPlus = db.nodes.create(Urlimp="Url Important")
          GoogleurlMinus = db.nodes.create(Urlval="Url Valid")
          s1.relationships.create("Link Website", GoogleurlPlus)
          s1.relationships.create("Link Website", GoogleurlMinus)
          GooglepdfPlus = db.nodes.create(Typepdfimp="Pdf Important")
          GooglepdfMinus = db.nodes.create(Typepdfval="Pdf Valid")
          s1.relationships.create("Link Pdf", GooglepdfPlus)
          s1.relationships.create("Link Pdf", GooglepdfMinus)
          Googleimgnode = db.nodes.create(Imgsname="Imgs")
          s1.relationships.create("Image File", Googleimgnode)
          Googlespecialnode = db.nodes.create(Specialname="Not handled yet")
          s1.relationships.create("Not handled", Googlespecialnode)
          labelwebsite.add(GoogleurlPlus, GoogleurlMinus)
          labelFile.add(GooglepdfPlus,GooglepdfMinus)
          labelIMG.add(Googleimgnode)
          labelspecial.add(Googlespecialnode)
for item in splitengine:
     if item.lower() == "bing":
          BingurlPlus = db.nodes.create(Urlimp="Url Important")
          BingurlMinus = db.nodes.create(Urlval="Url Valid")
          s2.relationships.create("Link Website", BingurlPlus)
          s2.relationships.create("Link Website", BingurlMinus)
          BingpdfPlus = db.nodes.create(Typepdfimp="Pdf Important")
          BingpdfMinus = db.nodes.create(Typepdfval="Pdf Valid")
          s2.relationships.create("Link Pdf", BingpdfPlus)
          s2.relationships.create("Link Pdf", BingpdfMinus)
          Bingimgnode = db.nodes.create(Imgsname="Imgs")
          s2.relationships.create("Image File", Bingimgnode)
          Bingspecialnode = db.nodes.create(Specialname="Not handled yet")
          s2.relationships.create("Not handled", Bingspecialnode)
          labelwebsite.add(BingurlPlus, BingurlMinus)
          labelFile.add(BingpdfPlus,BingpdfMinus)
          labelIMG.add(Bingimgnode)
          labelspecial.add(Bingspecialnode)
for item in splitengine:
     if item.lower() == "yahoo":
          YahoourlPlus = db.nodes.create(Urlimp="Url Important")
          YahoourlMinus = db.nodes.create(Urlval="Url Valid")
          s3.relationships.create("Link Website", YahoourlPlus)
          s3.relationships.create("Link Website", YahoourlMinus)
          YahoopdfPlus = db.nodes.create(Typepdfimp="Pdf Important")
          YahoopdfMinus = db.nodes.create(Typepdfval="Pdf Valid")
          s3.relationships.create("Link Pdf", YahoopdfPlus)
          s3.relationships.create("Link Pdf", YahoopdfMinus)
          Yahooimgnode = db.nodes.create(Imgsname="Imgs")
          s3.relationships.create("Image File", Yahooimgnode)
          Yahoospecialnode = db.nodes.create(Specialname="Not handled yet")
          s3.relationships.create("Not handled", Yahoospecialnode)
          labelwebsite.add(YahoourlPlus, YahoourlMinus)
          labelFile.add(YahoopdfPlus,YahoopdfMinus)
          labelIMG.add(Yahooimgnode)
          labelspecial.add(Yahoospecialnode)
for item in splitengine:
     if item.lower() == "pagesblanches":
          PagesBlanches = db.nodes.create(Pbname="Regions",Region="Regions", Nom="Regions", Adresse="Regions", telephone="Regions")
          s4.relationships.create("LinkResults", PagesBlanches)
          PbAccurate= db.nodes.create(Pbname="Proximity",Region="Proximity", Nom="Proximity", Adresse="Proximity", telephone="Proximity")
          s4.relationships.create("Results",PbAccurate)
          labelPbres.add(PagesBlanches)
          #labelPbregion.add(PbMayotte,PbMartinique,PbLaRunion,PbLaRunion,PbGuadeloupe,PbGuyane,PbRhoneAlpes,PbProvenceAlpesCotedAzur,PbPoitouCharentes,PbPicardie,PbPaysdelaLoire,PbNordPasdeCalais,PbMidiPyrnes,PbLorraine,PbLimousin,PbLanguedocRoussillon,PbiledeFrance,PbHauteNormandie,PbFrancheComt,PbCorse,PbChampagneArdenne,PbCentre,PbBretagne,PbBourgogne,PbBasseNormandie,PbAuvergne,PbAquitaine,PbAlsace)
          labelPbacu.add(PbAccurate)


print()
print()
print()
print()
print()

try:
                                        filelog = open("./Data/Final.log","r")
                                        filelog.close()
except:
                                        print("==")
                                        print("filelog does not exist Final.log)")
                                        print("Creating filelog")
                                        print("==")
                                        filelog = open("./Data/Final.log","w")
                                        filelog.write("")
                                        filelog.close()


filelog = open("./Data/Final.log","a")
filelog.write("\n"+str(timer)+"\n"+"For : "+str(argsname)+"\n")

for item in finalres:
                  filelog.write("\n"+str(item))

for item in specialres:
                  filelog.write("\n"+str(item))

for item in pdfinal:
                  filelog.write("\n"+str(item))

for item in bingpdfinal:
                  filelog.write("\n"+str(item))

for item in bingspecialres:
                  filelog.write("\n"+str(item))

for item in bingpdfinal:
                  filelog.write("\n"+str(item))
                  
                  
for item in yahoopdfinal:
                  filelog.write("\n"+str(item))

for item in yahoospecialres:
                  filelog.write("\n"+str(item))

for item in yahoopdfinal:
                  filelog.write("\n"+str(item))

filelog.close




print()
print()
print("##############################################")
print()
Fig = Figlet(font='cybermedium')
print(Fig.renderText('Writing Graph'))
print()
print("##############################################")
print()
print()


print()
for item in splitengine:
     if item.lower() == "pagesblanches":

          Fig = Figlet(font='cybermedium')
          print(Fig.renderText('Pages Blanches Results'))
          print("")
          print("Accurate:")
          for info in pageBacu:
                         info = info.split("#***#")
                         item = db.nodes.create(Region=info[0], Nom=info[1], Adresse=info[2], telephone=info[3])
                         PbAccurate.relationships.create("Infos",item)
                         labelPbacu.add(item)
                         print(item)
          print()
          print("global :")
          for info in Pb:
            try:
               info = info.split("#***#")
               print(info)
     
               if info[0] == "Alsace":
                    try:
                         type(PbAlsace)
                         item = db.nodes.create(Region=info[0], Nom=info[1], Adresse=info[2], telephone=info[3])
                         PbAlsace.relationships.create("Infos",item)
                         labelPbinfo.add(item)
                         print(item)
                    except NameError:
                         PbAlsace= db.nodes.create(Pbname="Alsace",Region="Alsace", Nom="", Adresse="", telephone="")
                         labelPbregion.add(PbAlsace)
                         PagesBlanches.relationships.create("Regions",PbAlsace)
                         item = db.nodes.create(Region=info[0], Nom=info[1], Adresse=info[2], telephone=info[3])
                         PbAlsace.relationships.create("Infos",item)
                         labelPbinfo.add(item)
                         print(item)
          
               if info[0] == "Aquitaine":
                    try:
                         type(PbAquitaine)
                         item = db.nodes.create(Region=info[0], Nom=info[1], Adresse=info[2], telephone=info[3])
                         PbAquitaine.relationships.create("Infos",item)
                         labelPbinfo.add(item)

                    except NameError:
                            PbAquitaine= db.nodes.create(Pbname="Aquitaine",Region="Aquitaine", Nom="", Adresse="", telephone="")
                            labelPbregion.add(PbAquitaine)
                            PagesBlanches.relationships.create("Regions",PbAquitaine)
                            item = db.nodes.create(Region=info[0], Nom=info[1], Adresse=info[2], telephone=info[3])
                            PbAquitaine.relationships.create("Infos",item)
                            labelPbinfo.add(item)
                            print(item)
               if info[0] == "Auvergne":
                    try:
                         type(PbAuvergne)
                         item = db.nodes.create(Region=info[0], Nom=info[1], Adresse=info[2], telephone=info[3])
                         PbAuvergne.relationships.create("Infos",item)
                         labelPbinfo.add(item)
                    except NameError:
                         PbAuvergne= db.nodes.create(Pbname="Auvergne",Region="Auvergne", Nom="", Adresse="", telephone="")
                         labelPbregion.add(PbAuvergne)
                         PagesBlanches.relationships.create("Regions",PbAuvergne)
                         item = db.nodes.create(Region=info[0], Nom=info[1], Adresse=info[2], telephone=info[3])
                         PbAuvergne.relationships.create("Infos",item)
                         labelPbinfo.add(item)
                         print(item)
               if info[0] == "Basse-Normandie":

                    try:
                        type(PbBasseNormandie)
                        item = db.nodes.create(Region=info[0], Nom=info[1], Adresse=info[2], telephone=info[3])
                        PbBasseNormandie.relationships.create("Infos",item)
                        labelPbinfo.add(item)
                        print(item)
                    except NameError:
                        PbBasseNormandie= db.nodes.create(Pbname="Basse-Normandie",Region="Basse-Normandie", Nom="", Adresse="", telephone="")
                        labelPbregion.add(PbBasseNormandie)
                        PagesBlanches.relationships.create("Regions",PbBasseNormandie)
                        item = db.nodes.create(Region=info[0], Nom=info[1], Adresse=info[2], telephone=info[3])
                        PbBasseNormandie.relationships.create("Infos",item)
                        labelPbinfo.add(item)

               if info[0] == "Bourgogne":

                    try:
                        type(PbBourgogne)
                        item = db.nodes.create(Region=info[0], Nom=info[1], Adresse=info[2], telephone=info[3])
                        PbBourgogne.relationships.create("Infos",item)
                        labelPbinfo.add(item)
                        print(item)
                    except NameError:
                         PbBourgogne= db.nodes.create(Pbname="Bourgogne",Region="Bourgogne", Nom="", Adresse="", telephone="")
                         labelPbregion.add(PbBourgogne)
                         PagesBlanches.relationships.create("Regions",PbBourgogne)
                         item = db.nodes.create(Region=info[0], Nom=info[1], Adresse=info[2], telephone=info[3])
                         PbBourgogne.relationships.create("Infos",item)
                         labelPbinfo.add(item)
                         print(item)
               if info[0] == "Bretagne":
                    try:
                        type(PbBretagne)
                        item = db.nodes.create(Region=info[0], Nom=info[1], Adresse=info[2], telephone=info[3])
                        PbBretagne.relationships.create("Infos",item)
                        labelPbinfo.add(item)
                        print(item)
                    except NameError:
                         PbBretagne= db.nodes.create(Pbname="Bretagne",Region="Bretagne", Nom="", Adresse="", telephone="")
                         labelPbregion.add(PbBretagne)
                         PagesBlanches.relationships.create("Regions",PbBretagne)
                         item = db.nodes.create(Region=info[0], Nom=info[1], Adresse=info[2], telephone=info[3])
                         PbBretagne.relationships.create("Infos",item)
                         labelPbinfo.add(item)
                         print(item)

               if info[0] == "Centre":
                    try:
                        type(PbCentre)
                        item = db.nodes.create(Region=info[0], Nom=info[1], Adresse=info[2], telephone=info[3])
                        PbCentre.relationships.create("Infos",item)
                        labelPbinfo.add(item)
                        print(item)
                    except NameError:  
                         PbCentre= db.nodes.create(Pbname="Centre",Region="Centre", Nom="", Adresse="", telephone="")
                         labelPbregion.add(PbCentre)
                         PagesBlanches.relationships.create("Regions",PbCentre)
                         item = db.nodes.create(Region=info[0], Nom=info[1], Adresse=info[2], telephone=info[3])
                         PbCentre.relationships.create("Infos",item)
                         labelPbinfo.add(item)
                         print(item)
               if info[0] == "Champagne-Ardenne":
                    try:
                        type(PbChampagneArdenne)
                        item = db.nodes.create(Region=info[0], Nom=info[1], Adresse=info[2], telephone=info[3])
                        PbChampagneArdenne.relationships.create("Infos",item)
                        labelPbinfo.add(item)
                        print(item)
                    except NameError:
                         PbChampagneArdenne= db.nodes.create(Pbname="Champagne-Ardenne",Region="Champagne-Ardenne", Nom="", Adresse="", telephone="")
                         labelPbregion.add(PbChampagneArdenne)
                         PagesBlanches.relationships.create("Regions",PbChampagneArdenne)
                         item = db.nodes.create(Region=info[0], Nom=info[1], Adresse=info[2], telephone=info[3])
                         PbChampagneArdenne.relationships.create("Infos",item)
                         labelPbinfo.add(item)
                         print(item)          
               if info[0] == "Corse":
                    try:
                        type(PbCorse)
                        item = db.nodes.create(Region=info[0], Nom=info[1], Adresse=info[2], telephone=info[3])
                        PbCorse.relationships.create("Infos",item)
                        labelPbinfo.add(item)
                        print(item)
                    except NameError:
                         PbCorse= db.nodes.create(Pbname="Corse",Region="Corse", Nom="", Adresse="", telephone="")
                         labelPbregion.add(PbCorse)
                         PagesBlanches.relationships.create("Regions",PbCorse)
                         item = db.nodes.create(Region=info[0], Nom=info[1], Adresse=info[2], telephone=info[3])
                         PbCorse.relationships.create("Infos",item)
                         labelPbinfo.add(item)
                         print(item)
               if info[0] == "Franche-Comté":
                    try:
                        type(PbFrancheComt)
                        item = db.nodes.create(Region=info[0], Nom=info[1], Adresse=info[2], telephone=info[3])
                        PbFrancheComt.relationships.create("Infos",item)
                        labelPbinfo.add(item)
                        print(item)
                    except NameError:
                        PbFrancheComt= db.nodes.create(Pbname="Franche-Comté",Region="Franche-Comté", Nom="", Adresse="", telephone="")
                        labelPbregion.add(PbFrancheComt)
                        PagesBlanches.relationships.create("Regions",PbFrancheComt)
                        item = db.nodes.create(Region=info[0], Nom=info[1], Adresse=info[2], telephone=info[3])
                        PbFrancheComt.relationships.create("Infos",item)
                        labelPbinfo.add(item)
                        print(item)
               if info[0] == "Haute-Normandie":
                    try:
                        type(PbHauteNormandie)
                        item = db.nodes.create(Region=info[0], Nom=info[1], Adresse=info[2], telephone=info[3])
                        PbHauteNormandie.relationships.create("Infos",item)
                        labelPbinfo.add(item)
                        print(item)
                    except NameError:
                        PbHauteNormandie= db.nodes.create(Pbname="Haute-Normandie",Region="Haute-Normandie", Nom="", Adresse="", telephone="")
                        labelPbregion.add(PbHauteNormandie)
                        PagesBlanches.relationships.create("Regions",PbHauteNormandie)
                        item = db.nodes.create(Region=info[0], Nom=info[1], Adresse=info[2], telephone=info[3])
                        PbHauteNormandie.relationships.create("Infos",item)
                        labelPbinfo.add(item)
                        print(item)
               if info[0] == "Île-de-France":
                    try:
                        type(PbiledeFrance)
                        item = db.nodes.create(Region=info[0], Nom=info[1], Adresse=info[2], telephone=info[3])
                        PbiledeFrance.relationships.create("Infos",item)
                        labelPbinfo.add(item)
                        print(item)
                    except NameError:
                        PbiledeFrance= db.nodes.create(Pbname="Île-de-France",Region="Île-de-France", Nom="", Adresse="", telephone="")
                        labelPbregion.add(PbiledeFrance)
                        PagesBlanches.relationships.create("Regions",PbiledeFrance)
                        item = db.nodes.create(Region=info[0], Nom=info[1], Adresse=info[2], telephone=info[3])
                        PbiledeFrance.relationships.create("Infos",item)
                        labelPbinfo.add(item)
                        print(item)
               if info[0] == "Languedoc-Roussillon":
                    try:
                        type(PbLanguedocRoussillon)
                        item = db.nodes.create(Region=info[0], Nom=info[1], Adresse=info[2], telephone=info[3])
                        PbLanguedocRoussillon.relationships.create("Infos",item)
                        labelPbinfo.add(item)
                        print(item)
                    except NameError:
                        PbLanguedocRoussillon= db.nodes.create(Pbname="Languedoc-Roussillon",Region="Languedoc-Roussillon", Nom="", Adresse="", telephone="")
                        labelPbregion.add(PbLanguedocRoussillon)
                        PagesBlanches.relationships.create("Regions",PbLanguedocRoussillon)
                        item = db.nodes.create(Region=info[0], Nom=info[1], Adresse=info[2], telephone=info[3])
                        PbLanguedocRoussillon.relationships.create("Infos",item)
                        labelPbinfo.add(item)
                        print(item)
               if info[0] == "Limousin":
                    try:
                         type(PbLimousin)
                         item = db.nodes.create(Region=info[0], Nom=info[1], Adresse=info[2], telephone=info[3])
                         PbLimousin.relationships.create("Infos",item)
                         labelPbinfo.add(item)
                         print(item)
                    except NameError:
                         PbLimousin= db.nodes.create(Pbname="Limousin",Region="Limousin", Nom="", Adresse="", telephone="")
                         labelPbregion.add(PbLimousin)
                         PagesBlanches.relationships.create("Regions",PbLimousin)
                         item = db.nodes.create(Region=info[0], Nom=info[1], Adresse=info[2], telephone=info[3])
                         PbLimousin.relationships.create("Infos",item)
                         labelPbinfo.add(item)
                         print(item)


               if info[0] == "Lorraine":
                    try:
                        type(PbLorraine)
                        item = db.nodes.create(Region=info[0], Nom=info[1], Adresse=info[2], telephone=info[3])
                        PbLorraine.relationships.create("Infos",item)
                        labelPbinfo.add(item)
                        print(item)
                    except NameError:
               
                        PbLorraine= db.nodes.create(Pbname="Lorraine",Region="Lorraine", Nom="", Adresse="", telephone="")
                        labelPbregion.add(PbLorraine)
                        PagesBlanches.relationships.create("Regions",PbLorraine)
                        item = db.nodes.create(Region=info[0], Nom=info[1], Adresse=info[2], telephone=info[3])
                        PbLorraine.relationships.create("Infos",item)
                        labelPbinfo.add(item)
                        print(item)

               if info[0] == "Midi-Pyrénées":
                    try:
                        type(PbMidiPyrnes)
                        item = db.nodes.create(Region=info[0], Nom=info[1], Adresse=info[2], telephone=info[3])
                        PbMidiPyrnes.relationships.create("Infos",item)
                        labelPbinfo.add(item)
                        print(item)
                    except NameError:
                        PbMidiPyrnes= db.nodes.create(Pbname="Midi-Pyrénées",Region="Midi-Pyrénées", Nom="", Adresse="", telephone="")
                        labelPbregion.add(PbMidiPyrnes)
                        PagesBlanches.relationships.create("Regions",PbMidiPyrnes)
                        item = db.nodes.create(Region=info[0], Nom=info[1], Adresse=info[2], telephone=info[3])
                        PbMidiPyrnes.relationships.create("Infos",item)
                        labelPbinfo.add(item)
                        print(item)

               if info[0] == "Nord-Pas-de-Calais":
                    try:
                        type(PbNordPasdeCalais)
                        item = db.nodes.create(Region=info[0], Nom=info[1], Adresse=info[2], telephone=info[3])
                        PbNordPasdeCalais.relationships.create("Infos",item)
                        labelPbinfo.add(item)
                        print(item)
                    except NameError:
                        PbNordPasdeCalais= db.nodes.create(Pbname="Nord-Pas-de-Calais",Region="Nord-Pas-de-Calais", Nom="", Adresse="", telephone="")
                        labelPbregion.add(PbNordPasdeCalais)
                        PagesBlanches.relationships.create("Regions",PbNordPasdeCalais)
                        item = db.nodes.create(Region=info[0], Nom=info[1], Adresse=info[2], telephone=info[3])
                        PbNordPasdeCalais.relationships.create("Infos",item)
                        labelPbinfo.add(item)
                        print(item)
               if info[0] == "Pays de la Loire":
                    try:
                        type(PbPaysdelaLoire)
                        item = db.nodes.create(Region=info[0], Nom=info[1], Adresse=info[2], telephone=info[3])
                        PbPaysdelaLoire.relationships.create("Infos",item)
                        labelPbinfo.add(item)
                        print(item)

                    except NameError:
                        PbPaysdelaLoire= db.nodes.create(Pbname="Pays de la Loire",Region="Pays de la Loire", Nom="", Adresse="", telephone="")
                        labelPbregion.add(PbPaysdelaLoire)
                        PagesBlanches.relationships.create("Regions",PbPaysdelaLoire)
                        item = db.nodes.create(Region=info[0], Nom=info[1], Adresse=info[2], telephone=info[3])
                        PbPaysdelaLoire.relationships.create("Infos",item)
                        labelPbinfo.add(item)
                        print(item)

               if info[0] == "Picardie":
                    try:
                       type(PbPicardie)
                       item = db.nodes.create(Region=info[0], Nom=info[1], Adresse=info[2], telephone=info[3])
                       PbPicardie.relationships.create("Infos",item)
                       labelPbinfo.add(item)
                       print(item)
                    except NameError:
                       PbPicardie= db.nodes.create(Pbname="Picardie",Region="Picardie", Nom="", Adresse="", telephone="")
                       labelPbregion.add(PbPicardie)
                       PagesBlanches.relationships.create("Regions",PbPicardie)
                       item = db.nodes.create(Region=info[0], Nom=info[1], Adresse=info[2], telephone=info[3])
                       PbPicardie.relationships.create("Infos",item)
                       labelPbinfo.add(item)
                       print(item)

               if info[0] == "Poitou-Charentes":
                    try:
                        type(PbPoitouCharentes)
                        item = db.nodes.create(Region=info[0], Nom=info[1], Adresse=info[2], telephone=info[3])
                        PbPoitouCharentes.relationships.create("Infos",item)
                        labelPbinfo.add(item)
                        print(item)
                    except NameError:
                        PbPoitouCharentes= db.nodes.create(Pbname="Poitou-Charentes",Region="Poitou-Charentes", Nom="", Adresse="", telephone="")
                        labelPbregion.add(PbPoitouCharentes)
                        PagesBlanches.relationships.create("Regions",PbPoitouCharentes)
                        item = db.nodes.create(Region=info[0], Nom=info[1], Adresse=info[2], telephone=info[3])
                        PbPoitouCharentes.relationships.create("Infos",item)
                        labelPbinfo.add(item)
                        print(item)
               if info[0] == "Provence-Alpes-Côte+d'Azur":

                    try:
                        type(PbProvenceAlpesCotedAzur)
                        item = db.nodes.create(Region=info[0], Nom=info[1], Adresse=info[2], telephone=info[3])
                        PbProvenceAlpesCotedAzur.relationships.create("Infos",item)
                        labelPbinfo.add(item)
                        print(item)
                    except NameError:
                        PbProvenceAlpesCotedAzur= db.nodes.create(Pbname="Provence-Alpes-Côte+d'Azur",Region="Provence-Alpes-Côte+d'Azur", Nom="", Adresse="", telephone="")
                        labelPbregion.add(PbProvenceAlpesCotedAzur)
                        PagesBlanches.relationships.create("Regions",PbProvenceAlpesCotedAzur)
                        item = db.nodes.create(Region=info[0], Nom=info[1], Adresse=info[2], telephone=info[3])
                        PbProvenceAlpesCotedAzur.relationships.create("Infos",item)
                        labelPbinfo.add(item)
                        print(item)

               if info[0] == "Rhône-Alpes":
                    try:
                        type(PbRhoneAlpes)
                        item = db.nodes.create(Region=info[0], Nom=info[1], Adresse=info[2], telephone=info[3])
                        PbRhoneAlpes.relationships.create("Infos",item)
                        labelPbinfo.add(item)
                        print(item)
                    except NameError:
                        PbRhoneAlpes= db.nodes.create(Pbname="Rhône-Alpes",Region="Rhône-Alpes", Nom="", Adresse="", telephone="")
                        labelPbregion.add(PbRhoneAlpes)
                        PagesBlanches.relationships.create("Regions",PbRhoneAlpes)
                        item = db.nodes.create(Region=info[0], Nom=info[1], Adresse=info[2], telephone=info[3])
                        PbRhoneAlpes.relationships.create("Infos",item)
                        labelPbinfo.add(item)
                        print(item)
               if info[0] == "Guadeloupe":
                    try:
                        type(PbGuadeloupe)
                        item = db.nodes.create(Region=info[0], Nom=info[1], Adresse=info[2], telephone=info[3])
                        PbGuadeloupe.relationships.create("Infos",item)
                        labelPbinfo.add(item)
                        print(item)
                    except NameError:
                        PbGuadeloupe= db.nodes.create(Pbname="Guadeloupe",Region="Guadeloupe", Nom="", Adresse="", telephone="")
                        labelPbregion.add(PbGuadeloupe)
                        PagesBlanches.relationships.create("Regions",PbGuadeloupe)
                        item = db.nodes.create(Region=info[0], Nom=info[1], Adresse=info[2], telephone=info[3])
                        PbGuadeloupe.relationships.create("Infos",item)
                        labelPbinfo.add(item)
                        print(item)
               if info[0] == "Guyane":
                    try:
                        type(PbGuyane)
                        item = db.nodes.create(Region=info[0], Nom=info[1], Adresse=info[2], telephone=info[3])
                        PbGuyane.relationships.create("Infos",item)
                        labelPbinfo.add(item)
                        print(item)
                    except NameError:
                        PbGuyane= db.nodes.create(Pbname="Guyane",Region="Guyane", Nom="", Adresse="", telephone="")
                        labelPbregion.add(PbGuyane)
                        PagesBlanches.relationships.create("Regions",PbGuyane)
                        item = db.nodes.create(Region=info[0], Nom=info[1], Adresse=info[2], telephone=info[3])
                        PbGuyane.relationships.create("Infos",item)
                        labelPbinfo.add(item)
                        print(item)
               if info[0] == "La+Réunion":
                    try:
                        type(PbLaRunion)
                        item = db.nodes.create(Region=info[0], Nom=info[1], Adresse=info[2], telephone=info[3])
                        PbLaRunion.relationships.create("Infos",item)
                        labelPbinfo.add(item)
                        print(item)
                    except NameError:
                        PbLaRunion= db.nodes.create(Pbname="La+Réunion",Region="La+Réunion", Nom="", Adresse="", telephone="")
                        labelPbregion.add(PbLaRunion)
                        PagesBlanches.relationships.create("Regions",PbLaRunion)
                        item = db.nodes.create(Region=info[0], Nom=info[1], Adresse=info[2], telephone=info[3])
                        PbLaRunion.relationships.create("Infos",item)
                        labelPbinfo.add(item)
                        print(item)
               if info[0] == "Martinique":
                    try:
                        type(PbMartinique)
                        item = db.nodes.create(Region=info[0], Nom=info[1], Adresse=info[2], telephone=info[3])
                        PbMartinique.relationships.create("Infos",item)
                        labelPbinfo.add(item)
                        print(item)
                    except NameError:
                        PbMartinique= db.nodes.create(Pbname="Martinique",Region="Martinique", Nom="", Adresse="", telephone="")
                        labelPbregion.add(PbMartinique)
                        PagesBlanches.relationships.create("Regions",PbMartinique)
                        item = db.nodes.create(Region=info[0], Nom=info[1], Adresse=info[2], telephone=info[3])
                        PbMartinique.relationships.create("Infos",item)
                        labelPbinfo.add(item)
                        print(item)
               if info[0] == "Mayotte":
                    try:
                        type(PbMayotte)
                        item = db.nodes.create(Region=info[0], Nom=info[1], Adresse=info[2], telephone=info[3])
                        PbMayotte.relationships.create("Infos",item)
                        labelPbinfo.add(item)
                        print(item)
                    except NameError:
                        PbMayotte= db.nodes.create(Pbname="Mayotte",Region="Mayotte", Nom="", Adresse="", telephone="")
                        labelPbregion.add(PbMayotte)
                        PagesBlanches.relationships.create("Regions",PbMayotte)
                        item = db.nodes.create(Region=info[0], Nom=info[1], Adresse=info[2], telephone=info[3])
                        PbMayotte.relationships.create("Infos",item)
                        labelPbinfo.add(item)
                        print(item)

            except Exception as e:
                    print(e)



print()
for item in splitengine:
     if item.lower() == "google":
          Fig = Figlet(font='cybermedium')
          print(Fig.renderText('Google Important links'))
          print()


          for glink in googlelink:
            try:
              glink = glink.split("#***#")
    
              item = db.nodes.create(Titre=glink[0], Lien=glink[1], Description=glink[2])
              GoogleurlPlus.relationships.create("Important Link",item)
              labelsiteverified.add(item)
              print(item)
              #s1.relationships.create("Source Url", item)
            except Exception as e:
                    print(e)


          print()
          Fig = Figlet(font='cybermedium')
          print(Fig.renderText('Google Interesting links'))
          print()



          for glink in googlelinkchance:

            try:
              glink = glink.split("#***#")
    
              item = db.nodes.create(Titre=glink[0], Liens=glink[1], Description=glink[2])
              GoogleurlMinus.relationships.create("Valid Link",item)
              labelsitechance.add(item)
              print(item)
              #s1.relationships.create("Source Url", item)
            except Exception as e:

                    print(e)

          print()
          Fig = Figlet(font='cybermedium')
          print(Fig.renderText('Google Important PDF'))
          print()

          for pdf in googlepdf:
            try:
              pdf = pdf.split("#***#")
    
              item = db.nodes.create(Titre=pdf[1],Lien=pdf[0], Description=pdf[1])
              GooglepdfPlus.relationships.create("Pdf Important",item)
              labelpdfverified.add(item)
              print(item)
              #s1.relationships.create("Source File", item)
            except Exception as e:
                    print(e)

          print()
          Fig = Figlet(font='cybermedium')
          print(Fig.renderText('Google Interesting PDF'))
          print()


          for pdf in googlepdfchance:
            try:
              pdf = pdf.split("#***#")
              print(pdf)
              item = db.nodes.create(Titre=pdf[1],Lien=pdf[0], Description=pdf[1])
              GooglepdfMinus.relationships.create("Pdf Valid",item)
              labelpdfchance.add(item)
              print(item)
              #s1.relationships.create("Source File", item)
            except Exception as e:
               print(e)

          print()
          Fig = Figlet(font='cybermedium')
          print(Fig.renderText('Google not parsed'))
          print()
          for spec in googlespecial:
            try:
              item = db.nodes.create(Specname=spec)
              Googlespecialnode.relationships.create("Not handled yet",item)
              labelspecialres.add(item)
              print(item)
              #s1.relationships.create("Source item", item)
            except Exception as e:
                    print(e)

          print()
          Fig = Figlet(font='cybermedium')
          print(Fig.renderText('Google Pictures'))
          print()
          for fileimg in googleimg:

            try:
              item = db.nodes.create(Filename=fileimg)
              Googleimgnode.relationships.create("Picture",item)
              labelIMG.add(item)
              print(item)
              #s1.relationships.create("Source File", item)
            except Exception as e:
                    print(e)




print()
for item in splitengine:
     if item.lower() == "bing":
          Fig = Figlet(font='cybermedium')
          print(Fig.renderText('Bing Important Links'))
          print()

          for blink in binglink:

            try:
              blink = blink.split("#***#")
              item = db.nodes.create(Titre=blink[0], Lien=blink[1], Description=blink[2])
              BingurlPlus.relationships.create("Important Link",item)
              labelsiteverified.add(item)
              print(item)
              #s1.relationships.create("Source Url", item)
            except Exception as e:
                    print(e)


          print()
          Fig = Figlet(font='cybermedium')
          print(Fig.renderText('Bing Interesting Links'))
          print()



          for blink in binglinkchance:

            try:
              blink = blink.split("#***#")
              item = db.nodes.create(Titre=blink[0], Lien=blink[1], Description=blink[2])
              BingurlMinus.relationships.create("Valid Pdf",item)
              labelsitechance.add(item)
              print(item)
              #s1.relationships.create("Source Url", item)
            except Exception as e:

                    print(e)

          print()
          Fig = Figlet(font='cybermedium')
          print(Fig.renderText('Bing Important PDF'))
          print()

          for pdf in bingpdf:
            try:
              pdf = pdf.split("#***#")
              item = db.nodes.create(Titre=pdf[1],Lien=pdf[0], Description=pdf[1])
              BingpdfPlus.relationships.create("Pdf Important",item)
              labelpdfverified.add(item)
              print(item)
              #s1.relationships.create("Source File", item)
            except Exception as e:
                    print(e)

          print()
          Fig = Figlet(font='cybermedium')
          print(Fig.renderText('Bing Interesting PDF'))
          print()


          for pdf in bingpdfchance:
            try:
              pdf = pdf.split("#***#")
              item = db.nodes.create(Titre=pdf[1],Lien=pdf[0], Description=pdf[1])
              BingpdfMinus.relationships.create("Pdf Valid",item)
              labelpdfchance.add(item)
              print(item)
              #s1.relationships.create("Source File", item)
            except Exception as e:
               print(e)
          print()
          Fig = Figlet(font='cybermedium')
          print(Fig.renderText('Bing not parsed'))
          print()
          for spec in bingspecial:
            try:
              item = db.nodes.create(Specname=spec)
              Bingspecialnode.relationships.create("Not handled yet",item)
              labelspecialres.add(item)
              print(item)
              #s1.relationships.create("Source item", item)
            except Exception as e:
                    print(e)

          print()
          Fig = Figlet(font='cybermedium')
          print(Fig.renderText('Bing picture'))
          print()
          print("google actually..")
          print()
          for fileimg in bingimg:

            try:
              item = db.nodes.create(Filename=fileimg)
              Bingimgnode.relationships.create("Picture",item)
              labelIMG.add(item)
              print(item)
              #s1.relationships.create("Source File", item)
            except Exception as e:
                    print(e)


for item in splitengine:
     if item.lower() == "yahoo":
          print()
          Fig = Figlet(font='cybermedium')
          print(Fig.renderText('Yahoo Important Links'))
          print()

          for ylink in yahoolink:

            try:
              ylink = ylink.split("#***#")
              item = db.nodes.create(Titre=ylink[0], Lien=ylink[1], Description=ylink[2])
              YahoourlPlus.relationships.create("Important Link",item)
              labelsiteverified.add(item)
              print(item)
              #s1.relationships.create("Source Url", item)
            except Exception as e:
                    print(e)


          print()
          Fig = Figlet(font='cybermedium')
          print(Fig.renderText('Yahoo Interesting Links'))
          print()



          for ylink in yahoolinkchance:

            try:
              ylink = ylink.split("#***#")
              item = db.nodes.create(Titre=ylink[0], Lien=ylink[1], Description=ylink[2])
              YahoourlMinus.relationships.create("Valid Link",item)
              labelsitechance.add(item)
              print(item)
              #s1.relationships.create("Source Url", item)
            except Exception as e:

                    print(e)

          print()
          Fig = Figlet(font='cybermedium')
          print(Fig.renderText('Yahoo Important PDF'))
          print()

          for pdf in yahoopdf:
            try:
              pdf = pdf.split("#***#")
              item = db.nodes.create(Titre=pdf[1],Lien=pdf[0], Description=pdf[1])
              YahoopdfPlus.relationships.create("Pdf Important",item)
              labelpdfverified.add(item)
              print(item)
              #s1.relationships.create("Source File", item)
            except Exception as e:
                    print(e)

          print()
          Fig = Figlet(font='cybermedium')
          print(Fig.renderText('Yahoo Interesting PDF'))
          print()


          for pdf in yahoopdfchance:
            try:
              pdf = pdf.split("#***#")
              item = db.nodes.create(Titre=pdf[1],Lien=pdf[0], Description=pdf[1])
              YahoopdfMinus.relationships.create("Pdf Valid",item)
              labelpdfchance.add(item)
              print(item)
              #s1.relationships.create("Source File", item)
            except Exception as e:
               print(e)

          print()
          Fig = Figlet(font='cybermedium')
          print(Fig.renderText('Yahoo not parsed'))
          print("")

          for spec in yahoospecial:
            try:
              item = db.nodes.create(Specname=spec)
              Yahoospecialnode.relationships.create("Not handled yet",item)
              labelspecialres.add(item)
              print(item)
              #s1.relationships.create("Source item", item)
            except Exception as e:
                    print(e)
          Fig = Figlet(font='cybermedium')
          print(Fig.renderText('Yahoo Picture'))
          print()
          print("Still google..")
          print("")
          for fileimg in yahooimg:

            try:
              item = db.nodes.create(Filename=fileimg)
              Yahooimgnode.relationships.create("Picture",item)
              labelIMG.add(item)
              print(item)
              #s1.relationships.create("Source File", item)
            except Exception as e:
                    print(e)

          print()
Fig = Figlet(font='cybermedium')
print(Fig.renderText('=The End='))
print()

