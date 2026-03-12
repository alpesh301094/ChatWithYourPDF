from langchain_community.vectorstores import Chroma

def get_chroma_vectorstore(chunks, embeddings):

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="./chroma_db"
    )

    return vectorstore