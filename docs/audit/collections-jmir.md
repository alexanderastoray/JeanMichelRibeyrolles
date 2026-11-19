# Collections

> Audit du 18/11/2026. Données relevées sur la page en ligne avec le navigateur Chrome piloté par Playwright (MCP).

## Informations

| Champ | Valeur |
|---|---|
| URL | https://jeanmichelribeyrolles.fr/collections-jmir/ |
| Accès | Menu + footer |
| Statut HTTP | 200 |
| `<title>` (37 car.) | Jean-Michel RIBEYROLLES - Collections |
| Meta description (123 car.) | JmiR, Sculpteur, Musicien, Collections, Sculpteur sur bois, Sculpteur sur bois brûlé, sculpture murale, sculpture sur socle |
| Canonical | https://jeanmichelribeyrolles.fr/collections-jmir/ |
| Robots | index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1 |
| Langue | fr-FR |

## Titres

**H1** : ❌ aucun

**H2** (4) :

- Les Arcs-en-ciel Noirs
- Les Miroirs d’Enigme
- Les Gardiens de la Terre
- Collection Privée

_Footer commun : 3 H2 « INFORMATION », « MENTIONS LÉGALES », « NAVIGATION » (non comptés ci-dessus)._

## Structure des sections

1. Bandeau (image de fond CSS), sans texte
2. H2 « Les Arcs-en-ciel Noirs » — widgets : titre, séparateur, image, bouton — 2 image(s)
   - Texte : « Les Arcs-en-ciel Noirs Découvrir »
3. H2 « Les Miroirs d’Enigme » — widgets : titre, séparateur, image, bouton — 4 image(s)
   - Texte : « Les Miroirs d’Enigme Découvrir »
4. H2 « Les Gardiens de la Terre » — widgets : titre, séparateur, image, bouton — 2 image(s)
   - Texte : « Les Gardiens de la Terre Découvrir »
5. H2 « Collection Privée » — widgets : titre, séparateur, image, bouton — 3 image(s)
   - Texte : « Collection Privée Découvrir »

Footer commun : bloc INFORMATION (adresse), MENTIONS LÉGALES (crédits, lien), NAVIGATION (5 liens), logos.

## Images

11 image(s) dans le contenu (0 sans `alt`, 11 avec `alt` vide), plus 2 logos dans le footer. Dimensions : taille en pixels du fichier servi (suffixe WordPress `-LxH` quand il existe, sinon taille mesurée).

| # | Fichier | Dimensions (px) | alt | Zone |
|---|---|---|---|---|
| 1 | `24FMR0303-Vue-1-80-x-30-x-3-cm-Frene-Acier-683x1024.jpg` | 683×1024 | ⚠️ vide | main |
| 2 | `24FM0503-Vue-1-55-x-37-x-4-cm-Frene-Acier-698x1024.jpg` | 698×1024 | ⚠️ vide | main |
| 3 | `21CM0109-Vue-1-38-x-48-x-4-Cedre-Metal-1024x684.jpg` | 1024×684 | ⚠️ vide | main |
| 4 | `23CM0307-Vue-1-20-x-3-cm-Cedre-Acier-1024x684.jpg` | 1024×684 | ⚠️ vide | main |
| 5 | `23FM0112-Vue-1-36-x-34-x-3-cm-Frene-Acier-1024x768.jpg` | 1024×768 | ⚠️ vide | main |
| 6 | `22DM0206-Vue-1-47-x-38-x-4-cm-Pin-douglas-Acier-1024x684.jpg` | 1024×684 | ⚠️ vide | main |
| 7 | `23CM0408-Vue-1-75-x-25-x-48-cm-Cedre-Acier-671x1024.jpg` | 671×1024 | ⚠️ vide | main |
| 8 | `23DM0101-Vue-1-115-x-32-x-4-cm-Pin-douglas-Acier-684x1024.jpg` | 684×1024 | ⚠️ vide | main |
| 9 | `21DM0305-Vue-1-110-x-40-x-25-Douglas-Metal-682x1024.jpg` | 682×1024 | ⚠️ vide | main |
| 10 | `22FM0305-Vue-1-36-x-31-x-3-Frene-Acier-1024x684.jpg` | 1024×684 | ⚠️ vide | main |
| 11 | `19MBDF0212-4-mains-Vue-1-42-x-78-x-5-Douglas-Frene-En-duo-Nathalie-RIBEYROLLES-1024x683.jpg` | 1024×683 | ⚠️ vide | main |
| 12 | `logo-2-blanc-1024x948.png` | 1024×948 | ⚠️ vide | footer |
| 13 | `AAF_LOGO_OK.png` | 369×391 | ⚠️ vide | footer |

Images de fond CSS (pas d’attribut `alt` possible) : `Bandeau-COLLECTIONS.jpg`

## Problèmes constatés

- 🟠 P2 — Aucun H1 sur la page (le titre principal est un H2).
- 🟠 P2 — 11 image(s) de contenu sans texte alternatif (0 sans attribut, 11 vides).
- 🟠 P2 — La meta description est une liste de mots-clés, pas une phrase.
- 🟡 P3 — Chaque collection a 2 à 4 liens vers la même page (images + bouton « Découvrir ») : liens redondants.
- 🟡 P3 — Le nom de l'image `19MBDF0212-4-mains-…-En-duo-Nathalie-RIBEYROLLES` ne suit pas le format des autres fichiers (voir `oeuvres.md`).
- 🟡 P3 — Éléments communs (footer, bandeau) : voir [README](README.md#éléments-communs-à-toutes-les-pages).
