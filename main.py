import conditions.cond1 as cond1
from conditions.cond1 import *

def main(src_ip,dst_ip,event_name,id,raw_log):
    conditions = [ x for x in dir(cond1) if "__" not in x ]
    args = [src_ip,dst_ip,event_name,id,raw_log]
    params = []
    for i in range(len(conditions)):
        params.append(args)
    for func, param in zip(conditions, params):
        eval(func+"("+str(param)[1:-1]+")")


if __name__ == "__main__": 
    main("10.10.10.10","1.1.1.1","DNS Query","AE12","ini virus")