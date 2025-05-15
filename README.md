# Analyse non supervisée de l’adoption des bus scolaires électriques aux États-Unis

## Présentation

Ce projet explore l’adoption des bus scolaires électriques (Electric School Buses - ESBs) dans les districts scolaires américains, à partir des données fournies par le World Resources Institute (version août 2024).

L’objectif est de détecter des profils types, des comportements atypiques et des relations significatives entre adoption technologique et contexte socio-économique, en utilisant des techniques d’apprentissage non supervisé.

---

## Données

Les données sont structurées en plusieurs feuilles Excel, notamment :
- **District-level data** : caractéristiques sociales, économiques, environnementales, nombre d’ESBs
- **Bus-level data** : détail par bus (statut, financement, OEM, etc.)
- **State-level data** : agrégation par État
- **Utilities** : fournisseurs d’électricité associés aux districts

---

## Méthodologie

### 1. Prétraitement
- Normalisation des variables quantitatives
- Création de variables binaires (ex : pollution élevée, pauvreté élevée)
- Exclusion des colonnes peu renseignées

### 2. Réduction de dimension
- Application de **PCA** pour explorer la structure latente
- Visualisation en 2D des districts selon les deux premières composantes

### 3. Clustering
- Utilisation de **KMeans** (k optimal = 4)
- Analyse des profils moyens par cluster

### 4. Détection d’anomalies
- Application de **Isolation Forest**
- Identification de districts atypiques dans leurs caractéristiques combinées

### 5. Règles d’association
- Application d’**Apriori**
- Découverte de règles fréquentes entre variables socio-environnementales et adoption

---

## Résultats clés

- **Cluster 3** : districts à forte pauvreté, mais très avancés dans l’adoption des ESBs
- **Cluster 1** : districts riches, mais à faible adoption
- **Anomalies** : districts avec adoption extrême ou incohérente (ex : adoption sans justification apparente)
- **Règles d’association** : 
  - Les districts à revenu élevé et pollution PM2.5 élevée ont souvent aussi un niveau d’ozone élevé
  - Pauvreté élevée + ozone élevé impliquent souvent PM2.5 élevé

---

## Visualisations

- PCA (réduction à 2D)
- Méthode du coude et score de silhouette pour KMeans
- Clusters affichés sur carte interactive (Mapbox + Folium)
- Moyennes des indicateurs par cluster
- Règles d’association triées par lift

---

## Données générées

- `districts_with_cluster_anomaly.csv` : table finale enrichie avec le cluster et l’étiquette anomalie

---

## Pistes futures

- Analyse temporelle des phases de déploiement (commande → livraison → opération)
- Étude détaillée des **sources de financement** et leur rôle dans l’adoption
- Intégration de la **dimension géographique** plus fine (cartes choroplèthes)