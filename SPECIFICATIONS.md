# Spécifications fonctionnelles — Gestion du prix Goncourt

## 1. Objet

L'application accompagne le jury du prix Goncourt dans la consultation des
ouvrages, la gestion des membres et l'organisation des tours de vote. Elle est
utilisée depuis une interface en ligne de commande et persiste les données dans
une base MySQL/MariaDB.

## 2. Acteurs

| Acteur | Description |
| --- | --- |
| Visiteur | Personne non authentifiée pouvant consulter les livres |
| Membre | Juré authentifié qui consulte la sélection et vote |
| Président | Juré responsable de la saisie des résultats et de l'annonce |
| Administrateur | Utilisateur qui gère les membres et les livres |

## 3. Données métier

- **Personne** : prénom, nom et âge.
- **Utilisateur** : personne possédant un courriel, un mot de passe et un statut.
- **Membre** : utilisateur appartenant au jury.
- **Président** : utilisateur chargé de superviser les votes.
- **Auteur** : personne associée à une biographie.
- **Livre** : titre, auteur, résumé, date de publication, éditeur, personnages
  principaux, nombre de pages, ISBN et prix.

## 4. Cas d'utilisation et critères d'acceptation

### UC01 — Consulter les livres

L'utilisateur demande la liste. Le système affiche au minimum le titre et
l'auteur de chaque livre chargé, une seule fois.

### UC02 — S'authentifier

**Précondition :** l'utilisateur existe dans la base.

1. L'utilisateur saisit son courriel et son mot de passe.
2. Le système vérifie les informations.
3. Il retourne le statut `President`, `Member` ou `Admin` et affiche le menu lié.

En cas d'informations incorrectes ou de base inaccessible, aucun menu protégé
ne doit être affiché.

### UC03 — Voter en tant que membre

**Précondition :** l'utilisateur est authentifié comme membre.

Le système affiche les livres et leur identifiant. Le membre sélectionne le
nombre de livres imposé pour le tour. Chaque identifiant doit exister, un même
livre ne peut être choisi deux fois et le nombre attendu doit être respecté.

### UC04 — Saisir et classer les votes

**Précondition :** l'utilisateur est authentifié comme président.

Le président saisit le nombre de votes de chaque livre. Le système refuse les
valeurs non entières ou négatives, classe les livres par nombre de votes
décroissant et affiche le nombre de livres retenu pour le tour.

### UC05 — Annoncer la sélection

Le président confirme les livres retenus. La saisie se termine uniquement
lorsque le nombre attendu de livres a été sélectionné.

### UC06 — Gérer les membres

L'administrateur peut créer, rechercher, modifier et supprimer un membre. Une
opération réussie est persistée ; en cas d'erreur, la transaction est annulée.

### UC07 — Gérer les livres

L'administrateur peut créer, rechercher, modifier et supprimer un livre. Si son
auteur n'existe pas, celui-ci est créé avant le livre.
