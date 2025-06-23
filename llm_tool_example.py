# Example: LLM with Tool Calling (OpenAI + Shell Command)
# This script demonstrates how to use OpenAI's function calling to execute a shell command as a tool.
# Requires: openai>=1.0.0, python-dotenv (for API key management)

import os
import openai
import subprocess
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define the tool schema for function calling
functions = [
    {
        "name": "run_shell_command",
        "description": "Run a shell command and return its output.",
        "parameters": {
            "type": "object",
            "properties": {
                "command": {"type": "string", "description": "The shell command to execute."}
            },
            "required": ["command"]
        }
    }
]

def run_shell_command(command: str) -> str:
    try:
        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, text=True, timeout=10)
        return result.strip()
    except Exception as e:
        return f"Error: {e}"

# Main LLM interaction loop
def main():
    user_prompt = "List all files in the current directory."
    messages = [
        {"role": "system", "content": "You are an AI agent with access to a shell tool. Use the tool to answer user requests that require system access."},
        {"role": "user", "content": user_prompt}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=messages,
        functions=functions,
        function_call="auto"
    )
    message = response["choices"][0]["message"]
    if message.get("function_call"):
        func_name = message["function_call"]["name"]
        args = eval(message["function_call"]["arguments"])
        if func_name == "run_shell_command":
            output = run_shell_command(args["command"])
            print(f"\n[TOOL OUTPUT]\n{output}\n")
        else:
            print("Unknown tool requested.")
    else:
        print(message["content"])

if __name__ == "__main__":
    main()
