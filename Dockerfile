
# Image de base avec une version explicite
FROM python:3.12-slim

# Répertoire de travail
WORKDIR /app

# Copier les dépendances en premier pour exploiter le cache
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code de l'application
COPY app.py .

# Port utilisé par Flask
EXPOSE 5000

# Commande de démarrage
CMD ["python", "app.py"]
