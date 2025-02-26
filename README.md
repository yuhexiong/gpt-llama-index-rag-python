# GPT Llama Index RAG


使用 Llama index 實現 RAG  
**沒什麼特別的 就用 module 給 gpt 塞小抄**  

## Overview
- openai v1.64.0
- llama_index v0.12.19

參考指令
```
pip install openai==1.64.0 llama_index==0.12.19
```

自行去 [OpenAI](https://platform.openai.com/) 生成 Key(必要時須付費)，更新 .env  
data 下面放小抄，已有兩個範例資料  
程式讀完小抄以後會放在 `index_storage` 底下  

## 參考

文件(**Github README 比官網完整**): 
- [Llama Index Github](https://github.com/run-llama/llama_index)  
- [LlamaIndex Starter Tutorial](https://docs.llamaindex.ai/en/stable/getting_started/starter_example/)