# FastAPI + SvelteKit Boilerplate

Simple boilerplate for machine learning web app with **FastAPI** as the backend and **SvelteKit** as the frontend.

---

## 🚨 Prerequisites

Before you begin, make sure you have the following installed:

- **Python 3.7+**: For the FastAPI backend
- **Node.js** (v14.x or later): For the SvelteKit frontend
- **npm** (comes with Node.js): To manage the frontend dependencies

To check if you have these installed, run the following commands:

```bash
# Check Python version
python --version

# Check Node.js version
node --version

# Check npm version
npm --version
```

## 🚀 Getting Started

Follow these steps to set up and run the project locally.

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/malwanaf/fastapi-sveltekit.git
cd fastapi-sveltekit
```

### 2. Frontend Setup

Go to the frontend directory, and install all the dependencies.

```bash
npm install
```

### 3. Backend Setup

Go to the backend directory 

```bash
cd backend
```

Make a python virtual environtment

```bash
python -m venv venv
```

Activate the virtual environment

```bash
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

Install all the requirements (backend/requirements.txt)

```bash
pip install -r requirements.txt
```

### 4. Run the Frontend and the backend

Run the sveltekit for development

```bash
npm run dev
```

Run the FastAPI server

```bash
uvicorn main:app --reload
```

#### Everything is Set



