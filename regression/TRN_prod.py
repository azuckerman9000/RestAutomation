from httprequests import SignOn, TPS, SIS

IdentityToken= 'PHNhbWw6QXNzZXJ0aW9uIE1ham9yVmVyc2lvbj0iMSIgTWlub3JWZXJzaW9uPSIxIiBBc3NlcnRpb25JRD0iX2I3MTRlMGIzLWE3MWQtNDExZC1hNDE4LTJlMDIxMTVkNjMzMSIgSXNzdWVyPSJJcGNBdXRoZW50aWNhdGlvbiIgSXNzdWVJbnN0YW50PSIyMDE0LTAzLTEwVDIyOjQzOjExLjA1OFoiIHhtbG5zOnNhbWw9InVybjpvYXNpczpuYW1lczp0YzpTQU1MOjEuMDphc3NlcnRpb24iPjxzYW1sOkNvbmRpdGlvbnMgTm90QmVmb3JlPSIyMDE0LTAzLTEwVDIyOjQzOjExLjA1OFoiIE5vdE9uT3JBZnRlcj0iMjAxNy0wMy0xMFQyMjo0MzoxMS4wNThaIj48L3NhbWw6Q29uZGl0aW9ucz48c2FtbDpBZHZpY2U+PC9zYW1sOkFkdmljZT48c2FtbDpBdHRyaWJ1dGVTdGF0ZW1lbnQ+PHNhbWw6U3ViamVjdD48c2FtbDpOYW1lSWRlbnRpZmllcj5BQjMzQzhCQUJFMzEzMDBDPC9zYW1sOk5hbWVJZGVudGlmaWVyPjwvc2FtbDpTdWJqZWN0PjxzYW1sOkF0dHJpYnV0ZSBBdHRyaWJ1dGVOYW1lPSJTQUsiIEF0dHJpYnV0ZU5hbWVzcGFjZT0iaHR0cDovL3NjaGVtYXMuaXBjb21tZXJjZS5jb20vSWRlbnRpdHkiPjxzYW1sOkF0dHJpYnV0ZVZhbHVlPkFCMzNDOEJBQkUzMTMwMEM8L3NhbWw6QXR0cmlidXRlVmFsdWU+PC9zYW1sOkF0dHJpYnV0ZT48c2FtbDpBdHRyaWJ1dGUgQXR0cmlidXRlTmFtZT0iU2VyaWFsIiBBdHRyaWJ1dGVOYW1lc3BhY2U9Imh0dHA6Ly9zY2hlbWFzLmlwY29tbWVyY2UuY29tL0lkZW50aXR5Ij48c2FtbDpBdHRyaWJ1dGVWYWx1ZT44Y2JjNDNjYi1lYjgzLTQxYWEtYjNkNy05NDBkOGFlYjM0YTg8L3NhbWw6QXR0cmlidXRlVmFsdWU+PC9zYW1sOkF0dHJpYnV0ZT48c2FtbDpBdHRyaWJ1dGUgQXR0cmlidXRlTmFtZT0ibmFtZSIgQXR0cmlidXRlTmFtZXNwYWNlPSJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcyI+PHNhbWw6QXR0cmlidXRlVmFsdWU+QUIzM0M4QkFCRTMxMzAwQzwvc2FtbDpBdHRyaWJ1dGVWYWx1ZT48L3NhbWw6QXR0cmlidXRlPjwvc2FtbDpBdHRyaWJ1dGVTdGF0ZW1lbnQ+PFNpZ25hdHVyZSB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC8wOS94bWxkc2lnIyI+PFNpZ25lZEluZm8+PENhbm9uaWNhbGl6YXRpb25NZXRob2QgQWxnb3JpdGhtPSJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzEwL3htbC1leGMtYzE0biMiPjwvQ2Fub25pY2FsaXphdGlvbk1ldGhvZD48U2lnbmF0dXJlTWV0aG9kIEFsZ29yaXRobT0iaHR0cDovL3d3dy53My5vcmcvMjAwMC8wOS94bWxkc2lnI3JzYS1zaGExIj48L1NpZ25hdHVyZU1ldGhvZD48UmVmZXJlbmNlIFVSST0iI19iNzE0ZTBiMy1hNzFkLTQxMWQtYTQxOC0yZTAyMTE1ZDYzMzEiPjxUcmFuc2Zvcm1zPjxUcmFuc2Zvcm0gQWxnb3JpdGhtPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwLzA5L3htbGRzaWcjZW52ZWxvcGVkLXNpZ25hdHVyZSI+PC9UcmFuc2Zvcm0+PFRyYW5zZm9ybSBBbGdvcml0aG09Imh0dHA6Ly93d3cudzMub3JnLzIwMDEvMTAveG1sLWV4Yy1jMTRuIyI+PC9UcmFuc2Zvcm0+PC9UcmFuc2Zvcm1zPjxEaWdlc3RNZXRob2QgQWxnb3JpdGhtPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwLzA5L3htbGRzaWcjc2hhMSI+PC9EaWdlc3RNZXRob2Q+PERpZ2VzdFZhbHVlPnQyYW0rMk9sRXpzU1dHVnVnOVR0a3BuMkNVST08L0RpZ2VzdFZhbHVlPjwvUmVmZXJlbmNlPjwvU2lnbmVkSW5mbz48U2lnbmF0dXJlVmFsdWU+TFdQa1JmME1FTitOVWo4aTRyWFcwZEVIQWRKcmU1bndFaGlpMWpSVU9Bbnd6aTNJT0NDNlZsUTBialkxQlhtSEZGN1doT3UxWlZzRUtRaWtlczZnRE04R2xKaUw0dHYwN2VYUkZlQWhWSWFLM29BTEpOc2VpUVpzMkRvVnJMSEZqajVjM3htNkxGb1Z3MThnNEFzVFc1YlorRDJrVW5FcU5JTlQ4bzJ5NVp1T2pLWU54cGJOQzJoZ1RZYjVoV0JzTTFjWEY3aWk5VUhudGFKeFg1dUVPenVVWVh0TW40K0hvMFQwS05SaFFVWmpQellBcHVZQWphL1RZSDQvT01LWkRvN0JDa1VRbHU2NnJicmJ0ZU11Z0lzRW0wcWJCUUNvQnRLUlp2a0JZZVZaMkZuZWJTeW5ieVpQL3I4OXNXQW53YnRIWk5FY3NnKzhicmowWFFLSyt3PT08L1NpZ25hdHVyZVZhbHVlPjxLZXlJbmZvPjxvOlNlY3VyaXR5VG9rZW5SZWZlcmVuY2UgeG1sbnM6bz0iaHR0cDovL2RvY3Mub2FzaXMtb3Blbi5vcmcvd3NzLzIwMDQvMDEvb2FzaXMtMjAwNDAxLXdzcy13c3NlY3VyaXR5LXNlY2V4dC0xLjAueHNkIj48bzpLZXlJZGVudGlmaWVyIFZhbHVlVHlwZT0iaHR0cDovL2RvY3Mub2FzaXMtb3Blbi5vcmcvd3NzL29hc2lzLXdzcy1zb2FwLW1lc3NhZ2Utc2VjdXJpdHktMS4xI1RodW1icHJpbnRTSEExIj54QVQzaU4yalZ5bkhkb1ZSMWxxdmlmU2tiVlE9PC9vOktleUlkZW50aWZpZXI+PC9vOlNlY3VyaXR5VG9rZW5SZWZlcmVuY2U+PC9LZXlJbmZvPjwvU2lnbmF0dXJlPjwvc2FtbDpBc3NlcnRpb24+'
MerchantProfileId = 'SnapProdGHC'
ServiceId = '4379D1300C'
base_url = "https://api.cip.goevo.com/2.1.25/REST/"

trn_ngt_sessiontoken = SignOn.SignOnWithToken(base_url,IdentityToken)
#SIS.SaveMerchantProfiles(base_url,trn_ngt_sessiontoken,ProfileId="SnapProdGHC",ServiceId="4379D1300C",TerminalId="54747",MerchantId="54747_EVO",ServiceName="EVO Intl GmbH BCP Host Capture")
#SIS.GetMerchantProfile(base_url,trn_ngt_sessiontoken,MerchantProfileId,ServiceId)
TPS.Authorize(base_url,trn_ngt_sessiontoken,ServiceId,MerchantProfileId=MerchantProfileId,CVData="123",CVDataProvided="Provided",PAN="4003000123456781",Expire="1215",ApplicationProfileId="1",CustomerData=None,EMVData=None,ApplicationConfigurationData=None,EcommerceSecurityData=None,AlternativeMerchantData=None,AVSData=None,IntlAVSData=None,Level2Data=None,InterchangeData=None)
