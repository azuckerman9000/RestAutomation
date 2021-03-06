from schemamodels import TPSSchema
from miscutils import logger,assertor
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
        if key in inputs.keys():           
            temp_dict[key] = inputs[key]       
    return temp_dict

# HTTP Request Functions
def Ping(base_url,SessionToken):
    url = base_url + "TPS.svc/ping"
    try:
        r = requests.get(url, auth = HTTPBasicAuth(SessionToken,''), headers = {"content-type":"application/json"}, verify = False)        
        logger.Log(r,"Ping")
        r.raise_for_status()
        print("--Ping returned successful")                       
    except requests.exceptions.HTTPError as Error:
        print("--Ping Returned Error: %s." % Error)            
        return

def Authorize(base_url,SessionToken,ServiceId,AppConfig=False,assertions=None,**kwargs):
    request_template = copy.deepcopy(getattr(TPSSchema,"Authorize"))       
    body = setReq(request_template,**kwargs)
    
    if AppConfig is False: #Checks if AppConfigData is set for eServices relating to EMV Data
        del body["Transaction"]["ApplicationConfigurationData"]
        del body["Transaction"]["TenderData"]["EMVData"]
        
    url = base_url + "TPS.svc/" + ServiceId
    try:
        r = requests.post(url,auth = HTTPBasicAuth(SessionToken,''), data=json.dumps(body,sort_keys=True), headers = {"content-type":"application/json"}, verify = False)        
        logger.Log(r,"Authorize")        
        r.raise_for_status()
        print("--Authorize returned successful")
        logger.LogAssertions(assertor.assertor(r,assertions))
        return json.loads(r.text)                       
    except requests.exceptions.HTTPError as Error:
        print("--Authorize Returned Error: %s." % Error)            
        return
    
def AuthorizeAndCapture(base_url,SessionToken,ServiceId,AppConfig=False,assertions=None,**kwargs):
    request_template = copy.deepcopy(getattr(TPSSchema,"Authorize"))  
    body = setReq(request_template,**kwargs)
          
    if AppConfig is False: #Checks if AppConfigData is set for eServices relating to EMV Data
        del body["Transaction"]["ApplicationConfigurationData"]
        del body["Transaction"]["TenderData"]["EMVData"]
        
    body["$type"] = "AuthorizeAndCaptureTransaction,http://schemas.evosnap.com/CWS/v2.0/Transactions/Rest"
    url = base_url + "TPS.svc/" + ServiceId
    try:
        r = requests.post(url,auth = HTTPBasicAuth(SessionToken,''), data=json.dumps(body,sort_keys=True), headers = {"content-type":"application/json"}, verify = False)        
        logger.Log(r,"AuthorizeAndCapture")
        r.raise_for_status()
        print("--AuthorizeAndCapture returned successful")
        logger.LogAssertions(assertor.assertor(r,assertions))
        return json.loads(r.text)              
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
    
    #del body["DifferenceData"]["TenderData"]["$type"]
    body["DifferenceData"]["TransactionId"] = TxnGUID
    
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
    
def Adjust(base_url,SessionToken,ServiceId,TxnGUID,**kwargs):
    if TxnGUID == None:
        return
    request_template = copy.deepcopy(getattr(TPSSchema,"Adjust")) 
    body = setReq(request_template,**kwargs)
    url = base_url + "TPS.svc/" + ServiceId + "/" + TxnGUID
    try:
        r = requests.put(url,auth = HTTPBasicAuth(SessionToken,''), data=json.dumps(body,sort_keys=True), headers = {"content-type":"application/json"}, verify = False)        
        logger.Log(r,"Adjust")
        r.raise_for_status()
        print("--Adjust returned successful")
        return json.loads(r.text)["TransactionId"]                       
    except requests.exceptions.HTTPError as Error:
        print("--Adjust Returned Error: %s." % Error)            
        return
    
