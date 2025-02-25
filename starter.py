import os

import openai
from dotenv import load_dotenv
from llama_index.core import Settings, SimpleDirectoryReader, VectorStoreIndex
from llama_index.llms.openai import OpenAI

load_dotenv()  # 從 .env 載入環境變數

# 取得 OpenAI API Key
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key or openai_api_key == "":
    raise Exception("OPENAI_API_KEY not found in .env file.")
openai.api_key = openai_api_key


# 設定全局 LLM
Settings.llm = OpenAI(model="gpt-4o-mini", temperature=0)

# 載入資料
documents = SimpleDirectoryReader("data").load_data()

# 建立索引，會自動使用全局 Settings 設定
index = VectorStoreIndex.from_documents(documents)

# 儲存索引到資料夾 index_storage
index.storage_context.persist(persist_dir="index_storage")

# 查詢索引
query_engine = index.as_query_engine()
response = query_engine.query("LlamaIndex 可以做什麼？")
print(response)
