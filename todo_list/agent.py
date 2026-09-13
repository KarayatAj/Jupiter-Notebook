from google.adk.agents.llm_agent import LlmAgent

from pydantic import BaseModel, Field
from datetime import date

class TodoItem(BaseModel):
    task: str = Field(description="Task name")
    due_date: date = Field(description="YYYY-MM-DD format")
    priority: str = Field(description="low/medium/high")

root_agent = LlmAgent(
    name="todo_agent",
    model="gemini-3.6-flash",
    instruction="""Generate todo items in exact JSON format.
    Make sure the response is in exact JSON format with the key 'todo' and the value is the TodoItem object
    1. task: task name
    2. due_date: due date in YYYY-MM-DD format
    3. priority: priority in low/medium/high format
    example output: {'todo': {'task': 'Buy milk', 'due_date': '2022-12-01', 'priority': 'low'}} 
    """,
    output_schema=TodoItem,
    output_key="todo"
)

# Example usage (for standalone script execution)
if __name__ == "__main__":
    from google.adk.runners import InMemoryRunner
    runner = InMemoryRunner(agent=root_agent)
    response = runner.run("Create high-priority task to call client today")
    print(response)

