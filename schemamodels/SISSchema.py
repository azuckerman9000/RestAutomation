SaveMerchantProfiles =  [{
        "$type": "MerchantProfile, http://schemas.evosnap.com/CWS/v2.0/ServiceInformation",
        "ProfileId": "Auto_SOAP_Ecommerce_A",
        "ServiceId": "1257A00001",
        "ServiceName": "AutoResp",
        "LastUpdated": "2013-01-10T11:06:44.087",
        "MerchantData": {
            "CustomerServiceInternet": None,
            "CustomerServicePhone": "303 4446598",            
            "Address": {"Street1":"1123",
                "Street2":None,             
                "City":"Denver",
                "StateProvince":"CO",
                "PostalCode":"80202",
                "CountryCode":"USA",
                "AddressType":None},
            "MerchantId": "1234",
            "Name": "TestTest",
            "Phone": "303 6659878",
            "TaxId": None,
            "BankcardMerchantData": {
                "ABANumber": None,
                "AcquirerBIN": None,
                "AgentBank": None,
                "AgentChain": None,
                "Aggregator": False,
                "ClientNumber": None,
                "IndustryType": "Ecommerce",
                "Location": None,
                "MerchantType": None,
                "PrintCustomerServicePhone": False,
                "QualificationCodes": None,
                "ReimbursementAttribute": None,
                "SIC": None,
                "SecondaryTerminalId": None,
                "SettlementAgent": None,
                "SharingGroup": None,
                "StoreId": "9",
                "TerminalId": "12345",
                "TimeZoneDifferential": None,
                "CardBrandIdentifiers_3DSecure":[
                                                 {"MerchantNumber":None,
                                                  "MerchantBankId":None,
                                                  "MerchantUrl":None,
                                                  "CardBrand3DSecureProgram":"NotSet",
                                                  "DirectoryServerUrl":None,
                                                  "RootCertificate":None
                                                  }
                                                 ]
            }
        },
        "TransactionData": {
            "BankcardTransactionDataDefaults": {
                "CurrencyCode": "USD",
                "CustomerPresent": "Ecommerce",
                "EntryMode": "Keyed",
                "RequestACI": "IsCPSMeritCapable",
                "RequestAdvice": "Capable"
            }
        },
        "RestrictedOperations": None,
        "HostedPayments": None,
        "RuleCategories":None
    }]

ApplicationData = {
                   "ApplicationAttended":True,
                   "ApplicationLocation":"OnPremises",
                   "ApplicationName":"Pay2Win",
                   "DeveloperId":"3",
                   "HardwareType":"PC",
                   "PINCapability":"PINSupported",
                   "PTLSSocketId":"MIIFCzCCA/OgAwIBAgICAoAwDQYJKoZIhvcNAQEFBQAwgbExNDAyBgNVBAMTK0lQIFBheW1lbnRzIEZyYW1ld29yayBDZXJ0aWZpY2F0ZSBBdXRob3JpdHkxCzAJBgNVBAYTAlVTMREwDwYDVQQIEwhDb2xvcmFkbzEPMA0GA1UEBxMGRGVudmVyMRowGAYDVQQKExFJUCBDb21tZXJjZSwgSW5jLjEsMCoGCSqGSIb3DQEJARYdYWRtaW5AaXBwYXltZW50c2ZyYW1ld29yay5jb20wHhcNMTMwODIzMTg1NjA5WhcNMjMwODIxMTg1NjA5WjCBjDELMAkGA1UEBhMCVVMxETAPBgNVBAgTCENvbG9yYWRvMQ8wDQYDVQQHEwZEZW52ZXIxGjAYBgNVBAoTEUlQIENvbW1lcmNlLCBJbmMuMT0wOwYDVQQDEzRxYmtXM25TZ0FJQUFBUDhBSCtDY0FBQUVBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUE9MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAx68dD32BLjiDC9RdkIFY2P8N/bzvV75qWWemh0hO3zswggMY6BtKM7xVAoeVbEUP/HxOSlBasKE4tY/Y9hfDoqaszojt5BfqGYqAnUZ/7yjlfROdDu5q1p7AJ8DsEg9o5rpp0/88tj1+XK43JpE0PHtRecCdpsiKGclAdvaGRiXVMR0U6/nNjoNdptSo3Kd8DXSU4xWfiwrVWYUMu9otetiwutJNB3jUfsW5incr1OZ7vkFa58Eltb57UygQ5i31FSrVuBfS4UMQKVBP1V7wsVQlcC+QBNjlsGiATzdqtJBgcaI+BkPEJkF7kpDae3fNbQ77AhVFsoGV30bZCSoSNwIDAQABo4IBTjCCAUowCQYDVR0TBAIwADAdBgNVHQ4EFgQU2t+wf1VVGvks5M1zZlNa92YYUAEwgeYGA1UdIwSB3jCB24AU3+ASnJQimuunAZqQDgNcnO2HuHShgbekgbQwgbExNDAyBgNVBAMTK0lQIFBheW1lbnRzIEZyYW1ld29yayBDZXJ0aWZpY2F0ZSBBdXRob3JpdHkxCzAJBgNVBAYTAlVTMREwDwYDVQQIEwhDb2xvcmFkbzEPMA0GA1UEBxMGRGVudmVyMRowGAYDVQQKExFJUCBDb21tZXJjZSwgSW5jLjEsMCoGCSqGSIb3DQEJARYdYWRtaW5AaXBwYXltZW50c2ZyYW1ld29yay5jb22CCQD/yDY5hYVsVzA1BgNVHR8ELjAsMCqgKKAmhiRodHRwOi8vY3JsLmlwY29tbWVyY2UuY29tL2NhLWNybC5jcmwwDQYJKoZIhvcNAQEFBQADggEBAIGOvmbUPdUs3FMbQ95rpT7hShEkAbRnQjp8yY1ql48obQM0mTjQ4CfAXPELZ1xe8KyC4jaurW9KMuCkApwC8b8cgdKWg1ujtKkrNGhhDQRLcclNB6q5JTXrP0gQgrr43yHxh4vaAA8GTvkg7j2hrTUkksmc7JNIto0XsHlfvrUv8XCQIeQsFyy/nLHpQIkXwvAS6fcml6KMRTgQJm2yLZCfYVs6n18VDd9LCYWO9Y6majWoqgyHZ5Gy2qT7V+YxgDMUrZa7Fd66xHTWskO8wc7kuW5ZKaB29ewbAXIY31AHi4dAuGS6znPxnRg1kE01aDQ1FFCcajKtovg3di8PICU=",
                   "ReadCapability":"MSRKeyICC",
                   "SerialNumber":"345",
                   "SoftwareVersion":"1.0",
                   "SoftwareVersionDate":"2015-10-07T18:35:58.209Z",
                   "VendorId":"444",
                   "EncryptionType":"MagneSafeV4V5Compatible",
                   "DeviceSerialNumber":None,
                   "EMVTerminalData":{
                        "CardRetentionCapability":True,
                        "CardDataOutputCapability":"ICC",
                        "CardHolderAuthenticationCapability":"PIN",
                        "PINMaxCharacters":"P06",
                        "TerminalOperator":"CardAcceptorOp",
                        "TerminalOutputCapability":"PrintDisplay"
                        }
                   }