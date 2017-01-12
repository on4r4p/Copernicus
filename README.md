#Copernicus


Osint tool to get results from Google, Bing, Yahoo,British Telecom,PagesBlanches,PaginasBlancas,lullar, about people.

1. No Smeging Api key required.

2. Will not get your ip banned.

3. Get images from google

4. Filter each websites results to be sure to retreive what we looking for . (including pdf)

5. If strict search result failed for one website try another finding method helped by a list of words provided by user.

6. Search in french city specified by user for family name ,adresses,phone numbers.
Search in all regions in France for family name ,adresses,phone numbers.
 Search in all cities in France with more than 10 thousand inhabitants for family name ,adresses,phone numbers (never tested  yet suspected to block your ip)
 
7. Search in United-Kingdom city specified by user for family name ,adresses,phone numbers.
 Search in all cities in United-Kingdom for family name ,adresses,phone numbers.
 
8. Search in spanish city specified by user for family name ,adresses,phone numbers.
 Search in all cities in Spain for family name ,adresses,phone numbers.
 
9. Search social relations with Lullar if email is provided
 
10. Then make a graph in neo4j .

^(Consider downloading [Linkification](https://addons.mozilla.org/fr/firefox/addon/linkification/)  for Firefox or [Clickable links](https://chrome.google.com/webstore/detail/clickable-links/mgamelhnfokapndfdodnmfiningckjia) for Chrome if you want to work directly in neo4j .)^




![](http://img15.hostingpics.net/pics/938427copernicus0.png) 

 - usage: copernicus.py [-h] [-e 'ENGINE'] [-i  'True/False']  [-l 'LANG'] [-pb 'True/False'] [-s 'NAME'] [-f
   FAMILY NAME] [-a OPTION] [-c CITY] [-fa TRUE-FALSE] [-m EMAIL]

>./copernicus.py -e google,yahoo,pagesblanches,lullar -s "Someone you looking for" -f "looking for" -c paris -a lot,of,words,to,add,here,in,relation,with,the,people,you,search,if,you,want,more,results,"dont forget to quote space",doh  -pb true -i true -m some@mail.something
   
###To do list:
- Rewrite all this shit
- Add Install setup 
-   ~~Add whitepage engine for fr.~~
-   ~~Add whitepage engine for uk.~~
-   ~~Add whitepage engine for es.~~
-   Add whitepage engine for ru.
-   Add whitepage engine for usa.
-  Add ability to save current session and continue where it stopped in  case of uncaught error.
-  Add graphml , gephi , cytoscape ,export format .
-  Add image search for yahoo and bing
- ~~Add Email search~~
- Add Search results function for other file format 
- Add Search by language in Bing
- Add nickname guessing function.
- Add email guessing function.
- ~~Add FullAuto mode for PagesBlanches (testings all cities with more than 10 000 inhabitants )~~

*Wrote this cause of the maltego community limitation (12 results only)*
