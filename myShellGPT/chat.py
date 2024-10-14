from time import sleep
from openai import OpenAI
from models import get_cur_model, get_cur_model_name, get_cur_model_type

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
     "content":"你是我的智能助手，你需要根据我的输入给出中文回复。"}
]
}

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

