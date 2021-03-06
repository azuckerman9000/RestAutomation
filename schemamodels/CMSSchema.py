Subscription = {
                "Description":None,
                "SubscriptionReferenceId":None,
                "StartDate":"2016-05-02T14:35:11.497Z",
                "EndDate":"2017-05-11T14:35:11.497Z",
                "IntervalUnit":"NotSet",
                "IntervalLength":None,
                "NextProcessingDate":"2016-05-20T14:35:11.497Z",
                "TotalInvoices":None,
                "TotalTrialInvoices":None,
                "Amount":0.0,
                "TrialAmount":0.0,
                "Order":{
                         "BillingData":None,
                         "ShippingData":None,
                         "CustomerCode":None,
                         "CurrencyCode":"NotSet",
                         "Description":None,
                         "Enable3D":False,
                         "InvoiceReferenceId":None,
                         "PromotionCode":None,
                         "ShipmentId":None,
                         "ShipCode":None,
                         "ShippingTotal":0.0,
                         "ShipMethod":None,
                         "DiscountTotal":0.0,
                         "DutyAmount":0.0,
                         "SubTotal":0.0,
                         "TaxTotal":0.0,
                         "GrandTotal":0.0,
                         "TaxRate":0.0,
                         "TaxExempt":"NotSet",
                         "TaxExemptNumber":None,
                         "OrderItems":None,
                         "ItemizedTaxes":None
                         },
                "ServiceId":None,
                "AutoRenew":False
                }

CustomerId = {
              "CustomerReferenceId":None,
              "PAN":None,
              "EmailAddress":None,
              "TelephoneNumber":None
              }

SubmitSubscription = {
                    "Subscription":Subscription,
                    "PaymentData":{
                                   "PaymentType":"NotSet",
                                   "CardType":"NotSet",
                                   "BankAccountType":"NotSet",
                                   "PaymentAccountNumber":None,
                                   "PaymentRoutingNumber":None,
                                   "PaymentAccountName":None,
                                   "PaymentAccountExpiration":None,
                                   "PaymentAccountDataToken":None
                                    },
                    "CustomerId":CustomerId,
                    "Scope":"NotSet"                    
                    }

UpdateSubscriptionState = {
                           "SubscriptionState":"NotSet"                           
                           }

QuerySubscriptions = {
                      "QueryParameters":{
                                         "CreatedDate":{
                                                        "StartDate":"2016-05-02T17:25:55.262Z",
                                                        "EndDate":"2016-05-02T17:25:55.262Z"
                                                        },
                                         "SubscriptionReferenceId":None,
                                         "SubscriptionState":"NotSet",
                                         "CustomerId":CustomerId,
                                         "MerchantProfileIds":None
                                         },
                      "MerchantProfileId":None,
                      "Scope":"NotSet",
                      "PagingParameters":{
                                          "Page":0,
                                          "PageSize":50
                                          }
                      }