#Copernicus
 
 

Osint tool to get results from Google, Bing, Yahoo,British Telecom,Pages Blanches,Paginas Blancas,SpravKaru,Das Telefon Bush,YellowPages,Instagram,Twitter,Youtube,WeChat,GooglePlus,Linkedin,Myspace,Flickr,Foursquare,PhotoBucket,Picturetrail,Wayn,Dek-d,Pinterest,Badoo,Blogger,Tumblr,Skype,Facebook about peoples.

1. No Smeging Api key required.

2. Will not get your ip banned.

3. Get images from Google,Bing,Yahoo

4. Filter each websites results to be sure to retreive what we looking for . (including pdf)

5. If strict search result failed for one website try another finding method helped by a list of words provided by user.

6. Catch all emails found in webpages .

7. Search in a french's city specified by user for family name ,adresses,phone numbers.
Search  all regions in France for family name ,adresses,phone numbers.
 Search  all cities in France with more than 10 thousand inhabitants for family name ,adresses,phone numbers (never tested  yet suspected to block your ip)
 
8. Search in United-Kingdom a city specified by user for family name ,adresses,phone numbers.
 Search  all cities in United-Kingdom for family name ,adresses,phone numbers.
 
9. Search in a spanish's city specified by user for family name ,adresses,phone numbers.
 Search all cities in Spain for family name ,adresses,phone numbers.
 
10. Search in a russian city's specified by user for family name ,adresses,phone numbers.
 Search all cities in Russia for family name ,adresses,phone numbers.
 
11. Search in an american's city specified by user for family name ,adresses,phone numbers.
 Search all States of Usa for family name ,adresses,phone numbers. 
 
12. Search german's city specified by user for family name ,adresses,phone numbers.
 Search all cities in Germany for family name ,adresses,phone numbers. 
 
13. Search social relations with Lullar() if email is provided
(Ask Instagram,Twitter,Youtube,WeChat,GooglePlus,Linkedin,Myspace,Flickr,Foursquare,PhotoBucket,Picturetrail,Wayn,Dek-d,Pinterest,Badoo,Blogger,Tumblr)

14. Generate all possible combinations of mails adresses then check if they exist . If they exist , will ask Lullar() .

15. Search in Skype Directory (can use results to guess emails)
 
16. Search in Facebook Directory  (can use results to guess emails)

17. Search in Darksearch.com for onion links

18. Search in Irc logs from various servers .
 
19. Then make a graph in neo4j .

