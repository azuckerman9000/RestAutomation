from httprequests import SignOn, SIS, TMS, TPS
from miscutils import dataquery

#Identity Token for ServiceKey BBE2F64B19200001
#IdentityToken = 'PHNhbWw6QXNzZXJ0aW9uIE1ham9yVmVyc2lvbj0iMSIgTWlub3JWZXJzaW9uPSIxIiBBc3NlcnRpb25JRD0iXzJlM2UzNTNkLWRlYjktNDVhNC05ZTIxLTg2MzZiZWEzMzg3MSIgSXNzdWVyPSJJcGNBdXRoZW50aWNhdGlvbiIgSXNzdWVJbnN0YW50PSIyMDE0LTExLTEzVDE2OjUwOjEwLjYyOFoiIHhtbG5zOnNhbWw9InVybjpvYXNpczpuYW1lczp0YzpTQU1MOjEuMDphc3NlcnRpb24iPjxzYW1sOkNvbmRpdGlvbnMgTm90QmVmb3JlPSIyMDE0LTExLTEzVDE2OjUwOjEwLjYyOFoiIE5vdE9uT3JBZnRlcj0iMjAxNy0xMS0xM1QxNjo1MDoxMC42MjhaIj48L3NhbWw6Q29uZGl0aW9ucz48c2FtbDpBZHZpY2U+PC9zYW1sOkFkdmljZT48c2FtbDpBdHRyaWJ1dGVTdGF0ZW1lbnQ+PHNhbWw6U3ViamVjdD48c2FtbDpOYW1lSWRlbnRpZmllcj5CQkUyRjY0QjE5MjAwMDAxPC9zYW1sOk5hbWVJZGVudGlmaWVyPjwvc2FtbDpTdWJqZWN0PjxzYW1sOkF0dHJpYnV0ZSBBdHRyaWJ1dGVOYW1lPSJTQUsiIEF0dHJpYnV0ZU5hbWVzcGFjZT0iaHR0cDovL3NjaGVtYXMuaXBjb21tZXJjZS5jb20vSWRlbnRpdHkiPjxzYW1sOkF0dHJpYnV0ZVZhbHVlPkJCRTJGNjRCMTkyMDAwMDE8L3NhbWw6QXR0cmlidXRlVmFsdWU+PC9zYW1sOkF0dHJpYnV0ZT48c2FtbDpBdHRyaWJ1dGUgQXR0cmlidXRlTmFtZT0iU2VyaWFsIiBBdHRyaWJ1dGVOYW1lc3BhY2U9Imh0dHA6Ly9zY2hlbWFzLmlwY29tbWVyY2UuY29tL0lkZW50aXR5Ij48c2FtbDpBdHRyaWJ1dGVWYWx1ZT5jNmZjOTFlZi0zM2ZkLTQ2OTktYTdhMi02OWUxZWJlOGZmYTQ8L3NhbWw6QXR0cmlidXRlVmFsdWU+PC9zYW1sOkF0dHJpYnV0ZT48c2FtbDpBdHRyaWJ1dGUgQXR0cmlidXRlTmFtZT0ibmFtZSIgQXR0cmlidXRlTmFtZXNwYWNlPSJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcyI+PHNhbWw6QXR0cmlidXRlVmFsdWU+QkJFMkY2NEIxOTIwMDAwMTwvc2FtbDpBdHRyaWJ1dGVWYWx1ZT48L3NhbWw6QXR0cmlidXRlPjwvc2FtbDpBdHRyaWJ1dGVTdGF0ZW1lbnQ+PFNpZ25hdHVyZSB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC8wOS94bWxkc2lnIyI+PFNpZ25lZEluZm8+PENhbm9uaWNhbGl6YXRpb25NZXRob2QgQWxnb3JpdGhtPSJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzEwL3htbC1leGMtYzE0biMiPjwvQ2Fub25pY2FsaXphdGlvbk1ldGhvZD48U2lnbmF0dXJlTWV0aG9kIEFsZ29yaXRobT0iaHR0cDovL3d3dy53My5vcmcvMjAwMC8wOS94bWxkc2lnI3JzYS1zaGExIj48L1NpZ25hdHVyZU1ldGhvZD48UmVmZXJlbmNlIFVSST0iI18yZTNlMzUzZC1kZWI5LTQ1YTQtOWUyMS04NjM2YmVhMzM4NzEiPjxUcmFuc2Zvcm1zPjxUcmFuc2Zvcm0gQWxnb3JpdGhtPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwLzA5L3htbGRzaWcjZW52ZWxvcGVkLXNpZ25hdHVyZSI+PC9UcmFuc2Zvcm0+PFRyYW5zZm9ybSBBbGdvcml0aG09Imh0dHA6Ly93d3cudzMub3JnLzIwMDEvMTAveG1sLWV4Yy1jMTRuIyI+PC9UcmFuc2Zvcm0+PC9UcmFuc2Zvcm1zPjxEaWdlc3RNZXRob2QgQWxnb3JpdGhtPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwLzA5L3htbGRzaWcjc2hhMSI+PC9EaWdlc3RNZXRob2Q+PERpZ2VzdFZhbHVlPmlDSk9ZZ0FNYkJKL21kcHhZSFNmL2tyNFRPZz08L0RpZ2VzdFZhbHVlPjwvUmVmZXJlbmNlPjwvU2lnbmVkSW5mbz48U2lnbmF0dXJlVmFsdWU+QURBcXBZRjh3Y2x5VHFQSFFlN2szYzQvY2hYTFFVYXZQWXdreUVoMTNzU0pYcUhCaFRQK3ZSbzZ3YjRIcmtlTWRsRHR0L0RZcVg4UEdsY1FkcXNxd3E1YWQwMlpjRWViYktkNGZxcVNxUU10UEdLL2lkb0ZkRFg4WG9LYkN5ZFdPL2JOZ2V6M2JtTXZNejczMlpVR2ZlMlVtSERPa3M3Q3ZNU1B0NTZaVjUyNklvVDRNdDhBWDNsNllvcklMNklpOWgvVndySjZHa0h2eGdtenRoeEVGeEZqSlhYek1QZWlzOHFRQmpIeUJZOGhON2dqeHNnWXpWTytzUjUvWEppVFZ1ZGx6a3RoTXJ3VENSUVFETjR1ZHRac0oydE9FTDRGKzJjNm5MZmluWGdGVjlGQkYzbDhqRGQwNnpsL2kxdW53OUJybE1TUHlaanVtQ21TRXRTaUR3PT08L1NpZ25hdHVyZVZhbHVlPjxLZXlJbmZvPjxvOlNlY3VyaXR5VG9rZW5SZWZlcmVuY2UgeG1sbnM6bz0iaHR0cDovL2RvY3Mub2FzaXMtb3Blbi5vcmcvd3NzLzIwMDQvMDEvb2FzaXMtMjAwNDAxLXdzcy13c3NlY3VyaXR5LXNlY2V4dC0xLjAueHNkIj48bzpLZXlJZGVudGlmaWVyIFZhbHVlVHlwZT0iaHR0cDovL2RvY3Mub2FzaXMtb3Blbi5vcmcvd3NzL29hc2lzLXdzcy1zb2FwLW1lc3NhZ2Utc2VjdXJpdHktMS4xI1RodW1icHJpbnRTSEExIj5QTE5QWDBOYmJZeEE3TVpxd2hSZkxJcFd2VkE9PC9vOktleUlkZW50aWZpZXI+PC9vOlNlY3VyaXR5VG9rZW5SZWZlcmVuY2U+PC9LZXlJbmZvPjwvU2lnbmF0dXJlPjwvc2FtbDpBc3NlcnRpb24+'

