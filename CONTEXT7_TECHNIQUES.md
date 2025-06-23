# System Prompt Techniques & Tool Patterns (Context7 Extract)

## Key Techniques for System Prompts

- **Explicit Tool Invocation**: Use XML/JSON schemas to define tool calls, e.g.,
  ```xml
  <read_file>
    <path>src/main.js</path>
  </read_file>
  ```
- **Stepwise Reasoning**: Structure agent thinking in explicit steps, e.g.,
  ```json
  {
    "step": 1,
    "thought": "Analyze the user request and decompose into subtasks",
    "tools": ["files", "shell", "notion"],
    "next": "Plan tool usage and execution order"
  }
  ```
- **Plan/Act Modes**: Separate planning from execution, e.g.,
  ```xml
  <plan_mode_respond>
    <response>Your response here</response>
  </plan_mode_respond>
  ```
- **Tool Schema Enforcement**: Always validate tool parameters and schemas before execution.
- **Security Boundaries**: Never expose secrets, always require confirmation for destructive actions.
- **Fallback & Recovery**: Define policies for error handling and rollback.
- **Multi-agent Orchestration**: Use dispatcher cores to route tasks to the best agent.
- **Memory & Context Management**: Save and update important context for continuity.

## Example: Tool Call in System Prompt
```xml
<execute_command>
  <command>npm run dev</command>
  <requires_approval>false</requires_approval>
</execute_command>
```

## Example: Creating a New Task
```xml
<new_task>
  <context>Implement refresh token and RBAC</context>
</new_task>
```

## Further Reading
- [System Prompts and Models of AI Tools (Context7)](https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools)
- [OpenAI Function Calling Guide](https://platform.openai.com/docs/guides/function-calling)
- [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2303.11366)
