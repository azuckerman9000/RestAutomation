### All for 6B2866C8FD500001 ServiceKey ###

### ServiceIds ###
ServiceId_NGTHC_Host = "1B04F00001"
ServiceId_NGTTC_Host = "1256B00001"
ServiceId_TRNHC_Host = "A2A8200001"

### MerchantProfileIds ###
MPID_NGTHC_Ecomm = "NGTHC_Host_Ecomm_Reg"
MPID_NGTHC_MOTO = "NGTHC_Host_MOTO_Reg"
MPID_NGTHC_Retail = "NGTHC_Host_Retail_Reg"
MPID_NGTHC_Restaurant = "NGTHC_Host_Restaurant_Reg"




### MerchantProfiles ###

NGT_HC_MPIDs = {
                "EcommHC": {
                            "ProfileId": MPID_NGTHC_Ecomm,
                            "ServiceId":ServiceId_NGTHC_Host,
                            "TerminalId":"98765432160601",
                            "MerchantId":"6000006",
                            "IndustryType":"Ecommerce",
                            "EntryMode":"Keyed",
                            "CustomerPresent":"Ecommerce",
                            "CardBrandIdentifiers_3DSecure":None
                            },
                "MOTOHC": {
                            "ProfileId": MPID_NGTHC_MOTO,
                            "ServiceId":ServiceId_NGTHC_Host,
                            "TerminalId":"98765432160601",
                            "MerchantId":"6000006",
                            "IndustryType":"MOTO",
                            "EntryMode":"Keyed",
                            "CustomerPresent":"MOTOCC",
                            "CardBrandIdentifiers_3DSecure":None
                            },
                "RetailHC": {
                            "ProfileId": MPID_NGTHC_Retail,
                            "ServiceId":ServiceId_NGTHC_Host,
                            "TerminalId":"98765432160601",
                            "MerchantId":"6000006",
                            "IndustryType":"Retail",
                            "EntryMode":"Track2DataFromMSR",
                            "CustomerPresent":"Present",
                            "CardBrandIdentifiers_3DSecure":None
                            },
                "RestaurantHC": {
                            "ProfileId": MPID_NGTHC_Restaurant,
                            "ServiceId":ServiceId_NGTHC_Host,
                            "TerminalId":"98765432160601",
                            "MerchantId":"6000006",
                            "IndustryType":"Restaurant",
                            "EntryMode":"Track2DataFromMSR",
                            "CustomerPresent":"Present",
                            "CardBrandIdentifiers_3DSecure":None
                            }
                }

