from httprequests import SignOn, TPS, SIS
from testcases import SBXregression

base_url = "https://api.ciptest.goevo.local/2.1.26/REST/"

Idt = "PHNhbWw6QXNzZXJ0aW9uIE1ham9yVmVyc2lvbj0iMSIgTWlub3JWZXJzaW9uPSIxIiBBc3NlcnRpb25JRD0iXzdjNTU0NDhmLTNkYWUtNDc0NS04MDBhLWU4ZWI3YjZjZDg4NCIgSXNzdWVyPSJJcGNBdXRoZW50aWNhdGlvbiIgSXNzdWVJbnN0YW50PSIyMDE1LTA5LTEwVDE5OjMwOjI3LjI5MVoiIHhtbG5zOnNhbWw9InVybjpvYXNpczpuYW1lczp0YzpTQU1MOjEuMDphc3NlcnRpb24iPjxzYW1sOkNvbmRpdGlvbnMgTm90QmVmb3JlPSIyMDE1LTA5LTEwVDE5OjMwOjI3LjI5MVoiIE5vdE9uT3JBZnRlcj0iMjAxOC0wOS0xMFQxOTozMDoyNy4yOTFaIj48L3NhbWw6Q29uZGl0aW9ucz48c2FtbDpBZHZpY2U+PC9zYW1sOkFkdmljZT48c2FtbDpBdHRyaWJ1dGVTdGF0ZW1lbnQ+PHNhbWw6U3ViamVjdD48c2FtbDpOYW1lSWRlbnRpZmllcj40REJBMzZDOEZENTAwMDAxPC9zYW1sOk5hbWVJZGVudGlmaWVyPjwvc2FtbDpTdWJqZWN0PjxzYW1sOkF0dHJpYnV0ZSBBdHRyaWJ1dGVOYW1lPSJTQUsiIEF0dHJpYnV0ZU5hbWVzcGFjZT0iaHR0cDovL3NjaGVtYXMuaXBjb21tZXJjZS5jb20vSWRlbnRpdHkiPjxzYW1sOkF0dHJpYnV0ZVZhbHVlPjREQkEzNkM4RkQ1MDAwMDE8L3NhbWw6QXR0cmlidXRlVmFsdWU+PC9zYW1sOkF0dHJpYnV0ZT48c2FtbDpBdHRyaWJ1dGUgQXR0cmlidXRlTmFtZT0iU2VyaWFsIiBBdHRyaWJ1dGVOYW1lc3BhY2U9Imh0dHA6Ly9zY2hlbWFzLmlwY29tbWVyY2UuY29tL0lkZW50aXR5Ij48c2FtbDpBdHRyaWJ1dGVWYWx1ZT4wMjNiNmRlMy1kOWIwLTQ1YTItYmMwMC1iZGI0N2VlZjE0ZjU8L3NhbWw6QXR0cmlidXRlVmFsdWU+PC9zYW1sOkF0dHJpYnV0ZT48c2FtbDpBdHRyaWJ1dGUgQXR0cmlidXRlTmFtZT0ibmFtZSIgQXR0cmlidXRlTmFtZXNwYWNlPSJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcyI+PHNhbWw6QXR0cmlidXRlVmFsdWU+NERCQTM2QzhGRDUwMDAwMTwvc2FtbDpBdHRyaWJ1dGVWYWx1ZT48L3NhbWw6QXR0cmlidXRlPjwvc2FtbDpBdHRyaWJ1dGVTdGF0ZW1lbnQ+PFNpZ25hdHVyZSB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC8wOS94bWxkc2lnIyI+PFNpZ25lZEluZm8+PENhbm9uaWNhbGl6YXRpb25NZXRob2QgQWxnb3JpdGhtPSJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzEwL3htbC1leGMtYzE0biMiPjwvQ2Fub25pY2FsaXphdGlvbk1ldGhvZD48U2lnbmF0dXJlTWV0aG9kIEFsZ29yaXRobT0iaHR0cDovL3d3dy53My5vcmcvMjAwMC8wOS94bWxkc2lnI3JzYS1zaGExIj48L1NpZ25hdHVyZU1ldGhvZD48UmVmZXJlbmNlIFVSST0iI183YzU1NDQ4Zi0zZGFlLTQ3NDUtODAwYS1lOGViN2I2Y2Q4ODQiPjxUcmFuc2Zvcm1zPjxUcmFuc2Zvcm0gQWxnb3JpdGhtPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwLzA5L3htbGRzaWcjZW52ZWxvcGVkLXNpZ25hdHVyZSI+PC9UcmFuc2Zvcm0+PFRyYW5zZm9ybSBBbGdvcml0aG09Imh0dHA6Ly93d3cudzMub3JnLzIwMDEvMTAveG1sLWV4Yy1jMTRuIyI+PC9UcmFuc2Zvcm0+PC9UcmFuc2Zvcm1zPjxEaWdlc3RNZXRob2QgQWxnb3JpdGhtPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwLzA5L3htbGRzaWcjc2hhMSI+PC9EaWdlc3RNZXRob2Q+PERpZ2VzdFZhbHVlPndCU2dqb0s3U0ZCQmlDZjBnaWhEQ2x0L24wRT08L0RpZ2VzdFZhbHVlPjwvUmVmZXJlbmNlPjwvU2lnbmVkSW5mbz48U2lnbmF0dXJlVmFsdWU+WjRXTjcwY3FyU0d3NElxUjVOcC8zU1NTTVZ1YU0vNFVaQysyQTNNWFVKRTh6SDVqdDh6ZVFEYUliOEh5aWpGWTJseGU1TFBFeDczVGdqZ3RvemdpbDUyME9sQ2p5Q25FdlFXdGg4RHg4Y1h2VHp2OHlrNmFKbUE3MGpDZlB3ZjB5WUlLd1dVbWlVbzl1NG1FVFpmQ1VZZzNIWGZWRUxFZ2hOZ0Q0cVRQdkpDSStlWVRQQm9GKy9lOGF4U3JkR1R1QTdEUXJxaEFpdmRySVRDeTZmL2VNcWkrc3kzbEZScG1OVUtkVEhQek1YTTlJdU1KVXB0VjA0dHNBNTJNMmR4ZnppdVRvTXA2QU85RUlUai9nUURxeHlFdjlCMkI3c2VYVUhza256MkxsTkFJeEZBbUhSZGJsV0tLdkY3T1hPdTFmSFlYN1c0OFN2QlVaNjNpR05uelpRPT08L1NpZ25hdHVyZVZhbHVlPjxLZXlJbmZvPjxvOlNlY3VyaXR5VG9rZW5SZWZlcmVuY2UgeG1sbnM6bz0iaHR0cDovL2RvY3Mub2FzaXMtb3Blbi5vcmcvd3NzLzIwMDQvMDEvb2FzaXMtMjAwNDAxLXdzcy13c3NlY3VyaXR5LXNlY2V4dC0xLjAueHNkIj48bzpLZXlJZGVudGlmaWVyIFZhbHVlVHlwZT0iaHR0cDovL2RvY3Mub2FzaXMtb3Blbi5vcmcvd3NzL29hc2lzLXdzcy1zb2FwLW1lc3NhZ2Utc2VjdXJpdHktMS4xI1RodW1icHJpbnRTSEExIj5QTE5QWDBOYmJZeEE3TVpxd2hSZkxJcFd2VkE9PC9vOktleUlkZW50aWZpZXI+PC9vOlNlY3VyaXR5VG9rZW5SZWZlcmVuY2U+PC9LZXlJbmZvPjwvU2lnbmF0dXJlPjwvc2FtbDpBc3NlcnRpb24+"
fourd_sessiontoken = SignOn.SignOnWithToken(base_url,Idt) #For ServiceKey 4DBA36C8FD500001
"""
### Basic Sandbox Tests ###
for tcname, testcase in SBXregression.Generic_Sandbox.items():
    print(tcname)
    TPS.Authorize(base_url,fourd_sessiontoken,**testcase)
    print("-------------------")
    
### MPI Tests ###
print("3DSecure_MPI Workflow")
MPI_Resp = TPS.Authorize(base_url,fourd_sessiontoken,**SBXregression.MPI["MPI_3DSecure"])
if MPI_Resp["PaymentAuthorizationRequest"]:
    PaRes = TPS.GetPARes(MPI_Resp["PaymentAuthorizationRequest"])
    GUID = TPS.Resubmit(base_url,fourd_sessiontoken,TxnGUID=MPI_Resp["TransactionId"],PaymentAuthorizationResponse=PaRes,**SBXregression.MPI["Resubmit3D"])
    GUID2 = TPS.Capture(base_url,fourd_sessiontoken,SBXregression.MPI["MPI_3DSecure"]["ServiceId"],GUID)
    TPS.ReturnById(base_url,fourd_sessiontoken,SBXregression.MPI["MPI_3DSecure"]["ServiceId"],GUID2,TenderData=None,Amount="1.00")
    print("-------------------")
TPS.Authorize(base_url,fourd_sessiontoken,**SBXregression.MPI["MPI_NotEnrolled"])
print("-------------------")

### PINDebit Tests ###
PINDebit_GUID = TPS.AuthorizeAndCapture(base_url,fourd_sessiontoken,**SBXregression.PINDebit["PINDebit_Basic"])["TransactionId"]
TPS.ReturnById(base_url,fourd_sessiontoken,TxnGUID=PINDebit_GUID,**SBXregression.PINDebit["PINDebit_Basic"])
print("-------------------")

### Email Receipts ###
for tcname, testcase in SBXregression.EmailReceipt.items():
    print(tcname)
    Email_Guid = TPS.Authorize(base_url,fourd_sessiontoken,**testcase)["TransactionId"]
    TPS.SendReceipt(base_url,fourd_sessiontoken,Email_Guid,"alan.zuckerman@evopayments.com")
    print("-------------------")
"""    
resp = TPS.Authorize(base_url,fourd_sessiontoken,**SBXregression.Generic_Sandbox["EMVData"])
UndoData = {
            "Track2Data":"4003000123456781=15125025432198712345",
            "CardSecurityData": None,
            "EcommerceSecurityData": None,
            "CardholderIdType": "Manual",
            "TenderType": "ProcessAsCredit",
            "TokenInformation": None,
            "EMVData": {
                "ApplicationId": "A0000001523010",
                "ApplicationInterchangeProfile": "5800",
                "ApplicationTransactionCount": "0001",
                "ApplicationUsageControl": None,
                "ApplicationVersionNumber": "0001",
                "AuthorizationAmount": "000000003700",
                "AuthorizationResponseCode": None,
                "CVMList": "0000000000000000420142035E031F03",
                "CVMResults": "5E0300",
                "CardSequenceNumber": "01",
                "CashBackAmount": None,
                "CryptogramInformationData": "00",
                "Cryptogram": "566F1395FED5833B",
                "CustomerExclusiveData": None,
                "DedicatedFileName": None,
                "FormFactorIndicator": None,
                "InterfaceDeviceSerialNumber": "15900179",
                "IssuerActionDefault": "F040C42800",
                "IssuerActionDenial": None,
                "IssuerActionOnline": None,
                "IssuerApplicationData": "0105200003200000",
                "IssuerScriptResults": None,
                "LocalTransactionDate": "160418",
                "TerminalCapability": "60B8C8",
                "TerminalCountryCode": "840",
                "TerminalType": "22",
                "TerminalVerifyResult": "4000008040",
                "CurrencyCode": "840",
                "SequenceNumber": "00001108",
                "TransactionType": "00",
                "UnpredictableNumber": "78082F1F"
            },
        "ForceVoid": False,
        "TransactionCode": "NotSet",
        "UndoReason": "CustomerCancellation"
            }
TPS.Undo(base_url,fourd_sessiontoken,SBXregression.Generic_Sandbox["EMVData"]["ServiceId"],resp["TransactionId"],**UndoData)
