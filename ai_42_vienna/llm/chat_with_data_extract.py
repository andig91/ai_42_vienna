from dotenv import load_dotenv
import os
#import streamlit as st
import langchain
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import WebBaseLoader, TextLoader, DirectoryLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain.callbacks import StdOutCallbackHandler
import json
langchain.debug = True
langchain.verbose=True


loader = DirectoryLoader('./wikiartikel/plain/', glob="./*.txt", loader_cls=TextLoader)

data = loader.load()
fileOut = open("./wikiartikel/output_load.txt", "w")
fileOut.write(str(data))
fileOut.close()
print(data)
       