#Prod Token
#IdentityToken = "PHNhbWw6QXNzZXJ0aW9uIE1ham9yVmVyc2lvbj0iMSIgTWlub3JWZXJzaW9uPSIxIiBBc3NlcnRpb25JRD0iX2U1ODFkMmNmLWQ5ZGItNDA4YS04Y2I4LTMyMWNhN2E0Zjk1NSIgSXNzdWVyPSJJcGNBdXRoZW50aWNhdGlvbiIgSXNzdWVJbnN0YW50PSIyMDE1LTAzLTI0VDE0OjQwOjUwLjAwOVoiIHhtbG5zOnNhbWw9InVybjpvYXNpczpuYW1lczp0YzpTQU1MOjEuMDphc3NlcnRpb24iPjxzYW1sOkNvbmRpdGlvbnMgTm90QmVmb3JlPSIyMDE1LTAzLTI0VDE0OjQwOjUwLjAwOVoiIE5vdE9uT3JBZnRlcj0iMjAxOC0wMy0yNFQxNDo0MDo1MC4wMDlaIj48L3NhbWw6Q29uZGl0aW9ucz48c2FtbDpBZHZpY2U+PC9zYW1sOkFkdmljZT48c2FtbDpBdHRyaWJ1dGVTdGF0ZW1lbnQ+PHNhbWw6U3ViamVjdD48c2FtbDpOYW1lSWRlbnRpZmllcj5DMTBDRjlFMzdBNjEzMDBDPC9zYW1sOk5hbWVJZGVudGlmaWVyPjwvc2FtbDpTdWJqZWN0PjxzYW1sOkF0dHJpYnV0ZSBBdHRyaWJ1dGVOYW1lPSJTQUsiIEF0dHJpYnV0ZU5hbWVzcGFjZT0iaHR0cDovL3NjaGVtYXMuaXBjb21tZXJjZS5jb20vSWRlbnRpdHkiPjxzYW1sOkF0dHJpYnV0ZVZhbHVlPkMxMENGOUUzN0E2MTMwMEM8L3NhbWw6QXR0cmlidXRlVmFsdWU+PC9zYW1sOkF0dHJpYnV0ZT48c2FtbDpBdHRyaWJ1dGUgQXR0cmlidXRlTmFtZT0iU2VyaWFsIiBBdHRyaWJ1dGVOYW1lc3BhY2U9Imh0dHA6Ly9zY2hlbWFzLmlwY29tbWVyY2UuY29tL0lkZW50aXR5Ij48c2FtbDpBdHRyaWJ1dGVWYWx1ZT5mMDNkOGE2MS0xZmM1LTQ4NTItOTFmYi0yZmY2ZTc2YzFjYzk8L3NhbWw6QXR0cmlidXRlVmFsdWU+PC9zYW1sOkF0dHJpYnV0ZT48c2FtbDpBdHRyaWJ1dGUgQXR0cmlidXRlTmFtZT0ibmFtZSIgQXR0cmlidXRlTmFtZXNwYWNlPSJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcyI+PHNhbWw6QXR0cmlidXRlVmFsdWU+QzEwQ0Y5RTM3QTYxMzAwQzwvc2FtbDpBdHRyaWJ1dGVWYWx1ZT48L3NhbWw6QXR0cmlidXRlPjwvc2FtbDpBdHRyaWJ1dGVTdGF0ZW1lbnQ+PFNpZ25hdHVyZSB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC8wOS94bWxkc2lnIyI+PFNpZ25lZEluZm8+PENhbm9uaWNhbGl6YXRpb25NZXRob2QgQWxnb3JpdGhtPSJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzEwL3htbC1leGMtYzE0biMiPjwvQ2Fub25pY2FsaXphdGlvbk1ldGhvZD48U2lnbmF0dXJlTWV0aG9kIEFsZ29yaXRobT0iaHR0cDovL3d3dy53My5vcmcvMjAwMC8wOS94bWxkc2lnI3JzYS1zaGExIj48L1NpZ25hdHVyZU1ldGhvZD48UmVmZXJlbmNlIFVSST0iI19lNTgxZDJjZi1kOWRiLTQwOGEtOGNiOC0zMjFjYTdhNGY5NTUiPjxUcmFuc2Zvcm1zPjxUcmFuc2Zvcm0gQWxnb3JpdGhtPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwLzA5L3htbGRzaWcjZW52ZWxvcGVkLXNpZ25hdHVyZSI+PC9UcmFuc2Zvcm0+PFRyYW5zZm9ybSBBbGdvcml0aG09Imh0dHA6Ly93d3cudzMub3JnLzIwMDEvMTAveG1sLWV4Yy1jMTRuIyI+PC9UcmFuc2Zvcm0+PC9UcmFuc2Zvcm1zPjxEaWdlc3RNZXRob2QgQWxnb3JpdGhtPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwLzA5L3htbGRzaWcjc2hhMSI+PC9EaWdlc3RNZXRob2Q+PERpZ2VzdFZhbHVlPkcxem9sc201QTRmK0QwY1g4WTVET2F0SmF1ND08L0RpZ2VzdFZhbHVlPjwvUmVmZXJlbmNlPjwvU2lnbmVkSW5mbz48U2lnbmF0dXJlVmFsdWU+V0M3bi92eWttYlJzNWVWZWpzLzhOUEF1UTlpWXluRHdpZndFWklELzlhTm91WU5ZNVZMZmxQTERMSFE5RjZNMi9sUTMrMlNCcWFQU3NUdG8yRGZUQXkzbnVmMnExRnpHRHBSSU5UZ0IrVlZUR1J2VlpFTTZOcWJHYkRXNmRuQ2JDSXpYTnUrSWs0a1Z5dE9HNzBOMmQ4RnBIOEVIcm9adVFTSXBlbFo5TkdmeGFqTXF3TmRXZHBLRHJHVGNESW1uQ2R5UmFCZThSOTVVQ044M2w2ZUdpOXBrMjkzREVwaHNib2RMTWcxUFhMT2htWmk1ZnBZUG85TlE1N3JyVjMxdU5lMmh1M0FjeUZQd2srZURUM2VXaS9kNTVKTXIwTDFLMlF4aEJVeUZENVAweW1QNWlNN3B0S3dvTnNzeDY0NCsyZUxBaGhoSmlYUXg4bjhLNFlwbkR3PT08L1NpZ25hdHVyZVZhbHVlPjxLZXlJbmZvPjxvOlNlY3VyaXR5VG9rZW5SZWZlcmVuY2UgeG1sbnM6bz0iaHR0cDovL2RvY3Mub2FzaXMtb3Blbi5vcmcvd3NzLzIwMDQvMDEvb2FzaXMtMjAwNDAxLXdzcy13c3NlY3VyaXR5LXNlY2V4dC0xLjAueHNkIj48bzpLZXlJZGVudGlmaWVyIFZhbHVlVHlwZT0iaHR0cDovL2RvY3Mub2FzaXMtb3Blbi5vcmcvd3NzL29hc2lzLXdzcy1zb2FwLW1lc3NhZ2Utc2VjdXJpdHktMS4xI1RodW1icHJpbnRTSEExIj54QVQzaU4yalZ5bkhkb1ZSMWxxdmlmU2tiVlE9PC9vOktleUlkZW50aWZpZXI+PC9vOlNlY3VyaXR5VG9rZW5SZWZlcmVuY2U+PC9LZXlJbmZvPjwvU2lnbmF0dXJlPjwvc2FtbDpBc3NlcnRpb24+"


