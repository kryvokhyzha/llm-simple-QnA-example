from fastapi import FastAPI

from src.helper.api_utils import create_service


app: FastAPI = create_service(
    "src.chains.conversation_retrieval_agent_ks.agent:agent",
    # "src.chains.conversation_chat:chain",
    # "src.chains.conversation_retrieval_chat:chain",
    # "src.chains.qa_retrieval:chain",
    title="LangChain Server",
    version="1.0",
    description="API server for LangChain's agents and chains.",
)
