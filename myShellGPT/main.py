from chat import chat
from utils import response_print
import os
from models import set_cur_model, change_model_type, get_cur_model_type

# 上一轮询问得到的ｓｈｅｌｌ命令
last_command=""

while True:
    # 对话还是命令提问
    cur_model_type=get_cur_model_type()
    # 提示用户输入
    query_sts=input("("+cur_model_type+")>>>")

    if query_sts.startswith("--type"):
        change_model_type(query_sts[7:])
    elif query_sts.startswith("--model"):
        set_cur_model(query_sts[8:])
    else:
        if query_sts=="e":
            os.system(last_command)
            last_command=""
        else:
            response=chat(query_sts)
            if cur_model_type=="shell":
                last_command=response
            response_print(response)


