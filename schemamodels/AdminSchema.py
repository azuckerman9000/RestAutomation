UserInfo = {
            "Email":None,
            "FirstName":None,
            "LastName":None,
            "Region":None,
            "Role":None,
            "Username":None,
            "Password":None,
            "MerchantInfo": {
                             "MerchantProfileId":None,
                             "ServiceKey":None,
                             "MerchantMetaData":None
                             }
            }

CreateUser = {              
              "UserInfo":UserInfo
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

AddMerchantToUserCredential = {
                               "merchant": {
                                            "MerchantProfileId":None,
                                            "ServicveKey":None,
                                            "MerchantMetaData":None
                                            }
                               }