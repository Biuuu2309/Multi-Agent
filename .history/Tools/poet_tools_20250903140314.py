from langchain.tools import Tool
from langchain_community.chat_models import ChatOllama # <-- Dòng mới

# Khởi tạo model LLM Local từ Ollama
llm = ChatOllama(model="llama3") # <-- Sử dụng model bạn đã kéo về, ví dụ "llama3", "mistral"
# Tool cho Agent Nhà Thơ
def write_poem(theme: str) -> str:
    """Viết một bài thơ ngắn về chủ đề được cho."""
    poem = llm.invoke(f"Hãy viết một bài thơ ngắn 4 câu về chủ đề: {theme}")
    return poem.content

poem_tool = Tool(
    name="PoemWriter",
    func=write_poem,
    description="Useful for writing a short poem about a given theme. Input should be the theme."
)