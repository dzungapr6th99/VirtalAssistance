from fastapi import FastAPI, File, UploadFile
from logging import Logger
from pymilvus import Milvus

class QAServiceHelper:
    def __init__(self) -> None:
        self.Name = "QA Server"
        
    async def chat(chat_id: str = '', question: str= '' ):
        
        
        return True
    
    async def queryVectorDb():
        