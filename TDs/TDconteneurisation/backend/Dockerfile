FROM debian:latest

# Utiliser une image Debian de base
FROM debian:latest

# Installer les paquets nécessaires
RUN apt update && apt install -y bash htop vim net-tools

# Ajouter une variable d'environnement contenant votre prénom
ENV OWNER=Boris

RUN useradd nonroot
USER nonroot

# Utiliser `sleep` pour garder le conteneur actif
CMD ["sleep", "3600"]