def ReturnById(base_url,SessionToken,ServiceId,TxnGUID,**kwargs):
    if TxnGUID == None:
        return
    kwargs["TransactionId"] = TxnGUID
    request_template = copy.deepcopy(getattr(TPSSchema,"ReturnById")) 
    body = setReq(request_template,**kwargs)
    url = base_url + "TPS.svc/" + ServiceId
    try:
        r = requests.post(url,auth = HTTPBasicAuth(SessionToken,''), data=json.dumps(body,sort_keys=True), headers = {"content-type":"application/json"}, verify = False)        
        logger.Log(r,"ReturnById")
        r.raise_for_status()
        print("--ReturnById returned successful")
        return json.loads(r.text)["TransactionId"]                       
    except requests.exceptions.HTTPError as Error:
        print("--ReturnById Returned Error: %s." % Error)            
        return
    
def ReturnUnlinked(base_url,SessionToken,ServiceId,AppConfig=False,**kwargs):
    request_template = copy.deepcopy(getattr(TPSSchema,"Authorize"))  
    body = setReq(request_template,**kwargs)
          
    if AppConfig is False: #Checks if AppConfigData is set for eServices relating to EMV Data
        del body["Transaction"]["ApplicationConfigurationData"]
        del body["Transaction"]["TenderData"]["EMVData"]
        
    body["$type"] = "ReturnUnlinked,http://schemas.evosnap.com/CWS/v2.0/Transactions/Rest"
    url = base_url + "TPS.svc/" + ServiceId
    try:
        r = requests.post(url,auth = HTTPBasicAuth(SessionToken,''), data=json.dumps(body,sort_keys=True), headers = {"content-type":"application/json"}, verify = False)        
        logger.Log(r,"ReturnUnlinked")
        r.raise_for_status()
        print("--ReturnUnlinked returned successful")
        return json.loads(r.text)["TransactionId"]               
    except requests.exceptions.HTTPError as Error:
        print("--ReturnUnlinked Returned Error: %s." % Error)            
        return
    
def Resubmit(base_url,SessionToken,ServiceId,TxnGUID,**kwargs):
    if TxnGUID == None:
        return
    kwargs["TransactionId"] = TxnGUID
    request_template = copy.deepcopy(getattr(TPSSchema,"Resubmit"))        
    body = setReq(request_template,**kwargs)
    
    if "PaymentAuthorizationResponse" in kwargs.keys(): #If PaRes is passed in request, change type to 3Dsecure Resubmit
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
    
def RequestKey(base_url,SessionToken,ServiceId,**kwargs):
    request_template = copy.deepcopy(getattr(TPSSchema,"RequestKey"))        
    body = setReq(request_template,**kwargs)
    
    url = base_url + "TLS/REST/SecureMessaging.svc/" + ServiceId
    try:
        r = requests.post(url,auth = HTTPBasicAuth(SessionToken,''), data=json.dumps(body,sort_keys=True), headers = {"content-type":"application/json"}, verify = False)        
        logger.Log(r,"RequestKey")
        r.raise_for_status()
        print("--RequestKey returned successful")                       
    except requests.exceptions.HTTPError as Error:
        print("--RequestKey Returned Error: %s." % Error)            
        return
    
def SendReceipt(base_url,SessionToken,TxnGUID,Email):
    url = base_url + "TPS.svc/sendReceipt"
    body = {"TransactionId":TxnGUID,"Email":Email}
    try:
        r = requests.post(url,auth = HTTPBasicAuth(SessionToken,''), data=json.dumps(body,sort_keys=True), headers = {"content-type":"application/json"}, verify = False)
        logger.Log(r,"SendRecipt")
        r.raise_for_status()
        print("--SendReceipt returned successful")                       
    except requests.exceptions.HTTPError as Error:
        print("--SendReceipt Returned Error: %s." % Error)            
        return
    
def GetPARes(PaReq):
    url = "https://dropit.3dsecure.net:9443/PIT/ACS"    
    body = {"PaReq":PaReq,"TermUrl":"127.0.0.1","MD":"90128006"}    
    try:
        r = requests.post(url, data=body, headers = {"content-type":"application/x-www-form-urlencoded","charset":"UTF-8"})
        start = r.text.find('PaRes" VALUE="')
        end = r.text.find('<INPUT TYPE="hidden" NAME="MD" VALUE="90128006">')
        print("--Retrieved PaReq")
        return(r.text[start + 14:end-15])
        r.raise_for_status()
    except requests.exceptions.HTTPError as Error:
        print("--GetPARes Returned Error: %s." % Error)            
        return    
