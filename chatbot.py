from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma 
import gradio as gr 
from dotenv import load_dotenv 
import os 

load_dotenv() 

# Configuration 
CHROMA_PATH = r"chroma_db" 

# ✅ Use free Hugging Face embeddings for retrieval
embeddings_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Gemini LLM for answers (still uses your .env key)
llm = ChatGoogleGenerativeAI( 
    model="gemini-2.5-pro",   # you can change to "gemini-1.5-pro-latest" if needed
    google_api_key=os.getenv("GOOGLE_API_KEY"), 
    temperature=0.5 
) 

# Connect to Chroma DB 
vector_store = Chroma( 
    collection_name="example_collection", 
    embedding_function=embeddings_model, 
    persist_directory=CHROMA_PATH, 
) 

# Setup Retriever 
num_results = 5 
retriever = vector_store.as_retriever(search_kwargs={'k': num_results}) 

# Response function 
def stream_response(message, history): 
    docs = retriever.invoke(message) 
    knowledge = "\n\n".join([doc.page_content for doc in docs]) 

    rag_prompt = f""" 
    You are an assistant that answers questions using only the information in the "The knowledge" section. 
    Do not use internal knowledge or mention the knowledge source to the user. 

    If you cannot find the answer in the "The knowledge" section, respond with "I don't know."

    But if you are asked natural questions or narutal statements like greetings and directions that are not related to the knowledge, you can answer them using your internal knowledge. 
    But do not make up facts or information, and for such questions, you can respond with "I don't know."  

    The question: {message} 

    Conversation history: {history} 

    The knowledge: {knowledge} 
    """ 

    partial_message = "" 
    for response in llm.stream(rag_prompt): 
        partial_message += response.content 
        yield partial_message 

# Gradio App 
chatbot = gr.ChatInterface( 
    stream_response, 
    textbox=gr.Textbox(placeholder="Ask something...", container=False, autoscroll=True, scale=7), 
) 

chatbot.launch(share=True)
