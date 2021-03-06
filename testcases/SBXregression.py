##### ServiceKey is 4DBA36C8FD500001 ####
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

Generic_Sandbox = {
                   "Ecomm_Basic" : {
                                    "ServiceId":ServiceId_GenHC,
                                    "MerchantProfileId":MPID_Ecomm_HC,
                                    "CustomerData":None,
                                    "AlternativeMerchantData":None,
                                    "ApplicationConfigurationData":None,
                                    "EcommerceSecurityData":None,
                                    "EMVData":None,
                                    "Geolocation":None,
                                    "InterchangeData":None,
                                    "Level2Data":None,
                                    "AVSData":None,
                                    "InternationalAVSData":None,
                                    "CVDataProvided":"Provided",
                                    "CVData":"123",
                                    "Track2Data":None,
                                    "PAN":"4003000123456781",
                                    "CardType":"Visa",
                                    "CustomerPresent":"Ecommerce",
                                    "EntryMode":"Keyed",
                                    "assertions":[("exists","PaymentAccountDataToken",True),("exists","MaskedPAN",True),("isvalue","TransactionState","Authorized"),("isvalue","StatusCode","000")]                                      
                                    },
                   "MOTO_Basic" : {
                                    "ServiceId":ServiceId_GenHC,
                                    "MerchantProfileId":MPID_MOTO_HC,
                                    "CustomerData":None,
                                    "AlternativeMerchantData":None,
                                    "ApplicationConfigurationData":None,
                                    "EcommerceSecurityData":None,
                                    "EMVData":None,
                                    "Geolocation":None,
                                    "InterchangeData":None,
                                    "Level2Data":None,
                                    "AVSData":None,
                                    "InternationalAVSData":None,
                                    "CVDataProvided":"Provided",
                                    "CVData":"123",
                                    "Track2Data":None,
                                    "PAN":"4003000123456781",
                                    "CardType":"Visa",
                                    "CustomerPresent":"MOTOCC",
                                    "EntryMode":"Keyed",
                                    "assertions":[("exists","PaymentAccountDataToken",True),("exists","MaskedPAN",True),("isvalue","TransactionState","Authorized"),("isvalue","StatusCode","000")]                                      
                                    },
                   "Retail_Basic" : {
                                    "ServiceId":ServiceId_GenHC,
                                    "MerchantProfileId":MPID_Retail_HC,
                                    "CustomerData":None,
                                    "AlternativeMerchantData":None,
                                    "ApplicationConfigurationData":None,
                                    "EcommerceSecurityData":None,
                                    "EMVData":None,
                                    "Geolocation":None,
                                    "InterchangeData":None,
                                    "Level2Data":None,
                                    "CardSecurityData":None,                                    
                                    "Track2Data":"4003000123456781=15125025432198712345",
                                    "PAN":None,
                                    "CardType":"Visa",
                                    "CustomerPresent":"Present",
                                    "EntryMode":"Track2DataFromMSR",
                                    "assertions":[("exists","PaymentAccountDataToken",True),("exists","MaskedPAN",True),("isvalue","TransactionState","Authorized"),("isvalue","StatusCode","000")]                                      
                                    },
                   "Restaurant_Basic" : {
                                    "ServiceId":ServiceId_GenHC,
                                    "MerchantProfileId":MPID_Restaurant_HC,
                                    "CustomerData":None,
                                    "AlternativeMerchantData":None,
                                    "ApplicationConfigurationData":None,
                                    "EcommerceSecurityData":None,
                                    "EMVData":None,
                                    "Geolocation":None,
                                    "InterchangeData":None,
                                    "Level2Data":None,
                                    "CardSecurityData":None,                                    
                                    "Track2Data":"4003000123456781=15125025432198712345",
                                    "PAN":None,
                                    "CardType":"Visa",
                                    "CustomerPresent":"Present",
                                    "EntryMode":"Track2DataFromMSR",
                                    "assertions":[("exists","PaymentAccountDataToken",True),("exists","MaskedPAN",True),("isvalue","TransactionState","Authorized"),("isvalue","StatusCode","000")]                                      
                                    },
                   "Ecomm_IntlAVS" : {
                                    "ServiceId":ServiceId_GenHC,
                                    "MerchantProfileId":MPID_Ecomm_HC,
                                    "CustomerData":None,
                                    "AlternativeMerchantData":None,
                                    "ApplicationConfigurationData":None,
                                    "EcommerceSecurityData":None,
                                    "EMVData":None,
                                    "Geolocation":None,
                                    "InterchangeData":None,
                                    "Level2Data":None,
                                    "AVSData":None,
                                    "InternationalAVSData":{"HouseNumber":"34","Street":"1st","City":"Denver","PostalCode":"80202","Country":"USA"},
                                    "CVDataProvided":"Provided",
                                    "CVData":"123",
                                    "Track2Data":None,
                                    "PAN":"54545454545454",
                                    "CardType":"Discover",
                                    "CustomerPresent":"Ecommerce",
                                    "EntryMode":"Keyed",
                                    "assertions":[("exists","PaymentAccountDataToken",True),("exists","MaskedPAN",True),("isvalue","TransactionState","Authorized"),("isvalue","StatusCode","000")]                                      
                                    },
                   "Token_Basic" : {
                                    "ServiceId":ServiceId_GenHC,
                                    "MerchantProfileId":MPID_Retail_HC,
                                    "CustomerData":None,
                                    "AlternativeMerchantData":None,
                                    "ApplicationConfigurationData":None,
                                    "EcommerceSecurityData":None,
                                    "EMVData":None,
                                    "Geolocation":None,
                                    "InterchangeData":None,
                                    "Level2Data":None,
                                    "CardSecurityData":None,                                    
                                    "CardData":None,
                                    "PaymentAccountDataToken":"c3691461-2930-42e6-8d64-0f9d963663e8a9fa06e6-ddbc-4d03-b412-cbdfead9aad0",
                                    "CustomerPresent":"Present",
                                    "EntryMode":"Track2DataFromMSR",
                                    "assertions":[("exists","PaymentAccountDataToken",True),("exists","MaskedPAN",True),("isvalue","TransactionState","Authorized"),("isvalue","StatusCode","000")]                                      
                                    },                   
                   "EMV":   {                       
                              "ServiceId":ServiceId_GenHC,
                              "MerchantProfileId":MPID_Retail_HC,
                              "ApplicationProfileId":"65360",                      
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
                              "Geolocation":None,
                              "SecureEMVData":"C00A88888827500096400049C408374245FFFFF1007FC28201902ACEAF5307FE9DD78F127BE032FB7C1732A8E13AE30ED7216B37F85B75DE97CE4105E51834F58D1ED22F19C60D64D892150B0FD0D20681700C06CD6A56BB2479C23FFF51489C7757EEB279805F00EF57777EBB9497E9AB1927A9FEE05D8DB56AD134B3997AD8B759B1715E3C4038646FC8611955DB68EF765E59C0516D75C93619981BB74DE65EC77739E4EFE019FA9387B222A8C1B2A80F4251E192180D25643D6680C6A7F9787415D2F46D25EF846DD329768B29483FC77EF11D62DAD40222345584B495E1B032238EE871FDEF403E5ED3B1D9EA32A45382A3C0D05697F6724ED33E99BC0C5AB714329A47FE92B8ADF0E4178AA2DC32E06C404F27FE078BD649EE19EF6464856DF5DFD07983A2D60940E8D6880ADF4214BA980EC5579F599E82AEF840073F50E9558FCFCB8537896717227A0B6D871116FBBB6A19611B5004A15FECD53D93F963C8020A588285D842263067FA8B37DB02A5DC6350767C0A9EEECE3403A46E19EB624A156CF5D400522D2DB422991C40F436A2C6007D47D362BA162BAEC46425F763D615CE4603F5A8C70A88888827500096200045C818397B012ECB9B7A2117AF6CC503ACFE8BC6D2F2DA3BC68D354F08A000000025010801950500000080009A031601299B02E8009C01005F201041454950532032302F56455220322E305F24032001319F02060000000052009F03060000000000009F1A0208409F1C0831313232333334349F2608489C14732D1E36AC9F270180",
                              "DeviceSerialNumber":"88888827500116",
                              "VendorId":"3E3246482E",
                              "Amount":"10.00",                      
                              "EntryMode":"ChipReliable",
                              "CustomerPresent":"Present",
                              "assertions":[("exists","PaymentAccountDataToken",True),("exists","MaskedPAN",True),("isvalue","TransactionState","Authorized"),("isvalue","StatusCode","000")]
                              },                   
                   "EMVData":   {                       
                          "ServiceId":ServiceId_GenHC,
                          "MerchantProfileId":MPID_Retail_HC,
                          "ApplicationProfileId":"65360",                      
                          "CustomerData":None,                                                                       
                          "EMVData":{
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
                                "CryptogramInformationData": "80",
                                "Cryptogram": "A7368B0D59C173D6",
                                "CustomerExclusiveData": None,
                                "DedicatedFileName": None,
                                "FormFactorIndicator": None,
                                "InterfaceDeviceSerialNumber": "15900179",
                                "IssuerActionDefault": "F040C42800",
                                "IssuerActionDenial": None,
                                "IssuerActionOnline": None,
                                "IssuerApplicationData": "0105A00003000000",
                                "IssuerScriptResults": None,
                                "LocalTransactionDate": "160418",
                                "TerminalCapability": "60B8C8",
                                "TerminalCountryCode": "840",
                                "TerminalType": "22",
                                "TerminalVerifyResult": "4000008000",
                                "CurrencyCode": "840",
                                "SequenceNumber": "00001108",
                                "TransactionType": "00",
                                "UnpredictableNumber": "78082F1F"
                            },
                          "DeviceSerialNumber":"615900179",
                          "ApplicationConfigurationData":{
                                "ApplicationAttended": True,
                                "ApplicationLocation": "OnPremises",
                                "HardwareType": "DialTerminal",
                                "PINCapability": "PINVerifiedByDevice",
                                "ReadCapability": "MSREMVICC",
                                "EMVTerminalData": {
                                    "CardDataOutputCapability": "ICC",
                                    "CardRetentionCapability":True,
                                    "CardholderAuthenticationCapability": "PIN",
                                    "PINMaxCharacters": "P12",
                                    "TerminalOperator": "Admin",
                                    "TerminalOutputCapability": "PrintDisplay"
                                }
                            },        
                          "CardSecurityData":None,
                          "Track2Data":"4003000123456781=15125025432198712345",
                          "EcommerceSecurityData":None,
                          "AlternativeMerchantData":None,
                          "Level2Data":None,
                          "InterchangeData":None,
                          "AppConfig":True,
                          "Geolocation":None,
                          "VendorId":"3E3246482E",
                          "Amount":"37.00",                      
                          "EntryMode":"ChipReliable",
                          "CustomerPresent":"Present",
                          "CardholderAuthenticationEntity": "ICC",
                          "assertions":[("exists","PaymentAccountDataToken",True),("exists","MaskedPAN",True),("isvalue","TransactionState","Authorized"),("isvalue","StatusCode","000")]
                          }
                   }

