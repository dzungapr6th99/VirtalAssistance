from ollama import Client
from langchain.text_splitter import TextSplitter, RecursiveCharacterTextSplitter
from langchain_milvus import Milvus
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain_community.document_loaders import WebBaseLoader
from langchain.chat_models.ollama import ChatOllama


class RAG():
    def __init__(self, vectorStore: Milvus, llm: ChatOllama):
        self.vectorStore = vectorStore
        self.llmModel = llm 
    def 

