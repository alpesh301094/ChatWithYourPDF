import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain.chains.question_answering import load_qa_chain
from langchain_openai import ChatOpenAI
from vector_store import get_chroma_vectorstore

import os
from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

st.title("📄 AI PDF Question Answering")

uploaded_file = st.file_uploader("Upload your PDF", type="pdf")

if uploaded_file:

    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    loader = PyPDFLoader("temp.pdf")
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings()

    vectorstore = get_chroma_vectorstore(chunks, embeddings)

    query = st.text_input("Ask a question about the PDF")

    if query:
        docs = vectorstore.similarity_search(query, k=3)

        llm = ChatOpenAI(model="gpt-4o-mini")

        chain = load_qa_chain(llm, chain_type="stuff")

        response = chain.run(
            input_documents=docs,
            question=query
        )

        st.write("### Answer")
        st.write(response)


# streamlit run app.py