MPI = {
       "MPI_3DSecure" : {
                        "ServiceId":ServiceId_GenHC,
                        "MerchantProfileId":MPID_Ecomm_HC,
                        "CustomerData":None,
                        "AlternativeMerchantData":None,
                        "ApplicationConfigurationData":None,
                        "EcommerceSecurityData":None,
                        "EMVData":None,
                        "Geolocation":None,
                        "InterchangeData":None,
                        "Level2Data":None,
                        "AVSData":None,
                        "InternationalAVSData":None,
                        "CVDataProvided":"Provided",
                        "CVData":"200",
                        "Track2Data":None,
                        "PAN":"4111111111111111",
                        "CardType":"Visa",
                        "CustomerPresent":"Ecommerce",
                        "EntryMode":"Keyed",
                        "Is3DSecure":True,
                        "assertions":[("exists","PaymentAccountDataToken",True),("exists","MaskedPAN",True),("isvalue","TransactionState","Declined"),("isvalue","StatusCode","3D")]                                      
                        },
       "MPI_NotEnrolled" : {
                        "ServiceId":ServiceId_GenHC,
                        "MerchantProfileId":MPID_Ecomm_HC,
                        "CustomerData":None,
                        "AlternativeMerchantData":None,
                        "ApplicationConfigurationData":None,
                        "EcommerceSecurityData":None,
                        "EMVData":None,
                        "Geolocation":None,
                        "InterchangeData":None,
                        "Level2Data":None,
                        "AVSData":None,
                        "InternationalAVSData":None,
                        "CVDataProvided":"Provided",
                        "CVData":"200",
                        "Track2Data":None,
                        "PAN":"4003000123456781",
                        "CardType":"Visa",
                        "CustomerPresent":"Ecommerce",
                        "EntryMode":"Keyed",
                        "Is3DSecure":True,
                        "assertions":[("exists","PaymentAccountDataToken",True),("exists","MaskedPAN",True),("isvalue","TransactionState","Authorized"),("isvalue","StatusCode","000")]                                      
                        },
       "Resubmit3D" : {
                       "ServiceId":ServiceId_GenHC,
                       "ResubmitReason":"Resubmission",
                       "CVV":"200"
                      }
       }

