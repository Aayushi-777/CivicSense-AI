## 🏙️ CivicSense AI  
A Smart City Complaint Analyzer & Auto-Prioritization System built using **FastAPI, Bootstrap 5, NLP (LLM), and OpenCV**, designed to classify civic complaints, assign priority, and display them on a smart dashboard.

---

## 🚀 Features

- ✅ Text + Image complaint submission
- ✅ AI-based complaint classification (Water, Garbage, Road, Electricity)
- ✅ Hybrid AI system (Rule-based + LLM)
- ✅ Automatic priority & severity scoring
- ✅ Smart dashboard with real-time data
- ✅ Delete specific complaints
- ✅ Bootstrap 5 responsive UI
- ✅ Computer Vision (OpenCV-based image analysis)
- ✅ REST API with FastAPI
- ✅ SQLite database integration

---

## 🧠 AI & Processing

- **NLP Model:** Groq LLM (LLaMA 3.1)
- **Computer Vision:** OpenCV (edge detection + brightness analysis)
- **Approach:** Hybrid (Rule-based + AI)
- **Category Detection:** Keyword + AI classification
- **Priority Logic:** Rule override + AI scoring

---

## 🏗️ Project Structure

civicsense-ai/
│
├── api/
│   ├── complaints.py
│   └── dashboard.py
│
├── agents/
│   ├── nlp_agent.py
│   ├── priority_agent.py
│   ├── vision_agent.py
│   ├── routing_agent.py
│   └── orchestrator.py
│
├── core/
│   ├── database.py
│   └── models.py
│
├── static/
│   ├── index.html
│   ├── dashboard.html
│   ├── favicon.ico
│   └── site.webmanifest
│
├── uploads/
│
├── main.py
├── requirements.txt
└── README.md

---

## 📊 System Workflow

1. User submits complaint (text + image)
2. NLP Agent classifies category
3. Vision Agent analyzes image (optional)
4. Priority Agent assigns severity & priority
5. Routing Agent assigns department
6. Data stored in database
7. Dashboard displays prioritized complaints

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository
```bash
git clone https://github.com/your-username/civicsense-ai.git
cd civicsense-ai
```
### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```
### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
### 4️⃣ Setup Environment Variables
Create a .env file:
```bash
GROQ_API_KEY=your_api_key_here
```
### ▶️ Run the Application
```bash
uvicorn main:app --reload
```
Open in the browser:
http://127.0.0.1:8000

---

### 🧩 Technologies Used
- Python
- FastAPI
- Bootstrap 5
- Groq API (LLM)
- OpenCV
- SQLite
- HTML, CSS, JavaScript

### 🚀 Future Enhancements
- 📊 Graph-based analytics dashboard
- 🗺️ Map-based complaint tracking
- 📱 Mobile app integration
- 🌐 Multilingual support
- 🔔 Real-time notifications

### 👩‍💻 Team
- Simran Arya
- Anshika Singh
- Aayushi Vinod
- Payoshi Gupta
