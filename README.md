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

## References
- [Landing Orquestração IA (GitHub)](https://github.com/bluma05/landing-orquestracao-ia)
- [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2303.11366)
- [OpenAI Function Calling Cookbook](https://github.com/openai/openai-cookbook/blob/main/examples/Function_calling_with_OpenAI_API.ipynb)
- [Auto-GPT](https://github.com/Significant-Gravitas/Auto-GPT)
- [Microsoft Semantic Kernel](https://github.com/microsoft/semantic-kernel)

## Author
Developed by BluMA – 2025
