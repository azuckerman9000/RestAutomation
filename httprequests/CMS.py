from schemamodels import CMSSchema
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
        if key in inputs.keys():
            temp_dict[key] = inputs[key]
    return temp_dict

# CMS HTTP Requests
        
def SaveSubscription(base_url,SessionToken,**kwargs):    
    request_template = copy.deepcopy(getattr(CMSSchema,"SaveSubscription"))  
    body = setReq(request_template,**kwargs)
    url = base_url + "DataServices/CMS.svc/subscriptions/" + kwargs["MerchantProfileId"]
    try:
        r = requests.post(url,auth = HTTPBasicAuth(SessionToken,''), data=json.dumps(body,sort_keys=True), headers = {"content-type":"application/json"}, verify = False)
        logger.Log(r,"SaveSubscription")
        r.raise_for_status()
        print("--Subscription Saved:")

    except requests.exceptions.HTTPError as Error:
        print("--SaveSubscription Returned Error: %s." % Error)            
        return