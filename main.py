import kimi
from kimi import chat
import os
last_command=""
def change_type(type):
    kimi.cur_type=type
while True:

    query_sts=input("("+kimi.cur_type+")>>>")
    if query_sts.startswith("--"):
        change_type(query_sts[2:])

    else:
        if query_sts=="e":
            os.system(last_command)
            last_command=""
        else:
            response=chat(query_sts)
            if kimi.cur_type=="shell":
                last_command=response
            print(response)

