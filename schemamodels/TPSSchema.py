Authorize = {
  "$type":"AuthorizeTransaction,http://schemas.evosnap.com/CWS/v2.0/Transactions/Rest",
  "ApplicationProfileId":"4084",
  "MerchantProfileId":"Auto_SOAP_Ecommerce_A",
  "Transaction":{
    "$type":"BankcardTransactionPro,http://schemas.evosnap.com/CWS/v2.0/Transactions/Bankcard/Pro",
    "Addendum":None,
    "ApplicationConfigurationData":{
        "ApplicationAttended":True,
        "ApplicationLocation":"OnPremises",
        "HardwareType":"PC",
        "PINCapability":"PINNotSupported",
        "ReadCapability":"MSRKeyICC",
        "EMVTerminalData":{
            "CardDataOutputCapability":"ICC",
            "CardRetentionCapability":True,
            "CardholderAuthenticationCapability":"PIN",
            "PINMaxCharacters":"P12",
            "TerminalOperator":"CardAcceptorOp",
            "TerminalOutputCapability":"PrintDisplay"
            }        
        },
    "CustomerData":{
      "BillingData":None,
      "CustomerId":None,
      "CustomerTaxId":None,
      "ShippingData":None
    },
    "ReportingData":None,
    "TenderData":{
      "$type":"BankcardTenderDataPro,http://schemas.evosnap.com/CWS/v2.0/Transactions/Bankcard/Pro",
      "CardData":{
        "CardType":"Visa",
        "CardholderName":"John Doe",
        "Expire":"1215",
        "PAN":"4003000123456781",
        "Track2Data":None
        },
      "CardSecurityData":{
        "AVSData":{
          "CardholderName":None,
          "City":None,
          "Email":None,
          "Phone":None,
          "StateProvince":None,
          "PostalCode":None,
          "Country":"NotSet",
          "Phone":None,
          "Email":None
            },
        "InternationalAVSData":{
            "HouseNumber":None,
            "Street":None,
            "POBoxNumber":None,
            "City":None,
            "StateProvince":None,
            "PostalCode":None,
            "Country":"NotSet"
          },
        "CVDataProvided":"NotSet",
        "CVData":None,
        "IdentificationInformation":None,
        "KeySerialNumber":None,
        "PIN":None
      },
      "DeviceSerialNumber":None,
      "EncryptionKeyId":None,
      "EMVEncryptionKeyId":None,
      "MACEncryptionKeyId":None,
      "SecureEMVData":None,
      "SecureMACData":None,
      "PaymentAccountDataToken":None,
      "SecurePaymentAccountData":None,
      "SwipeStatus":None,
      "CardholderIdentification":None,
      "CardholderIdType":"NotSet",
      "EMVData":{
         "ApplicationId":"A0000000041010",
         "ApplicationInterchangeProfile":"5800",
         "ApplicationTransactionCount":"000D",
         "ApplicationUsageControl":"FF00",
         "ApplicationVersionNumber":None,
         "AuthorizationAmount":"000000000700",
         "AuthorizationResponseCode":"00",
         "CVMList":"000000000000000042015E0342031F03",
         "CVMResults":"5E0300",
         "CardAuthenticationReliabilityIndex":None,
         "CardAuthenticationResultsCode":None,
         "CashBackAmount":None,
         "ChipConditionCode":None,
         "CryptogramInformationData":"40",
         "Cryptogram":"8C270F78A4CE5260",
         "InterfaceDeviceSerialNumber":None,
         "IssuerActionDefault":"F050040800",
         "IssuerActionDenial":None,
         "IssuerActionOnline":None,
         "IssuerApplicationData":"0110A00001220000000000000000000000FF",
         "IssuerScriptResults":None,
         "LocalTransactionDate":"141028",
         "TerminalCapability":"E0F8C8",
         "TerminalCountryCode":"840",
         "TerminalType":None,
         "TerminalVerifyResult":"42C0008000",
         "TransactionCategoryCode":None,
         "CurrencyCode":"840",
         "SequenceNumber":None,
         "TransactionType":"0",
         "UnpredictableNumber":"D863A470"         
            }
    },
    "TransactionData":{
      "AccountType":"NotSet",
      "Amount":"1.00",
      "CurrencyCode":"USD",
      "CustomerPresent":"Ecommerce",
      "EmployeeId":"6768",
      "OrderNumber":"2",
      "EntryMode":"Keyed",
      "Reference":"jdhfjd",
      "TransactionCode":"Override",
      "TransactionDateTime":"2015-04-03T13:50:16",
      "IS3DSecure":False,
      "CardholderAuthenticationEntity":"NotSet",
      "CardPresence":False
    }
  }
}

Capture = {"$type": "Capture,http://schemas.evosnap.com/CWS/v2.0/Transactions/Rest",
           "ApplicationProfileId": "4084",
           "BankcardCapture": {
                "$type":"BankcardCapture,http://schemas.evosnap.com/CWS/v2.0/Transactions/Bankcard/Pro",
                "Amount":None,
                "ChargeType":None,
                "Level2Data":None,
                "LineItemDetails":None,
                "ShippingData":None
                }
           }

Undo = {"$type": "Undo,http://schemas.evosnap.com/CWS/v2.0/Transactions/Rest",
        "ApplicationProfileId": "4084",
        "BankcardUndo": {
            "$type": "BankcardUndo,http://schemas.evosnap.com/CWS/v2.0/Transactions/Bankcard",
            "PINDebitReason":None,
            "ForceVoid":None,
            "TransactionCode":None}
        }

Resubmit = {"$type": "ResubmitTransaction,http://schemas.evosnap.com/CWS/v2.0/Transactions/Rest",            
            "Transaction":
                {"TransactionId":None,
                 "CVV":None,
                 "ResubmitReason":"NotSet",
                 "PaymentAuthorizationResponse":None},
            "ApplicationProfileId": "4084"
            }

RequestKey = {"$type":"KeyTransaction,http://schemas.evosnap.com/CWS/v2.0/Transactions/Rest",
                "Transaction":{
                    "$type":"EncryptionTransaction,http://schemas.evosnap.com/CWS/v2.0/Transactions/Encryption",
                    "TenderData":{
                        "ChipConditionCode":"testcode",
                        "EntryMode":"ContactlessMChipOrSmartCard"
                        },
                    "TransactionData":{
                        "Terminal":{
                            "SerialNumber":"123-adgh",
                            "VendorName":"HappyPOS"
                            },
                        "Amount":"0.00",
                        "CurrencyCode":"NotSet"                        
                        }
                    },
              "ApplicationProfileId": None,
              "MerchantProfileId":None
             }