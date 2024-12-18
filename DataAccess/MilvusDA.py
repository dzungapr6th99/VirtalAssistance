from langchain.vectorstores import Milvus
import pymilvus
from Entities.CommonLib import ConfigData
from pymilvus import Connections, MilvusClient
class MilvusDA:
    
    def __init__(self, ip, port, token) -> None:
        self.__ipAddress = ip
        self.__port = port
        self.__milvusToken = token
        self.client = MilvusClient(uri= self.__ipAddress + ":" + self.__port)
        
    

        
