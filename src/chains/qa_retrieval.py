import os

from dotenv import find_dotenv, load_dotenv
from langchain.chains import RetrievalQA
from langchain.chat_models import AzureChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
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

chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=doc_store.as_retriever(),
    return_source_documents=False,
)


if __name__ == "__main__":
    chain.run("What is the meaning of life?")
