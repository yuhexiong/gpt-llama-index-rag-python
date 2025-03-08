# GPT Llama Index RAG

**(also provided Traditional Chinese version document [README-CH.md](README-CH.md).)**


Using Llama Index integrated with OpenAI GPT to implement RAG, enabling it to read files from the directory and provide better-informed answers.  

## Overview

- Module: openai v1.64.0
- RAG: llama_index v0.12.19

## Run

### Prerequisites

1. Obtain an API key from [OpenAI](https://platform.openai.com/) (a paid subscription may be required) and update your `.env` file with the key.
2. Place your reference notes or documents in the `data` directory. Two sample files are already provided.
3. After reading the documents, the program will store the generated index in the `index_storage` directory.

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
- [LlamaIndex Starter Tutorial](https://docs.llamaindex.ai/en/stable/getting_started/starter_example/)
