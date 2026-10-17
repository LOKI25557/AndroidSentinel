
from fastapi import FastAPI

app = FastAPI(
    title="AndroidSentinel",
    description=(
        "AI-Assisted Android Application Security "
        "and Forensic Analysis Platform"
    ),
    version="0.1.0",
)


@app.get("/api/health", tags=["Health"])
def health_check() -> dict[str, str]:
    return {
        "status": "ok",
        "service": "AndroidSentinel",
    }

@app.get("/")
def root() -> dict[str, str]:
    return {
        "message": "Welcome to AndroidSentinel",
        "docs": "/docs",
        "health": "/api/health",
    }