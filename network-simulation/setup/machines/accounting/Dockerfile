FROM python:3.11-slim

# 2. On définit le dossier de travail à l'intérieur du conteneur
WORKDIR /app

RUN apt-get update && apt-get install -y iproute2 && rm -rf /var/lib/apt/lists/*

# 3. On copie le script Python de votre PC vers le conteneur
COPY app.py /app/app.py

# 4. On indique que le conteneur va utiliser le port 8000
EXPOSE 8000

# 5. La commande exécutée automatiquement au démarrage du conteneur
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
CMD ["python", "app.py"]
