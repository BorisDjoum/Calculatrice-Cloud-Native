# Calculatrice Distribuée

Ce projet implémente une calculatrice distribuée utilisant une architecture microservices avec RabbitMQ pour la gestion des files d'attente et Redis pour le stockage des résultats.

## Architecture du système

L'application se compose de plusieurs composants interconnectés :

1. **Frontend** :
   - Interface utilisateur HTML avec JavaScript pour l'interaction.
   - Envoie les calculs à l'API backend et affiche les résultats.

2. **Backend** :
   - Reçoit les requêtes de calcul du frontend.
   - Envoie les calculs à RabbitMQ pour traitement asynchrone.
   - Fournit des endpoints pour envoyer des calculs et récupérer les résultats.

3. **RabbitMQ** :
   - Gère la file d'attente des calculs à effectuer.

4. **Consumer** :
   - Récupère les calculs de la file RabbitMQ.
   - Effectue les opérations mathématiques.
   - Enregistre les résultats dans Redis.

5. **Redis** :
   - Stocke les résultats des calculs pour une récupération rapide.

## Fonctionnalités du Frontend

Le frontend JavaScript offre les fonctionnalités suivantes :

- Validation des entrées utilisateur (nombres valides, division par zéro).
- Affichage d'un loader pendant le traitement du calcul.
- Gestion des erreurs (champs vides, erreurs de connexion).
- Récupération asynchrone des résultats avec un système de polling.

### Processus de calcul

1. L'utilisateur entre deux nombres et sélectionne un opérateur.
2. Le frontend envoie une requête POST à `/api/v1/calcul` avec les données du calcul.
3. L'API retourne un ID unique pour le calcul.
4. Le frontend interroge périodiquement `/api/v1/calcul/{id}` pour obtenir le résultat.
5. Le résultat est affiché une fois disponible ou une erreur est signalée après un certain délai.

## Utilisation

### Démarrage des services

Pour lancer l'application localement :

1. Construire les images Docker :
   ```
   docker-compose build
   ```

2. Démarrer tous les services :
   ```
   docker-compose up
   ```

3. Accéder à l'interface de la calculatrice :
   Ouvrez un navigateur et allez sur `http://localhost:8080/`

### Interaction avec l'API

1. Envoyer un calcul :
   ```
   POST /api/v1/calcul
   Body: { "tuple": ["5", "+", "3"] }
   ```

2. Récupérer un résultat :
   ```
   GET /api/v1/calcul/{id}
   ```

## Gestion des erreurs

Le système gère plusieurs types d'erreurs :
- Entrées utilisateur invalides
- Division par zéro
- Erreurs de connexion à l'API
- Timeout pour les calculs longs

## Conteneurisation et Kubernetes

Ce projet utilise la conteneurisation et Kubernetes pour assurer une gestion efficace et scalable des différents composants de l'application.

### Conteneurisation

Chaque composant de l'application (API Backend, Consumer, Frontend) est conteneurisé à l'aide de Docker. Cela permet :

- Une isolation des dépendances pour chaque service
- Une portabilité accrue entre les environnements de développement et de production
- Une gestion simplifiée des versions et des déploiements

Le projet utilise un fichier `docker-compose.yml` pour définir et orchestrer les services localement, facilitant ainsi le développement et les tests.

