##### Service Ids #####
ServiceId_GenHC = "35EDC00001"
ServiceId_GenTC = "A175B00001"
ServiceId_NGTHC_Host = "1B04F00001"
ServiceId_eSvc_Host = "C668F00001"

##### Merchant Profile Ids #####
MPID_MOTO_HC = "Generic_MOTO_HC"
MPID_Ecomm_HC = "Generic_Ecomm_HC"
MPID_Retail_HC = "Generic_Retail_HC"
MPID_Restaurant_HC = "Generic_Restaurant_HC"
MPID_MOTO_TC = "Generic_MOTO_TC"
MPID_Ecomm_TC = "Generic_Ecomm_TC"
MPID_Retail_TC = "Generic_Retail_TC"
MPID_Restaurant_TC = "Generic_Restaurant_TC"
MPID_Retail_HC_NGTHC_Host = "NGT_H2H_HC"
MPID_Retail_HC_eSvc_Host = "eServices_H2H_HC"

Generic = {
           "Level2Data":{
                          "ServiceId":ServiceId_GenHC,
                          "MerchantProfileId":MPID_Restaurant_HC,
                          "ApplicationProfileId":"65360",
                          "CustomerData":None,                                                                       
                          "EMVData":None,
                          "ApplicationConfigurationData":None,                               
                          "EcommerceSecurityData":None,
                          "AlternativeMerchantData":None,                               
                          "InterchangeData":None,
                          "CardSecurityData":None,
                          "CustomerPresent":"NotSet",                               
                          "Track2Data":"4003000123456781=15125025432198712345",
                          "PAN":None,
                          "EntryMode":"Track2DataFromMSR",
                          "Level2Data":{"BaseAmount":"1.00","CompanyName":"Bababa","OrderNumber":"2","TaxExempt":{"IsTaxExempt":"Exempt"}}                     
                          },
           "OrderNumEcommHappy":{
                               "ServiceId":ServiceId_GenTC,
                               "MerchantProfileId":MPID_Ecomm_TC,
                               "CustomerData":None,                                                                       
                               "EMVData":None,
                               "ApplicationConfigurationData":None,
                               "CardSecurityData":None,
                               "EcommerceSecurityData":None,                               
                               "Level2Data":None,
                               "InterchangeData":None,
                               "CustomerPresent":"NotSet",
                               "TransactionDateTime":None,
                               "AlternativeMerchantData":None,
                               "OrderNumber":"45"                           
                               }
           }

