from collections.abc import Iterator
from typing import Any, Literal, Mapping, Optional, Sequence, Union
from typing_extensions import Unpack
from langchain_community.llms.ollama import Ollama
from ollama._types import Options
from pydantic.config import ConfigDict
from langchain_core.outputs import GenerationChunk, LLMResult
from pymilvus import Milvus, MilvusClient
import ollama
from typing import Any, AnyStr, Union, Optional, Sequence, Mapping, Literal
#from langchain_community.llms import ollama
class CustomizeOllama(Ollama):
    def __init__(self, milvusDataHost: MilvusClient):
        super().__init__()
        self.VectorStore = milvusDataHost
   
        
class MyOllamaClient(ollama.Client):
    def __init__(self, host: str , milvusDb: MilvusClient | None = None, **kwargs) -> None:
        self.milvusDb = milvusDb
        super().__init__(host, **kwargs)
    
    def generate(self, model: str = '', prompt: str = '',system: str = '', template: str = '', context: Sequence[int] | None = None, stream: bool = False, raw: bool = False, format: Literal['', 'json'] = '', images: Sequence[AnyStr] | None = None, options: Options | None = None, keep_alive: float | str | None = None,   collectionName: str= '',) -> Mapping[str, Any] | Iterator[Mapping[str, Any]]:
        query_vector = super().embeddings(model= model ,prompt= prompt)
        vectorPrompt = self.milvusDb.search(collection_name= collectionName, data = [prompt])
        return super().generate(model, prompt, system, template, context, stream, raw, format, images, options, keep_alive)
    
    def search_similary_prompt(self, collection_name: str, query_vector: list, top_k: int = 5):
        search_params = {
            "metric_type": "L2",  # Euclidean distance
            "params": {"nprobe": 10}
        }
        result = self.milvusDb.search(
            collection_name=collection_name,
            data=[query_vector],
            anns_field="vector",
            param=search_params,
            limit=top_k
        )
        return result 
