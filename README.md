
# EyeOnThreat
EyeOnThreat&trade; is a service to gathering, classify, enrich and distribute or give access to various types of intelligence information, collected by multiple and non-homogeneous sources, related to consolidated or emerging cyber threats

Project home page: https://www.eyeonthre.at

Entity
------------

EyeOnThreat&trade; is able to extract a number of entities used to contextualize and classify cyber threat intelligence information. Each single information is enriched, classified and transformed to provide more details that can be used as an Indicator of Compromise (IoC) and more generally as actionable intelligence. Every collected data is saved in a single location represented by the EyeOnThreat Global Threat Repository and made available throught EyeOnThreat&trade; Services: 

* **IP**: IP addresses referable to threats and/or malicious actors
* **Domain**: Domains used to host and distribute malware, unreliable domains
* **URL**: URLs known as phishing sites, websites that hosts Exploit Kits
* **E-mail**: Emails used for spam or phishing campaigns, compromised email accounts, email used to distribute malspam
* **Credit Card**: Stolen credit cards that are sold on blackmarkets or published on forums
* **Hash**: File recognized as malicious and related to old/new threats or exploit kits

RestFull API
------------
The access to the information present in the Global Threat Database is guaranteed in a rapid and reliable way by a RESTful API system:

* **Cyber Threat Feed**: 
Feed mode provides access to a dataset of information in CSV format, useful for the classification and prioritization of threats in automated detection and blocking mechanisms

* **Cyber Threat Hunting**: 
Hunting mode provides the possibility to search for information and indicators present stored in the database. Through this mode it is possible to investigate on a given entity among those stored, looking for clues useful to detect threats.

Installation
------------
To install EyeOnThreat Python library:

    git clone https://github.com/L-TMS-CERT/EyeOnThreat.git
    cd XXXXXXXXXXXXXXXXXXXX

Usage Example
------------

Import Library:

    from eyeonthreat import threat_aggregator

Get API Token :

> NOTE: This method allow you to retrive the TOKEN used by EyeOnThreat Services.

    auth = threat_aggregator.Authentication()
    auth.getAuthToken(user,passwd)
    
    Response:
    
    {
        "data": {"token": "ImKlcnRhLOpwdzo9hkplc2ki.DA8xyg.3TidfdlOkGwpKNsfdsTx8Ht-12sIze6rQ"},
        "service": {"status": "valid"}
    }
    
    
Services Initalization:

    feed = threat_aggregator.Feed(token)
    hunting = threat_aggregator.Hunting(token)
    info = threat_aggregator.Info(token)

Services Example:

> Retrive Threat Feed

    feed.getFeed() # Retrive All indicator for the last 24h
    feed.getFeedEntity("ip") # Retrive IP Type indicator for the last 24h
    feed.getFeedEntity("url") # Retrive URL Type indicator for the last 24h
    feed.getFeedCategory("ip","Malware") # Retrive Malware IP Type indicator for the last 24h 
    feed.getFeedSubCategory("ip","Malware","CnC") # Retrive Malware IP Type indicator for the last 24h where subcategory is CnC
    
> Search Threat Information

    hunting.searchIPv4("value") # Search Information about IP
    hunting.searchURL("value") # Search Information about Domain
    hunting.searchURL("value") # Search Information about URL
    hunting.searchHash("value") # Search Information about HASH
    hunting.searchEmail("value") # Search Information about EMAIL
   
> Info 

    info.getCategories() # Returns a list of Category and Subcategory that can be used to filter a csv feed

USAGE LIMITATIONS
------------
  
Documentation
-------------
Full API Documentation is available at https://www.eyeonthre.at/site/api.html .
