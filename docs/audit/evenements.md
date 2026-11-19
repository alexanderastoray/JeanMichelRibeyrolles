# Evénements

> Audit du 18/11/2026. Données relevées sur la page en ligne avec le navigateur Chrome piloté par Playwright (MCP).

## Informations

| Champ | Valeur |
|---|---|
| URL | https://jeanmichelribeyrolles.fr/evenements/ |
| Accès | Footer uniquement |
| Statut HTTP | 200 |
| `<title>` (36 car.) | Jean-Michel RIBEYROLLES - Evènements |
| Meta description (126 car.) | Jean-Michel RIBEYROLLES Evénements, JmiR , Sculpteur, Musicien, Sculpteur sur bois, Sculpteur sur bois brûlé, sculpture murale |
| Canonical | https://jeanmichelribeyrolles.fr/evenements/ |
| Robots | index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1 |
| Langue | fr-FR |

## Titres

**H1** : ❌ aucun

**H2** (6) :

- Evènements
- 2024
- 2023
- 2022
- 2021
- 2020

_Footer commun : 3 H2 « INFORMATION », « MENTIONS LÉGALES », « NAVIGATION » (non comptés ci-dessus)._

## Structure des sections

1. Bandeau (image de fond CSS), sans texte
2. H2 « Evènements » — widgets : titre, séparateur
   - Texte : « Evènements »
3. H2 « 2024 » / H6 « 21 février au 05 mars » / H4 « EXPOSITION PLURIEL » / H6 « 01 au 3 mars » / H4 « Salon international d’art contemporain » / H4 « Art3f » (+89 titres) — widgets : titre, séparateur, texte
   - Texte : « 2024 21 février au 05 mars EXPOSITION PLURIEL Salle Balène à Figeac (46) 01 au 3 mars Salon international d’art contemporain Art3f Le MEET à Toulouse (31) 01 au 05 mai Salon 349 GALLERY avec Collections privées Pierre SOULAGES Saint-Orens (31) 04 mai au 12 juin ART Points de Vue Présence en personne… »

Footer commun : bloc INFORMATION (adresse), MENTIONS LÉGALES (crédits, lien), NAVIGATION (5 liens), logos.

## Images

0 image(s) dans le contenu (0 sans `alt`, 0 avec `alt` vide), plus 2 logos dans le footer. Dimensions : taille en pixels du fichier servi (suffixe WordPress `-LxH` quand il existe, sinon taille mesurée).

| # | Fichier | Dimensions (px) | alt | Zone |
|---|---|---|---|---|
| 1 | `logo-2-blanc-1024x948.png` | 1024×948 | ⚠️ vide | footer |
| 2 | `AAF_LOGO_OK.png` | 369×391 | ⚠️ vide | footer |

Images de fond CSS (pas d’attribut `alt` possible) : `Bandeau-EVENEMENTS.jpg`

## Problèmes constatés

- 🔴 P1 — 13 titres d'événements sont des liens vers `#` (EXPOSITION PLURIEL, Salon 349 GALLERY ×2, ART Points de Vue, Maison Louis DAVID, ART & JAZZ DANS MA COUR, Exposition « La Main Est l'Outil #4 », Salon de Sculpture Terre & Flamme, Salon international d'art contemporain, Sculpture monumentale contemporaine, Galerie Paul Sibra, Salon d'art international, Nice Art Expo) : liens cassés.
- 🔴 P1 — Contenu périmé : le dernier événement date de novembre 2024, rien pour 2025 ni 2026 (alors que la page ART'elier montre une exposition d'août 2025).
- 🟠 P2 — Aucun H1 sur la page (le titre principal est un H2).
- 🟠 P2 — La meta description est une liste de mots-clés, pas une phrase.
- 🟠 P2 — Page absente du menu principal (seulement dans le footer).
- 🟡 P3 — Orthographe du nom de page incohérente : « Evènements » (titre, H2) / « Evénements » (footer, meta description). Forme recommandée : « Événements ».
- 🟡 P3 — « Grandville (50) » → « Granville ».
- 🟡 P3 — « 9ième édition » → « 9e édition ».
- 🟡 P3 — « Saint Antonin Noble Val » → « Saint-Antonin-Noble-Val » ; « Saint Orens » et « Saint-Orens » coexistent.
- 🟡 P3 — 2020 : ordre chronologique cassé (« 7 au 14 septembre » est listé après « 29 août au 04 septembre »).
- 🟡 P3 — Formats de date mélangés : « 01 au 3 mars », « Du 10 au 13 novembre », « 22 octobre au 24 octobre ».
- 🟡 P3 — Éléments communs (footer, bandeau) : voir [README](README.md#éléments-communs-à-toutes-les-pages).
