from ast import List
from asyncio.windows_events import NULL
from pickle import FALSE
from ollama import Client
from langchain.text_splitter import TextSplitter, RecursiveCharacterTextSplitter
from langchain_milvus import Milvus
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain_community.document_loaders import WebBaseLoader
from langchain.chat_models.ollama import ChatOllama
from langchain_community.graphs import Neo4jGraph
from langchain_experimental.llms.ollama_functions import OllamaFunctions
from langchain_experimental.graph_transformers import LLMGraphTransformer
class RAG():
    def __init__(self, vectorStore: Milvus, llmGraph: ChatOllama):
        self.vectorStore = vectorStore
        self.graphLLM = llmGraph 
        self.graph = Neo4jGraph()
    def RAG(self, doc: str = '', allow_nodes: List[str] = [], node_properties: List[str] = [], allow_relationship: List[str]= [], node_properties_bool: bool = False):
        graphTranformer = LLMGraphTransformer(llm = self.graphLLM, allowed_nodes= allow_nodes, node_properties = node_properties, allowed_relationships= allow_relationship)
        if (node_properties == NULL or len(node_properties) == 0):
            graphTranformer = LLMGraphTransformer(llm = self.graphLLM, allowed_nodes= allow_nodes, node_properties = node_properties_bool, allowed_relationships= allow_relationship)
        graphTranformer.convert_to_graph_documents(doc)
        self.graph.add_graph_documents(doc)
        
