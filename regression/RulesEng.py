from httprequests import SignOn, TPS, SIS
from testcases import CWSRules24R1
from miscutils import dataquery

base_url = "https://api.ciptest.goevo.local/2.1.23/REST/"

sessiontoken = SignOn.SignOnWithToken(base_url,dataquery.getIdentityToken("TEST","6B2866C8FD500001"))

Scenario_Address = ["CustBillingAddress1","CustBillingAddress2","CustShippingAddress1","CustShippingAddress2"]
Scenario_IntlAddress = ["CustIntlBillingAddress1"]
Scenario_IntlAVS = ["IntlAVS1","IntlAVS2"]
Scenario_Sig = ["SigCaptured"]
Scenario_Ecom = ["EcommSecurityData"]
Scenario_CustPres = ["CustPresent"]
for testcase in Scenario_CustPres:
    TPS.Authorize(base_url,sessiontoken,**CWSRules24R1.TPSTestCases[testcase])
