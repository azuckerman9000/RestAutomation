from schemamodels import SISSchema
import json, requests, copy
from requests.auth import HTTPBasicAuth
from miscutils import logger

# Request Builder and Utility Functions
def setReq(schema,**kwargs):
    req = schema
    if len(kwargs.keys()) != 0:
        req = [popSaveReq(req,kwargs)]
    return req
        

def popSaveReq(req_dict,inputs):
    temp_dict = req_dict
    for key, value in req_dict.items():
        if isinstance(value,dict):
            popSaveReq(value,inputs)
        if key in inputs.keys():
            temp_dict[key] = inputs[key]
    return temp_dict

# SIS HTTP Requests
        
def SaveMerchantProfiles(base_url,SessionToken,**kwargs):    
    request_template = copy.deepcopy(getattr(SISSchema,"SaveMerchantProfiles"))  
    body = setReq(request_template[0],**kwargs)
    MerchantProfileId = body[0]["ProfileId"]
    ServiceId = body[0]["ServiceId"]
    url = base_url + "SIS.svc/merchProfile?serviceId=" + ServiceId
    try:
        r = requests.put(url,auth = HTTPBasicAuth(SessionToken,''), data=json.dumps(body,sort_keys=True), headers = {"content-type":"application/json"}, verify = False)
        logger.Log(r,"SaveMerchantProfiles")
        r.raise_for_status()
        print("--MerchantProfile Saved:",MerchantProfileId)
        return MerchantProfileId,ServiceId
    except requests.exceptions.HTTPError as Error:
        print("--SaveMerchantProfiles Returned Error: %s." % Error)            
        return
    
def GetMerchantProfiles(base_url,SessionToken):
    url = base_url + "SIS.svc/merchProfile"
    try:
        r = requests.get(url,auth = HTTPBasicAuth(SessionToken,''),headers = {"content-type":"application/json"}, verify = False)
        logger.Log(r,"GetMerchantProfiles")
        r.raise_for_status()
        print("--GetMerchantProfiles returned",len(json.loads(r.text)),"Merchant Profiles")        
    except requests.exceptions.HTTPError as Error:
        print("--GetMerchantProfiles Returned Error: %s." % Error)            
        return
    
def GetMerchantProfile(base_url,SessionToken,MerchantProfileId,ServiceId):
    url = base_url + "SIS.svc/merchProfile/" + MerchantProfileId + "?serviceId=" + ServiceId
    try:
        r = requests.get(url,auth = HTTPBasicAuth(SessionToken,''),headers = {"content-type":"application/json"}, verify = False)
        logger.Log(r,"GetMerchantProfile")
        r.raise_for_status()
        print("--GetMerchantProfile returned Profile:", MerchantProfileId)
        print(r.text)              
    except requests.exceptions.HTTPError as Error:
        print("--GetMerchantProfile Returned Error: %s." % Error)            
        return
    
def DeleteMerchantProfile(base_url,SessionToken,MerchantProfileId,ServiceId):
    url = base_url + "SIS.svc/merchProfile/" + MerchantProfileId + "?serviceId=" + ServiceId
    try:
        r = requests.delete(url,auth = HTTPBasicAuth(SessionToken,''),headers = {"content-type":"application/json"}, verify = False)
        logger.Log(r,"DeleteMerchantProfile")
        r.raise_for_status()
        print("--DeleteMerchantProfile successful")
        print(r.text)              
    except requests.exceptions.HTTPError as Error:
        print("--DeleteMerchantProfile Returned Error: %s." % Error)            
        return
    
def GetServiceInformation(base_url,SessionToken):
    url = base_url + "SIS.svc/serviceInformation"
    try:
        r = requests.get(url,auth = HTTPBasicAuth(SessionToken,''),headers = {"content-type":"application/json"}, verify = False)
        logger.Log(r,"GetServiceInformation")
        r.raise_for_status()
        print("--GetServiceInformation returned successfully")                    
    except requests.exceptions.HTTPError as Error:
        print("--GetServiceInformation Returned Error: %s." % Error)            
        return
    
def SaveApplicationData(base_url,SessionToken,**kwargs):
    request_template = copy.deepcopy(getattr(SISSchema,"ApplicationData"))  
    body = setReq(request_template,**kwargs)    
    url = base_url + "SIS.svc/appProfile"
    try:
        r = requests.put(url,auth = HTTPBasicAuth(SessionToken,''), data=json.dumps(body[0],sort_keys=True), headers = {"content-type":"application/json"}, verify = False)
        logger.Log(r,"SaveApplicationData")
        r.raise_for_status()
        print("--Applicationdata Saved")        
    except requests.exceptions.HTTPError as Error:
        print("--SaveApplicationData Returned Error: %s." % Error)            
        return

def GetApplicationData(base_url,SessionToken,AppProfileId):     
    url = base_url + "SIS.svc/appProfile/" + AppProfileId
    try:
        r = requests.get(url,auth = HTTPBasicAuth(SessionToken,''), headers = {"content-type":"application/json"}, verify = False)
        logger.Log(r,"GetApplicationData")
        r.raise_for_status()
        print("--Applicationdata Returned")        
    except requests.exceptions.HTTPError as Error:
        print("--GetApplicationData Returned Error: %s." % Error)            
        return
