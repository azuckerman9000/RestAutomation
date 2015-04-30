from schemamodels import TPSSchema
from miscutils import logger
import json, requests, copy
from requests.auth import HTTPBasicAuth

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

# HTTP Request Functions

def Authorize(base_url,SessionToken,ServiceId,**kwargs):
    request_template = copy.deepcopy(getattr(TPSSchema,"Authorize"))       
    body = setReq(request_template,**kwargs)
    if "HouseNumber" in kwargs.keys():
        del body["Transaction"]["TenderData"]["CardSecurityData"]["AVSData"]
    else:
        del body["Transaction"]["TenderData"]["CardSecurityData"]["InternationalAVSData"]
    url = base_url + "TPS.svc/" + ServiceId
    try:
        r = requests.post(url,auth = HTTPBasicAuth(SessionToken,''), data=json.dumps(body,sort_keys=True), headers = {"content-type":"application/json"}, verify = False)        
        logger.Log(r,"Authorize")
        r.raise_for_status()
        print("--Authorize returned successful")
        return json.loads(r.text)["TransactionId"]                       
    except requests.exceptions.HTTPError as Error:
        print("--Authorize Returned Error: %s." % Error)            
        return
    
def AuthorizeAndCapture(base_url,SessionToken,ServiceId,**kwargs):
    request_template = copy.deepcopy(getattr(TPSSchema,"Authorize"))  
    body = setReq(request_template,**kwargs)
    if "HouseNumber" in kwargs.keys():
        del body["Transaction"]["TenderData"]["CardSecurityData"]["AVSData"]
    else:
        del body["Transaction"]["TenderData"]["CardSecurityData"]["InternationalAVSData"]
    body["$type"] = "AuthorizeAndCaptureTransaction,http://schemas.evosnap.com/CWS/v2.0/Transactions/Rest"
    url = base_url + "TPS.svc/" + ServiceId
    try:
        r = requests.post(url,auth = HTTPBasicAuth(SessionToken,''), data=json.dumps(body,sort_keys=True), headers = {"content-type":"application/json"}, verify = False)        
        logger.Log(r,"AuthorizeAndCapture")
        r.raise_for_status()
        print("--AuthorizeAndCapture returned successful")
        return json.loads(r.text)["TransactionId"]               
    except requests.exceptions.HTTPError as Error:
        print("--AuthorizeAndCapture Returned Error: %s." % Error)            
        return
    
def Capture(base_url,SessionToken,ServiceId,TxnGUID,**kwargs):
    if TxnGUID == None:
        return
    request_template = copy.deepcopy(getattr(TPSSchema,"Capture")) 
    body = setReq(request_template,**kwargs)
    url = base_url + "TPS.svc/" + ServiceId + "/" + TxnGUID
    try:
        r = requests.put(url,auth = HTTPBasicAuth(SessionToken,''), data=json.dumps(body,sort_keys=True), headers = {"content-type":"application/json"}, verify = False)        
        logger.Log(r,"Capture")
        r.raise_for_status()
        print("--Capture returned successful")
        return json.loads(r.text)["TransactionId"]                       
    except requests.exceptions.HTTPError as Error:
        print("--Capture Returned Error: %s." % Error)            
        return
    
def Undo(base_url,SessionToken,ServiceId,TxnGUID,**kwargs):
    if TxnGUID == None:
        return
    request_template = copy.deepcopy(getattr(TPSSchema,"Undo")) 
    body = setReq(request_template,**kwargs)
    url = base_url + "TPS.svc/" + ServiceId + "/" + TxnGUID
    try:
        r = requests.put(url,auth = HTTPBasicAuth(SessionToken,''), data=json.dumps(body,sort_keys=True), headers = {"content-type":"application/json"}, verify = False)        
        logger.Log(r,"Undo")
        r.raise_for_status()
        print("--Undo returned successful")
        return json.loads(r.text)["TransactionId"]                       
    except requests.exceptions.HTTPError as Error:
        print("--Undo Returned Error: %s." % Error)            
        return
    
def Resubmit(base_url,SessionToken,ServiceId,TxnGUID,**kwargs):
    if TxnGUID == None:
        return
    kwargs["TransactionId"] = TxnGUID
    request_template = copy.deepcopy(getattr(TPSSchema,"Resubmit"))        
    body = setReq(request_template,**kwargs)
    if "PaymentAuthorizationResponse" in kwargs.keys():
        body["Transaction"]["$type"] = "Resubmit3DSecure,http://schemas.evosnap.com/CWS/v2.0/Transactions/Bankcard"    
    url = base_url + "TPS.svc/" + ServiceId
    try:
        r = requests.post(url,auth = HTTPBasicAuth(SessionToken,''), data=json.dumps(body,sort_keys=True), headers = {"content-type":"application/json"}, verify = False)        
        logger.Log(r,"Resubmit")
        r.raise_for_status()
        print("--Resubmit returned successful")
        return json.loads(r.text)["TransactionId"]               
    except requests.exceptions.HTTPError as Error:
        print("--Resubmit Returned Error: %s." % Error)            
        return