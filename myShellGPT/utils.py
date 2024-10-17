import models


def response_print(response):
    model_name= models.get_cur_model_name()
    print(model_name+": \033[1;32m"+response+"\033[0m")
def color_print(text,color):
    color_dict={"green":["\033[1;32m","\033[0m"],
                "red":["\033[1;31m","\033[0m"],
                "blue":["\033[1;36m","\033[0m"]}
    print(color_dict[color][0]+text+color_dict[color][1])
def code_save(code_path, last_response):
    with open(code_path, 'w', encoding='utf-8') as file:
        file.write(last_response)
        color_print("🤩file has already write into "+code_path,"blue")
