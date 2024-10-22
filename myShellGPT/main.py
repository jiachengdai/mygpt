from chat import chat, addRole
import utils
from utils import response_print
import os
from models import set_cur_model, change_model_type, get_cur_model_type

# 上一轮询问得到的shell命令
last_response = ""
def handle_command(query_sts):
    if query_sts.startswith("--role"):
        change_model_type(query_sts[7:])
    elif query_sts.startswith("--model"):
        set_cur_model(query_sts[8:])
    elif query_sts.startswith("--add role"):
        role_name = input("输入角色名称: ")
        role_settings = input("输入角色设定: ")
        addRole(role_name, role_settings)
    elif query_sts.lower() in ['exit', 'quit']:
        utils.color_print("再见😉","blue")
        exit()
    elif query_sts.startswith("--help"):
        utils.print_help()
    else:
        return False  # 非命令输入
    return True  # 已处理命令


while True:
    # 对话还是命令提问
    cur_model_type = get_cur_model_type()
    # 提示用户输入
    query_sts = input("(" + cur_model_type + ")>>>")
    if handle_command(query_sts):
        continue

    if cur_model_type == "shell" and query_sts == "e":
        if last_response:
            confirm = input("即将执行命令: {}\n确认执行？(y/n): ".format(last_response)).strip().lower()
            if confirm == 'y':
                os.system(last_response)
                last_response = ""
                utils.color_print("命令执行成功🌟", "blue")
            else:
                utils.color_print("命令执行已取消","blue")
        else:
            print("没有可执行的命令🤨","blue")
    elif cur_model_type == "code" and query_sts.startswith("--to"):
        code_path = query_sts[4:].strip()
        utils.code_save(code_path, last_response)

    else:
        response = chat(query_sts)
        last_response = response
        response_print(response)