NGTrans = {
           "Retail_EncTrack2" : {
                      "MerchantProfileId":MPID_NGTHC_Retail,                      
                      "ServiceId":ServiceId_NGTHC_Host,                        
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
           "Retail_Track2" : {
                    "MerchantProfileId":MPID_NGTHC_Retail,                      
                    "ServiceId":ServiceId_NGTHC_Host,
                    "CustomerData":None,
                    "AlternativeMerchantData":None,
                    "ApplicationConfigurationData":None,
                    "EcommerceSecurityData":None,
                    "EMVData":None,
                    "EmailReceipt":None,
                    "GeoLocation":None,
                    "InterchangeData":None,
                    "Level2Data":None,
                    "CardSecurityData":None,                                    
                    "Track2Data":"374245455400001=140820112091234500000",
                    "PAN":None,
                    "CardType":"AmericanExpress",
                    "CustomerPresent":"Present",
                    "EntryMode":"Track2DataFromMSR",
                    "Amount":"10.00",
                    "assertions":[("exists","PaymentAccountDataToken",True),("exists","MaskedPAN",True),("isvalue","TransactionState","Authorized"),("isvalue","StatusCode","000")]                                      
                    },
           "NGT_EncEMV" : {
                      "MerchantProfileId":MPID_NGTHC_Retail,                      
                      "ServiceId":ServiceId_NGTHC_Host,
                      "ApplicationProfileId":"5680",                      
                      "CustomerData":None,                                                                       
                      "EMVData":None,
                      "ApplicationConfigurationData":None,
                      "CardSecurityData":None,
                      "AVSData":None,
                      "InternationalAVSData":None,
                      "CVDataProvided":"NotSet",
                      "CardData":None,
                      "EcommerceSecurityData":None,
                      "AlternativeMerchantData":None,
                      "Level2Data":None,
                      "InterchangeData":None,
                      "AppConfig":True,
                      "SecureEMVData":"4F07A0000000041010500A4D41535445524341524457115413330000000011D25126010000000000820230008407A0000000041010950500000080009A031512169B02E8009C01005F2A0208405F3401039F02060000000020009F03060000000000009F0607A00000000410109F090200029F10120210A5800F040000000000000000000000FF9F1101019F120A4D6173746572436172649F1A0208409F1B04000000009F1E0838313238303539359F21032058189F26081CB1BBBDDDFDC7DF9F2701809F3303E0F8C89F34034103029F3501229F360200279F3704B508EDBD9F3901059F4005F000F0A0019F4104000000289F530152",
                      "DeviceSerialNumber":"88888806500285",
                      "VendorId":"3E3246482E",
                      "Amount":"36.00",
                      "EncryptionKeyId":"8888882750011620001F",               
                      "EntryMode":"ChipReliable",
                      "CustomerPresent":"Present",
                      "assertions":[("exists","PaymentAccountDataToken",True),("exists","MaskedPAN",True),("isvalue","TransactionState","Authorized"),("isvalue","StatusCode","1")]                   
                      },
           "NGT_EncEMV2" : {
                      "MerchantProfileId":MPID_NGTHC_Retail,                      
                      "ServiceId":ServiceId_NGTHC_Host,
                      "ApplicationProfileId":"5680",                      
                      "CustomerData":None,                                                                       
                      "EMVData":None,
                      "ApplicationConfigurationData":None,
                      "CardSecurityData":None,
                      "AVSData":None,
                      "InternationalAVSData":None,
                      "CVDataProvided":"NotSet",
                      "CardData":None,
                      "EcommerceSecurityData":None,
                      "AlternativeMerchantData":None,
                      "Level2Data":None,
                      "InterchangeData":None,
                      "AppConfig":True,
                      "SecureEMVData":"4F08A000000003101005500D564953412043524544495420335A0847617300000022225A0847617300000022225F201A56495341204143515549524552205445535420434152442030355F201A56495341204143515549524552205445535420434152442030355F24032212315F24032212315F280208405F280208405F2D08727565736465656e5F2D08727565736465656e5F300202015F300202015F3401099F0702FF809F0702FF809F1101059F120DB2D8E1D020BAE0D5D4D8E220339F1A0208409F1B04000000009F1E0850543034303031394F08A000000003101005500D5649534120435245444954203382025C008408A000000003101005950502000080009A031605059B02E8009C01005F2A0208405F3401099F02060000000001009F03060000000000009F0608A0000000031010059F0902008C9F100706010A03A000009F1101059F120DB2D8E1D020BAE0D5D4D8E220339F1A0208409F1B04000000009F1E0850543034303031399F21030344229F2608FF44F3E206837C789F2701809F33036028C89F34031E03009F3501229F360200019F3704F2E991D99F3901059F4005F000F0A0019F4104000006429F530152",
                      "SecurePaymentAccountData":"355E148ABF74C8D6CC17F316DD4DFF0DBE973D8A1E3F5532719CD1BC3FD2FF624022B1EE57D26370",
                      "DeviceSerialNumber":"88888806500286",
                      "VendorId":"6C78A66750",
                      "Amount":"1.00",
                      "EncryptionKeyId":"FFFF0000000001A000C5",               
                      "EntryMode":"ChipReliable",
                      "CustomerPresent":"Present",
                      "assertions":[("exists","PaymentAccountDataToken",True),("exists","MaskedPAN",True),("isvalue","TransactionState","Authorized"),("isvalue","StatusCode","1")]                   
                      },
           "Poynt_PIN" : {
                      "MerchantProfileId":MPID_NGTHC_Retail,                      
                      "ServiceId":ServiceId_NGTHC_Host,
                      "ApplicationProfileId":"5680",                      
                      "CustomerData":None,                                                                       
                      "EMVData":None,
                      "ApplicationConfigurationData":None,                      
                      "AVSData":None,
                      "InternationalAVSData":None,
                      "CVDataProvided":"NotSet",
                      "CardData":None,
                      "EcommerceSecurityData":None,
                      "AlternativeMerchantData":None,
                      "Level2Data":None,
                      "InterchangeData":None,
                      "AppConfig":True,
                      "SecureEMVData":"57136011000995500000D25121011111199911111F",
                      "KeySerialNumber":"0000030100000005",
                      "PIN":"31121436BCDFF0BC",
                      "DeviceSerialNumber":"88888806500286111",
                      "VendorId":"6C3CEBC59F",
                      "Amount":"1.00",
                      #"EncryptionKeyId":"0000030100000005",               
                      "EntryMode":"Track2DataFromMSR",
                      "AccountType":"CheckingAccount",
                      "CustomerPresent":"Present",
                      "assertions":[("exists","PaymentAccountDataToken",True),("exists","MaskedPAN",True),("isvalue","TransactionState","Authorized"),("isvalue","StatusCode","1")]                   
                      }
           }

