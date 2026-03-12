# 📄 AI PDF Question Answering (RAG) using LangChain

An AI-powered application that allows users to **upload a PDF and ask questions about its content**.
The system uses **Retrieval-Augmented Generation (RAG)** to retrieve relevant text chunks from the document and generate answers using an LLM.

Built with **LangChain, Streamlit, and Chroma Vector Database**.

---

## 🚀 Features

* Upload any PDF document
* Automatically extract and split document text
* Generate embeddings for semantic search
* Store embeddings in a vector database
* Ask questions about the document
* Retrieve the most relevant chunks using similarity search
* Generate AI-powered answers based on document context

---

## 🧠 Tech Stack

* Python 3.10
* LangChain
* OpenAI
* Streamlit
* Chroma Vector Database
* PyPDF

---

## 📂 Project Structure

```
ChatWithYourPDF/
│
├── app.py                # Streamlit application
├── vector_store.py       # Chroma vector database logic
├── requirements.txt      # Project dependencies
├── .env                  # OpenAI API key
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```
git clone https://github.com/YOUR_USERNAME/chat-with-your-pdf.git
cd chat-with-your-pdf
```

---

### 2️⃣ Create Conda Environment

Make sure **Anaconda or Miniconda** is installed.

Create a new environment:

```
conda create -n venv python=3.10
```

Activate the environment:

```
conda activate venv
```

---

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Add OpenAI API Key

Create a `.env` file in the root directory.

```
OPENAI_API_KEY=your_openai_api_key_here
```

---

## ▶ Run the Application

Start the Streamlit application:

```
streamlit run app.py
```

Then open your browser:

```
http://localhost:8501
```

---

## 🧠 How It Works

1. User uploads a PDF file
2. The document is loaded using `PyPDFLoader`
3. Text is split into smaller chunks
4. Each chunk is converted into embeddings
5. Embeddings are stored in the Chroma vector database
6. User asks a question
7. Similar chunks are retrieved using semantic search
8. The LLM generates an answer using the retrieved context

---

## 📦 Dependencies

```
streamlit==1.33.0
langchain==0.1.20
langchain-community==0.0.38
langchain-openai==0.1.7
chromadb==0.4.24
openai==1.14.3
pypdf==4.2.0
tiktoken==0.7.0
pydantic==1.10.13
httpx==0.27.0
python-dotenv==1.0.1
```

---

## 📸 Demo

Upload a PDF → Ask a question → Get AI-generated answers based on the document.

Example:

**Question**

```
What is the main topic of this document?
```

**Answer**

```
The document explains the fundamentals of machine learning and its applications.
```

## 👨‍💻 Author

Alpesh Patel
Senior Software Developer | Learning AI & Data Engineering

---

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.