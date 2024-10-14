from utils import response_print
import os
from modules import set_cur_module,cur_module,change_module_type

last_command=""
def change_type(module_type):
    change_module_type(module_type)
while True:

    query_sts=input("("+cur_module.module_type+")>>>")
    if query_sts.startswith("--type"):
        change_type(query_sts[7:])
    elif query_sts.startswith("--model"):
        set_cur_module(query_sts[8:])
    else:
        if query_sts=="e":
            os.system(last_command)
            last_command=""
        else:
            response=cur_module.chat(query_sts)
            if cur_module.module_type=="shell":
                last_command=response
            response_print(response)