#IdentityToken = dataquery.getIdentityToken("TEST","6B2866C8FD500001")
#base_url = "https://api.ciptest.goevo.local/REST/2.0.22/"
#session_token = SignOn.SignOnWithToken(base_url,IdentityToken)
#SIS.GetServiceInformation(base_url,session_token)
#SIS.SaveMerchantProfiles(base_url,session_token,ProfileId="EVO_SOAP_Restaurant_HostCap",ServiceId="911C800001")
#TMS.QueryTransactionsSummary(base_url,session_token,MerchantProfileIds = ["Auto_SOAP_Ecommerce_A"])
#auth_guid = TPS.Authorize(base_url,session_token,"911C800001",Amount= "2.00",MerchantProfileId="EVO_SOAP_Restaurant_HostCap")
base_url = "https://api.ciptest.goevo.local/2.1.22/REST/"
IdentityToken = dataquery.getIdentityToken("TEST","6B2866C8FD500001")
session_token = SignOn.SignOnWithToken(base_url,IdentityToken)
#SIS.GetServiceInformation(base_url,session_token)
SIS.GetMerchantProfiles(base_url,session_token)
#guid = TPS.Authorize(base_url,session_token,"372EC00001",MerchantProfileId="EVOIntl_SOAP_Ecommerce_HostCap",CVData="123",CVDataProvided="Provided")
#TPS.Resubmit(base_url,session_token,"372EC00001",guid,ResubmitReason="Resubmission")



