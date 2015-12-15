import os, datetime

def Log(resp_obj,op_name):
    data_files = os.path.join(os.path.dirname( __file__ ), '..', 'files')
    datapath = os.path.abspath(os.path.join(data_files,"testlog.txt"))
    logfile = open(datapath, "a")
    
    line1 = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S") + " --- " + op_name + " --- StatusCode: " + str(resp_obj.status_code) + " --- " + resp_obj.url + "\n"
    line2 = "--Request: " 
    if resp_obj.request.body != None:
        line2 += resp_obj.request.body + "\n"
    else:
        line2 += "\n"
    line3 = "--Response: "
    if resp_obj.status_code == 404:
        line3 += resp_obj.reason + "\n"
    else:
        line3 += resp_obj.text + "\n"
    
    logfile.write(line1+line2+line3)
    logfile.close()
    
def LogAssertions(details):
    if details is None:
        return
    data_files = os.path.join(os.path.dirname( __file__ ), '..', 'files')
    datapath = os.path.abspath(os.path.join(data_files,"testlog.txt"))
    logfile = open(datapath, "a")
    
    detail_string = "{"
    for assertion_result in details:
        detail_string += str(assertion_result) 
    detail_string += "}\n"   
    logfile.write(detail_string)
    logfile.close()
    
    