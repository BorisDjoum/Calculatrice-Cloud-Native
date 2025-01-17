## Structure Kubernetes

Le projet utilise une organisation structurée des fichiers de configuration Kubernetes, facilitant la gestion et le déploiement des différents composants de l'application. Voici la structure détaillée :

### Organisation des fichiers

Chaque composant majeur de l'application possède son propre dossier contenant les fichiers de configuration Kubernetes nécessaires :

- **Backend** :
  - `deployment.yaml` : Définit le déploiement de l'API backend.
  - `service.yaml` : Configure le service Kubernetes pour exposer l'API.

- **Frontend** :
  - `deployment.yaml` : Gère le déploiement de l'interface utilisateur.
  - `service.yaml` : Définit le service pour accéder au frontend.

- **Consumer** :
  - `deployment.yaml` : Configure le déploiement du consumer.

- Autres composants (comme Redis, RabbitMQ) suivent une structure similaire.

- `ingress.yaml` : Définit les règles d'accès externe pour l'API et le frontend.


### Avantages de cette organisation

1. **Modularité** : Chaque composant est isolé, facilitant les mises à jour et la maintenance.
2. **Clarté** : La structure est intuitive, permettant une navigation rapide entre les différents services.
3. **Flexibilité** : Permet d'ajuster facilement les configurations spécifiques à chaque composant.

### Particularité du Consumer

Le consumer ne possède qu'un fichier `deployment.yaml`, car il n'a pas besoin d'être exposé directement comme un service. Il interagit uniquement avec RabbitMQ et Redis en interne.

### Déploiement

Pour déployer l'application sur Kubernetes :

1. Appliquez les fichiers de déploiement :
   ```
   kubectl apply -f backend/deployment.yaml
   kubectl apply -f backend/service.yaml
   kubectl apply -f frontend/deployment.yaml
   kubectl apply -f frontend/service.yaml
   kubectl apply -f consumer/deployment.yaml
   ```

2. Vérifiez le statut des déploiements :
   ```
   kubectl get deployments
   kubectl get services
   ```

