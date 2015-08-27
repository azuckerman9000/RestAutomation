from httprequests import SignOn, TPS, SIS
from miscutils import dataquery

base_url = "https://api.ciptest.goevo.local/2.1.23/REST/"

# Get Test Data From database
trn_ngt_IdentityToken = dataquery.getIdentityToken("TEST","6B2866C8FD500001")
ptrc_IdentityToken = dataquery.getIdentityToken("TEST","183B6712DC700001")
eSvc_IdentityToken = dataquery.getIdentityToken("TEST","DD6265F71F100001")

trn_serviceId = dataquery.getServiceId("TEST","EvoIntl","HostCap","Sandbox")
eSvc_serviceId = dataquery.getServiceId("TEST","eServices","HostCap","Host")
ngt_serviceId = dataquery.getServiceId("TEST","NGTrans","HostCap","Host")
ptrc_serviceId = dataquery.getServiceId("TEST","Paytrace","HostCap","Host")

ngt_MerchProfId = "HCRestaurantMerch"
#trn_MerchProfId = "EVOIntl_SOAP_Ecommerce_HostCap_TestHost"
trn_MerchProfId = "TRN_Ecommerce_SBX"
ptrc_MerchProfId = "PayTrace_SOAP_Restaurant_HC_TestHost"
eSvc_MerchProfId = "eServices_SOAP_CardPresent_HC"

#TRON Tests
trn_ngt_sessiontoken = SignOn.SignOnWithToken(base_url,trn_ngt_IdentityToken)
TPS.Authorize(base_url,trn_ngt_sessiontoken,"911C800001",MerchantProfileId=ngt_MerchProfId,CustomerPresent="Present",EcommerceSecurityData=None,CardSecurityData=None)


#TPS.Authorize(base_url,trn_ngt_sessiontoken,trn_serviceId,MerchantProfileId=trn_MerchProfId,CVData="123",CVDataProvided="Provided",EcommerceSecurityData=None,AVSData=None)
"""
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

"""
#SIS.SaveMerchantProfiles(base_url,trn_ngt_sessiontoken,ProfileId="TRN_Ecommerce_SBX",ServiceId=trn_serviceId)
#TPS.Authorize(base_url,trn_ngt_sessiontoken,trn_serviceId,MerchantProfileId=trn_MerchProfId,CVData="123",CVDataProvided="Provided",CustomerId="3",Address={"Street1":"1st","City":"Denver","StateProvince":"CO","PostalCode":"80202","CountryCode":"USA"})

#TPS.Authorize(base_url,trn_ngt_sessiontoken,trn_serviceId,MerchantProfileId=trn_MerchProfId,CVData="123",CVDataProvided="Provided",CustomerId="3",BusinessName="Apple",InternationalAddress={"HouseNumber":"1234","Street1":"1st","City":"Denver","StateProvince":"CO","PostalCode":"80202","CountryCode":"USA"})
"""
TPS.Authorize(base_url,trn_ngt_sessiontoken,trn_serviceId,MerchantProfileId=trn_MerchProfId,CVData="123",CVDataProvided="Provided",CustomerId="3",BusinessName="Apple",InternationalAddress={"HouseNumber":"1234","Street1":"1st","City":"Denver","StateProvince":"Colorado","PostalCode":"80202","CountryCode":"USA"})
TPS.Authorize(base_url,trn_ngt_sessiontoken,trn_serviceId,MerchantProfileId=trn_MerchProfId,CVData="123",CVDataProvided="Provided",CustomerId="3",BusinessName="Apple",InternationalAddress={"HouseNumber":"1234","Street1":"1st","City":"Denver","PostalCode":"80202","CountryCode":"USA"})
TPS.Authorize(base_url,trn_ngt_sessiontoken,trn_serviceId,MerchantProfileId=trn_MerchProfId,CVData="123",CVDataProvided="Provided",CustomerId="3",BusinessName="Apple",InternationalAddress={"HouseNumber":"1234","Street1":"1st","City":"Denver","StateProvince":"CO","PostalCode":"80202","CountryCode":"CAN"})
TPS.Authorize(base_url,trn_ngt_sessiontoken,trn_serviceId,MerchantProfileId=trn_MerchProfId,CVData="123",CVDataProvided="Provided",CustomerId="3",BusinessName="Apple",InternationalAddress={"HouseNumber":"1234","Street1":"1st","City":"Denver","StateProvince":"BC","PostalCode":"80202","CountryCode":"CAN"})
TPS.Authorize(base_url,trn_ngt_sessiontoken,trn_serviceId,MerchantProfileId=trn_MerchProfId,CVData="123",CVDataProvided="Provided",CustomerId="3",BusinessName="Apple",InternationalAddress={"HouseNumber":"1234","Street1":"1st","City":"Denver","StateProvince":"British Columbia","PostalCode":"80202","CountryCode":"CAN"})
"""
#TPS.Authorize(base_url,trn_ngt_sessiontoken,trn_serviceId,MerchantProfileId=trn_MerchProfId,CVData="123",CVDataProvided="Provided",CustomerId="3",BusinessName="Apple",InternationalAddress={"HouseNumber":"1234","Street1":"1st","City":"Denver","PostalCode":"80202","CountryCode":"FRA"},AVSData=None,TokenData="sdhjfh84hr843hr",TokenIndicator="VPAS",XID="firjti4")
#Magensa
#SIS.SaveMerchantProfiles(base_url,trn_ngt_sessiontoken,ProfileId="MagensaMerch",ServiceId="A121700011")
#TPS.Authorize(base_url,trn_ngt_sessiontoken,ServiceId="A121700011",MerchantProfileId="MagensaMerch",EcommerceSecurityData=None,CardData=None,InternationalAVSData=None,SecurePaymentAccountData="6425239DBCFCF994F8EFCC14D0E5A3F06566F186F5C59DEB957CBE1DDAF20319CB56A5E07ACC1E46",EncryptionKeyId="9011880B1CBB6500007B",IdentificationInformation="1C7A9CE5FAFA9F20EE1F2A7D2C8C49DA07BAF2AD4A107FB0DA2F86FDEE0801CD53495FFD8141F4328D8B08B0569A1B33BBA25A8DD0805765",SwipeStatus="61401000")
#TPS.Authorize(base_url,trn_ngt_sessiontoken,ServiceId="A021700011",MerchantProfileId="ReDMerch",EcommerceSecurityData=None,InternationalAVSData=None)