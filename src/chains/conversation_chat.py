import os

from dotenv import find_dotenv, load_dotenv
from langchain.chains import ConversationChain
from langchain.chat_models import AzureChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.memory import ConversationSummaryMemory
from langchain.vectorstores import Qdrant
from qdrant_client import QdrantClient


_ = load_dotenv(find_dotenv())

embeddings = OpenAIEmbeddings(deployment=os.getenv("EMBEDDING_DEPLOYMENT_NAME"))

doc_store = Qdrant(
    client=QdrantClient(url=os.getenv("QDRANT_URL")),
    collection_name=os.getenv("QDRANT_COLLECTION_NAME"),
    embeddings=embeddings,
)

llm = AzureChatOpenAI(
    deployment_name=os.getenv("LLM_DEPLOYMENT_NAME"),
    temperature=0,
    verbose=False,
)

memory = ConversationSummaryMemory(llm=llm, memory_key="history", return_messages=True)
chain = ConversationChain(
    llm=llm,
    memory=memory,
)


if __name__ == "__main__":
    chain.run("What is the meaning of life?")
