

# DeepSeek 多轮对话 Demo

## 功能
使用 Python 调用 DeepSeek API，实现终端中的多轮对话。

## 实现思路
使用 while 循环持续接收用户输入，
并通过 messages 列表保存 user 和 assistant 的历史消息，
实现上下文多轮对话。

## 学到了什么
- DeepSeek API 的基本调用
- messages 的作用
- system、user、assistant 三种角色
- while 循环实现连续对话
- list.append() 保存历史消息

## 运行方法
运行 main.py，在终端输入问题即可开始对话。

输入 exit 结束程序。