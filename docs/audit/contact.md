# Contact

> Audit du 18/11/2026. Données relevées sur la page en ligne avec le navigateur Chrome piloté par Playwright (MCP).

## Informations

| Champ | Valeur |
|---|---|
| URL | https://jeanmichelribeyrolles.fr/contact/ |
| Accès | Menu + footer |
| Statut HTTP | 200 |
| `<title>` (33 car.) | Jean-Michel RIBEYROLLES - Contact |
| Meta description (136 car.) | Jean-Michel RIBEYROLLES Contact, Sculpteur, Musicien, Sculpteur sur bois, Sculpteur sur bois brûlé sculpture murale, sculpture sur socle |
| Canonical | https://jeanmichelribeyrolles.fr/contact/ |
| Robots | index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1 |
| Langue | fr-FR |

## Titres

**H1** : ❌ aucun

**H2** (1) :

- CONTACTEZ-NOUS

_Footer commun : 3 H2 « INFORMATION », « MENTIONS LÉGALES », « NAVIGATION » (non comptés ci-dessus)._

## Structure des sections

1. Bandeau (image de fond CSS), sans texte
2. H2 « CONTACTEZ-NOUS » / H6 « ART'elier Samonteil » — widgets : titre, boîte icône, carte Google Maps, formulaire Formidable
   - Texte : « CONTACTEZ-NOUS Pour une visite personnalisée et en musique « live » ou pour de plus amples renseignements, nous vous invitons à nous laisser vos coordonnées ou à nous contacter à l’un des numéros indiqués. Nous nous ferons un plaisir de vous répondre. A bientôt. +33 (0)6 85 81 31 48 +33 (0)6 78 38 7… »

Footer commun : bloc INFORMATION (adresse), MENTIONS LÉGALES (crédits, lien), NAVIGATION (5 liens), logos.

## Images

0 image(s) dans le contenu (0 sans `alt`, 0 avec `alt` vide), plus 2 logos dans le footer. Dimensions : taille en pixels du fichier servi (suffixe WordPress `-LxH` quand il existe, sinon taille mesurée).

| # | Fichier | Dimensions (px) | alt | Zone |
|---|---|---|---|---|
| 1 | `logo-2-blanc-1024x948.png` | 1024×948 | ⚠️ vide | footer |
| 2 | `AAF_LOGO_OK.png` | 369×391 | ⚠️ vide | footer |

Images de fond CSS (pas d’attribut `alt` possible) : `Bandeau-CONTACT.jpg`

## Problèmes constatés

- 🟠 P2 — Aucun H1 sur la page (le titre principal est un H2).
- 🟠 P2 — La meta description est une liste de mots-clés, pas une phrase.
- 🟠 P2 — Deux formulaires complets dans le code (« Formulaire PC » et « Formulaire Mobile »), l'un avec Captcha, l'autre avec reCAPTCHA : le même contenu est dupliqué et maintenu deux fois.
- 🟠 P2 — Champs sans libellé visible (placeholder seulement) et aucun champ obligatoire, y compris l'e-mail.
- 🟠 P2 — Les numéros de téléphone ne sont pas cliquables (pas de lien `tel:`).
- 🟠 P2 — Un `<iframe>` sans `src` dans la page.
- 🟡 P3 — Placeholder « Telephone » → « Téléphone ».
- 🟡 P3 — Formats de téléphone différents de la page Mentions légales (`+33 (0)6 85 81 31 48` ici, `06.85.81.31.48` là-bas).
- 🟡 P3 — Éléments communs (footer, bandeau) : voir [README](README.md#éléments-communs-à-toutes-les-pages).
