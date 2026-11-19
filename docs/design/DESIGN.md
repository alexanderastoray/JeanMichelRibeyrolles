# Identité visuelle — jeanmichelribeyrolles.fr

> Relevé du 18/11/2026 sur 3 pages : accueil, `/les-arcs-en-ciel-noir/`, `/artelier/`.
> Valeurs lues avec `getComputedStyle` dans Chrome (Playwright), en 1440 px et en 390 px de large.
> Site WordPress, thème OceanWP, constructeur Elementor. Aucune modification faite sur le site.
> Données brutes : `.playwright-mcp/design-data/*.json`. Captures : [captures/](captures/).

## En bref

- **Ambiance** : site sombre. Fonds gris anthracite et noirs, texte blanc, un seul accent ocre/orange `#DD9933`.
- **Typographies** : Open Sans pour la structure (menu, titres, footer), Roboto pour les textes courants et les boutons, Swanky and Moo Moo (manuscrite) pour l'accroche de l'accueil.
- **Refonte — Roboto remplace Open Sans** : Roboto pour tout le texte (paragraphes, titres, menu, footer), Swanky and Moo Moo pour le logo du header et l'accroche uniquement. Roboto est un choix de l'artiste : ne pas la remplacer. Les relevés ci-dessous décrivent le site actuel.
- **Formes** : angles droits partout (`border-radius: 0`). Titres de section centrés et soulignés d'un petit filet ocre.
- **Points faibles** :
  - Open Sans n'est jamais chargée : le navigateur la remplace par une police système.
  - Les couleurs et polices globales d'Elementor sont restées aux valeurs par défaut du kit, et la page ne les utilise pas.
  - Les tailles de titres varient d'une page à l'autre.

## Palette

