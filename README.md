
# EyeOnThreat&trade;
EyeOnThreat™ provides Feed or API access to a relevant part of Cyber Threat Intelligence Information gathered, analyzed and released by:

* Lutech ThreatOculus™ threat researchers and analysts team
* Lutech ThreatCure™ breach detection and incident response team
* Lutech ethical hacking and vulnerability research team
* Multiple open and private sources

The possibility to access a contextualized and enriched database of threats through a single and reliable channel is a fundamental element in a cyber security strategy. Knowledge of where risks are created and evolve, is essential in a process of verification and validation, usally performed by structures facilities like SOCs and CERTs. It's a service for gathering, classifying, enriching and distributing or giving access to various types of intelligence information, collected by multiple and non-homogenous sources, related to consolidated or emerging cyber threats. 

Project home page: https://www.eyeonthre.at

Entity
------------

EyeOnThreat&trade; is able to extract a number of entities used to contextualize and classify cyber threat intelligence information. Each single information is enriched, classified and transformed to provide more details that can be used as an Indicator of Compromise (IoC) and more generally as actionable intelligence. Every collected data is saved in a single location represented by the EyeOnThreat Global Threat Repository and made available throught EyeOnThreat&trade; Services: 

* **IP**: IP addresses referable to threats and/or malicious actors
* **Domain**: Domains used to host and distribute malware, unreliable domains or involved in other threats
* **URL**: URLs known as phishing sites, websites that hosts Exploit Kits or involved in other threats
* **E-mail**: Emails used for spam, phishing or malware distribution campaigns
* **User Credential**: Compromised emails or accounts 
* **Credit Card**: Stolen credit cards that are sold on blackmarkets, published on forums or discovered in other sources
* **Malware Sample**: File recognized as malicious and related to old/new threats or exploit kits 
* **Exploit Kit**: Up-to-date informations about exploit kits 

RestFul API
------------
The access to the information present in the Global Threat Database is guaranteed in a rapid and reliable way by a RESTful API system:

* **Cyber Threat Feed**: 
Feed mode provides access to a dataset of information in CSV format, useful for the classification and prioritization of threats in automated detection and blocking mechanisms.

* **Cyber Threat Hunting**: 
Hunting mode provides the possibility to search for information and indicators stored in the database. Through this mode it is possible to investigate on a given entity among those stored, looking for clues useful to detect threats.

Requirements
------------

To use EyeOnThreat you need to have a valid API token. You can request a free token with usage limits here https://www.eyeonthre.at/site/#try .

To request a full access to api services contact us at info@lutech[.]it

Usage
------------
To use EyeOnThreat Python library:

    git clone https://github.com/L-TMS-CERT/EyeOnThreat.git


Import Library:

    import eyeonthreat

Get API Token :

> NOTE: This method allow you to retrive the TOKEN used by EyeOnThreat&trade;.

    auth = eyeonthreat.Authentication()
    auth.getAuthToken(user,passwd)
    
    Response:
    
    {
        "data": {"token": "ImKlcnRhLOpwdzo9hkplc2ki.DA8xyg.3TidfdlOkGwpKNsfdsTx8Ht-12sIze6rQ"},
        "service": {"status": "valid"}
    }
    
    
Services Initalization:

    feed = eyeonthreat.Feed(token)
    hunting = eyeonthreat.Hunting(token)
    info = eyeonthreat.Info(token)

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
 
* **Rate Limit**: The API rate limit is set to 1 requests per second. If this limit is exceeded, the request is rejected.
  
* **Query Limit**: Free accounts have a queries limit set to 100 queries per day.Exceeding this limit the account is blocked.
  
  
Documentation
-------------
Full API Documentation is available at https://www.eyeonthre.at/site/api.html .
