# 🤖 My AI Assistant

An AI-powered chat application built with **Streamlit** and **Groq** that lets users ask questions, maintain a chat history during the session, and upload PDF documents to ask document-related questions.

## ✨ Features

- **AI Chat:** Ask questions and receive AI-generated responses.
- **PDF Q&A:** Upload a PDF and ask questions about its extracted text.
- **Session Chat History:** View recent conversation messages during the current session.
- **PDF Text Extraction:** Extract text from PDF pages using `pypdf`.
- **Simple Controls:** Clear the chat or remove the uploaded PDF from the sidebar.
- **Secure API-Key Configuration:** Read the Groq API key from Streamlit secrets or an environment variable.

## 🧰 Tech Stack

- **Python**
- **Streamlit** — web interface
- **Groq Python SDK** — AI chat completions
- **pypdf** — PDF text extraction

## 🧩 Skills Demonstrated

- **Python Programming:** Application logic and integration of the AI service.
- **Streamlit:** Interactive chat interface, sidebar controls, and session-state handling.
- **Generative AI (GenAI):** AI-generated responses using a language model accessed through Groq.
- **Groq API Integration:** Sends conversation messages to the configured chat-completions model.
- **Prompt Engineering:** Uses system instructions and uploaded-document context to guide responses.
- **PDF Processing (`pypdf`):** Extracts text from uploaded PDF files.
- **Session State Management:** Keeps chat messages and extracted PDF text available during the active Streamlit session.
- **API-Key and Secrets Management:** Reads `GROQ_API_KEY` from Streamlit secrets or an environment variable.
- **Git & GitHub:** Relevant for version control and publishing the project, if used.

## 📁 Project Structure

```text
AI_CHATBOT/
├── app.py
├── .gitignore
├── requirements.txt
└── README.md
```

> Keep your actual API key out of source code and version control. Do not commit `.env` files or `.streamlit/secrets.toml` containing secrets.

## ⚙️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
cd YOUR-REPOSITORY
```

Replace the URL and repository name with your own GitHub repository details.

### 2. Create and activate a virtual environment

**Windows (PowerShell / Command Prompt):**

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

Create a `requirements.txt` file with:

```text
streamlit
groq
pypdf
```

Then install the packages:

```bash
python -m pip install -r requirements.txt
```

### 4. Configure your Groq API key

Create a Groq API key in your Groq account, then set it locally.

**Option A — Environment variable (PowerShell):**

```powershell
$env:GROQ_API_KEY="your_groq_api_key_here"
```

**Option B — Streamlit secrets:**

Create `.streamlit/secrets.toml` in your local project and add:

```toml
GROQ_API_KEY = "your_groq_api_key_here"
```

Never commit your real API key. The included `.gitignore` should exclude `.env` and `.streamlit/secrets.toml`.

### 5. Run the app

```bash
streamlit run app.py
```

Streamlit will provide a local URL to open the application in your browser.

## 💬 How to Use

1. Start the app.
2. Enter a question in the chat box.
3. To ask about a document, use **Upload PDF** in the sidebar.
4. Ask questions related to the uploaded PDF.
5. Select **Remove PDF** to clear the document context.
6. Select **Clear Chat** to reset the visible conversation history.

## 🧠 How It Works

1. The app reads the Groq API key from Streamlit secrets or the `GROQ_API_KEY` environment variable.
2. When a PDF is uploaded, `pypdf` extracts text from its pages.
3. The app prepares a system instruction and includes extracted PDF text (up to 30,000 characters) as context.
4. Recent conversation messages are sent to the configured Groq chat-completions model.
5. The generated response is displayed and added to the session's chat history.

## 🔐 Security & Limitations

- **Protect your API key:** Never hard-code it, commit it, or share screenshots that expose it.
- **PDF support:** Text extraction works best with text-based PDFs. Scanned PDFs may require OCR, which this version does not implement.
- **Document context:** The app currently includes up to 30,000 characters of extracted PDF text in its document context.
- **Session history:** Chat history is stored in Streamlit session state and is not a persistent database.
- **Model availability:** The app uses the model ID `openai/gpt-oss-20b` through Groq. Confirm that this model ID is available to your Groq account; update it in `app.py` if needed.
- **Response quality:** AI responses can be incomplete or incorrect. Verify important information independently.

## 🛠️ Troubleshooting

### `GROQ_API_KEY` not found

Set the environment variable or configure `.streamlit/secrets.toml`, then restart the app.

### Module not found

Activate your virtual environment and run:

```bash
python -m pip install -r requirements.txt
```

### PDF text is empty

The PDF may contain scanned images rather than selectable text. OCR support would be needed to extract text from those pages.

### Model/API error

Check your internet connection, API key, account access, rate limits, and the model ID configured in `app.py`.

## 🚀 Future Improvements

- Add streaming responses.
- Add support for multiple PDF files.
- Improve long-document retrieval with chunking and embeddings.
- Add OCR support for scanned PDFs.
- Add persistent conversation storage.
- Add automated tests and deployment instructions.

## 👨‍💻 Author

**Rohan Thosar**

Add your preferred profile links here:

- GitHub: `https://github.com/rohanthosar213-source`
- LinkedIn: `https://linkedin.com/in/rohan-thosar213`

## 📄 License

Choose a license before publishing this project. If you want others to reuse and modify the code, consider adding a `LICENSE` file with an appropriate open-source license.
