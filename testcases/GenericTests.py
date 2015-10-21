##### Generic Sandbox Tests for 24R1 on ServiceKey 4DBA36C8FD500001 #####

##### Service Ids #####
ServiceId_GenHC = "35EDC00001"
ServiceId_GenTC = "A175B00001"

##### Merchant Profile Ids #####
MPID_MOTO_HC = "Generic_MOTO_HC"
MPID_Ecomm_HC = "Generic_Ecomm_HC"
MPID_Retail_HC = "Generic_Retail_HC"
MPID_Restaurant_HC = "Generic_Restaurant_HC"
MPID_MOTO_TC = "Generic_MOTO_TC"
MPID_Ecomm_TC = "Generic_Ecomm_TC"
MPID_Retail_TC = "Generic_Retail_TC"
MPID_Restaurant_TC = "Generic_Restaurant_TC"

##### Test Cases #####

AuthOnly = {
            "CustomerPresent1":{
                               "ServiceId":ServiceId_GenTC,
                               "MerchantProfileId":MPID_Ecomm_TC,
                               "CustomerData":None,                                                                       
                               "EMVData":None,
                               "ApplicationConfigurationData":None,
                               "CardSecurityData":None,
                               "EcommerceSecurityData":None,
                               "AlternativeMerchantData":None,
                               "Level2Data":None,
                               "InterchangeData":None,
                               "CustomerPresent":"NotSet",
                               "TransactionDateTime":None
                               },
            "CustomerPresent2":{
                               "ServiceId":ServiceId_GenTC,
                               "MerchantProfileId":MPID_MOTO_TC,
                               "ApplicationProfileId":"65360",
                               "CustomerData":None,                                                                       
                               "EMVData":None,
                               "ApplicationConfigurationData":None,
                               "CardSecurityData":None,
                               "EcommerceSecurityData":None,
                               "AlternativeMerchantData":None,
                               "Level2Data":None,
                               "InterchangeData":None,
                               "CustomerPresent":"NotSet"
                               #"EmployeeId":None
                               },
            "CustomerPresent3":{
                               "ServiceId":ServiceId_GenTC,
                               "MerchantProfileId":MPID_Retail_TC,
                               #"ServiceId":"3CF9E00001",
                               #"MerchantProfileId":"Kyle Test",
                               "ApplicationProfileId":"65360",
                               "CustomerData":None,                                                                       
                               "EMVData":None,
                               "ApplicationConfigurationData":None,
                               "CardSecurityData":None,
                               "EcommerceSecurityData":None,
                               "AlternativeMerchantData":None,
                               "Level2Data":None,
                               "InterchangeData":None,
                               "CustomerPresent":"NotSet",
                               "Track2Data":"4003000123456781=15125025432198712345",
                               "PAN":None,
                               "EntryMode":"Track2DataFromMSR"                                                            
                               },
            "CustomerPresent4":{
                               "ServiceId":ServiceId_GenTC,
                               "MerchantProfileId":MPID_Restaurant_TC,
                               "ApplicationProfileId":"65360",
                               "CustomerData":None,                                                                       
                               "EMVData":None,
                               "ApplicationConfigurationData":None,
                               "CardSecurityData":None,
                               "EcommerceSecurityData":None,
                               "AlternativeMerchantData":None,
                               "Level2Data":None,
                               "InterchangeData":None,
                               "CustomerPresent":"NotSet"
                               }
            }

AllRules  = {
            "AcctTypeReq":{
                               "ServiceId":ServiceId_GenHC,
                               "MerchantProfileId":MPID_Restaurant_HC,
                               "ApplicationProfileId":"65360",
                               "CustomerData":None,                                                                       
                               "EMVData":None,
                               "ApplicationConfigurationData":None,                               
                               "EcommerceSecurityData":None,
                               "AlternativeMerchantData":None,
                               "Level2Data":None,
                               "InterchangeData":None,
                               "AVSData":None,
                               "InternationalAVSData":None,
                               "CustomerPresent":"NotSet",
                               "KeySerialNumber":"856290000060027C",
                               "PIN":"D8BC0FAF9BBD9B17",
                               "Track2Data":"4003000123456781=15125025432198712345",
                               "PAN":None,
                               "EntryMode":"Track2DataFromMSR"                         
                            },
             "BillingAdrHappy":{
                               "ServiceId":ServiceId_GenHC,
                               "MerchantProfileId":MPID_Restaurant_HC,
                               "ApplicationProfileId":"65360",
                               "ShippingData":None,                                                                       
                               "EMVData":None,
                               "ApplicationConfigurationData":None,                               
                               "EcommerceSecurityData":None,
                               "AlternativeMerchantData":None,
                               "Level2Data":None,
                               "InterchangeData":None,
                               "CardSecurityData":None,
                               "CustomerPresent":"NotSet",                               
                               "Track2Data":"4003000123456781=15125025432198712345",
                               "PAN":None,
                               "EntryMode":"Track2DataFromMSR",
                               "Address":{"Street1":"1st","City":"Denver","PostalCode":"80202","CountryCode":"USA"}                         
                            },
             "BillingAdrSad":{
                               "ServiceId":ServiceId_GenHC,
                               "MerchantProfileId":MPID_Restaurant_HC,
                               "ApplicationProfileId":"65360",
                               "ShippingData":None,                                                                       
                               "EMVData":None,
                               "ApplicationConfigurationData":None,                               
                               "EcommerceSecurityData":None,
                               "AlternativeMerchantData":None,
                               "Level2Data":None,
                               "InterchangeData":None,
                               "CardSecurityData":None,
                               "CustomerPresent":"NotSet",                               
                               "Track2Data":"4003000123456781=15125025432198712345",
                               "PAN":None,
                               "EntryMode":"Track2DataFromMSR",
                               "Address":{"Street1":"1st","CountryCode":"USA"}                         
                            },
             "CustServPhone":{
                               "ServiceId":ServiceId_GenTC,
                               "MerchantProfileId":MPID_MOTO_TC,
                               "ApplicationProfileId":"65360",
                               "CustomerData":None,                                                                       
                               "EMVData":None,
                               "ApplicationConfigurationData":None,
                               "CardSecurityData":None,
                               "EcommerceSecurityData":None,
                               "AlternativeMerchantData":None,
                               "Level2Data":None,
                               "InterchangeData":None,
                               "CustomerPresent":"NotSet"
                               #"EmployeeId":None
                               },           
            }