from schemamodels import TMSSchema
from miscutils import logger
import json, requests, copy
from requests.auth import HTTPBasicAuth

# Request Builder and Utility Functions
def setQueryReq(qschema,**kwargs):
    qreq = qschema
    if len(kwargs.keys()) != 0:
        qreq = popSaveReq(qreq,kwargs)
    return qreq
        

def popSaveReq(req_dict,inputs):
    temp_dict = req_dict
    for key, value in req_dict.items():
        if isinstance(value,dict):
            popSaveReq(value,inputs)
        elif key in inputs.keys():
            temp_dict[key] = inputs[key]
    return temp_dict

# HTTP Request Functions

def QueryTransactionsSummary(base_url,SessionToken,**kwargs):
    request_template = copy.deepcopy(getattr(TMSSchema,"TxnSummary"))  
    body = setQueryReq(request_template,**kwargs)
    url = base_url + "DataServices/TMS.svc/transactionsSummary"
    try:
        r = requests.post(url,auth = HTTPBasicAuth(SessionToken,''), data=json.dumps(body,sort_keys=True), headers = {"content-type":"application/json"}, verify = False)        
        logger.Log(r,"QueryTransactionsSummary")
        r.raise_for_status()
        print("--QueryTransactionsSummary returned successful")               
    except requests.exceptions.HTTPError as Error:
        print("--QueryTransactionsSummary Returned Error: %s." % Error)            
        return
    
def QueryTransactionDetails(base_url,SessionToken,**kwargs):
    request_template = copy.deepcopy(getattr(TMSSchema,"TxnDetail"))  
    body = setQueryReq(request_template,**kwargs)
    url = base_url + "DataServices/TMS.svc/transactionsDetail"
    try:
        r = requests.post(url,auth = HTTPBasicAuth(SessionToken,''), data=json.dumps(body,sort_keys=True), headers = {"content-type":"application/json"}, verify = False)        
        logger.Log(r,"QueryTransactionsDetail")
        r.raise_for_status()
        print("--QueryTransactionsDetail returned successful")               
    except requests.exceptions.HTTPError as Error:
        print("--QueryTransactionsDetail Returned Error: %s." % Error)            
        return
    
def QueryTransactionFamilies(base_url,SessionToken,**kwargs):
    request_template = copy.deepcopy(getattr(TMSSchema,"TxnFamily"))  
    body = setQueryReq(request_template,**kwargs)
    url = base_url + "DataServices/TMS.svc/transactionsFamily"
    try:
        r = requests.post(url,auth = HTTPBasicAuth(SessionToken,''), data=json.dumps(body,sort_keys=True), headers = {"content-type":"application/json"}, verify = False)        
        logger.Log(r,"QueryTransactionsFamily")
        r.raise_for_status()
        print("--QueryTransactionsFamily returned successful")               
    except requests.exceptions.HTTPError as Error:
        print("--QueryTransactionsFamily Returned Error: %s." % Error)            
        return
    
def QueryBatch(base_url,SessionToken,**kwargs):
    request_template = copy.deepcopy(getattr(TMSSchema,"QueryBatch"))
    body = setQueryReq(request_template,**kwargs)
    url = base_url + "DataServices/TMS.svc/batch"
    try:
        r = requests.post(url,auth = HTTPBasicAuth(SessionToken,''), data=json.dumps(body,sort_keys=True), headers = {"content-type":"application/json"}, verify = False)        
        logger.Log(r,"QueryBatch")
        r.raise_for_status()
        print("--QueryBatch returned successful")               
    except requests.exceptions.HTTPError as Error:
        print("--QueryBatch Returned Error: %s." % Error)            
        return