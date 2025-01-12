from typing import TypedDict


class ChunkNode(TypedDict):
   """
   This class is an object contain field for chunk
   FileName: Name of file chunked, include path
   Chunk: Chunk of content in file. if file is document, chunk is a paragraph, if file is code chunk is the function of code or hole file or the splited of file
   Module: The module of file, which is the file written about (functions, screen, api, ...)?
   """
   FileName: str
   Chunk: str
   Module: str
   Type: str