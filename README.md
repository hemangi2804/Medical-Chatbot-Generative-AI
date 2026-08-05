# 🩺 End-to-End Medical Chatbot using Generative AI

An AI-powered Medical Chatbot built using **Retrieval-Augmented Generation (RAG)**. The chatbot retrieves relevant information from medical PDF documents using **Pinecone Vector Database** and generates intelligent, context-aware responses using **OpenAI's Large Language Models (LLMs)** through **LangChain**.

---

## 🚀 Features

- 📄 Extracts information from medical PDF documents
- ✂️ Splits documents into semantic text chunks
- 🧠 Generates embeddings using Hugging Face models
- 📌 Stores embeddings in Pinecone Vector Database
- 🔍 Performs semantic similarity search
- 🤖 Generates intelligent responses using OpenAI LLM
- 💬 Interactive chatbot built with Flask
- ⚡ Retrieval-Augmented Generation (RAG) architecture
- ☁️ AWS Cloud deployment ready

---

## 🛠️ Tech Stack

- Python 3.10
- LangChain
- OpenAI API
- Hugging Face Embeddings
- Pinecone Vector Database
- Flask
- PyPDF
- Sentence Transformers
- Python Dotenv
- AWS (EC2, ECR, Docker)
- Git & GitHub

---

## 📂 Project Structure

```text
Medical-Chatbot-Generative-AI/
│
├── Data/                      # Medical PDF files
├── research/                  # Jupyter notebooks
├── src/
│   ├── helper.py
│   ├── prompt.py
│   └── __init__.py
│
├── app.py
├── setup.py
├── requirements.txt
├── template.py
├── store_index.py
├── .env
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/hemangi2804/Medical-Chatbot-Generative-AI.git
```

### 2. Navigate to the Project

```bash
cd Medical-Chatbot-Generative-AI
```

### 3. Create a Virtual Environment

Using Conda:

```bash
conda create -n medibot python=3.10 -y
conda activate medibot
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root directory.

```env
OPENAI_API_KEY=your_openai_api_key

PINECONE_API_KEY=your_pinecone_api_key
PINECONE_INDEX_NAME=medical-chatbot

AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_DEFAULT_REGION=your_region
```

---

## 📚 Add Medical PDFs

Place all medical PDF documents inside the `Data/` folder.

```text
Data/
│
├── anatomy-and-physiology.pdf
├── diabetes.pdf
├── hypertension.pdf
├── first-aid.pdf
└── medicines.pdf
```

---

## ▶️ Run the Application

Create the vector database:

```bash
python store_index.py
```

Start the chatbot:

```bash
python app.py
```

Open your browser:

```
http://127.0.0.1:5000
```

---

## 🔄 RAG Workflow

```text
Medical PDF Documents
        │
        ▼
Document Loader
        │
        ▼
Recursive Character Text Splitter
        │
        ▼
Hugging Face Embeddings
        │
        ▼
Pinecone Vector Database
        │
        ▼
Retriever
        │
        ▼
OpenAI LLM
        │
        ▼
Medical Chatbot Response
```

---

## ☁️ AWS Deployment

The application can be deployed on AWS using:

- Amazon EC2
- Amazon ECR
- Docker
- GitHub Actions (CI/CD)
- IAM Roles
- Security Groups

Deployment Pipeline:

```text
GitHub
   │
   ▼
GitHub Actions
   │
   ▼
Docker Build
   │
   ▼
Amazon ECR
   │
   ▼
Amazon EC2
   │
   ▼
Medical Chatbot Application
```

---

## 🐳 Docker

Build the Docker image:

```bash
docker build -t medical-chatbot .
```

Run the Docker container:

```bash
docker run -p 5000:5000 medical-chatbot
```

---

## 📈 Future Enhancements

- 🎙️ Voice-enabled chatbot
- 🧾 Medical report summarization
- 📷 OCR support for prescriptions
- 🌍 Multi-language support
- 🔐 User authentication
- 📊 Chat history
- ☸️ Kubernetes deployment
- 📱 Mobile-friendly UI

---

## 📌 Disclaimer

This chatbot is developed for **educational and research purposes only**. It should not be used as a substitute for professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare professional for medical concerns.

---

## 👩‍💻 Author

**Hemangi Mistari**

- GitHub: https://github.com/hemangi2804
- LinkedIn: https://www.linkedin.com/in/your-linkedin-profile/

---

## ⭐ Support

If you found this project helpful, please consider giving it a ⭐ on GitHub.
