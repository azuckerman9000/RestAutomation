from httprequests import SignOn, TPS, SIS, TMS
from testcases import GenericTests

base_url = "https://us002-dv-cip01.evosnap.local/2.1.23/TPS.svc"

Idt = ""
sessiontoken = SignOn.SignOnWithToken(base_url,Idt)

TPS.Authorize(base_url,sessiontoken,**GenericTests.AllRules["BillingAdrHappy"])