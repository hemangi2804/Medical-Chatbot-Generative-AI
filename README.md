# 🩺 Medical Chatbot - Generative AI

A Generative AI-powered medical chatbot that provides answers to health-related questions using information extracted from an anatomy and physiology knowledge base.

This project uses **Retrieval Augmented Generation (RAG)** to retrieve relevant medical information from documents and generate meaningful responses using AI.

---

# 🚀 Features

- 🤖 AI-powered medical question answering
- 📚 PDF-based medical knowledge retrieval
- 🔍 Semantic search using embeddings
- 🧠 Retrieval Augmented Generation (RAG)
- 💬 Interactive chatbot interface
- 🏥 Answers based on anatomy and physiology knowledge
- 📄 Document processing and vector database search

---

# 🏗️ How It Works

```
User Question
       |
       ↓
Chat Interface
       |
       ↓
Question Embedding
       |
       ↓
Vector Database Search
       |
       ↓
Medical PDF Knowledge Base
       |
       ↓
Relevant Context Retrieval
       |
       ↓
Generative AI Model
       |
       ↓
Final Answer
```

---

# 📂 Project Structure

```
Medical-Chatbot-Generative-AI
│
├── Data
│   └── anatomy-and-physiology.pdf
│
├── src
│   ├── helper.py
│   ├── prompt.py
│   └── other modules
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── vectorstore
```

---

# 📥 Required Medical Knowledge PDF

This chatbot uses the following medical knowledge file:

```
Data/anatomy-and-physiology.pdf
```

The PDF contains the medical information used by the chatbot to answer user questions.

Due to GitHub's file size limit, the PDF is hosted separately.

Download the required PDF file here:

[📄 Download Anatomy and Physiology PDF](https://drive.google.com/file/d/1QPsSteRjfYW2a1wOzMzHk2LnwxVTerxV/view?usp=sharing)

After downloading:

1. Create a folder named:

```
Data
```

2. Place the downloaded file inside:

```
Data/anatomy-and-physiology.pdf
```

Your project structure should be:

```
Medical-Chatbot-Generative-AI
│
└── Data
    └── anatomy-and-physiology.pdf
```

---

# 🛠️ Installation Guide

## Step 1: Clone Repository

```bash
git clone https://github.com/hemangi2804/Medical-Chatbot-Generative-AI.git
```

Move into the project folder:

```bash
cd Medical-Chatbot-Generative-AI
```

---

## Step 2: Create Virtual Environment

For Windows:

```bash
python -m venv medibot
```

Activate the environment:

```bash
medibot\Scripts\activate
```

---

## Step 3: Install Dependencies

Install required packages:

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a file named:

```
.env
```

Add your API key:

```
OPENAI_API_KEY=your_api_key_here
```

Add your actual API key in place of `your_api_key_here`.

---

# ▶️ Run the Application

Start the chatbot:

```bash
python app.py
```

The chatbot will run locally.

Open the application in your browser and start asking medical questions.

---

# 🧠 Technologies Used

- Python
- Generative AI
- Retrieval Augmented Generation (RAG)
- LangChain
- Embeddings
- Vector Database
- Large Language Models
- PDF Document Processing
- Natural Language Processing

---

# 🔄 RAG Pipeline

The chatbot follows this workflow:

1. Load medical PDF document
2. Split document into smaller chunks
3. Convert text chunks into embeddings
4. Store embeddings in vector database
5. Retrieve relevant medical information
6. Generate answers using an AI model

---

# ⚠️ Medical Disclaimer

This chatbot is created for educational purposes only.

It is not a replacement for professional medical advice, diagnosis, or treatment.

Always consult a qualified healthcare professional for medical decisions.

---

# 👩‍💻 Author

**Hemangi**

GitHub Profile:

https://github.com/hemangi2804

---

# ⭐ Support

If you find this project useful, consider giving it a star ⭐ on GitHub.