Adaptor = {
           "NGT_EncTrack2" : {
                      "MerchantProfileId":MPID_Retail_HC_NGTHC_Host,
                      #"MerchantProfileId":"Kyle Test",
                      "ServiceId":ServiceId_NGTHC_Host,
                      #"ServiceId":"3CF9E00001",   
                      "CustomerData":None,                                                                       
                      "EMVData":None,
                      "ApplicationConfigurationData":None,
                      "CardSecurityData":None,
                      "CardData":None,
                      "EcommerceSecurityData":None,
                      "AlternativeMerchantData":None,
                      "Level2Data":None,
                      "InterchangeData":None,
                      "AppConfig":True,
                      "SecurePaymentAccountData":"174DDE8041A112B02EC04395838A1CA307BA4A64BA213317443C0A5C1E0F43C0615EA69615018FF1",
                      "DeviceSerialNumber":"88888806500285",
                      "VendorId":"3E3246482E",
                      "Amount":"36.00",
                      "EncryptionKeyId":"8888882750011620001F",
                      "EntryMode":"Track2DataFromMSR",
                      "CustomerPresent":"Present",
                      "assertions":[("exists","PaymentAccountDataToken",True),("exists","MaskedPAN",True),("isvalue","TransactionState","Authorized"),("isvalue","StatusCode","1")]                   
                      },
           "NGT_EncEMV" : {
                      "MerchantProfileId":MPID_Retail_HC_NGTHC_Host,
                      #"MerchantProfileId":"Kyle Test",
                      "ServiceId":ServiceId_NGTHC_Host,
                      #"ServiceId":"3CF9E00001",                      
                      "CustomerData":None,                                                                       
                      "EMVData":None,
                      "ApplicationConfigurationData":None,
                      "CardSecurityData":None,
                      "CardData":None,
                      "EcommerceSecurityData":None,
                      "AlternativeMerchantData":None,
                      "Level2Data":None,
                      "InterchangeData":None,
                      "AppConfig":True,
                      "SecureEMVData":"C00A8888882750011640005AC408476173FFFFFF0010C28201A8B33B0927BAADEA449D8948B7DC19FB9AC44BD3B0C7BD26137B4554A1CF89DAFE5A41F1E84BE50DD5603FA3DB3B698C2D99E221600C4C459733B2063462DD7AEF018F8AADCBC56E3416A9F35B7659A0B1307E712C6A60F73F1CC5ABC9B8E36EA2FAE6DC27F69BF702FD75F60987B5BC9E790B30922D299BDC750553C208DCBD5A560F9A759FE2ACF9EFFBFA94808344D0494DDB30EF221117361DB682225E5E7A1B2BAF0C11D03C75CEC518598978C429AE93DB36EDC8EF63B9CD7559F01C8513DDE1D21EB6265F42EAC16FB073C4F299CBEDDE97A4FA07112320A5D304F77604A1AFF06CEE4A74C3567C98D785C6E7D9167E6A78D334806D64000E03E8B8DB12814C2C7EC3F55A269D1282807882B139C8B09EC270037768286849A8584384B80041BB15E9801A009D16B2A4E8A48FA33DF4AFFC1CC2AEC9F4CCB2076F52349292D0A09842E0763A17872BFCC4CA3A293F3A67DE3F4252C7AB95135A833A8EF3FCF76F58657F264A2CAF2A25E3F69E2B2604D0EA76623278F23F61F1995485FAE36C2592DB19ED1DE090C360E6498B0878033AB9B0591B67EDA41E9DA5139339038AB3B414FA7CCBC70A8888882750011620004FC818C40EBD605D30807234C8FB1DE43EF87F80234128D19041394F07A0000000031010950502004080009B02E8005F201A56495341204143515549524552205445535420434152442030395F24032212319F02060000000010009F120F4352454449544F20444520564953419F1C0831313232333334349F26083ACA2B6EB44D4F549F2701809A031512119C01009F1A020840",
                      "DeviceSerialNumber":"88888827500116",
                      "VendorId":"3E3246482E",
                      "Amount":"10.00",                      
                      "EntryMode":"Track2DataFromMSR",
                      "CustomerPresent":"Present",
                      "assertions":[("exists","PaymentAccountDataToken",True),("exists","MaskedPAN",True),("isvalue","TransactionState","Authorized"),("isvalue","StatusCode","1")]                   
                      },
           "eSvc_EncEMV" : {
                      "MerchantProfileId":MPID_Retail_HC_eSvc_Host,                      
                      "ServiceId":ServiceId_eSvc_Host,                                           
                      "CustomerData":None,                                                                       
                      "EMVData":None,                      
                      "CardSecurityData":None,
                      "CardData":None,
                      "EcommerceSecurityData":None,
                      "AlternativeMerchantData":None,
                      "Level2Data":None,
                      "InterchangeData":None,
                      "AppConfig":True,
                      "SecureEMVData":"C00A88888827500116400083C408476173FFFFFF0010C28201A855138FD86A632232776A8D4CFBD49C1EB9F10B7A7783F340EAD803677A4CE91264085DCD443A76D9B5C8E9934E567AD690E69B95173903D754F75AF5154BD64D5E45689389345F7B45309B9B1F3CB161E0A30ADB826A71D564BC2ADAB7E941D04A6F902E1F5E9DCB181CA68A548B4FD3DDF46A672EDFA4B7BABAA17700A395529E2EB05AA1DE08190E1AAF8610CD3779964C18730B7FDF78578E781A74ACE32DCE6695CCBD6A9B9ED6329AE2D8DEA1EFED4B039A5DD129B80030F27E8309E311B301B6776BF74352E2594A379F347B3427C89192025926DD86E3616340520AEC30FA8F2282378B0B796FE3E8955C1C9DDCFD98C7C8E46176F746DE8FB3B80032C849228D5A8F1D40B2814DAF92097D3F2ECDD91754087583B1ABA191B55B81B6E955A236A09BAE552925AB7608850D0A243F5D66646CE14ED37C6BC4F65348315BB7CA4DBA7272A47CF3382BA0510D530A0FE750CA739F224599ED37182389FDC8A4F6DAF746A677114D39C2F5D52D6CE138406CB4A072786BB0FD6F5E083F3F92F43EBECDF0223A4BD194C862C8ABA8264DF772BF5E2EBF8EC06CB219A046D80F87C9D0B2283C5FC70A8888882750011620006AC818161691C32608D8F33FAE913EE7D21A4187368344A3B5DA514F07A0000000031010950502004080009B02E8005F201A56495341204143515549524552205445535420434152442030395F24032212319F02060000000010009F120F4352454449544F20444520564953419F1C0831313232333334349F2608F0DA3A02E8D6E3679F2701809A031512139C01009F1A020840",
                      "DeviceSerialNumber":"88888827500116",
                      "VendorId":"3E3246482E",
                      "CardholderIdType":"DigitalSig",
                      "CardholderAuthenticationEntity":"ICC",
                      "CardRetentionCapability":False,
                      "Amount":"10.00",                      
                      "EntryMode":"Track2DataFromMSR",
                      "CustomerPresent":"Present",
                      "assertions":[("exists","PaymentAccountDataToken",True),("exists","MaskedPAN",True),("isvalue","TransactionState","Authorized"),("isvalue","StatusCode","1")]                   
                      }
           }