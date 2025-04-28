# API de Transcription Audio en Texte avec Whisper et FastAPI

Ce projet est une API simple utilisant [FastAPI](https://fastapi.tiangolo.com/) et [OpenAI Whisper](https://github.com/openai/whisper) pour transcrire des fichiers audio en texte au format `.srt` (fichier de sous-titres).

## Fonctionnalités

- Upload d'un fichier audio (`.mp3`, `.wav`, etc.)
- Transcription de l'audio en texte avec timestamps
- Téléchargement immédiat du fichier `.srt` généré
- Suppression automatique des fichiers après l'envoi

---

## Prérequis

- **Python 3.8 ou supérieur**
- **`ffmpeg` installé** (obligatoire pour Whisper)
- **Connexion Internet** pour télécharger les modèles Whisper
- **creation dossier uploads
## Installation

### 1. Cloner le projet

```bash
git clone https://github.com/eyasa250/whisper-api.git
cd whisper-api
### 2. Créer un environnement virtuel et l'activer

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

### 3. Installer les dépendances

```bash
pip install -r requirements.txt

### 4. Installer ffmpeg
```bash
brew install ffmpeg


Lancement de l'API
Lancez le serveur FastAPI avec uvicorn :

uvicorn main:app --host 0.0.0.0 --port 8000

L'API sera disponible sur :

http://127.0.0.1:8000/transcribe/
