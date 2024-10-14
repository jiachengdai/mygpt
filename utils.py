import models

def response_print(response):
    model_name=models.get_cur_model_name()
    print(model_name+": \033[1;32m"+response+"\033[0m")