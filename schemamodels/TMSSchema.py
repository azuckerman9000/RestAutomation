TxnSummary = {
"$type": "QueryTransactionsSummary,http://schemas.evosnap.com/CWS/v2.0/DataServices/TMS/Rest",
"queryTransactionsParameters": {
"Amounts": None,
"ApprovalCodes": None,
"BatchIds": None,
"MerchantProfileIds": None,
"OrderNumbers": None,
"ServiceIds": None,
"ServiceKeys": None,
"TransactionIds": None,
"CaptureStates": None,
"TransactionStates": None,
"CardTypes": None,
"CaptureDateRange": None,
"TransactionDateRange": None,
"QueryType": "AND",
"IncludeRelated": False,
"IsAcknowledged": "NotSet"
},
"pagingParameters": {
"Page": 0,
"PageSize": 50
}
}

TxnDetail = {
"$type": "QueryTransactionsDetail,http://schemas.evosnap.com/CWS/v2.0/DataServices/TMS/Rest",
"queryTransactionsParameters": {
"Amounts": None,
"ApprovalCodes": None,
"BatchIds": None,
"MerchantProfileIds": None,
"OrderNumbers": None,
"ServiceIds": None,
"ServiceKeys": None,
"TransactionIds": None,
"CaptureStates": None,
"TransactionStates": None,
"CardTypes": None,
"CaptureDateRange": None,
"TransactionDateRange": None,
"QueryType": "AND",
"IncludeRelated": False,
"IsAcknowledged": "NotSet"
},
"pagingParameters": {
"Page": 0,
"PageSize": 50
}
}

TxnFamily = {

"queryTransactionsParameters": {
"Amounts": None,
"ApprovalCodes": None,
"BatchIds": None,
"MerchantProfileIds": None,
"OrderNumbers": None,
"ServiceIds": None,
"ServiceKeys": None,
"TransactionIds": None,
"CaptureStates": None,
"TransactionStates": None,
"CardTypes": None,
"CaptureDateRange": None,
"TransactionDateRange": None,
"QueryType": "AND",
"IncludeRelated": False,
"IsAcknowledged": "NotSet"
},
"pagingParameters": {
"Page": 0,
"PageSize": 50
}
}

Batch = {"$type": "QueryBatch,http://schemas.evosnap.com/CWS/v2.0/DataServices/TMS/Rest",
         "queryBatchParameters": {
             "BatchDateRange":None,
             "BatchIds":None,
             "MerchantProfileIds":None,
             "ServiceKeys": None,
             "TransactionIds": None
             },
         "pagingParameters": {
            "Page": 0,
            "PageSize": 50
            }
         }