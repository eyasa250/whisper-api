from fastapi import FastAPI, UploadFile, File, BackgroundTasks
from fastapi.responses import FileResponse
import whisper
import os
import uuid
import shutil

app = FastAPI()
model = whisper.load_model("base")

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def format_timestamp(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int((seconds % 1) * 1000)
    return f"{hours:02}:{minutes:02}:{secs:02},{millis:03}"

@app.post("/transcribe/")
async def transcribe(
    background_tasks: BackgroundTasks,  # 💡 Recevoir BackgroundTasks ici
    file: UploadFile = File(...)
):
    file_id = str(uuid.uuid4())
    file_path = os.path.join(UPLOAD_DIR, f"{file_id}_{file.filename}")

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = model.transcribe(file_path)

    srt_filename = f"{file_id}.srt"
    srt_path = os.path.join(UPLOAD_DIR, srt_filename)
    with open(srt_path, "w", encoding="utf-8") as srt_file:
        for i, segment in enumerate(result["segments"]):
            start = segment["start"]
            end = segment["end"]
            text = segment["text"].strip()

            srt_file.write(f"{i+1}\n")
            srt_file.write(f"{format_timestamp(start)} --> {format_timestamp(end)}\n")
            srt_file.write(f"{text}\n\n")

    os.remove(file_path)  # Supprimer le fichier audio immédiatement

    # ✅ Planifier la suppression du fichier .srt après réponse
    background_tasks.add_task(os.remove, srt_path)

    return FileResponse(srt_path, filename=srt_filename, media_type="application/x-subrip")