| Couleur | Hex | Rôle constaté |
|---|---|---|
| ![](https://placehold.co/16x16/DD9933/DD9933.png) | `#DD9933` | **Accent unique** : fond des boutons, menu actif et au survol, filets sous les titres, liens dans le texte (« prendre rendez-vous »), noms du Livre d'or |
| ![](https://placehold.co/16x16/81847D/81847D.png) | `#81847D` | Fond des boutons au survol (accueil) |
| ![](https://placehold.co/16x16/2D2D2D/2D2D2D.png) | `#2D2D2D` | Fond de page (`body`) et des sections de contenu |
| ![](https://placehold.co/16x16/0A0A0A/0A0A0A.png) | `#0A0A0A` | Fond du header et des liens du menu |
| ![](https://placehold.co/16x16/1D1B1A/1D1B1A.png) | `#1D1B1A` | Fond du footer (zone widgets) |
| ![](https://placehold.co/16x16/1B1B1B/1B1B1B.png) | `#1B1B1B` | Fond du bas de footer (`#footer-bottom`) |
| ![](https://placehold.co/16x16/111111/111111.png) | `#111111` | Fond de 15 blocs sur ART'elier (Livre d'or / carrousel, à confirmer) |
| ![](https://placehold.co/16x16/2C2C2C/2C2C2C.png) | `#2C2C2C` | 2 blocs sur ART'elier (probablement les flèches du carrousel, à confirmer) |
| ![](https://placehold.co/16x16/000000/000000.png) | `#000000` / `rgba(0,0,0,.4)` | Texte des boutons ; voile sombre sur les images de bandeau |
| ![](https://placehold.co/16x16/FFFFFF/FFFFFF.png) | `#FFFFFF` | Texte principal : paragraphes, titres, menu |
| ![](https://placehold.co/16x16/F8F2F2/F8F2F2.png) | `#F8F2F2` | Titres de section des pages intérieures (blanc cassé, très proche de `#FFF`) |
| ![](https://placehold.co/16x16/BFBFBF/BFBFBF.png) | `#BFBFBF` | Dates du Livre d'or (ART'elier) |
| ![](https://placehold.co/16x16/C7C8CD/C7C8CD.png) | `#C7C8CD` | Titres de colonnes du footer (« INFORMATION »…), lien « Mentions légales » |
| ![](https://placehold.co/16x16/848692/848692.png) | `#848692` | Texte et liens du footer |
| ![](https://placehold.co/16x16/4A4A4A/4A4A4A.png) | `#4A4A4A` | Couleur de texte par défaut du `body` (OceanWP), presque invisible sur `#2D2D2D` et remplacée partout par les widgets |

Restes non utilisés ou incohérents :
- `#13AFF0` (bleu par défaut d'OceanWP) : couleur des liens du footer au survol, hors charte.
- `#333333` : couleur des `<a>` du footer, masquée par le `<span>` en `#848692` à l'intérieur.

### Variables CSS Elementor (kit `elementor-kit-442`)

Ces valeurs sont celles du kit Elementor par défaut. **Le site ne les utilise pas** : couleurs et polices sont saisies directement dans chaque widget.

| Variable | Valeur |
|---|---|
| `--e-global-color-primary` | `#6EC1E4` |
| `--e-global-color-secondary` | `#54595F` |
| `--e-global-color-text` | `#7A7A7A` |
| `--e-global-color-accent` | `#61CE70` |
| `--e-global-color-78c43809` | `#4054B2` |
| `--e-global-color-6f1c2291` | `#23A455` |
| `--e-global-color-794ae475` | `#000` |
| `--e-global-color-7c6cae40` | `#FFF` |
| `--e-global-color-2543f153` | `#000000` |
| `--e-global-typography-primary-font-family` / `-weight` | `"Roboto"` / `600` |
| `--e-global-typography-secondary-font-family` / `-weight` | `"Roboto Slab"` / `400` |
| `--e-global-typography-text-font-family` / `-weight` | `"Roboto"` / `400` |
| `--e-global-typography-accent-font-family` / `-weight` | `"Roboto"` / `500` |

## Typographies

### Choix pour la refonte

| Police | Graisses | Usage |
|---|---|---|
| **Roboto** | 300, 400, 500, 700 (pas d'italique : les vers des collections sont en romain) | Tout le texte : paragraphes, titres, menu, cartels, boutons, footer |
| **Swanky and Moo Moo** | 400 (pas de faux gras) | Logo du header et accroche de l'accueil uniquement |

Open Sans n'est plus utilisée. Les graisses 600 relevées sur le site actuel passent en Roboto 500.

### Polices réellement chargées (site actuel)

| Police | Graisses chargées | Source | Usage |
|---|---|---|---|
| **Roboto** | 400, 500 (accueil) ; 400, 600, 600 italique (ART'elier) | Copie locale Elementor : `/wp-content/uploads/elementor/google-fonts/` | Paragraphes, boutons |
| **Swanky and Moo Moo** | 400 | Chargée **deux fois** : copie locale Elementor + Google Fonts (`fonts.googleapis.com`, qui demande 18 variantes de 100 à 900i, puis `fonts.gstatic.com`) | Accroche « Sculpteur - Musicien » (accueil) |
| Font Awesome 5 Free | 900 | Plugin Elementor | Icônes (flèches des boutons, chevron du menu) |

Déclarées mais non utilisées sur ces 3 pages :
- **Roboto Slab** : `robotoslab.css` est chargée, mais aucun élément ne l'utilise.
- Font Awesome 6 (thème), Font Awesome 5 Brands, `FontAwesome` v4-shims, `eicons`, `simple-line-icons`.

⚠️ **Open Sans** est la police calculée du `body`, du menu, des titres et du footer. Aucune règle `@font-face` ne la déclare et aucun fichier n'est téléchargé. Le rendu dépend donc des polices installées chez le visiteur : Open Sans si elle est présente, sinon la police sans-serif du système (Arial, Helvetica, Liberation Sans…). Les captures montrent ce repli.

### Rôles typographiques

Valeurs du site actuel en 1440 px. Entre parenthèses : valeur en 390 px quand elle diffère. Dans la refonte, toutes les lignes en Open Sans passent en Roboto.

| Rôle | Famille | Taille / interligne | Graisse | Espacement | Couleur | Où |
|---|---|---|---|---|---|---|
| Corps (`body`) | Open Sans | 14 px / 25,2 px | 400 | normal | `#4A4A4A` sur `#2D2D2D` | Toutes |
| Menu principal | Open Sans | 14 px / 88 px (hauteur du header) | 400 | 0,6 px | `#FFF` ; actif et survol `#DD9933` | Toutes (desktop) |
| H1 accroche | Swanky and Moo Moo | 25 px / 25 px (20 px) | 700 (faux gras : la police n'existe qu'en 400) | 5 px | `#FFF` | Accueil seulement |
| H2 titre de section | Open Sans | 22 px / 22 px (accueil) ; 20 px / 20 px (pages intérieures) | 600 | normal | `#FFF` (accueil) ; `#F8F2F2` (pages intérieures) | Toutes |
| H2 fiche d'œuvre | Open Sans | 16 px / 16 px | 600 | normal | `#FFF` | Collections |
| H2 titre de colonne du footer | Open Sans | 14 px / 14 px | 600 | normal | `#C7C8CD` (capitales saisies dans le texte) | Toutes |
| H4 « ART'elier » (accroche) | Open Sans | 45 px / 63 px (30 / 42 px) | 600 | normal | `#FFF` | Accueil |
| H5 titre de vignette | Open Sans | 14 px / 19,6 px | 600 | normal | `#FFF` ; marge basse 12-15 px | Accueil (collections) |
| Paragraphe | Roboto | 16 px / 28,8 px | 400 | normal | `#FFF` ; marge basse 20 px | Toutes |
| Paragraphe d'intro | Open Sans | 16 px / 32 px (12 / 24 px) | 300 | normal | `#FFF` | Accueil (bloc ART'elier) |
| Lien dans le texte | Roboto | 16 px / 28,8 px | 400 (affiché en gras italique via les balises parentes) | normal | `#DD9933` | ART'elier |
| Bouton | Roboto | 16 px / 16 px | 500 | normal | `#000` sur `#DD9933` | Accueil |
| Flèches du carrousel | Open Sans | 32 px | 400 | normal | `#FFF` | ART'elier |
| Footer | Open Sans | 14 px / 25,2 px | 400 | normal | `#848692` | Toutes |

Aucun H1 sur les pages Arcs-en-ciel et ART'elier : le titre de page est un H2. Aucune transformation de casse (`text-transform: none` partout).

## Composants

- **Header** :
  - hauteur 88 px, fond `#0A0A0A`, conteneur à 90 % de la largeur ;
  - logo texte orange à gauche, menu à droite ;
  - liens avec `padding: 0 25px` ;
  - en 390 px, le menu est remplacé par une icône blanche qui ouvre un menu plein écran (OceanWP `fullscreen-mobile`).
- **Logo texte du header** (`#site-logo` > `a.site-title.site-logo-text`, texte « Jean-Michel RIBEYROLLES ») — styles calculés relevés avec Playwright le 2026-11-18 :

  | Élément | Largeur | font-family | font-size | font-weight | letter-spacing | color | text-transform | line-height |
  |---|---|---|---|---|---|---|---|---|
  | `#site-logo` | 1440 px | `"Open Sans", sans-serif` | 14 px | 400 | normal | `#4A4A4A` | none | 25,2 px |
  | `#site-logo` | 390 px | `"Open Sans", sans-serif` | 14 px | 400 | normal | `#4A4A4A` | none | 25,2 px |
  | lien `a` | 1440 px | `"Swanky and Moo Moo"` | 40 px | 400 | normal | `#DD9933` | none | 72 px |
  | lien `a` | 390 px | `"Swanky and Moo Moo"` | 38,93 px | 400 | normal | `#DD9933` | none | 70,08 px |

  - Le conteneur `#site-logo` n'affiche aucun texte propre : seuls les styles du lien sont visibles.
  - Le logo n'est pas une image : c'est du texte en Swanky and Moo Moo. Swanky and Moo Moo sert donc à l'accroche et au logo du header.
  - Pas de pile de secours après `"Swanky and Moo Moo"`.
  - En 390 px, la taille baisse légèrement (taille fluide). La boîte du lien mesure 394 px de large pour un viewport de 390 px.
- **Bouton** :
  - fond `#DD9933`, texte `#000`, Roboto 500 16 px, `padding: 15px 30px`, angles droits, icône » (Font Awesome) ;
  - au survol : fond `#81847D` ;
  - à vérifier : la couleur du texte au survol. La règle générique `.elementor-button:hover` la met en `#FFF`.
- **Titre de section** : texte centré, suivi d'un filet `#DD9933` court et centré (visible sur les captures, non mesuré).
- **Bandeau de page intérieure** :
  - image de fond plein écran avec voile `rgba(0,0,0,.4)` ;
  - hauteur 520 px (`padding: 250px 0`) ;
  - en 390 px : 182 px (`padding: 85px 0 75px`).
- **Hero de l'accueil** : image de fond `ACCUEIL.jpg`, hauteur 900 px (250 px en 390 px), accroche manuscrite et logo « JmiR » en haut à gauche.
- **Footer** :
  - fond `#1D1B1A`, puis `#1B1B1B` pour la ligne du bas ;
  - 4 colonnes de texte ;
  - logos JmiR et « Ateliers d'Art de France ».

## Espacements et mise en page

| Élément | Desktop 1440 px | Mobile 390 px |
|---|---|---|
| Largeur du contenu (`.elementor-container`) | 1140 px (variantes sur l'accueil : 1000, 700 et 1500 px) | 767 px max, soit pleine largeur |
| Conteneur du header et du footer | 90 % | 90 % |
| Hero de l'accueil | `padding-top: 150px`, hauteur 900 px | `50px 25px 25px`, hauteur 250 px |
| Sections de l'accueil | `100px 0 0`, `80px 0`, `70px 0 100px` | `55px 0 0`, `50px 30px`, `50px 20px` |
| Bandeau des pages intérieures | `250px 0` (520 px) | `85px 0 75px` (182 px) |
| Section d'intro des pages intérieures | `50px 0 0` à `100px 0 20px` | `60px 0 40px` |
| Fiches d'œuvre (Collections) | `20px 0` entre fiches | `50px 20px` |
| Galeries ART'elier | `10px` | `10px` |
| Marges de texte | `p` : 20 px en bas ; `h5` : 12-15 px en bas ; titres : 0 | idem |
| Rayons d'angle | 0 partout (les vignettes de galerie d'ART'elier ont un léger arrondi et une ombre, visibles sur les captures) | idem |

Rythme vertical dominant : multiples de 10 (10, 20, 50, 70, 80, 100, 150, 250 px), sans échelle stricte.

## Incohérences à corriger lors d'une refonte

1. **Open Sans n'est pas chargée** : le rendu dépend du poste du visiteur. Décision : Roboto la remplace (voir [Choix pour la refonte](#choix-pour-la-refonte)).
2. **La police d'accroche est chargée deux fois** : copie locale Elementor et Google Fonts avec 18 variantes, alors qu'une seule graisse (400) existe. L'appel Google Fonts pose aussi un problème RGPD.
3. **Polices inutiles** : Roboto Slab et plusieurs jeux d'icônes (Font Awesome 5 et 6, v4-shims, eicons, simple-line-icons) sont chargés sans être utilisés.
4. **Faux gras** sur l'accroche manuscrite (700 demandé, police disponible en 400 seulement).
5. **Kit Elementor non configuré** : les variables globales gardent les couleurs par défaut d'Elementor (bleu, vert). La vraie palette est saisie à la main dans chaque widget.
6. **Titres de section incohérents** : 22 px et `#FFF` sur l'accueil, 20 px et `#F8F2F2` ailleurs. Deux blancs différents.
7. **Deux familles pour le texte** (Open Sans et Roboto) sans répartition claire : le paragraphe d'intro de l'accueil est en Open Sans 300, les autres en Roboto 400. Décision : une seule famille, Roboto.
8. **Couleur de survol du footer** `#13AFF0`, bleu par défaut d'OceanWP, hors charte.
9. **Interligne de 1** sur les titres (22 px / 22 px) : serré pour les titres sur 2 lignes, comme les fiches d'œuvre en 390 px.

## Captures

Pleine page, avec la barre de défilement masquée dans le navigateur de capture pour obtenir la largeur exacte.

| Page | 1440 px | 390 px |
|---|---|---|
| Accueil | [accueil-1440.png](captures/accueil-1440.png) | [accueil-390.png](captures/accueil-390.png) |
| Les Arcs-en-ciel Noirs | [les-arcs-en-ciel-noir-1440.png](captures/les-arcs-en-ciel-noir-1440.png) | [les-arcs-en-ciel-noir-390.png](captures/les-arcs-en-ciel-noir-390.png) |
| ART'elier | [artelier-1440.png](captures/artelier-1440.png) | [artelier-390.png](captures/artelier-390.png) |

Sur la capture 1440 px de l'accueil, une bande grise apparaît au-dessus du header. C'est le header transparent et fixe, recomposé pendant la capture pleine page. Ce n'est pas un défaut du site.
