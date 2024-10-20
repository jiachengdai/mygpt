from time import sleep
from openai import OpenAI
from models import get_cur_model, get_cur_model_name, get_cur_model_type,model_types
import utils

last_model_name=get_cur_model_name()
model=get_cur_model()
client = OpenAI(
    api_key=model["api_key"],
    base_url=model["base_url"],
)

history_dict={
    "shell":[
    {"role": "system",
     "content": "你现在是一个Linux的命令助手，需要根据我提供的场景，返回特定的Linux命令，注意不要有其他内容，如果你认为场景模糊不清或有多种可能的结果，请返回最有可能的哪一种结果。总之就是不要输出除了命令之外的内容，也就是仅仅返回指令的字符串格式"}
],
    "dialog":[
    {"role": "system",
     "content":"你是我的智能助手，你需要根据我的输入给出中文回复。"}],
    "code":[
    {"role":"system",
     "content":'你现在是一个精通多种编程语言的代码高手，请根据我的提示输出代码，默认语言为python，如果我另外指定了语言，请使用它，请在代码第一行中注释体现语言类型，请仅包含代码内容，务必不要输出语言描述以及"""等Markdown的包裹'}]

}
def addRole(role_name,role_settings):

    if history_dict.get(role_name) is None:
        setting_dict=[{"role":"system","content":role_settings}]
        history_dict[role_name]=setting_dict
        model_types.append(role_name)
        utils.response_print("角色设定成功，键入--type [role name]以切换角色")
    else:
        print("\033[1;31m角色" + role_name + "已存在，请重新设定\033[0m")

def delHistory():
    model_type=get_cur_model_type()
    history_dict[model_type]= history_dict[model_type][0:1] + history_dict[model_type][-20:]

def check_change_model():
    model_name = get_cur_model_name()
    global client, model, last_model_name
    if model_name != last_model_name:
        model = get_cur_model()

        client = OpenAI(
            api_key=model["api_key"],
            base_url=model["base_url"],
        )
        last_model_name = model_name

def chat(query):
    check_change_model()
    model_type = get_cur_model_type()
    history=history_dict[model_type]
    if query=="":
        query+=" "
    try:
        history.append({
            "role": "user",
            "content": query
        })
        completion = client.chat.completions.create(
            model=model['model'],
            messages=history,
            temperature=0.3,
        )
        result = completion.choices[0].message.content
        history.append({
            "role": "assistant",
            "content": result
        })
        if len(history)>=40:
            delHistory()

    except Exception as e:
        if hasattr(e,'status_code')  and e.status_code == 429:
            # print("loading.....")
            sleep(50)
            result= chat(query)
        else:
            result = "error  "+e.body['message'] if e.body is not None else ""
    return result

