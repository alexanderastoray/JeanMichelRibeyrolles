# ART'elier

> Audit du 18/11/2026. Données relevées sur la page en ligne avec le navigateur Chrome piloté par Playwright (MCP).

## Informations

| Champ | Valeur |
|---|---|
| URL | https://jeanmichelribeyrolles.fr/artelier/ |
| Accès | Menu + footer |
| Statut HTTP | 200 |
| `<title>` (35 car.) | Jean-Michel RIBEYROLLES - ART’elier |
| Meta description (81 car.) | Invitation à découvrir l'univers d'un sculpteur-musicien à l'ART'elier Samonteil. |
| Canonical | https://jeanmichelribeyrolles.fr/artelier/ |
| Robots | index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1 |
| Langue | fr-FR |

## Titres

**H1** : ❌ aucun

**H2** (3) :

- ART'elier
- Exposition – Mémoire de Traces Oubliées
- Livre d'or

_Footer commun : 3 H2 « INFORMATION », « MENTIONS LÉGALES », « NAVIGATION » (non comptés ci-dessus)._

## Structure des sections

1. Bandeau (image de fond CSS), sans texte
2. H2 « ART'elier » — widgets : titre, séparateur, texte
   - Texte : « ART'elier Invitation à découvrir l’univers d’un sculpteur-musicien à l’ART’elier Samonteil.Venez vous évader au milieu de ses œuvres réalisées seul ou à « 4 mains » et de ses instruments de musique.Jean-Michel vous recevra dans une atmosphère musicale concoctée sur le moment, au gré de ses inspirati… »
3. widgets : HTML personnalisé — 3 image(s)
4. H2 « Exposition – Mémoire de Traces Oubliées » — widgets : titre, séparateur, texte
   - Texte : « Exposition – Mémoire de Traces Oubliées Espace OrlandoSur deux niveaux, l’artiste présentait ses trois univers :Miroirs d’énigme : pièces rondes, à poser ou suspendre, alliant douceur des formes et force des matières (bois et métal poli).Arcs-en-ciel noirs : œuvres où le bois, transformé par la tech… »
5. widgets : HTML personnalisé — 6 image(s)
6. H2 « Livre d'or » — widgets : titre, séparateur, icône, témoignages
   - Texte : « Livre d'or Un voyage à travers les matières, accompagné par une douce musique qui nous laisse partir dans l’imaginaire et l’eau. Des œuvres en bois d’une bouleversante originalité. Merci pour ces découvertes ! Marine Samedi 29 août 2020 Un lieu unique. Un plaisir de regarder des pièces de plus en pl… »

Footer commun : bloc INFORMATION (adresse), MENTIONS LÉGALES (crédits, lien), NAVIGATION (5 liens), logos.

## Images

9 image(s) dans le contenu (3 sans `alt`, 0 avec `alt` vide), plus 2 logos dans le footer. Dimensions : taille en pixels du fichier servi (suffixe WordPress `-LxH` quand il existe, sinon taille mesurée).

| # | Fichier | Dimensions (px) | alt | Zone |
|---|---|---|---|---|
| 1 | `2020-09-Exposition-ephemere-1.jpg` | 2816×2112 | ✅ « Œuvre 1 » | main |
| 2 | `2020-09-Exposition-ephemere-2.jpg` | 2816×2112 | ✅ « Œuvre 2 » | main |
| 3 | `2020-09-Exposition-ephemere-3.jpg` | 2816×2112 | ✅ « Œuvre 3 » | main |
| 4 | `20250826_152356.jpg` | 3468×4624 | ✅ « Œuvre 1 » | main |
| 5 | `20250826_151829.jpg` | 3468×4624 | ✅ « Œuvre 2 » | main |
| 6 | `20250826_152210.jpg` | 4624×3468 | ✅ « Œuvre 3 » | main |
| 7 | `20250826_151856.jpg` | 4624×3468 | ❌ absent | main |
| 8 | `20250826_151641.jpg` | non chargée | ❌ absent | main |
| 9 | `20250826_151732.jpg` | non chargée | ❌ absent | main |
| 10 | `logo-2-blanc-1024x948.png` | 1024×948 | ⚠️ vide | footer |
| 11 | `AAF_LOGO_OK.png` | 369×391 | ⚠️ vide | footer |

Images de fond CSS (pas d’attribut `alt` possible) : `Bandeau-ARTelier-Samonteil.jpg`

## Problèmes constatés

- 🟠 P2 — Aucun H1 sur la page (le titre principal est un H2).
- 🟠 P2 — Photos d'appareil photo brutes servies en pleine taille (`20250826_*.jpg`, 3468×4624 et 4624×3468 px) dans des vignettes de 314×235 px : poids de page inutile.
- 🟠 P2 — 3 images sans attribut `alt` (`20250826_151856.jpg`, `20250826_151641.jpg`, `20250826_151732.jpg`) ; les autres ont des `alt` génériques en double (« Œuvre 1 », « Œuvre 2 », « Œuvre 3 » apparaissent deux fois).
- 🟠 P2 — Exposition « Mémoire de Traces Oubliées – Espace Orlando » : ni date ni lieu complet.
- 🟡 P3 — 2 images du carrousel (`20250826_151641.jpg`, `20250826_151732.jpg`) n'étaient pas chargées au moment de la capture (hors écran, chargement différé) : à vérifier visuellement.
- 🟡 P3 — Carrousels codés à la main dans des widgets HTML (CSS et JS en ligne) : maintenance plus difficile que des widgets Elementor.
- 🟡 P3 — Livre d'or : tous les messages datent d'août/septembre 2020.
- 🟡 P3 — Livre d'or (citation de visiteurs) : « nous sommes délicatement invité » → « invités ».
- 🟡 P3 — Noms des collections écrits différemment du menu : « Miroirs d'énigme », « Arcs-en-ciel noirs », « Les gardiens de la Terre ».
- 🟡 P3 — Éléments communs (footer, bandeau) : voir [README](README.md#éléments-communs-à-toutes-les-pages).
