# Accueil

> Audit du 18/11/2026. Données relevées sur la page en ligne avec le navigateur Chrome piloté par Playwright (MCP).

## Informations

| Champ | Valeur |
|---|---|
| URL | https://jeanmichelribeyrolles.fr/ |
| Accès | Logo |
| Statut HTTP | 200 |
| `<title>` (70 car.) | Jean-Michel RIBEYROLLES , Sculpteur-Musicien, Sculpteur sur bois brûlé |
| Meta description (129 car.) | JmiR, Sculpteur, Musicien, Sculpteur sur bois, Sculpteur sur bois brûlé, sculpture murale, sculpture sur socle, sculpture 4 mains |
| Canonical | https://jeanmichelribeyrolles.fr/ |
| Robots | index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1 |
| Langue | fr-FR |

## Titres

**H1** : « Sculpteur - Musicien »

**H2** (2) :

- Collections
- Reportage France TV

_Footer commun : 3 H2 « INFORMATION », « MENTIONS LÉGALES », « NAVIGATION » (non comptés ci-dessus)._

## Structure des sections

1. H1 « Sculpteur - Musicien » — widgets : titre, image — 1 image(s)
   - Texte : « Sculpteur - Musicien »
2. H2 « Collections » / H5 « Les Arcs-en-ciel Noirs » / H5 « Les Miroirs d’Enigme » / H5 « Les Gardiens de la Terre » — widgets : titre, séparateur, image, boîte image, bouton — 4 image(s)
   - Texte : « Collections Les Arcs-en-ciel Noirs Les Miroirs d’Enigme Les Gardiens de la Terre Découvrir »
3. H2 « Reportage France TV » — widgets : titre, séparateur, texte, vidéo
   - Texte : « Reportage France TV Des sculptures inspirées du néolithique »
4. H4 « ART'elier » — widgets : titre, texte, bouton
   - Texte : « ART'elier Invitation à découvrir l’univers d’un sculpteur-musicien à l’ART’elier Samonteil.Ouverture de juin à octobre Lire la suite »

Footer commun : bloc INFORMATION (adresse), MENTIONS LÉGALES (crédits, lien), NAVIGATION (5 liens), logos.

## Images

5 image(s) dans le contenu (0 sans `alt`, 5 avec `alt` vide), plus 2 logos dans le footer. Dimensions : taille en pixels du fichier servi (suffixe WordPress `-LxH` quand il existe, sinon taille mesurée).

| # | Fichier | Dimensions (px) | alt | Zone |
|---|---|---|---|---|
| 1 | `logo-2-blanc-150x150.png` | 150×150 | ⚠️ vide | main |
| 2 | `24FM0203-Vue-1-65-x-47-x-4-cm-Frene-Acier-684x1024.jpg` | 684×1024 | ⚠️ vide | main |
| 3 | `23CM0307-Vue-1-20-x-3-cm-Cedre-Acier-1024x684.jpg` | 1024×684 | ⚠️ vide | main |
| 4 | `22DM0803-Vue-1-24-x-23-x-25-Pin-douglas-Aluminium-1024x684.jpg` | 1024×684 | ⚠️ vide | main |
| 5 | `23DM0205-Vue-1-127-x-15-x-55-cm-Pin-douglas-Acier-684x1024.jpg` | 684×1024 | ⚠️ vide | main |
| 6 | `logo-2-blanc-1024x948.png` | 1024×948 | ⚠️ vide | footer |
| 7 | `AAF_LOGO_OK.png` | 369×391 | ⚠️ vide | footer |

Images de fond CSS (pas d’attribut `alt` possible) : `ACCUEIL.jpg`

## Problèmes constatés

- 🟠 P2 — La meta description est une liste de mots-clés, pas une phrase.
- 🟠 P2 — Meta description identique à : `les-arcs-en-ciel-noir`, `catalogue`, `mentions-legales`.
- 🟠 P2 — Le `<title>` contient une espace avant la virgule : « Jean-Michel RIBEYROLLES **,** Sculpteur-Musicien ».
- 🟠 P2 — Le H1 « Sculpteur - Musicien » ne contient ni le nom de l'artiste ni la spécialité (sculpture sur bois brûlé).
- 🟡 P3 — Hiérarchie des titres irrégulière : H1, puis H2 « Collections » avec des H5 pour les collections, puis un H4 « ART'elier » sans H3.
- 🟡 P3 — Deux liens consécutifs vers `/les-miroirs-denigme/` (2 images liées dans le même bloc).
- 🟡 P3 — Liens-images sans texte ni `alt` (image du haut vers `/jmir-portrait/`, vignettes des collections) : intitulé vide pour les lecteurs d'écran.
- 🟡 P3 — Le bloc « Collections » ne présente que 3 collections ; « Collection Privée » n'y figure pas.
- 🟡 P3 — Bloc « Reportage France TV » : aucune date ni source du reportage, une seule ligne de texte.
- 🟡 P3 — Éléments communs (footer, bandeau) : voir [README](README.md#éléments-communs-à-toutes-les-pages).
