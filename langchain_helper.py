from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory

llm = GoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.7,
    google_api_key="AIzaSyBPqp1vpv2bouyJf6yGNkUoDMQiNiz17Tw"
)

# Use memory to store previous conversation
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

prompt = PromptTemplate(
    input_variables=["chat_history", "user_input"],
    template="""
You are an assistant that answers in Moroccan Darija only.

Conversation so far:
{chat_history}

User: {user_input}
Assistant (Darija only):
""")

# Initialize the chain globally
chat_chain = LLMChain(
    llm=llm,
    prompt=prompt,
    memory=memory,
    verbose=True  # optional, shows steps
)

def generate_content(user_input):
    response = chat_chain.invoke({"user_input": user_input})
    return response['text']
