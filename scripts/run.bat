echo "Download models"
python scripts/download_models.py
echo "Starting app"
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload