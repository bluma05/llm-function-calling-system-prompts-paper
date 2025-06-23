# LLM + Function Calling + Tools + System Prompts – Scientific Paper Landing

## Overview
This project delivers a scientific-style landing page that documents and demonstrates the orchestration of Large Language Models (LLMs), function calling, modular tools, and advanced system prompts for building unique, robust, and autonomous AI agents. The design is inspired by academic papers, with a focus on clarity, modularity, and best practices.

## Features
- **Scientific paper layout** with sidebar navigation and logical sections
- **TailwindCSS** for modern, responsive, and accessible design
- **Frames and callouts** for best practices, code examples, and agent prompt patterns
- **Real-world agent prompt examples** (BluMA, Cursor, Devin, Manus, etc.)
- **References** to foundational papers and open-source projects

## Sections
- Introduction
- LLM & Function Calling
- System Prompts
- Prompt Patterns
- Tools Integration
- Agent Examples
- Guides & Templates
- Use Cases
- References

## Usage
1. Clone or download this repository
2. Open `index.html` in your browser
3. Explore the scientific documentation and examples

## Technologies
- HTML5
- [TailwindCSS](https://tailwindcss.com/) (CDN)
- Optional: index.js for sidebar interactivity

## Example Agent Prompt (JSON)
```json
{
  "identity": "Scientific Agent",
  "purpose": "Autonomous LLM with function calling and modular tools",
  "principles": ["Structured reasoning", "Iterative refinement", "Security-first"],
  "tools": ["Shell", "File System", "Web API"],
  "communication": "Clear, concise, and scientific",
  "restrictions": ["Never expose secrets", "Never execute destructive actions without confirmation"]
}
```

## Best Practices
- Define clear agent identity and purpose in system prompts
- Explicitly list allowed tools and APIs
- Set strict boundaries for security and privacy
- Document fallback and error recovery strategies
- Enforce structured, scientific communication
- Always validate tool parameters and schemas before execution
- Never expose secrets or sensitive data in function calls
- Implement permission boundaries and confirmation for destructive actions
- Log all tool invocations for audit and debugging
- Design tools to be modular and composable

## Python Example: LLM with Tool Calling

A fully functional script using OpenAI's function calling to execute a shell command as a tool:

```python
import os
import openai
import subprocess
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

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
```

## System Prompt Techniques (Context7)

See `CONTEXT7_TECHNIQUES.md` for a summary of advanced prompt patterns, tool schemas, and orchestration strategies extracted from Context7 and open-source agents.

## CI/CD

This repo includes a GitHub Actions workflow for linting and testing Python scripts (see `.github/workflows/ci.yml`).

## References
- [Landing Orquestração IA (GitHub)](https://github.com/bluma05/landing-orquestracao-ia)
- [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2303.11366)
- [OpenAI Function Calling Cookbook](https://github.com/openai/openai-cookbook/blob/main/examples/Function_calling_with_OpenAI_API.ipynb)
- [Auto-GPT](https://github.com/Significant-Gravitas/Auto-GPT)
- [Microsoft Semantic Kernel](https://github.com/microsoft/semantic-kernel)
- [System Prompts and Models of AI Tools (Context7)](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)

## Author
Developed by BluMA – 2025
