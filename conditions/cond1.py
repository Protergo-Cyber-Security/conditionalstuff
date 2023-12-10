from helper.blockfw import blockfw_forti as __blockfw_forti__ 
from helper.avaction import isolateav as __isolateav__
def blockExternalAttempt(src_ip,dst_ip,event_name,id,raw_log):
    if src_ip == "10.10.10.10":
        __blockfw_forti__(src_ip)

def isolateifcontainvirus(src_ip,dst_ip,event_name,id,raw_log):
    import re
    if re.search('virus',raw_log):
        __isolateav__(id)
    else:
        print("not found")

## analyst tinggal bikin condition in python disini
## contoh lagi 
## def blockifnotstartwith104():
##     import re
##     if re.search('104.+',src_ip):
##        __blockfw_forti(src_ip)
##     else:
##         print("not found")


if __name__ == "__main__":
    pass