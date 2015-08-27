from httprequests import TMS, SignOn
from miscutils import dataquery

bb_sessiontoken = SignOn.SignOnWithToken(base_url,dataquery.getIdentityToken("TEST","BBE2F64B19200001"))


TMS.QueryTransactionsSummary(base_url,bb_sessiontoken,TransactionDateRange={"StartDateTime":"2015-07-01T14:08:41.237Z","EndDateTime":"2015-07-23T14:08:41.237Z"},MerchantProfileIds=["EncyrptionMerchantA"])