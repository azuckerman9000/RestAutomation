from schemamodels import AdminSchema
import json, requests, copy
from requests.auth import HTTPBasicAuth
from miscutils import logger

# Request Builder and Utility Functions
def setReq(schema,**kwargs):
    req = schema
    if len(kwargs.keys()) != 0:
        req = popSaveReq(req,kwargs)
    return req
        

def popSaveReq(req_dict,inputs):
    temp_dict = req_dict
    for key, value in req_dict.items():
        if isinstance(value,dict):
            popSaveReq(value,inputs)
        elif key in inputs.keys():
            temp_dict[key] = inputs[key]
    return temp_dict

# Admin HTTP Requests

######## UserManagement Operations ###############        
def CreateUser(base_url,SessionToken,**kwargs):    
    request_template = copy.deepcopy(getattr(AdminSchema,"CreateUser"))  
    body = setReq(request_template,**kwargs)   
    url = base_url + "Administration.svc/users/create"
    try:
        r = requests.put(url,auth = HTTPBasicAuth(SessionToken,''), data=json.dumps(body,sort_keys=True), headers = {"content-type":"application/json"}, verify = False)
        logger.Log(r,"CreateUser")
        r.raise_for_status()
        print("--User Created")        
    except requests.exceptions.HTTPError as Error:
        print("--CreateUser Returned Error: %s." % Error)            
        return

def UpdateUser(base_url,SessionToken,UserGuid,**kwargs):
    request_template = copy.deepcopy(getattr(AdminSchema,"UndateUser"))  
    body = setReq(request_template,**kwargs)   
    url = base_url + "Administration.svc/users/" + UserGuid +"/update"
    try:
        r = requests.put(url,auth = HTTPBasicAuth(SessionToken,''), data=json.dumps(body,sort_keys=True), headers = {"content-type":"application/json"}, verify = False)
        logger.Log(r,"UpdateUser")
        r.raise_for_status()
        print("--User Updated")        
    except requests.exceptions.HTTPError as Error:
        print("--UpdateUser Returned Error: %s." % Error)            
        return

def AddRegionToUserCredential(base_url,SessionToken,userGuid,regionName):
    url = base_url + "Administration.svc/users/" + userGuid +"/addRegion/" + regionName
    try:
        r = requests.put(url,auth = HTTPBasicAuth(SessionToken,''), headers = {"content-type":"application/json"}, verify = False)
        logger.Log(r,"AddRegionToUserCredential")
        r.raise_for_status()
        print("--Region added to User")        
    except requests.exceptions.HTTPError as Error:
        print("--AddRegionToUserCredential Returned Error: %s." % Error)            
        return
    
def AddMerchantToUserCredential(base_url,SessionToken,userGuid,**kwargs):
    request_template = copy.deepcopy(getattr(AdminSchema,"AddMerchantToUserCredntial"))  
    body = setReq(request_template,**kwargs)   
    url = base_url + "Administration.svc/users/" + userGuid +"/addMerchant"
    try:
        r = requests.put(url,auth = HTTPBasicAuth(SessionToken,''), data=json.dumps(body,sort_keys=True), headers = {"content-type":"application/json"}, verify = False)
        logger.Log(r,"AddMerchantToUserCredntial")
        r.raise_for_status()
        print("--Merchant added to User")        
    except requests.exceptions.HTTPError as Error:
        print("--AddMerchantToUserCredntial Returned Error: %s." % Error)            
        return

######## Query operations ############################    
def GetMerchants(base_url,SessionToken,**kwargs):
    request_template = copy.deepcopy(getattr(AdminSchema,"GetMerchants"))  
    body = setReq(request_template,**kwargs)   
    url = base_url + "Administration.svc/merchants"
    try:
        r = requests.post(url,auth = HTTPBasicAuth(SessionToken,''), data=json.dumps(body,sort_keys=True), headers = {"content-type":"application/json"}, verify = False)
        logger.Log(r,"GetMerchants")
        r.raise_for_status()
        print("--Retrieved Merchants")        
    except requests.exceptions.HTTPError as Error:
        print("--GetMerchants Returned Error: %s." % Error)            
        return

def ListScopes(base_url,SessionToken):
    url = base_url + "Administration.svc/scopes"
    try:
        r = requests.post(url,auth = HTTPBasicAuth(SessionToken,''), headers = {"content-type":"application/json"}, verify = False)
        logger.Log(r,"ListScopes")
        r.raise_for_status()
        print("--Retrieved Scopes")        
    except requests.exceptions.HTTPError as Error:
        print("--ListScopes Returned Error: %s." % Error)            
        return
    
def ListRoles(base_url,SessionToken,scopeId):
    url = base_url + "Administration.svc/roles/list/" + scopeId
    try:
        r = requests.post(url,auth = HTTPBasicAuth(SessionToken,''), headers = {"content-type":"application/json"}, verify = False)
        logger.Log(r,"ListRoles")
        r.raise_for_status()
        print("--Retrieved Roles")        
    except requests.exceptions.HTTPError as Error:
        print("--ListRoles Returned Error: %s." % Error)            
        return
    
def ListRoleClaims(base_url,SessionToken,roleName):
    url = base_url + "Administration.svc/roles/" + roleName + "/claims"
    try:
        r = requests.post(url,auth = HTTPBasicAuth(SessionToken,''), headers = {"content-type":"application/json"}, verify = False)
        logger.Log(r,"ListRoleClaims")
        r.raise_for_status()
        print("--Retrieved RoleClaims")        
    except requests.exceptions.HTTPError as Error:
        print("--ListRoleClaims Returned Error: %s." % Error)            
        return
    
def GetRoleClaims(base_url,SessionToken):
    url = base_url + "Administration.svc/roleClaims"
    try:
        r = requests.post(url,auth = HTTPBasicAuth(SessionToken,''), headers = {"content-type":"application/json"}, verify = False)
        logger.Log(r,"GetRoleClaims")
        r.raise_for_status()
        print("--Retrieved RoleClaims")        
    except requests.exceptions.HTTPError as Error:
        print("--GetRoleClaims Returned Error: %s." % Error)            
        return
