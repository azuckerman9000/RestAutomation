import requests, json
from requests.auth import HTTPBasicAuth
from miscutils import logger

#Identity Token for ServiceKey BBE2F64B19200001
#IdentityToken = 'PHNhbWw6QXNzZXJ0aW9uIE1ham9yVmVyc2lvbj0iMSIgTWlub3JWZXJzaW9uPSIxIiBBc3NlcnRpb25JRD0iXzJlM2UzNTNkLWRlYjktNDVhNC05ZTIxLTg2MzZiZWEzMzg3MSIgSXNzdWVyPSJJcGNBdXRoZW50aWNhdGlvbiIgSXNzdWVJbnN0YW50PSIyMDE0LTExLTEzVDE2OjUwOjEwLjYyOFoiIHhtbG5zOnNhbWw9InVybjpvYXNpczpuYW1lczp0YzpTQU1MOjEuMDphc3NlcnRpb24iPjxzYW1sOkNvbmRpdGlvbnMgTm90QmVmb3JlPSIyMDE0LTExLTEzVDE2OjUwOjEwLjYyOFoiIE5vdE9uT3JBZnRlcj0iMjAxNy0xMS0xM1QxNjo1MDoxMC42MjhaIj48L3NhbWw6Q29uZGl0aW9ucz48c2FtbDpBZHZpY2U+PC9zYW1sOkFkdmljZT48c2FtbDpBdHRyaWJ1dGVTdGF0ZW1lbnQ+PHNhbWw6U3ViamVjdD48c2FtbDpOYW1lSWRlbnRpZmllcj5CQkUyRjY0QjE5MjAwMDAxPC9zYW1sOk5hbWVJZGVudGlmaWVyPjwvc2FtbDpTdWJqZWN0PjxzYW1sOkF0dHJpYnV0ZSBBdHRyaWJ1dGVOYW1lPSJTQUsiIEF0dHJpYnV0ZU5hbWVzcGFjZT0iaHR0cDovL3NjaGVtYXMuaXBjb21tZXJjZS5jb20vSWRlbnRpdHkiPjxzYW1sOkF0dHJpYnV0ZVZhbHVlPkJCRTJGNjRCMTkyMDAwMDE8L3NhbWw6QXR0cmlidXRlVmFsdWU+PC9zYW1sOkF0dHJpYnV0ZT48c2FtbDpBdHRyaWJ1dGUgQXR0cmlidXRlTmFtZT0iU2VyaWFsIiBBdHRyaWJ1dGVOYW1lc3BhY2U9Imh0dHA6Ly9zY2hlbWFzLmlwY29tbWVyY2UuY29tL0lkZW50aXR5Ij48c2FtbDpBdHRyaWJ1dGVWYWx1ZT5jNmZjOTFlZi0zM2ZkLTQ2OTktYTdhMi02OWUxZWJlOGZmYTQ8L3NhbWw6QXR0cmlidXRlVmFsdWU+PC9zYW1sOkF0dHJpYnV0ZT48c2FtbDpBdHRyaWJ1dGUgQXR0cmlidXRlTmFtZT0ibmFtZSIgQXR0cmlidXRlTmFtZXNwYWNlPSJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcyI+PHNhbWw6QXR0cmlidXRlVmFsdWU+QkJFMkY2NEIxOTIwMDAwMTwvc2FtbDpBdHRyaWJ1dGVWYWx1ZT48L3NhbWw6QXR0cmlidXRlPjwvc2FtbDpBdHRyaWJ1dGVTdGF0ZW1lbnQ+PFNpZ25hdHVyZSB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC8wOS94bWxkc2lnIyI+PFNpZ25lZEluZm8+PENhbm9uaWNhbGl6YXRpb25NZXRob2QgQWxnb3JpdGhtPSJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzEwL3htbC1leGMtYzE0biMiPjwvQ2Fub25pY2FsaXphdGlvbk1ldGhvZD48U2lnbmF0dXJlTWV0aG9kIEFsZ29yaXRobT0iaHR0cDovL3d3dy53My5vcmcvMjAwMC8wOS94bWxkc2lnI3JzYS1zaGExIj48L1NpZ25hdHVyZU1ldGhvZD48UmVmZXJlbmNlIFVSST0iI18yZTNlMzUzZC1kZWI5LTQ1YTQtOWUyMS04NjM2YmVhMzM4NzEiPjxUcmFuc2Zvcm1zPjxUcmFuc2Zvcm0gQWxnb3JpdGhtPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwLzA5L3htbGRzaWcjZW52ZWxvcGVkLXNpZ25hdHVyZSI+PC9UcmFuc2Zvcm0+PFRyYW5zZm9ybSBBbGdvcml0aG09Imh0dHA6Ly93d3cudzMub3JnLzIwMDEvMTAveG1sLWV4Yy1jMTRuIyI+PC9UcmFuc2Zvcm0+PC9UcmFuc2Zvcm1zPjxEaWdlc3RNZXRob2QgQWxnb3JpdGhtPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwLzA5L3htbGRzaWcjc2hhMSI+PC9EaWdlc3RNZXRob2Q+PERpZ2VzdFZhbHVlPmlDSk9ZZ0FNYkJKL21kcHhZSFNmL2tyNFRPZz08L0RpZ2VzdFZhbHVlPjwvUmVmZXJlbmNlPjwvU2lnbmVkSW5mbz48U2lnbmF0dXJlVmFsdWU+QURBcXBZRjh3Y2x5VHFQSFFlN2szYzQvY2hYTFFVYXZQWXdreUVoMTNzU0pYcUhCaFRQK3ZSbzZ3YjRIcmtlTWRsRHR0L0RZcVg4UEdsY1FkcXNxd3E1YWQwMlpjRWViYktkNGZxcVNxUU10UEdLL2lkb0ZkRFg4WG9LYkN5ZFdPL2JOZ2V6M2JtTXZNejczMlpVR2ZlMlVtSERPa3M3Q3ZNU1B0NTZaVjUyNklvVDRNdDhBWDNsNllvcklMNklpOWgvVndySjZHa0h2eGdtenRoeEVGeEZqSlhYek1QZWlzOHFRQmpIeUJZOGhON2dqeHNnWXpWTytzUjUvWEppVFZ1ZGx6a3RoTXJ3VENSUVFETjR1ZHRac0oydE9FTDRGKzJjNm5MZmluWGdGVjlGQkYzbDhqRGQwNnpsL2kxdW53OUJybE1TUHlaanVtQ21TRXRTaUR3PT08L1NpZ25hdHVyZVZhbHVlPjxLZXlJbmZvPjxvOlNlY3VyaXR5VG9rZW5SZWZlcmVuY2UgeG1sbnM6bz0iaHR0cDovL2RvY3Mub2FzaXMtb3Blbi5vcmcvd3NzLzIwMDQvMDEvb2FzaXMtMjAwNDAxLXdzcy13c3NlY3VyaXR5LXNlY2V4dC0xLjAueHNkIj48bzpLZXlJZGVudGlmaWVyIFZhbHVlVHlwZT0iaHR0cDovL2RvY3Mub2FzaXMtb3Blbi5vcmcvd3NzL29hc2lzLXdzcy1zb2FwLW1lc3NhZ2Utc2VjdXJpdHktMS4xI1RodW1icHJpbnRTSEExIj5QTE5QWDBOYmJZeEE3TVpxd2hSZkxJcFd2VkE9PC9vOktleUlkZW50aWZpZXI+PC9vOlNlY3VyaXR5VG9rZW5SZWZlcmVuY2U+PC9LZXlJbmZvPjwvU2lnbmF0dXJlPjwvc2FtbDpBc3NlcnRpb24+'