^(Consider downloading [Linkification](https://addons.mozilla.org/fr/firefox/addon/linkification/)  for Firefox or [Clickable links](https://chrome.google.com/webstore/detail/clickable-links/mgamelhnfokapndfdodnmfiningckjia) for Chrome if you want to work directly in neo4j .)^

![ ](http://img11.hostingpics.net/pics/139823resc.png  "search engine")


![ ](https://s24.postimg.org/3y8y56wcl/piximg.jpg  "gimg")


![ ](http://img11.hostingpics.net/pics/384186Captcha.png  "yellowpages captcha bypass")



![](http://img15.hostingpics.net/pics/938427copernicus0.png) 

		- usage: copernicus.py [-h] [-e Engine] [-l LANG] [-c2e]
		                     [-c2w ] [-f2e] [-n2w] [-sm ] [-sk LOGIN-PASSWORD] [-sf LOGIN-PASSWORD] [-sa 'ALIAS'] [-s 'NAME'] [-f FAMILY NAME]
		                     [-a OPTION] [-c CITY] [-i ] [-m EMAIL]
		                     [-gm OPTION] [-fa TRUE-FALSE] [-LS] [-t TIME]
		- optional arguments:
		
		       -h, --help            show this help message and exit
		       
		       -e Engine, Engine Use specific search engine: -e yahoo,bing
		       
		       -l LANG, Country : en,zh-CN,es,ar,pt,ja,ru,fr,de...
		       
		       -c2e  Only use the city arg with search engine
		       
		       -c2w Only use the city arg with whitepages
		       
		       -f2e Search with full name not only Family name with skye or facebook 
		       -n2w Dont only use Family name with whitepages use fullname instead
		       
		       -sm , --scrapmail get all emails from results
		       
		       -sk LOGIN-PASSWORD,  Search Family name in Skype Directory.
		       
		       -sf LOGIN-PASSWORD,  Search Family name in Facebook Directory.

		       -sa 'ALIAS', Alias to Search
		       
		       -s 'NAME', Name to Search
		       
		       -f FAMILY NAME, --family FAMILY NAME
		       
		       -a OPTION, Word1,Word2,Word3
		       
		       -c CITY, --city   Specify city
		       
		       -i , Search and download pictures too
		       
		       -m EMAIL,  will ask lullar.com about it
		       
		       -gm OPTION, --guessmail OPTION
		        
		       -t TIME, --timesleep Resting time before each requests ( random between 42 to x where x is your choice)
		        
		       -gm OPTION Find all emails permutation and check if they exist.
		       	 Options:
						 leet for l33tsp34k
						  .-_ are chosen separators
						  23,42 People often add birthdate/postalcode/fav at the end number try to add some
						 badidea0000 to test all combinations from 0 to 9999 (even 2 digits is a bad idea). 
						 Another bad idea is the 'all' option which try over 4500 emails providers.
						 top10 option will use 10 most used provider 
						 The best option here is to add some domain yourself like this :
						 -gm @emailprovider1.com,@emailprovider2.ru
						 
						 Ex : -gm ._-,badidea00,leet,64,1984,666,all,top10,@emailprovider1.com,@emailprovider2.ru
						 
						
		           
		       -fa TRUE-FALSE, Take more than 3 hours can get your ip banned
		
		       -LS, --lastsession  Load last aborded sessions
		
	     
	
	
	
	>./copernicus.py -e google,yahoo,pagesblanches,lullar,skype,facebook -s "name+familyname" -f "Family name" -c paris -a lot,of,words,to,add,here,in,relation,with,the,people,you,search,if,you,want,more,results,"dont forget to quote space",doh   -i true -m some@mail.something -c2w  -gm .-,top10,leet,666,@postmaster.co.uk,@openmailbox.org -sk SkypeLogin,SkypePassword -sf FacebookLogin,FacebookPassword -f2e -n2w
	   
###To do list:
- Rewrite all this shit
- Add Install setup 
- ~~Add Irc Logs search.~~
- Add TinyEye search engine to compare with images results from Skype's avatar, Facebook ,and the first ten pictures from google bing  and yahoo.
-  Add graphml , mtgx export format .
-  ~~Add onion search engine~~
-   ~~Add whitepage engine for fr.~~
-   ~~Add whitepage engine for uk.~~
-   ~~Add whitepage engine for es.~~
-   ~~Add whitepage engine for ru.~~
-   ~~Add whitepage engine for usa.~~
-   ~~Add whitepage engine for ger.~~=
-   ~~Add Captcha solver for yellowpages.com.~~
-   ~~Add ability to choose to use city for engine or whitePages.~~
-   ~~Add ability to save current session and continue where it stopped in  case of uncaught error.~~
-  ~~Add image search for yahoo and bing~~
- ~~Add Email search~~
- ~~Add Search results function for other file format.~~
- ~~Add nickname guessing function.~~(Canceled unreliable |Skype def or Facebook has better chances to find nickname or Alias)
- ~~Save final results session.~~
- ~~Add Skype search~~
- ~~Add Facebook search~~
- ~~Add webmii search~~ (Canceled results similar to Copernicus.py)
- ~~Add nickname searching function (instead of only using people's names.)~~
- ~~Check Lullar results for false positive.~~
- ~~Add email guessing function.~~
- ~~Add email checking function.~~
- ~~catch all mails found in results~~
- ~~Add FullAuto mode for PagesBlanches (testings all cities with more than 10 000 inhabitants )~~

*Wrote this cause of the maltego community limitation (12 results only)*