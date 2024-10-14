import modules


def response_print(response):
    """
    print response word with module and colorful content
    :return: None
    by:jiachengdai
    """
    module_name=modules.get_cur_module_name()
    print(module_name+": \033[1;32m"+response+"\033[0m")

