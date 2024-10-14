# 所有可用模型的ＡＰＩ，ＵＲＬ，以及模型引擎名
models = {"chat-gpt": {"base_url": 'https://free.gpt.ge/v1/',
                       "api_key": 'sk-nHslw5xXWtKWcZoS695989Aa3eD94929930f7d364d351dF0', "model": "gpt-3.5-turbo"},
          "kimi": {"base_url": 'https://api.moonshot.cn/v1',
                   "api_key": 'sk-bYyvQmVrGmW4tZ61TGDfRxZVVoeHozROaZF4UGGGjcwixcra', "model": "moonshot-v1-8k"}
          }
# 所有可用的对话类型
model_types = ["shell", "dialog"]


# 当前使用模型的名称、类型、ＡＰＩ信息
cur_model = models["chat-gpt"]
cur_model_name = "chat-gpt"
cur_model_type = "dialog"


def set_cur_model(model_name):
    global cur_model_name, cur_model
    if model_name not in models.keys():
        print("\033[1;31mNo model named " + model_name + ", default chat-gpt\033[0m")
    else:
        cur_model_name = model_name
        cur_model = models[model_name]


def change_model_type(type_name):
    global cur_model_type
    if type_name not in model_types:
        print("\033[1;31mNo type named " + type_name + ", default dialog \033[0m")
        cur_model_type = "dialog"
    else:
        cur_model_type = type_name


def get_cur_model_name():
    return cur_model_name

def get_cur_model():
    return models[cur_model_name]

def get_cur_model_type():
    return cur_model_type
