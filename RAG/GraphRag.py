from ast import Dict, List
import os
from langchain_core.embeddings import Embeddings
from ollama import Client
from langchain_community import PyPDFLoader
from langchain.text_splitter import TextSplitter, RecursiveCharacterTextSplitter
from langchain_milvus import Milvus
from langchain_community.embeddings import HuggingFaceEmbeddings,OllamaEmbeddings
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
    def RAGByPath(self, path: str = ''):
        if (path == ''):
            return False
        fileCodes = ['.cs', '.cpp', '.html', '.cshtml', '.csprj', '.sln', '.xml', '.js', '.ts']
        fileUrd = '.pdf'
        listContent: List[str]
        listLoader = []
        for subdir, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(fileCodes):
                    f=open(os.path.join(subdir, file),'r')
                    content = f.read()
                    listContent.append(content)
                    f.close()
                elif file.endswith(fileUrd):
                    loader = PyPDFLoader(dirs)
                    listLoader.append(loader)
        #######
        RAG(content= listContent)
            
        return True
    def RAGForCode(self, path: str = '', className: str = '', layer: str= '', module: str = '', model_name: str = ''):
        """
        className: name of the class or which class is processed in file
        path: path of file code
        layer: which layer of the class in file code belong to?
        module: this class is served which module function?
        """        
        fileCodes = ['.cs', '.cpp', '.html', '.cshtml', '.csprj', '.sln', '.xml', '.js', '.ts']
        result = []
        f = open(path, 'r')
        content = f.read()
        f.close
        chunk_type = ''

        split_data = RecursiveCharacterTextSplitter.from_tiktoken_encoder(chunk_size=500, chunk_overlap=50)
        split_contents = split_data.split_text(content)
        if (path.endswith('.cs')):
            chunk_type = 'C#'
        elif (path.endswith('.js')):
            chunk_type = 'JavaScript'
        elif (path.endswith('html') or path.endswith('cshtml')):
            chunk_type = 'HTML'
        embedding = OllamaEmbeddings(model= model_name)
        for split_content in split_contents:
            result.append({"chunk_type": chunk_type, "module": module, "content": split_content
            })
        self.AddToMilvus(splitContent= result, embedding= embedding)
        return True
    def RAG(self, contents: List[str]= [], modelName: str = ''):
        embedding = OllamaEmbeddings(model= modelName)
        for content in contents:
            self.AddToMilvus(splitContent= content, embedding= embedding)
        
        return False
        
    def AddToMilvus(self ,splitContent: Dict[str, object] = [], embedding: Embeddings = None):
        self.vectorStore.from_texts(  
            documents=splitContent,
            embedding=embedding,
            metadatas= splitContent
            )
        self.vectorStore.as_retriever()