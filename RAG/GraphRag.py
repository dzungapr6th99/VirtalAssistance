from ast import List
import os
from asyncio.windows_events import NULL
from pickle import FALSE
from ollama import Client
from langchain_community import PyPDFLoader
from langchain.text_splitter import TextSplitter, RecursiveCharacterTextSplitter
from langchain_milvus import Milvus
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.document_loaders import PyPDFLoader, WebBaseLoader
from langchain.chat_models.ollama import ChatOllama
from langchain_community.graphs import Neo4jGraph
from langchain_experimental.llms.ollama_functions import OllamaFunctions
from langchain_experimental.graph_transformers import LLMGraphTransformer
class RAG():
    def __init__(self, vectorStore: Milvus, llmGraph: ChatOllama):
        self.vectorStore = vectorStore
        self.graphLLM = llmGraph 
        self.graph = Neo4jGraph()
    def RAG(self, path: str = ''):
        if (path == ''):
            return False
        fileCodes = ['.cs', '.cpp', '.html', '.cshtml', '.csprj', '.sln', '.xml', '.js', '.ts']
        fileUrd = '.pdf'
        for subdir, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(fileCodes):
                    f=open(os.path.join(subdir, file),'r')
                    content = f.read()
                    f.close()
                elif file.endswith(fileUrd):
                    loader = PyPDFLoader(dirs)
                    
        
        
    def AddToMilvus(self ,splitContent: List[str] = []):
        self.vectorStore.from_documents(  
            documents=splitContent,
            embedding=HuggingFaceEmbeddings(),
            )
        self.vectorStore.as_retriever()