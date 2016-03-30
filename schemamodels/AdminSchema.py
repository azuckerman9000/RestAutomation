UserInfo = {
            #"$type":"UserInfo",
            "Email":None,
            "FirstName":None,
            "LastName":None,
            "Region":None,
            "Role":None,
            "Username":None,            
            "MerchantProfileId":None,
            "ServiceKey":None            
            }



UpdateUser = {
              "UserGuid":None,              
              "UserInfo":UserInfo
              }    

GetMerchants = {
                "sortField":"CreatedDate",
                "sortType":"Descending",
                "pagingParameters": {
                                     "Page":0,
                                     "PageSize":50
                                     },
                "queryParameters": {
                                    "MerchantName":None,
                                    "Region":None,
                                    "SalesChannel":None,
                                    "ServiceKey":None
                                    }
                }

GetPaymentApplications = {
                "sortField":"CreatedDate",
                "sortType":"Descending",
                "pagingParameters": {
                                     "Page":0,
                                     "PageSize":50
                                     },
                "queryParameters": {                                    
                                    "Region":None,
                                    "SalesChannel":None                                    
                                    }
                }

AddMerchantToUserCredential = {
                               "merchant": {
                                            "MerchantProfileId":None,
                                            "ServicveKey":None,
                                            "MerchantMetaData":None
                                            }
                               }