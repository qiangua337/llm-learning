# Please install OpenAI SDK first: `pip3 install openai`
import os
from openai import OpenAI

# 创建与AI大模型交互的客户端对象 (DEEPSEEK_API_KEY 环境变量名字 , 值就是deepseek的API_KEY)
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'), base_url="https://api.deepseek.com")

# 与AI大模型进行交互
messages = [
        {
            "role": "system",
            "content": "你是一名可爱的AI助理，请用温柔可爱的语气回答用户问题"
        }
    ]

while True:

        user_input = input("你：")

        if user_input == "exit":
            break

        messages.append({
            "role": "user",
            "content": user_input
        })

        response = client.chat.completions.create(
            model="deepseek-v4-pro",
            messages=messages
        )

        ai_reply = response.choices[0].message.content

        print("AI：", ai_reply)

        messages.append({
            "role": "assistant",
            "content": ai_reply
        })
stream  =False,
reasoning_effort = "high",
extra_body={"thinking": {"type": "enabled"}}


# 输出大模型返回结果
print(response.choices[0].message.content)



