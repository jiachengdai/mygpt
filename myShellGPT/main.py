from chat import chat, addRole
import utils
from utils import response_print
import os
from models import set_cur_model, change_model_type, get_cur_model_type

# 上一轮询问得到的shell命令
last_response = ""

while True:
    # 对话还是命令提问
    cur_model_type = get_cur_model_type()
    # 提示用户输入
    query_sts = input("(" + cur_model_type + ")>>>")

    if query_sts.startswith("--role"):
        change_model_type(query_sts[7:])
    elif query_sts.startswith("--model"):
        set_cur_model(query_sts[8:])
    elif query_sts.startswith("--add role"):
        role_name = input("input role name: ")
        role_settings = input("input role settings: ")
        addRole(role_name, role_settings)
    else:
        if cur_model_type == "shell" and query_sts == "e":
            os.system(last_response)
            last_response = ""
            utils.color_print("命令执行成功🌟", "blue")
        elif cur_model_type == "code" and query_sts.startswith("--to"):
            code_path = query_sts[4:].strip()
            utils.code_save(code_path, last_response)

        else:
            response = chat(query_sts)
            last_response = response
            response_print(response)
