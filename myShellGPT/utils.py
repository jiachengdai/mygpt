import models
import os

def response_print(response):
    model_name= models.get_cur_model_name()
    print(model_name+": \033[1;32m"+response+"\033[0m")
def color_print(text,color):
    color_dict={"green":["\033[1;32m","\033[0m"],
                "red":["\033[1;31m","\033[0m"],
                "blue":["\033[1;36m","\033[0m"]}
    print(color_dict[color][0]+text+color_dict[color][1])
def code_save(code_path, last_response):
    dir_name = os.path.dirname(code_path)
    if dir_name and not os.path.exists(dir_name):
        os.makedirs(dir_name)
    with open(code_path, 'w', encoding='utf-8') as file:
        file.write(last_response)
        color_print("🤩file has already write into "+code_path,"blue")
def print_help():
    help_text = """
可用命令：
--type [role_name]    切换角色（dialog, shell, code 或自定义角色）
--model [model_name]  切换模型（chat-gpt, kimi）
--add role            添加新角色
--help                显示帮助信息
exit 或 quit          退出程序

在 code 角色中：
--to [file_path]      将生成的代码保存到指定路径

在 shell 角色中：
e                    执行上一次生成的命令

🟡请注意：
    在运行程序之前，需要在系统中设置以下环境变量，以确保程序能够正常访问 API：
    export CHAT_GPT_API_KEY='ChatGPT API 密钥'
    export KIMI_API_KEY='Kimi API 密钥'
"""
    print(help_text)