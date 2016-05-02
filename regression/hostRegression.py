from httprequests import SignOn, TPS, SIS
from testcases import testhostregression
from miscutils import dataquery

base_url = "https://api.ciptest.goevo.local/2.1.26/REST/"

sixb_sessiontoken = SignOn.SignOnWithToken(base_url,dataquery.getIdentityToken("TEST","6B2866C8FD500001"))

#SIS.SaveMerchantProfiles(base_url,sixb_sessiontoken,**testhostregression.NGT_HC_MPIDs["RetailHC"])
TPS.Authorize(base_url,sixb_sessiontoken,**testhostregression.NGTrans["Retail_Track2"])
