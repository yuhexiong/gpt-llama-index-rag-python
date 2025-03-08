# GPT Llama Index RAG

使用 Llama Index 整合 OpenAI GPT 實現 RAG，使其能夠讀取目錄中的文件並提供更有根據的答案。

## Overview

- 模組：openai v1.64.0
- RAG：llama_index v0.12.19


## Run

### Prerequisites

1. 從 [OpenAI](https://platform.openai.com/) 獲取 API 金鑰（可能需要付費訂閱），並將金鑰更新至 `.env` 檔案中。
2. 將你的參考筆記或文件放在 `data` 目錄中，已提供兩個範例文件。
3. 在讀取文件後，程式將把生成的索引儲存在 `index_storage` 目錄中。

### Install Module

```bash
pip install openai==1.64.0 llama_index==0.12.19
```

### Run
```bash
python starter.py
```

## References

- [Llama Index Github](https://github.com/run-llama/llama_index)
- [LlamaIndex  Starter Tutorial](https://docs.llamaindex.ai/en/stable/getting_started/starter_example/)