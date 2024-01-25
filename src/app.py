from fastapi import FastAPI

from src.langcorn import create_service


app: FastAPI = create_service(
    "src.chains.qa_retrieval:chain",
    "src.chains.conversation_retrieval_chat:chain",
    "src.chains.conversation_chat:chain",
)
