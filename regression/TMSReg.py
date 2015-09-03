from httprequests import TMS, SignOn
from testcases import TMSParams
from miscutils import dataquery

base_url = "https://api.ciptest.goevo.local/2.1.23/REST/"

sessiontoken = SignOn.SignOnWithToken(base_url,dataquery.getIdentityToken("TEST","6B2866C8FD500001"))

for testcase in TMSParams.TestCases.values():
    TMS.QueryTransactionsSummary(base_url,sessiontoken,**testcase)


#TMS.QueryTransactionsSummary(base_url,bb_sessiontoken,TransactionDateRange={"StartDateTime":"2015-07-01T14:08:41.237Z","EndDateTime":"2015-07-23T14:08:41.237Z"},MerchantProfileIds=["EncyrptionMerchantA"])