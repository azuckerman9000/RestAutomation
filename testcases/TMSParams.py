## ServiceKey is 6B2866C8FD500001 ##
ServiceId_NGT_SBX = "3CF9E00001"
MPID_NGT_SBX = "Kyle Test"

TestCases = {
             "MerchProfile1":{
                              "MerchantProfileIds":[MPID_NGT_SBX]
                              },
             "ServiceId1":{
                           "ServiceIds":[ServiceId_NGT_SBX]
                           },
             "DateRange1":{
                           "TransactionDateRange":{"StartDateTime":"2015-07-01T14:08:41.237Z","EndDateTime":"2015-07-23T14:08:41.237Z"}
                           },
             "Combo1":{
                        "MerchantProfileIds":[MPID_NGT_SBX,"MagensaMerch"],
                        "TransactionIds":["5b44d4ad0dc5489da6cbad87c999d021","c7d0bc5d32c74165ae5753099ee484a0","743236af9730405e9836f39748d103dc"]
                        },
             "Combo2":{
                       "MerchantProfileIds":[MPID_NGT_SBX],
                       "TransactionDateRange":{"StartDateTime":"2015-07-01T14:08:41.237Z","EndDateTime":"2015-07-23T14:08:41.237Z"}
                       }
             }