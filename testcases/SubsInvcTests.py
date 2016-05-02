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

Subscriptions = {                 
                 "Sub1":{
                        "CustomerId":None,
                        "MerchantProfileId":"Generic_Ecomm_HC",
                        "Description":"TrainsPlanesEtc",
                        "SubscriptionReferenceId":"1234",
                        "StartDate":"2016-05-03T14:35:11.497Z",
                        "EndDate":"2017-05-11T14:35:11.497Z",
                        "IntervalUnit":"Monthly",
                        "IntervalLength":"1",
                        "NextProcessingDate":"2016-05-20T14:35:11.497Z",
                        "TotalInvoices":"12",
                        "TotalTrialInvoices":None,
                        "Amount":10.00,
                        "TrialAmount":0.0,
                        "Order":{
                                 "BillingData":None,
                                 "ShippingData":None,
                                 "CustomerCode":None,
                                 "CurrencyCode":"USD",
                                 "Description":None,
                                 "Enable3D":False,
                                 "InvoiceReferenceId":"4321",
                                 "PromotionCode":None,
                                 "ShipmentId":"1111",
                                 "ShipCode":"2222",
                                 "ShippingTotal":12.00,
                                 "ShipMethod":"UPS",
                                 "DiscountTotal":0.0,
                                 "DutyAmount":1.00,
                                 "SubTotal":13.00,
                                 "TaxTotal":1.00,
                                 "GrandTotal":14.00,
                                 "TaxRate":0.0,
                                 "TaxExempt":"NotSet",
                                 "TaxExemptNumber":None,
                                 "OrderItems":None,
                                 "ItemizedTaxes":None
                                 },
                        "ServiceId":"35EDC00001",
                        "AutoRenew":False,                        
                        "PaymentType":"Credit",
                        "CardType":"Visa",
                        "PaymentAccountNumber":"4003000123456781",
                        "PaymentAccountExpiration":"1234",
                        "Scope":"MerchantProfileId"
                         }
                 }