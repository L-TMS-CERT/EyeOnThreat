# -*- coding: utf-8 -*-

###################################################################################################
## _author_ = "Lutech Cyber Threat Intelligence Team"                                            ##
## _copyright_ = "Copyright 2017, Lutech EyeOnThreat™""                                          ##
## _version_ = "1.0"                                                                             ##
## _status_ = "Stable"                                                                           ##
###################################################################################################

import requests


class Authentication:

    __BASE_URL = 'https://eyeonthre.at/auth/api'

    def getAuthToken(self, user, passwd):
        response = requests.get(self.__BASE_URL + '/token', verify=False, auth=(user, passwd))
        return response.content


class Feed:

    __BASE_URL = 'https://eyeonthre.at/threat/api/v1'

    def __init__(self,token):
        self.headers = {'Content-Type': 'application/json', 'charset': 'utf-8', 'Token': token}

    def getFeed(self, range=None):
        if range is None:
            response = requests.get(self.__BASE_URL + '/feed', headers=self.headers , verify=False)
        else:
            response = requests.get(self.__BASE_URL + '/' + range + '/feed', headers=self.headers , verify=False)
        return response.content

    def getFeedEntity(self, entity, range=None):
        if range is None:
            response = requests.get(self.__BASE_URL + '/feed/' + entity, headers=self.headers , verify=False)
        else:
            response = requests.get(self.__BASE_URL + '/' + range + '/feed/' + entity,
                                    headers=self.headers, verify=False)
        return response.content

    def getFeedCategory(self, entity, category, range=None):
        if range is None:
            response = requests.get(self.__BASE_URL + '/feed/' + entity + '/' + category,
                                    headers=self.headers, verify=False)
        else:
            response = requests.get(self.__BASE_URL + '/' + range + '/feed/' + entity + '/' + category,
                headers=self.headers, verify=False)
        return response.content

    def getFeedSubcategory(self, entity, category, subcategory, range=None):
        if range is None:
            response = requests.get(self.__BASE_URL + '/feed/' + entity + '/' + category + '/' + subcategory,
                headers=self.headers, verify=False)
        else:
            response = requests.get(self.__BASE_URL + '/'+ range + '/feed/' + entity + '/' + category + '/' + subcategory,
                headers=self.headers, verify=False)
        return response.content


class Info:

    __BASE_URL = 'https://eyeonthre.at'

    def __init__(self,token):
        self.headers = {'Content-Type': 'application/json', 'charset': 'utf-8', 'Token': token}

    def getCategories(self):
        response = requests.get(self.__BASE_URL + '/threat/api/v1/info', headers=self.headers,verify=False)
        return response.content

    def getAuthInfo(self):
        response = requests.get(self.__BASE_URL + '/auth/api/info', headers=self.headers ,verify=False)
        return response.content


class Hunting:

    __BASE_URL = 'https://eyeonthre.at/threat/api/v1/hunting'

    def __init__(self,token):
        self.headers = {'Content-Type': 'application/json', 'charset': 'utf-8', 'Token': token}

    def searchIPv4(self, ip, format="json"):
        response = requests.get(self.__BASE_URL + '/ip/' + ip + '/' + format,
                                headers=self.headers,verify=False)
        return response.content

    def searchDomain(self, domain, format="json"):
        response = requests.get(self.__BASE_URL + '/domain/' + domain + '/' + format,
            headers=self.headers,verify=False)
        return response.content

    def searchURL(self, url, format="json"):
        response = requests.get(self.__BASE_URL + '/url/' + url + '/' + format,
                                headers=self.headers, verify=False)
        return response.content

    def searchHash(self, hash, format="json"):
        response = requests.get(self.__BASE_URL + '/hash/' + hash + '/' + format,
                                headers=self.headers,verify=False)
        return response.content

    def searchEmail(self, email, format="json"):
        response = requests.get(self.__BASE_URL + '/email/' + email + '/' + format,
                                headers=self.headers,verify=False)
        return response.content
