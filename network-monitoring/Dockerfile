# 1. On choisit une image de base où Python est déjà installé
FROM python:3.11-slim

# 2. On définit le dossier de travail à l'intérieur du conteneur
WORKDIR /app

# 3. On copie le script Python de votre PC vers le conteneur
COPY app.py /app/app.py



# 4. On indique que le conteneur va utiliser le port 8000
EXPOSE 8000

# 5. La commande exécutée automatiquement au démarrage du conteneur
CMD pip install pysnmp python-nmap  && python app.py 
#CMD python app.py
