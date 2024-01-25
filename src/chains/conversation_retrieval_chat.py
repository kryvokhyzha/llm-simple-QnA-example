import os

from dotenv import find_dotenv, load_dotenv
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import AzureChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.memory import ConversationSummaryMemory
from langchain.prompts import PromptTemplate
from langchain.vectorstores import Qdrant
from qdrant_client import QdrantClient


_ = load_dotenv(find_dotenv())

condense_question_prompt_template = """Given the following conversation and a follow-up message, \
rephrase the follow-up message to a stand-alone question or instruction that \
represents the user's intent, add all context needed if necessary to generate a complete and \
unambiguous question or instruction, only based on the history, don't make up messages. \
Maintain the same language as the follow up input message.

Chat History:
{chat_history}

Follow Up Input: {question}
Standalone question or instruction:"""

combine_docs_chain_prompt_template = """Use the following pieces of context to answer the user's question. \
If you don't know the answer, just say that you don't know, don't try to make up an answer.

Question:
{question}

Context:
{context}
"""

condense_question_prompt = PromptTemplate.from_template(
    template=condense_question_prompt_template,
)
combine_docs_custom_prompt = PromptTemplate.from_template(
    template=combine_docs_chain_prompt_template,
)
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

memory = ConversationSummaryMemory(llm=llm, memory_key="chat_history", return_messages=True)
# memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    chain_type="stuff",
    retriever=doc_store.as_retriever(),
    memory=memory,
    condense_question_prompt=condense_question_prompt,
    combine_docs_chain_kwargs=dict(prompt=combine_docs_custom_prompt),
)
