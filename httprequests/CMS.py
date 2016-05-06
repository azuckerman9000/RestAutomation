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
        
def SubmitSubscription(base_url,SessionToken,**kwargs):    
    request_template = copy.deepcopy(getattr(CMSSchema,"SubmitSubscription"))  
    body = setReq(request_template,**kwargs)
    url = base_url + "DataServices/CMS.svc/subscriptions/" + kwargs["MerchantProfileId"]
    try:
        r = requests.post(url,auth = HTTPBasicAuth(SessionToken,''), data=json.dumps(body,sort_keys=True), headers = {"content-type":"application/json"}, verify = False)
        logger.Log(r,"SubmitSubscription")
        r.raise_for_status()
        print("--Subscription Saved")
        return r.text
    except requests.exceptions.HTTPError as Error:
        print("--SubmitSubscription Returned Error: %s." % Error)            
        return

def UpdateSubscription(base_url,SessionToken,SubscriptionReferenceId,**kwargs):    
    request_template = copy.deepcopy(getattr(CMSSchema,"SubmitSubscription"))  # Uses same object as SubmitSubscription
    body = setReq(request_template,**kwargs)
    url = base_url + "DataServices/CMS.svc/subscriptions/" + kwargs["MerchantProfileId"] + "/" + SubscriptionReferenceId
    try:
        r = requests.put(url,auth = HTTPBasicAuth(SessionToken,''), data=json.dumps(body,sort_keys=True), headers = {"content-type":"application/json"}, verify = False)
        logger.Log(r,"UpdateSubscription")
        r.raise_for_status()
        print("--Updated Subscription")

    except requests.exceptions.HTTPError as Error:
        print("--UpdateSubscriptionState Returned Error: %s." % Error)            
        return
        
def UpdateSubscriptionState(base_url,SessionToken,SubscriptionReferenceId,**kwargs):    
    request_template = copy.deepcopy(getattr(CMSSchema,"UpdateSubscriptionState"))  
    body = setReq(request_template,**kwargs)
    url = base_url + "DataServices/CMS.svc/subscriptions/" + kwargs["MerchantProfileId"] + "/" + SubscriptionReferenceId + "/state"
    try:
        r = requests.put(url,auth = HTTPBasicAuth(SessionToken,''), data=json.dumps(body,sort_keys=True), headers = {"content-type":"application/json"}, verify = False)
        logger.Log(r,"UpdateSubscriptionState")
        r.raise_for_status()
        print("--Updated SubscriptionState")

    except requests.exceptions.HTTPError as Error:
        print("--UpdateSubscriptionState Returned Error: %s." % Error)            
        return
    
def QuerySubscriptions(base_url,SessionToken,**kwargs):    
    request_template = copy.deepcopy(getattr(CMSSchema,"QuerySubscriptions"))  
    body = setReq(request_template,**kwargs)
    url = base_url + "DataServices/CMS.svc/subscriptionSummary"
    try:
        r = requests.post(url,auth = HTTPBasicAuth(SessionToken,''), data=json.dumps(body,sort_keys=True), headers = {"content-type":"application/json"}, verify = False)
        logger.Log(r,"QuerySubscriptions")
        r.raise_for_status()
        print("--Subscriptions Returned")

    except requests.exceptions.HTTPError as Error:
        print("--QuerySubscriptions Returned Error: %s." % Error)            
        return
    
def GetSubscription(base_url,SessionToken,SubscriptionReferenceId,MerchantProfileId):
    url = base_url + "DataServices/CMS.svc/subscriptions/" + MerchantProfileId + "/" + SubscriptionReferenceId
    try:
        r = requests.get(url,auth = HTTPBasicAuth(SessionToken,''), headers = {"content-type":"application/json"}, verify = False)
        logger.Log(r,"GetSubscription")
        r.raise_for_status()
        print("--Subscription Returned")

    except requests.exceptions.HTTPError as Error:
        print("--GetSubscription Returned Error: %s." % Error)            
        return
    
def DeleteSubscription(base_url,SessionToken,SubscriptionReferenceId,MerchantProfileId):
    url = base_url + "DataServices/CMS.svc/subscriptions/" + MerchantProfileId + "/" + SubscriptionReferenceId
    try:
        r = requests.delete(url,auth = HTTPBasicAuth(SessionToken,''), headers = {"content-type":"application/json"}, verify = False)
        logger.Log(r,"DeleteSubscription")
        r.raise_for_status()
        print("--Subscription Deleted")

    except requests.exceptions.HTTPError as Error:
        print("--DeleteSubscription Returned Error: %s." % Error)            
        return