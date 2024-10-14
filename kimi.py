from time import sleep

from openai import OpenAI
module_type= "dialog"
client = OpenAI(
    api_key="sk-bYyvQmVrGmW4tZ61TGDfRxZVVoeHozROaZF4UGGGjcwixcra",
    base_url="https://api.moonshot.cn/v1",
)

history_dict={
    "shell":[
    {"role": "system",
     "content": "你现在是一个Linux的命令助手，需要根据我提供的场景，返回特定的Linux命令，注意不要有其他内容，如果你认为场景模糊不清或有多种可能的结果，请返回最有可能的哪一种结果。总之就是不要输出除了命令之外的内容，也就是仅仅返回指令的字符串格式"}
],
    "dialog":[
    {"role": "system",
     "content":"你是KIMI，我的智能助手，你需要根据我的输入给出中文回复。"}
]
}

def delHistory():
    history_dict[module_type]= history_dict[module_type][0:1] + history_dict[module_type][-20:]
    print(history_dict[module_type])
def chat(query):
    history=history_dict[module_type]
    if query=="":
        query+=" "
    try:
        history.append({
            "role": "user",
            "content": query
        })
        completion = client.chat.completions.create(
            model="moonshot-v1-8k",
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

        if e.status_code is not None and e.status_code == 429:
            # print("loading.....")
            sleep(50)
            result= chat(query)
        else:
            result = "error  "+e.body['message'] if e.body is not None else ""
    return result