def SignOnWithToken(base_url,IdentityToken):
    url = base_url + "SvcInfo/token"
    try:
        r = requests.get(url,auth = HTTPBasicAuth(IdentityToken,""),headers = {"content-type":"application/json"}, verify = False)
        logger.Log(r,"SignOnWithToken")
        r.raise_for_status()
        print("--Signed On Successfully.")                      
        return r.text[1:-1]
    except requests.exceptions.HTTPError as Error:
        print("--SignOn Returned Error: %s." % Error)            
        return

def SignOnWithUsernamePassword(base_url,Username,Password,ServiceKey):
    url = base_url + "SvcInfo/user?servicekey=" + ServiceKey
    try:
        r = requests.get(url,auth = HTTPBasicAuth(Username,Password),headers = {"content-type":"application/json"}, verify = False)
        logger.Log(r,"SignOnWithUsernamePassword")
        r.raise_for_status()
        print("--Signed On Successfully with Username/Password.")
        return json.loads(r.text)
    except requests.exceptions.HTTPError as Error:
        print("--SignOnWithUsernamePassword Returned Error: %s." % Error)            
        return
    
def DelegatedSignOn(base_url,DelegatedSK,IdentityToken):
    url = base_url + "SvcInfo/delegated"
    body = {"onBehalfOfServiceKey":DelegatedSK}
    try:
        r = requests.post(url, data = json.dumps(body), auth = HTTPBasicAuth(IdentityToken,""),headers = {"content-type":"application/json"}, verify = False)
        logger.Log(r,"DelegatedSignOn")
        r.raise_for_status()
        print("--DelegatedSigned On Successfully.")
        return json.loads(r.text)
    except requests.exceptions.HTTPError as Error:
        print("--DelegatedSignOn Returned Error: %s." % Error)            
        return
    
def ChangePassword(base_url,Username,Password,ServiceKey,NewPassword):
    url = base_url + "SvcInfo/user/" + Username + "?ServiceKey=" + ServiceKey
    body = {"Password":NewPassword}
    try:
        r = requests.put(url, data = json.dumps(body), auth = HTTPBasicAuth(Username,Password),headers = {"content-type":"application/json"}, verify = False)
        logger.Log(r,"ChangePassword")
        r.raise_for_status()
        print("--ChangePassword Successfully to",NewPassword)
        return
    except requests.exceptions.HTTPError as Error:
        print("--ChangePassword Returned Error: %s." % Error)            
        return
    
def GetUserExpiration(base_url,Username,Password,ServiceKey):
    url = base_url + "SvcInfo/user/" + Username + "/expiration?ServiceKey=" + ServiceKey
    try:
        r = requests.get(url,auth = HTTPBasicAuth(Username,Password),headers = {"content-type":"application/json"}, verify = False)
        logger.Log(r,"GetUserExpiration")
        r.raise_for_status()
        print("--GetUserExpiration successful.", r.text)        
    except requests.exceptions.HTTPError as Error:
        print("--GetUserExpiration  Returned Error: %s." % Error)            
        return
