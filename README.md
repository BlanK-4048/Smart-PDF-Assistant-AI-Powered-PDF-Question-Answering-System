# 📄 Smart PDF Assistant – AI-Powered PDF Question Answering System

An AI-powered PDF assistant that allows users to upload PDF documents and interact with their contents through natural language conversations. Built using **Retrieval-Augmented Generation (RAG)**, the application retrieves relevant information from uploaded documents and generates context-aware responses using Large Language Models (LLMs).

## 🚀 Features

- **PDF Upload:** Upload and process PDF documents for analysis.
- **Natural Language Queries:** Ask questions about the uploaded documents in plain English.
- **Retrieval-Augmented Generation (RAG):** Retrieves relevant document chunks to generate accurate, context-aware answers.
- **Semantic Search:** Uses HuggingFace sentence embeddings to understand the meaning of queries.
- **Vector Database:** Stores and retrieves document embeddings efficiently using FAISS.
- **Conversational Interface:** Interact with PDF documents through an intuitive chatbot interface.
- **Context-Aware Responses:** Generates answers based on the information available in the uploaded documents.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Interactive web interface |
| LangChain | RAG pipeline and LLM integration |
| HuggingFace Embeddings | Text embedding generation |
| FAISS | Vector storage and similarity search |
| Google Gemini | LLM-based response generation |
| PyPDF | PDF text extraction |

## 🏗️ System Architecture

The application follows a Retrieval-Augmented Generation (RAG) workflow:

1. **PDF Upload:** The user uploads a PDF document.
2. **Text Extraction:** Extracts textual content from the uploaded PDF.
3. **Text Chunking:** Splits extracted text into smaller, manageable chunks.
4. **Embedding Generation:** Converts text chunks into vector embeddings using HuggingFace.
5. **Vector Storage:** Stores embeddings in a FAISS vector database.
6. **Similarity Search:** Retrieves the most relevant document chunks based on the user's question.
7. **Answer Generation:** Passes the retrieved context and user query to Google Gemini.
8. **Response Display:** Displays the generated answer through the Streamlit interface.

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/smart-pdf-assistant.git
cd smart-pdf-assistant
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

### 4. Configure API Key

Obtain a Google Gemini API key from [Google AI Studio](https://aistudio.google.com/).

Configure your API key using Streamlit secrets or an environment variable.

For Streamlit secrets, create:

`.streamlit/secrets.toml`

```toml
GOOGLE_API_KEY = "your_api_key_here"
```

Do not upload API keys or secrets to GitHub.

### 5. Run the Application

```bash
streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

## 📂 Project Structure

```text
Smart-PDF-Assistant/
│
├── app.py                  # Main Streamlit application
├── requirements.txt        # Project dependencies
├── .streamlit/
│   └── secrets.toml        # API configuration (not committed)
├── .gitignore              # Files excluded from Git
└── README.md               # Project documentation
```

*Note: Adjust the structure according to your actual repository.*

## 🔑 Key Concepts Used

- **Retrieval-Augmented Generation (RAG):** Combines information retrieval with LLM-based text generation.
- **Text Embeddings:** Represents textual information as numerical vectors.
- **Vector Similarity Search:** Finds relevant document sections based on semantic similarity.
- **Large Language Models:** Uses Google Gemini to generate natural language responses.
- **Natural Language Processing:** Enables users to interact with document content conversationally.

## 🔮 Future Enhancements

- Support for multiple PDF uploads.
- Chat history and conversational memory.
- Source citations with page numbers.
- Support for additional document formats such as DOCX and TXT.
- Improved retrieval accuracy through advanced chunking and reranking.
- Option to integrate locally hosted LLMs.

## 👨‍💻 Author

**Samik Sarkar**

B.Tech – Computer Science and Engineering

---

⭐ If you find this project useful, consider giving it a star!
