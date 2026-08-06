from flask import Flask, render_template, request, jsonify

import os
from dotenv import load_dotenv

# Helper functions
from src.helper import (
    download_hugging_face_embeddings,
    load_pdf_file,
    text_split
)

# Pinecone
from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore

# Groq LLM
from langchain_groq import ChatGroq

# Prompt
from langchain_core.prompts import ChatPromptTemplate

# Chains
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from src.prompt import *
import os

app = Flask(__name__)

load_dotenv()

PINECONE_API_KEY=os.environ.get('PINECONE_API_KEY')
GROQ_API_KEY=os.environ.get('GROQ_API_KEY')

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["GROQ_API_KEY"] = GROQ_API_KEY

embeddings = download_hugging_face_embeddings()

index_name = "medicalbot"

docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings
)

retriever = docsearch.as_retriever(search_type="similarity",search_kwargs={"k":3})

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.4,
    max_tokens=500,
    api_key=os.getenv("GROQ_API_KEY")
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}")
    ]
)

Question_ans_chain = create_stuff_documents_chain(llm,prompt)
Rag_chain = create_retrieval_chain(retriever,Question_ans_chain )


@app.route("/")
def index():
    return render_template("chat.html")


@app.route("/get", methods=["GET", "POST"])
def chat():
    # Get user message from frontend
    msg = request.form["msg"]
    print("User:", msg)

    # Get response from RAG chain
    response = Rag_chain.invoke({"input": msg})

    print("Bot:", response["answer"])

    # Send response back to frontend
    return response["answer"]


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)