"""
IdentityToken = dataquery.getIdentityToken("TEST","BBE2F64B19200001")
base_url = "https://api.ciptest.goevo.local/REST/2.0.22/"

#session_token = SignOn.SignOnWithToken(base_url,IdentityToken)
session_token = SignOn.SignOnWithUsernamePassword(base_url,"RestUser1","Passw0rd4","3196F64B19200001")["SessionToken"]
auth_guid = TPS.Authorize(base_url,session_token,"1257A00001",Amount= "2.00")
TPS.Undo(base_url,session_token,"1257A00001",auth_guid)
TMS.QueryTransactionsSummary(base_url,session_token,MerchantProfileIds = ["Auto_SOAP_Ecommerce_A"])

SignOn.GetUserExpiration(base_url,"RestUser1","Passw0rd3","3196F64B19200001")
SignOn.ChangePassword(base_url,"RestUser1","Passw0rd3","3196F64B19200001","Passw0rd4")
session_token = SignOn.DelegatedSignOn(base_url,"3196F64B19200001",IdentityToken)
session_token = SignOn.SignOnWithUsernamePassword(base_url,"RestUser1","Passw0rd4","3196F64B19200001")["SessionToken"]
SIS.SaveMerchantProfiles(base_url,session_token,ProfileId="Auto_SOAP_Ecommerce_A")
TMS.QueryTransactionsSummary(base_url,session_token,MerchantProfileIds = ["Auto_SOAP_Ecommerce_A"])
TPS.Authorize(base_url,session_token,"1257A00001")
TMS.QueryBatch(base_url,session_token,MerchantProfileIds = ["Auto_SOAP_Ecommerce_A"])
SIS.GetServiceInformation(base_url,session_token)
TPS.Capture(base_url,session_token,"1257A00001",auth_guid)
"""