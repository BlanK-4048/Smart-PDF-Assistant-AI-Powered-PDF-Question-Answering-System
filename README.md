# 📄 Smart PDF Assistant – AI-Powered PDF Question Answering System

# 📚 AI-Powered PDF Assistant using Retrieval-Augmented Generation (RAG)

An intelligent PDF Question Answering System that allows users to interact with PDF documents through natural language conversations. The application uses **Retrieval-Augmented Generation (RAG)** to retrieve relevant information from documents and generate context-aware responses using Google's Gemini 2.5 Pro.

Built using LangChain, HuggingFace embeddings, ChromaDB, and Gradio, the system provides an interactive way to search, understand, and extract information from PDF documents.

## 🚀 Features

- **PDF Document Processing:** Automatically loads and processes multiple PDF documents from a specified directory.
- **Natural Language Question Answering:** Ask questions about document contents using conversational language.
- **Retrieval-Augmented Generation (RAG):** Retrieves relevant document chunks to provide context-aware answers.
- **Semantic Search:** Uses HuggingFace sentence embeddings to identify relevant information based on meaning.
- **Vector Database:** Stores document embeddings persistently using ChromaDB.
- **LLM Integration:** Uses Google Gemini 2.5 Pro to generate responses based on retrieved document context.
- **Conversational Interface:** Provides an interactive chatbot interface using Gradio.
- **Streaming Responses:** Displays AI-generated answers progressively as they are generated.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| LangChain | RAG pipeline and document processing |
| Gradio | Interactive chatbot interface |
| Google Gemini 2.5 Pro | Natural language response generation |
| HuggingFace Embeddings | Semantic text representation |
| ChromaDB | Persistent vector database |
| PyPDF | PDF document loading and extraction |
| Sentence Transformers | Embedding generation |

## 🏗️ System Architecture

The application follows a Retrieval-Augmented Generation (RAG) architecture consisting of two major stages.

### 1. Document Ingestion Pipeline

1. **PDF Loading:** Loads PDF documents from the `data` directory using PyPDFDirectoryLoader.
2. **Text Extraction:** Extracts textual content from the uploaded PDF documents.
3. **Text Chunking:** Splits extracted text into smaller chunks using RecursiveCharacterTextSplitter.
4. **Embedding Generation:** Converts document chunks into numerical vectors using HuggingFace's `all-MiniLM-L6-v2` model.
5. **Vector Storage:** Stores document embeddings in ChromaDB for persistent retrieval.

### 2. Question Answering Pipeline

1. **User Query:** The user submits a question through the Gradio chatbot.
2. **Similarity Search:** The retriever searches ChromaDB for the five most relevant document chunks.
3. **Context Retrieval:** Retrieved document contents are combined into contextual knowledge.
4. **Prompt Construction:** The user query, conversation history, and retrieved context are passed into the RAG prompt.
5. **Response Generation:** Google Gemini 2.5 Pro generates an answer using the retrieved information.
6. **Streaming Output:** The generated response is progressively displayed in the Gradio interface.

## 📂 Project Structure

```text
RAG-Final2/
│
├── data/
│   ├── document1.pdf
│   ├── document2.pdf
│   └── ...
│
├── chroma_db/
│   └── Persistent vector database
│
├── chatbot.py
│   └── Gradio chatbot and RAG pipeline
│
├── ingest_database.py
│   └── PDF processing and database creation
│
├── .env
│   └── Google Gemini API configuration
│
├── requirements.txt
│   └── Project dependencies
│
└── README.md
```

## ⚙️ Installation and Setup

### Prerequisites

- Python 3.10 or later
- Google Gemini API Key
- Internet connection for downloading the embedding model and accessing Gemini

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/RAG-Final2.git
cd RAG-Final2
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows:**
```bash
venv\Scripts\activate
```

**Linux/macOS:**
```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the Gemini API Key

Obtain a Google Gemini API key from [Google AI Studio](https://aistudio.google.com/).

Create a `.env` file in the project root directory:

```env
GOOGLE_API_KEY=your_google_gemini_api_key
```

### 5. Add PDF Documents

Place the PDF documents you want to analyze inside the `data/` directory.

### 6. Create the Vector Database

Run the document ingestion script:

```bash
python ingest_database.py
```

This extracts the PDF content, generates embeddings, and stores them in ChromaDB.

### 7. Launch the Chatbot

Run the application:

```bash
python chatbot.py
```

Gradio will launch the chatbot interface and provide a local URL to access the application.

## 🧠 Key Concepts Implemented

- **Retrieval-Augmented Generation (RAG):** Combines document retrieval with large language model generation.
- **Semantic Embeddings:** Converts text into numerical vector representations.
- **Vector Similarity Search:** Retrieves relevant document chunks based on semantic similarity.
- **Text Chunking:** Breaks large documents into smaller, searchable segments.
- **Prompt Engineering:** Combines user queries, conversation history, and retrieved context to guide LLM responses.
- **Persistent Storage:** Maintains document embeddings using ChromaDB.

## 🔮 Future Enhancements

- Support for additional document formats such as DOCX and TXT.
- Multiple PDF uploads through the chatbot interface.
- Source citations with document names and page numbers.
- Improved retrieval accuracy through reranking techniques.
- Enhanced conversational memory.
- Support for locally hosted open-source LLMs.

## 👨‍💻 Author

**Samik Sarkar**

B.Tech – Computer Science and Engineering

---

⭐ If you find this project interesting, consider giving the repository a star!
