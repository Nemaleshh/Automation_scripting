# Automation Scripting & OTP Verification

A Python automation workflow integrating **Selenium WebDriver** and the **Google Gmail API** to automate web login flows and dynamically fetch real-time email verification codes (OTPs).

---

## 🎥 Demo Video

https://github.com/user-attachments/assets/ or view the recording below:

<video src="Recording%202026-10-05%20144958.mp4" controls="controls" width="100%"></video>

> 🔗 **Direct Link:** [Watch / Download Recording 2026-10-05 144958.mp4](Recording%202026-10-05%20144958.mp4)

---

## 🚀 Features

- **Browser Automation (Selenium)**: Automates browser interactions, navigating pages, interacting with forms, and submitting actions.
- **Gmail API Integration**: Securely connects to the user's Gmail inbox via OAuth 2.0 (`google-api-python-client`) to read real-time incoming messages.
- **Real-Time OTP Extraction**: Automatically searches for incoming verification emails and extracts 6-digit OTP codes from the subject line.
- **Multi-Box Input Handler**: Dynamically fills multi-character/digit verification input fields (such as 6-box segmented OTP inputs).

---

## 📁 Project Structure

```text
├── Recording 2026-10-05 144958.mp4  # Demo video recording
├── test.ipynb                       # Jupyter Notebook with full step-by-step automation & Gmail API code
├── test.py                          # Selenium automation script
├── .gitignore                       # Protects credentials and virtual environments
└── README.md                        # Project documentation
```

---

## 🛠️ Prerequisites & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Nemaleshh/Automation_scripting.git
cd Automation_scripting
```

### 2. Set Up Virtual Environment
```bash
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install selenium google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

---

## 🔐 Google API Setup

1. Enable the **Gmail API** in Google Cloud Console.
2. Download your OAuth 2.0 Client credentials and save them as `credentials.json` in the root folder.
3. On the first run, a browser window will open to authenticate and generate `token.json`.
> **Note:** `credentials.json` and `token.json` are excluded via `.gitignore` to prevent sensitive credentials from being committed.

---

## 💻 Usage

### Run via Jupyter Notebook
Launch Jupyter:
```bash
jupyter notebook test.ipynb
```
Step through the cells to authenticate with Gmail, trigger the web login, fetch the verification code, and complete the authentication.

### Run Python Script Directly
```bash
python test.py
```
