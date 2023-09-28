"""
Script to access the open ai's gpt-3.5-turbo model using python.
"""
import os
import openai
from dotenv import load_dotenv

load_dotenv()


class ChatGPT:
    def __init__(self):
        """
        method to access the open ai's access key and maintaing messages
        list of messages for the message context.
        """
        openai.api_key = os.getenv("OPENAI_API_KEY")
        self.messages = [
            {"role": "system", "content": "You are a intelligent assistant."}
        ]

    def chat(self):
        """
        method to input the query from the user and returning the solution.
        """
        try:
            while True:
                message = input("User Query : ")

                if (
                    message.lower() == "bye"
                    or message.lower() == "exit()"
                    or message.lower() == "exit"
                ):
                    print("Bye, Thanks for connecting us!!")
                    break
                if message:
                    self.messages.append(
                        {"role": "user", "content": message},
                    )
                    chat = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo", messages=self.messages
                    )
                reply = chat.choices[0].message.content
                print(f"ChatGPT: {reply}")
                self.messages.append({"role": "assistant", "content": reply})
        except KeyboardInterrupt as e:
            print("\nBye, Thanks for connecting us!!")


if __name__ == "__main__":
    gpt = ChatGPT()
    gpt.chat()
