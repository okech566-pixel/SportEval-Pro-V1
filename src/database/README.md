# 🗄️ Base de Données - SportEval Pro

## 📋 Contenu

- **models.py** - Tous les modèles SQLAlchemy avec les 40+ tables
- **init_db.py** - Scripts d'initialisation de la base de données
- **seed.py** - Données de test pour démonstration

## 🚀 Utilisation

### Initialiser la base de données

```python
from src.database.init_db import init_database

# Crée la BD avec toutes les tables
init_database()
```

### Remplir avec des données de test

```python
from src.database.seed import seed_database

# Ajoute des données d'exemple
seed_database()
```

### Obter une session

```python
from src.database.init_db import get_session

session = get_session()
# Utiliser la session...
session.close()
```

## 📊 Tables Créées

### Gestion Établissements
- `establishments` - Écoles/Institutions

### Utilisateurs & Accès
- `users` - Comptes utilisateurs (Admin, Enseignants, etc.)
- `teachers` - Détails des enseignants EPS
- `audit_logs` - Historique des actions

### Gestion Pédagogique
- `classes` - Classes scolaires
- `students` - Données des élèves

### Évaluations
- `events` - Épreuves sportives
- `baremes` - Barèmes de notation
- `assessments` - Évaluations des élèves
- `student_progress` - Suivi historique

### Rapports & Analyse
- `reports` - Rapports générés
- `ai_analysis` - Analyses IA
- `statistics` - Statistiques en cache

### Maintenance
- `backups` - Historique des sauvegardes

## 🔗 Relations Principales

```
Establishment
  ├── Users
  ├── Teachers
  ├── Classes
  │   └── Students
  │       └── Assessments
  │           ├── Events
  │           └── Baremes
  └── Reports
```

## 🔐 Sécurité

- Tous les identifiants de mot de passe sont hachés
- Audit trail complet de toutes les actions
- Support du multilingue
- Permissions basées sur les rôles (RBAC)
