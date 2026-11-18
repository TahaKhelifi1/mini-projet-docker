# Mini Projet Docker – Application Flask

## 1. Présentation

Ce projet consiste à conteneuriser une application web développée avec Flask en utilisant Docker.

L'objectif est de créer une image Docker optimisée, configurable et facilement déployable sur différents environnements.

## 2. Technologies utilisées

- Python 3.12
- Flask 3.1.2
- Docker
- Docker Hub

## 3. Image Docker publiée

L'image est disponible publiquement sur Docker Hub :

**Repository :** `tahakhelifi/mini-projet-docker`

Tags disponibles :
- `1.0.0` : première version
- `1.0.1` : deuxième version
- `1.0` : alias de la version `1.0.1`

## 4. Prérequis

- Docker installé
- Une connexion Internet

Aucune installation locale de Python ou de Flask n'est nécessaire pour exécuter l'application depuis l'image publiée.

## 5. Télécharger l'image

```bash
docker pull tahakhelifi/mini-projet-docker:1.0
```

## 6. Exécuter l'application

```bash
docker run -d \
  --name mini-projet-container \
  -p 8080:5000 \
  --memory 256m \
  --cpus 0.5 \
  tahakhelifi/mini-projet-docker:1.0
```

L'application sera accessible à l'adresse :

http://localhost:8080

## 7. Configurer le message avec une variable d'environnement

La variable `APP_MESSAGE` permet de personnaliser le message affiché par l'application sans modifier l'image Docker.

Exemple :

```bash
docker run -d \
  --name mini-projet-personnalise \
  -p 8081:5000 \
  -e APP_MESSAGE="Bonjour depuis Docker !" \
  --memory 256m \
  --cpus 0.5 \
  tahakhelifi/mini-projet-docker:1.0
```

L'application sera accessible sur :

http://localhost:8081

Si `APP_MESSAGE` n'est pas définie, l'application utilise le message par défaut.

## 8. Gestion du conteneur

Afficher les conteneurs actifs :

```bash
docker ps
```

Afficher les logs :

```bash
docker logs mini-projet-container
```

Arrêter le conteneur :

```bash
docker stop mini-projet-container
```

Supprimer le conteneur :

```bash
docker rm mini-projet-container
```

## 9. Construction locale de l'image

Pour construire l'image depuis le code source :

```bash
docker build -t mini-projet-docker:1.0.0 .
```

## 10. Optimisations et bonnes pratiques

- Utilisation d'une image de base avec une version explicite : `python:3.12-slim`.
- Utilisation de `WORKDIR` pour définir le répertoire de travail.
- Installation des dépendances avant la copie du code source afin d'optimiser le cache Docker.
- Utilisation de `.dockerignore` pour exclure les fichiers inutiles et sensibles.
- Utilisation de `0.0.0.0` pour rendre l'application accessible depuis le conteneur.
- Configuration du port avec `EXPOSE 5000`.
- Utilisation d'une variable d'environnement pour personnaliser le comportement de l'application.
- Limitation des ressources du conteneur à 256 MB de mémoire et 0.5 CPU.
- Publication de versions identifiées sur Docker Hub.

## 11. Liens du projet

- GitHub : https://github.com/TahaKhelifi1/mini-projet-docker
- Docker Hub : https://hub.docker.com/r/tahakhelifi/mini-projet-docker
