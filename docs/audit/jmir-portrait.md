# Portrait

> Audit du 18/11/2026. Données relevées sur la page en ligne avec le navigateur Chrome piloté par Playwright (MCP).

## Informations

| Champ | Valeur |
|---|---|
| URL | https://jeanmichelribeyrolles.fr/jmir-portrait/ |
| Accès | Menu + footer |
| Statut HTTP | 200 |
| `<title>` (41 car.) | Jean-Michel RIBEYROLLES - JmiR - Portrait |
| Meta description (154 car.) | Jean-Michel RIBEYROLLES, JmiR, Sculpteur, Musicien, Sculpteur sur bois, Sculpteur sur bois brûlé, sculpture murale, sculpture sur socle, sculpture 4 mains |
| Canonical | https://jeanmichelribeyrolles.fr/jmir-portrait/ |
| Robots | index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1 |
| Langue | fr-FR |

## Titres

**H1** : ❌ aucun

**H2** (1) :

- Messager du néolithique

_Footer commun : 3 H2 « INFORMATION », « MENTIONS LÉGALES », « NAVIGATION » (non comptés ci-dessus)._

## Structure des sections

1. Bandeau (image de fond CSS), sans texte
2. H2 « Messager du néolithique » — widgets : titre, séparateur, texte, image — 1 image(s)
   - Texte : « Messager du néolithique La sculpture et la musique ont fait irruption dans la vie de Jean-Michel RIBEYROLLES il y a longtemps. Les deux s’accordent et se répondent en parfaite complicité. Quand le sculpteur expose ses œuvres, il arrive que le musicien improvise quelques notes à l’accordéon ou au vio… »
3. widgets : image, texte — 1 image(s)
   - Texte : « L’univers de JmiR est profondément inspiré par le monde néolithique, les représentations grand format des premières traces de l’homme, les dolmens, les statues menhirs ou les imposants cairns. Qui sont ces bâtisseurs, avec quelles techniques et connaissances ont-ils pu créer ces formes ? C’est tout … »
4. widgets : texte, image — 1 image(s)
   - Texte : « A côté de son atelier qui plonge dans les vallons du Lot bordés par les tours du château de Saint-Laurent et la masse ocre de la forteresse de Castelneau, JmiR a aménagé une pièce claire et nue où il installe ses sculptures avec lesquelles il continue de dialoguer. « Cette pièce est un espace de vér… »

Footer commun : bloc INFORMATION (adresse), MENTIONS LÉGALES (crédits, lien), NAVIGATION (5 liens), logos.

## Images

3 image(s) dans le contenu (0 sans `alt`, 3 avec `alt` vide), plus 2 logos dans le footer. Dimensions : taille en pixels du fichier servi (suffixe WordPress `-LxH` quand il existe, sinon taille mesurée).

| # | Fichier | Dimensions (px) | alt | Zone |
|---|---|---|---|---|
| 1 | `Portrait-1-300x200.jpg` | 300×200 | ⚠️ vide | main |
| 2 | `Portrait-2-300x200.jpg` | 300×200 | ⚠️ vide | main |
| 3 | `Portrait-3-300x200.jpg` | 300×200 | ⚠️ vide | main |
| 4 | `logo-2-blanc-1024x948.png` | 1024×948 | ⚠️ vide | footer |
| 5 | `AAF_LOGO_OK.png` | 369×391 | ⚠️ vide | footer |

Images de fond CSS (pas d’attribut `alt` possible) : `Bandeau-PORTRAIT.jpg`

## Problèmes constatés

- 🟠 P2 — Aucun H1 sur la page (le titre principal est un H2).
- 🟠 P2 — 3 image(s) de contenu sans texte alternatif (0 sans attribut, 3 vides).
- 🟠 P2 — La meta description est une liste de mots-clés, pas une phrase.
- 🟠 P2 — Les 3 photos sont des miniatures de 300×200 px (`Portrait-1-300x200.jpg`…) : basse résolution pour la page de présentation de l'artiste.
- 🟡 P3 — « A côté » → « À côté ».
- 🟡 P3 — « la forteresse de Castelneau » : orthographe probable « Castelnau » (château de Castelnau-Bretenoux, Lot), à confirmer.
- 🟡 P3 — « les dégradés orangers du Douglas » → « orangés ».
- 🟡 P3 — Le texte est signé « Patrick Churlet » sans mention de son rôle (auteur, journaliste ?).
- 🟡 P3 — Éléments communs (footer, bandeau) : voir [README](README.md#éléments-communs-à-toutes-les-pages).
