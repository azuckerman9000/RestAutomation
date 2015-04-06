Authorize = {
  "$type":"AuthorizeTransaction,http://schemas.evosnap.com/CWS/v2.0/Transactions/Rest",
  "ApplicationProfileId":"4084",
  "MerchantProfileId":"Auto_SOAP_Ecommerce_A",
  "Transaction":{
    "$type":"BankcardTransactionPro,http://schemas.evosnap.com/CWS/v2.0/Transactions/Bankcard/Pro",
    "Addendum":None,
    "ApplicationConfigurationData":None,
    "CustomerData":{
      "BillingData":None,
      "CustomerId":None,
      "CustomerTaxId":None,
      "ShippingData":None
    },
    "ReportingData":None,
    "TenderData":{
      "CardData":{
        "CardType":"Visa",
        "CardholderName":"John Doe",
        "Expire":"1215",
        "PAN":"4003000123456781"
      },
      "CardSecurityData":{
        "AVSData":{
          "CardholderName":None,
          "City":None,
          "Email":None,
          "Phone":None,
          "StateProvince":None
        },
        "CVDataProvided":"NotSet",
        "IdentificationInformation":None
      },
      "DeviceSerialNumber":None,
      "EncryptionKeyId":None,
      "PaymentAccountDataToken":None,
      "SecurePaymentAccountData":None,
      "SwipeStatus":None
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
      "TransactionDateTime":"2013-04-03T13:50:16"
    }
  }
}

Capture = {"$type": "Capture,http://schemas.evosnap.com/CWS/v2.0/Transactions/Rest",
           "ApplicationProfileId": "4084",
           "BankcardCapture": {
                "$type":"BankcardUndoPro,http://schemas.evosnap.com/CWS/v2.0/Transactions/Bankcard/Pro",
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