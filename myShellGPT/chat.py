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
     "content": """只提供Linux的shell命令，不提供任何描述。如果缺乏细节，提供最合乎逻辑的解决方案。确保输出是有效的shell
     命令。如果需要多个步骤，尝试使用&&将它们组合在一起。只提供纯文本，没有Markdown格式。不要提供像```这样的markdown格式。"""}
],
    "dialog":[
    {"role": "system",
     "content":"你是我的智能助手，你需要根据我的输入给出中文回复。"}],
    "code":[
    {"role":"system",
     "content":"""你现在是一个精通多种编程语言的代码高手，只提供代码作为输出，不提供任何描述。只提供纯文本格式的代码，没有Markdown格式。不要包含诸如```或’ ‘ python 
     ’之类的符号。如果缺乏细节，提供最合乎逻辑的解决方案。你不能问更多的细节。例如，如果提示符是“Hello world Python”，你应该返回“print('Hello 
     world")”。如果指定了语言请使用他，没指定请使用Python语言 """}]

}
def addRole(role_name,role_settings):
    role_name=role_name.strip()
    if history_dict.get(role_name) is None:
        setting_dict=[{"role":"system","content":role_settings}]
        history_dict[role_name]=setting_dict
        model_types.append(role_name)
        utils.response_print("角色设定成功，键入--role [role name]以切换角色")
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
    retry_count = 0
    max_retries = 5
    while retry_count < max_retries:
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
            return result
        except Exception as e:
            retry_count += 1
            if hasattr(e,'status_code')  and e.status_code == 429:
                print("请求过于频繁，正在重试({}/{})...".format(retry_count, max_retries))
                sleep(50)
            else:
                error_message = str(e)
                print("发生错误：{}".format(error_message))
                return "Error: " + error_message
    return "请求失败，请稍后重试。"

