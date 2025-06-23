import os
              from openai import AzureOpenAI
              import subprocess
              from dotenv import load_dotenv
              
              load_dotenv()
              
              client = AzureOpenAI(
                      azure_endpoint='<YOUR_ENDPOINT>', 
                      api_key='YOUR_API_KEY',  
                      api_version="2024-05-01-preview"
                  )
              
              # Lista de comandos permitidos e seus aliases
              ALLOWED_COMMANDS = {
                  "python": ["python", "py", "python3"],
                  "pip": ["pip", "pip3"],
                  "dir": ["dir"],
                  "echo": ["echo"],
                  "type": ["type"],  # equivalente ao 'cat' no Windows
                  "ver": ["ver"],    # versão do Windows
                  "systeminfo": ["systeminfo"],
                  "where": ["where"] # equivalente ao 'which' no Linux
              }
              
              def is_command_allowed(command: str) -> bool:
                  """Verifica se o comando é permitido."""
                  # Pega o primeiro token como o comando principal
                  cmd_parts = command.strip().split()
                  if not cmd_parts:
                      return False
                  
                  base_cmd = cmd_parts[0].lower()
                  
                  # Verifica se o comando está na lista de permitidos
                  for allowed_variants in ALLOWED_COMMANDS.values():
                      if base_cmd in allowed_variants:
                          return True
                  return False
              
              def sanitize_command(command: str) -> str:
                  """Sanitiza o comando removendo caracteres e operadores perigosos."""
                  dangerous_chars = ['&', '|', ';', '>', '<', '`', '$', '(', ')', '[', ']', '{', '}', '\\']
                  sanitized = command
                  for char in dangerous_chars:
                      sanitized = sanitized.replace(char, '')
                  return sanitized.strip()
              
              def run_shell_command(command: str, timeout: int = 30) -> str:
                  """
                  Executa um comando no terminal com validações de segurança.
                  
                  Args:
                      command: O comando a ser executado
                      timeout: Tempo máximo de execução em segundos (padrão: 30s)
                  
                  Returns:
                      str: A saída do comando ou mensagem de erro
                  """
                  try:
                      # Sanitiza e valida o comando
                      sanitized_command = sanitize_command(command)
                      if not is_command_allowed(sanitized_command):
                          return f"Erro de segurança: Comando '{command}' não está na lista de comandos permitidos."
                      
                      # Executa o comando com timeout
                      result = subprocess.check_output(
                          sanitized_command,
                          shell=True,
                          stderr=subprocess.STDOUT,
                          text=True,
                          timeout=timeout
                      )
                      return result.strip()
                  except subprocess.TimeoutExpired:
                      return f"Erro: Comando excedeu o tempo limite de {timeout} segundos."
                  except subprocess.CalledProcessError as e:
                      return f"Erro ao executar comando: Código de saída {e.returncode}"
                  except Exception as e:
                      return f"Erro inesperado: {str(e)}"
              
              def list_files(timeout: int = 30) -> str:
                  """
                  Lista arquivos no diretório atual de forma segura.
                  
                  Args:
                      timeout: Tempo máximo de execução em segundos (padrão: 30s)
                  
                  Returns:
                      str: Lista de arquivos ou mensagem de erro
                  """
                  return run_shell_command("dir", timeout=timeout)
              
              tools = {
                  "run_shell_command": {
                      "name": "run_shell_command",
                      "description": "Executa um comando no terminal Windows e retorna sua saída. Apenas comandos da lista de permitidos são aceitos.",
                      "parameters": {
                          "type": "object",
                          "properties": {
                              "command": {"type": "string", "description": "O comando a ser executado."},
                              "timeout": {"type": "integer", "description": "Tempo máximo de execução em segundos (padrão: 30s)"}
                          },
                          "required": ["command"]
                      },
                      "function": run_shell_command
                  },
                  "list_files": {
                      "name": "list_files",
                      "description": "Lista arquivos no diretório atual usando o comando 'dir'.",
                      "parameters": {
                          "type": "object",
                          "properties": {},
                          "required": []
                      },
                      "function": list_files
                  }
              }
              
              class LLM:
                  def __init__(self, client, tools):
                      self.client = client
                      self.tools = tools
                      self.functions = [
                          {
                              "name": tool["name"],
                              "description": tool["description"],
                              "parameters": tool["parameters"]
                          }
                          for tool in tools.values()
                      ]
                  
                  def run(self, messages):
                      response = self.client.chat.completions.create(
                          model="gpt-4o",
                          messages=messages,
                          functions=self.functions,
                          function_call="auto"
                      )
                      
                      message = response.choices[0].message
                      
                      if message.function_call:
                          func_name = message.function_call.name
                          if func_name in self.tools:
                              try:
                                  args = eval(message.function_call.arguments)
                                  tool = self.tools[func_name]
                                  if args:
                                      result = tool["function"](args["command"])
                                  else:
                                      result = tool["function"]()
                                  
                                  # Adiciona o resultado da função ao contexto e pede interpretação
                                  messages.append({
                                      "role": "assistant",
                                      "content": None,
                                      "function_call": {
                                          "name": func_name,
                                          "arguments": message.function_call.arguments
                                      }
                                  })
                                  messages.append({
                                      "role": "function",
                                      "name": func_name,
                                      "content": result
                                  })
                                  return self.run(messages)
                              except Exception as e:
                                  return f"Erro ao executar {func_name}: {str(e)}"
                          else:
                              return f"Ferramenta desconhecida: {func_name}"
                      else:
                          return message.content
              
              def main():
                  llm = LLM(client, tools)
                  messages = [
                      {
                          "role": "system",
                          "content": "Você é um assistente que pode executar comandos no Windows e interpretar seus resultados. Use as ferramentas disponíveis quando necessário."
                      },
                      {
                          "role": "user",
                          "content": "qual é a versão do python instalado na maquina ?"
                      }
                  ]
                  
                  result = llm.run(messages)
                  print("\nResultado:")
                  print(result)
              
              if __name__ == "__main__":
                  main()
