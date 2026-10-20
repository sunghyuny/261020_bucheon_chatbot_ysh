from groq import Groq
from dotenv import load_dotenv
import os
import threading
import tkinter as tk
from tkinter import scrolledtext
load_dotenv()

client = Groq(api_key=(os.getenv("GROQ_API_KEY")))

messages = [    {
        "role":"system",
        "content":"You are a friendly chatbot. Ask the user what they need and answer helpfully. Reply in the same language the user writes in (Korean by default)."
    }]
root = tk.Tk()
root.title("groq")
root.geometry("500x600")
chat = scrolledtext.ScrolledText(root, state = "disabled")
chat.pack(expand=True, fill="both")
frame = tk.Frame(root)
frame.pack(fill='x')
entry = tk.Entry(frame)
entry.pack(side="left", expand=True, fill="x")

def add_chat(text):
    chat.config(state="normal")
    chat.insert("end", text + "\n\n")
    chat.config(state="disabled")
    chat.see("end")


def get_answer():
    # 별도 스레드에서 실행: 응답을 기다리는 동안 창이 멈추지 않게 한다
    try:
        res = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=messages
        )
        answer = res.choices[0].message.content
        messages.append({"role": "assistant", "content": answer})
        root.after(0, finish, "챗봇: " + answer)
    except Exception as e:
        messages.pop()  # 실패한 질문은 기록에서 제거
        root.after(0, finish, f"[오류] {e}")


def finish(text):
    # 위젯은 메인 스레드에서만 건드린다
    add_chat(text)
    btn.config(state="normal")
    entry.focus()


def send(event=None):
    if str(btn["state"]) == "disabled":
        return
    q = entry.get().strip()
    if not q:
        return
    entry.delete(0, "end")
    add_chat("나: " + q)
    messages.append({"role": "user", "content": q})
    btn.config(state="disabled")
    threading.Thread(target=get_answer, daemon=True).start()


btn = tk.Button(frame, text="전송", command=send)
btn.pack(side="right")
entry.bind("<Return>", send)
entry.focus()

root.mainloop()

# while True:
#     q = input("질문:")
    
#     messages.append({
#         "role":"user",
#         "content": q
#     })
#     if q=="exit":
#         print("종료")
#         break
#     res = client.chat.completions.create(
#         model = "openai/gpt-oss-20b",
#         messages = messages
#     )
#     answer = res.choices[0].message.content
        
#     print(answer)
    
#     messages.append(
#         {
#             "role":"assistant",
#             "content":answer,
#         }
#     )
    
    
