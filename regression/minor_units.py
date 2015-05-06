from httprequests import SignOn, TPS
from miscutils import dataquery

base_url = "https://api.ciptest.goevo.local/2.1.22/REST/"

# Get Test Data From database
trn_ngt_IdentityToken = dataquery.getIdentityToken("TEST","6B2866C8FD500001")
ptrc_IdentityToken = dataquery.getIdentityToken("TEST","183B6712DC700001")
eSvc_IdentityToken = dataquery.getIdentityToken("TEST","DD6265F71F100001")

trn_serviceId = dataquery.getServiceId("TEST","EvoIntl","HostCap","Host")
eSvc_serviceId = dataquery.getServiceId("TEST","eServices","HostCap","Host")
ngt_serviceId = dataquery.getServiceId("TEST","NGTrans","HostCap","Host")
ptrc_serviceId = dataquery.getServiceId("TEST","Paytrace","HostCap","Host")

ngt_MerchProfId = "RetailMerch"
trn_MerchProfId = "EVOIntl_SOAP_Ecommerce_HostCap_TestHost"
ptrc_MerchProfId = "PayTrace_SOAP_Restaurant_HC_TestHost"
eSvc_MerchProfId = "eServices_SOAP_CardPresent_HC"

#TRON Tests
trn_ngt_sessiontoken = SignOn.SignOnWithToken(base_url,trn_ngt_IdentityToken)
TPS.Authorize(base_url,trn_ngt_sessiontoken,trn_serviceId,MerchantProfileId=trn_MerchProfId,CVData="123",CVDataProvided="Provided")
TPS.Authorize(base_url,trn_ngt_sessiontoken,trn_serviceId,MerchantProfileId=trn_MerchProfId,CVData="123",CVDataProvided="Provided",Amount="1")
TPS.Authorize(base_url,trn_ngt_sessiontoken,trn_serviceId,MerchantProfileId=trn_MerchProfId,CVData="123",CVDataProvided="Provided",Amount="1.001")
TPS.Authorize(base_url,trn_ngt_sessiontoken,trn_serviceId,MerchantProfileId=trn_MerchProfId,CVData="123",CVDataProvided="Provided",Amount="1.1")
TPS.Authorize(base_url,trn_ngt_sessiontoken,trn_serviceId,MerchantProfileId=trn_MerchProfId,CVData="123",CVDataProvided="Provided",Amount="0.002")
TPS.Authorize(base_url,trn_ngt_sessiontoken,trn_serviceId,MerchantProfileId=trn_MerchProfId,CVData="123",CVDataProvided="Provided",Amount="2200.")

#NGTrans Tests
TPS.Authorize(base_url,trn_ngt_sessiontoken,ngt_serviceId,MerchantProfileId=ngt_MerchProfId,CustomerPresent="Present")

#eServices Tests
eSvc_sessiontoken = SignOn.SignOnWithToken(base_url,eSvc_IdentityToken)
TPS.Authorize(base_url,eSvc_sessiontoken,eSvc_serviceId,MerchantProfileId=eSvc_MerchProfId,AppConfig=True,CVData="123",CVDataProvided="Provided",CustomerPresent="Present",PAN="4761739001010119",Entrymode="ChipReliable",CardholderAuthenticationEntity="ICC",CardholderIdType="Manual")

#Paytrace Tests
ptrc_sessiontoken = SignOn.SignOnWithToken(base_url,ptrc_IdentityToken)
TPS.Authorize(base_url,ptrc_sessiontoken,ptrc_serviceId,MerchantProfileId=ptrc_MerchProfId,CVData="123",CVDataProvided="Provided",CustomerPresent="Present")



