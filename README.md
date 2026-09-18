# Gestion du prix Goncourt

Application console Python réalisée dans le cadre de l'évaluation « Python métier ».
Elle permet de consulter la sélection de livres, de gérer les auteurs et les
membres du jury, puis d'enregistrer et d'annoncer les votes selon le rôle de
l'utilisateur.

## Fonctionnalités

- consultation des livres et de leurs auteurs ;
- authentification d'un président, d'un membre ou d'un administrateur ;
- vote des membres du jury ;
- saisie et classement des votes par le président ;
- ajout, modification et suppression de membres et de livres par un administrateur ;
- démonstration avec des données statiques et avec une base MySQL/MariaDB.

Le détail des règles fonctionnelles et des critères d'acceptation se trouve
dans [SPECIFICATIONS.md](SPECIFICATIONS.md).

## Architecture

```text
evaluation_python_metier-main/
├── main.py                 # Point d'entrée et navigation entre les menus
├── Business/goncourt.py    # Couche métier et orchestration des cas d'usage
├── ihm/console.py          # Entrées et sorties de l'interface console
├── models/                 # Entités métier
├── daos/                   # Accès aux données et opérations CRUD
├── BDD/sql/                # Création et données de la base
├── BDD/Merise/             # Modèle de données Looping
└── UML/                    # Diagrammes de conception
```

Le programme suit une séparation en couches : l'interface console recueille
les choix, la classe `Goncourt` exécute les cas d'usage, et les DAO communiquent
avec la base de données. Les classes de `models/` représentent les objets métier.

## Prérequis

- Windows (le programme utilise actuellement la commande `pause`) ;
- Python 3.12 ou version ultérieure ;
- MySQL ou MariaDB ;
- paquet Python `PyMySQL`.

```bash
python -m pip install pymysql
```

## Installation de la base

1. Démarrer MySQL ou MariaDB.
2. Exécuter le script `BDD/sql/evaluation_python_metier.sql`.
3. Adapter dans `daos/dao.py` les paramètres `host`, `user` et `database` à
   votre environnement local.

La connexion est ouverte lors de l'import de `daos.dao`. La base doit donc être
disponible avant le lancement.