PINDebit = {
            "PINDebit_Basic" : {
                        "ServiceId":ServiceId_GenHC,
                        "MerchantProfileId":MPID_Retail_HC,
                        "CustomerData":None,
                        "AlternativeMerchantData":None,
                        "ApplicationConfigurationData":None,
                        "EcommerceSecurityData":None,
                        "EMVData":None,
                        "Geolocation":None,
                        "InterchangeData":None,
                        "Level2Data":None,
                        "InternationalAVSData":None,
                        "AVSData":None,
                        "CVDataProvided":"NotSet",
                        "KeySerialNumber":"856290000060027C",
                        "PIN":"D8BC0FAF9BBD9B17",
                        "AccountType":"CheckingAccount",                                  
                        "Track2Data":"4003000123456781=15125025432198712345",
                        "PAN":None,
                        "CardType":"Visa",
                        "CustomerPresent":"Present",
                        "EntryMode":"Track2DataFromMSR",
                        "assertions":[("exists","PaymentAccountDataToken",True),("exists","MaskedPAN",True),("isvalue","TransactionState","Captured"),("isvalue","StatusCode","000")]                                      
                        }
            }

EmailReceipt = {
                "Retail_Receipt" : {
                                    "ServiceId":ServiceId_GenHC,
                                    "MerchantProfileId":MPID_Retail_HC,
                                    "CustomerData":None,
                                    "AlternativeMerchantData":None,
                                    "ApplicationConfigurationData":None,
                                    "EcommerceSecurityData":None,
                                    "EMVData":None,
                                    "Geolocation":None,
                                    "InterchangeData":None,
                                    "Level2Data":None,
                                    "CardSecurityData":None,                                    
                                    "Track2Data":"4003000123456781=15125025432198712345",
                                    "PAN":None,
                                    "CardType":"Visa",
                                    "CustomerPresent":"Present",
                                    "EntryMode":"Track2DataFromMSR",
                                    "assertions":[("exists","PaymentAccountDataToken",True),("exists","MaskedPAN",True),("isvalue","TransactionState","Authorized"),("isvalue","StatusCode","000")]                                      
                                    },
                "Ecomm_Receipt" : {
                                    "ServiceId":ServiceId_GenHC,
                                    "MerchantProfileId":MPID_Ecomm_HC,
                                    "CustomerData":None,
                                    "AlternativeMerchantData":None,
                                    "ApplicationConfigurationData":None,
                                    "EcommerceSecurityData":None,
                                    "EMVData":None,
                                    "Geolocation":None,
                                    "InterchangeData":None,
                                    "Level2Data":None,
                                    "AVSData":None,
                                    "InternationalAVSData":None,
                                    "CVDataProvided":"Provided",
                                    "CVData":"123",
                                    "Track2Data":None,
                                    "PAN":"4003000123456781",
                                    "CardType":"Visa",
                                    "CustomerPresent":"Ecommerce",
                                    "EntryMode":"Keyed",
                                    "assertions":[("exists","PaymentAccountDataToken",True),("exists","MaskedPAN",True),("isvalue","TransactionState","Authorized"),("isvalue","StatusCode","000")]                                      
                                    }
                }