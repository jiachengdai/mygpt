import kimi
from kimi import module_type

cur_module_name="kimi"
cur_module=kimi
modules={'kimi':kimi}
module_typs=["shell","dialog"]
def set_cur_module(module_name):
    global cur_module_name,cur_module
    if module_name not in  modules.keys() :
        print("\033[1;31mNo module named "+module_name+", default kimi\033[0m")
    else:
        cur_module_name = module_name
        cur_module = modules[module_name]
def get_cur_module_name():
    return cur_module_name

def get_cur_module():
    return modules[cur_module_name]


def change_module_type(type_name):
    if type_name not in module_typs:
        print("\033[1;31mNo type named "+type_name+", default dialog \033[0m")
        cur_module.module_type="dialog"
    else:
        cur_module.module_type = type_name