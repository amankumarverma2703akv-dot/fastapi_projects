# 🚀 Production-Ready Loan Default Prediction API (FastAPI + Docker + Redis)

A high-performance, asynchronous REST API for machine learning model inference built with **FastAPI**, **Scikit-Learn**, **JWT Authentication**, **Redis**, and **Docker Compose**. Designed with containerized environments and automated unit testing (`pytest`) for seamless MLOps deployments.

---

## 🛠️ Tech Stack & Tools

* **Framework:** FastAPI (Python 3.11)
* **ML Pipeline:** Scikit-Learn (RandomForestClassifier), Joblib
* **Security & Auth:** OAuth2 + JWT (JSON Web Tokens via `python-jose`)
* **Database / Cache:** Redis (Token blacklisting / Rate limiting)
* **Testing:** Pytest + HTTPX (`TestClient`)
* **Containerization:** Docker & Docker Compose
* **Documentation:** OpenAPI / Swagger UI

---

## 📂 Project Architecture

```text
fastapi_projects/
├── app/
│   ├── api/             # API routes (Auth & ML Inference)
│   ├── core/            # Security & Config settings
│   ├── middleware/      # Custom middleware (CORS, Logging)
│   ├── services/        # Model loading & inference logic
│   └── main.py          # FastAPI application entry point
├── models/              # Trained ML model artifacts (.joblib)
├── tests/               # Automated unit & integration tests
├── docker-compose.yml   # Multi-container orchestration (App + Redis)
├── Dockerfile           # Optimized Python container image
└── requirements.txt     # Locked project dependencies
