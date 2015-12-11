import json

def assertor(response, assertions):
    if assertions is None:
        return
    response = json.loads(response.text)
    passcount = 0
    details = []    
    for assertion in assertions:
        if assertion[1] not in response.keys():
            #print("Field",assertion[1],"is not part of response. Skipping assertion...")
            details.append([assertion[1],"INVALID","Field is not in response. Skipped Assertion."])
            continue
        if assertion[0] == "exists":
            if response[assertion[1]] != "" and response[assertion[1]] is not None:
                if assertion[2] is True:
                    #print("PASS:", assertion[1], "exists in response")
                    details.append([assertion[1],"PASS","Existence of Field in Response is True"])
                    passcount += 1
                else:
                    #print("FAIL:", assertion[1], "exists in response")
                    details.append([assertion[1],"FAIL","Existence of Field in Response is True"])
            else:
                if assertion[2] is True:
                    #print("FAIL:", assertion[1], "does not exist in response")
                    details.append([assertion[1],"FAIL","Existence of Field in Response is False"])
                else:
                    #print("PASS:", assertion[1], "does not exist in response")
                    details.append([assertion[1],"PASS","Existence of Field in Response is False"])
                    passcount += 1
        elif assertion[0] == "isvalue":
            if response[assertion[1]] == assertion[2]:
                #print("PASS: The value of", assertion[1], "is equal to expected value:", assertion[2])
                details.append([assertion[1],"PASS","Field in Response is equal to expected value"])
                passcount += 1
            else:
                #print("FAIL: The value of", assertion[1], "is not equal to expected value:", assertion[2])
                details.append([assertion[1],"FAIL","Field in Response is NOT equal to expected value"])
        elif assertion[0] == "isnotvalue":
            if response[assertion[1]] != assertion[2]:
                #print("PASS: The value of", assertion[1], "is not equal to expected value:", assertion[2])
                details.append([assertion[1],"PASS","Field in Response is NOT equal to expected value"])
                passcount += 1
            else:
                #print("FAIL: The value of", assertion[1], "is equal to expected value:", assertion[2])
                details.append([assertion[1],"FAIL","Field in Response is equal to expected value"])
    print(str(passcount)+ "/" + str(len(assertions)) + " assertions are passing")
    return(details)