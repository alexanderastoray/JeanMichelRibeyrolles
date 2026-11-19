# Audit du site jeanmichelribeyrolles.fr

> Audit du 18/11/2026. Site WordPress (thème OceanWP, constructeur Elementor, SEO Yoast), hébergé chez o2switch.

## Méthode et limites

- Pages parcourues à partir du menu principal et du footer, puis liens internes sur un niveau de profondeur.
- Ignorés : `/wp-admin`, `/wp-json`, `/feed`, URL avec paramètres, ancres `#`, liens directs vers `/wp-content/`. Ces liens directs (340 images en grand format ouvertes en lightbox) n'ont **pas** été vérifiés.
- Sitemap lu : `/wp-sitemap.xml` redirige (301) vers `/sitemap_index.xml` (Yoast), qui contient `page-sitemap.xml` (12 URL) et `oceanwp_library-sitemap.xml` (1 URL).
- Aucun formulaire rempli, aucune modification sur le site.
- Un premier crawl automatique a été bloqué par l'hébergeur (HTTP 429, puis page « Test de sécurité » en 503). L'audit a été refait page par page dans le navigateur Chrome piloté par Playwright (MCP), avec l'accord du demandeur.
- Le niveau 1 n'a révélé aucune nouvelle page : tous les liens internes mènent aux 11 pages ci-dessous ou à des fichiers `/wp-content/`. Aucun lien externe trouvé (seuls Google Maps et reCAPTCHA, en iframe, sur la page Contact).
- Statut HTTP : statut de la page réellement servie après le test de sécurité, lu dans l'API Navigation Timing du navigateur.

## Arborescence

```text
https://jeanmichelribeyrolles.fr/
├── /                            Accueil (logo)                       200
├── /collections-jmir/           Collections (menu + footer)          200
│   ├── /les-arcs-en-ciel-noir/  Les Arcs-en-ciel Noirs (menu)        200   15 œuvres
│   ├── /les-miroirs-denigme/    Les Miroirs d'Enigme (menu)          200   17 œuvres
│   ├── /les-gardiens-de-la-terre/ Les Gardiens de la Terre (menu)    200   32 œuvres
│   └── /catalogue/              Collection Privée (menu)             200  110 œuvres
├── /artelier/                   ART'elier (menu + footer)            200
├── /jmir-portrait/              Portrait (menu + footer)             200
├── /contact/                    Contact (menu + footer)              200
├── /evenements/                 Evénements (footer seulement)        200
└── /mentions-legales/           Mentions légales (footer seulement)  200

Hors navigation, présentes dans le sitemap :
├── /elementor-2080/             « Footer » (modèle Elementor)        200   ⚠️ indexable
└── /?oceanwp_library=footer     modèle OceanWP                       redirige vers /
```

| Page | Fiche | P1 | P2 | P3 |
|---|---|---|---|---|
| Accueil | [accueil.md](accueil.md) | — | 4 | 5 |
| Collections | [collections-jmir.md](collections-jmir.md) | — | 3 | 2 |
| Les Arcs-en-ciel Noirs | [les-arcs-en-ciel-noir.md](les-arcs-en-ciel-noir.md) | 1 | 7 | 8 |
| Les Miroirs d'Enigme | [les-miroirs-denigme.md](les-miroirs-denigme.md) | — | 5 | 4 |
| Les Gardiens de la Terre | [les-gardiens-de-la-terre.md](les-gardiens-de-la-terre.md) | 2 | 3 | 8 |
| Collection Privée | [catalogue.md](catalogue.md) | 12 | 6 | 32 |
| ART'elier | [artelier.md](artelier.md) | — | 4 | 5 |
| Portrait | [jmir-portrait.md](jmir-portrait.md) | — | 4 | 4 |
| Contact | [contact.md](contact.md) | — | 6 | 2 |
| Evénements | [evenements.md](evenements.md) | 2 | 3 | 6 |
| Mentions légales | [mentions-legales.md](mentions-legales.md) | — | 3 | 5 |
| Œuvres (174 fiches) | [oeuvres.md](oeuvres.md) | | | |

## Synthèse des problèmes par priorité

- 🔴 **P1** : erreur visible ou donnée fausse, à corriger en premier.
- 🟠 **P2** : SEO, accessibilité, performance ou contenu incomplet.
- 🟡 **P3** : coquilles, cohérence, finitions.

Total par page (hors éléments communs) : 17 P1, 48 P2, 81 P3. Le détail de chaque problème est dans la fiche de la page.

### 🔴 P1 — À corriger en premier

- **Site** — Page `/elementor-2080/` publique et indexable (`index, follow`), présente dans le sitemap : c'est le modèle de footer Elementor, titre « Footer », avec du texte de démo d'un autre site (« © 2026 Fazhie », « HELP & INFORMATION », « Track Order », « Careers », « Investors »…). À dépublier ou passer en `noindex`, et à retirer du sitemap.
- **Toutes les pages** — Footer : « © 2026 Jean-Michel **Riberyrolles** » → « Ribeyrolles ». Coquille sur toutes les pages.
- **Collection Privée** — 8 fiches (sections 69 à 77, sauf 76) affichent une 2e « Référence : 22FM0404 » dans leur titre (copier-coller probable).
- **Les Arcs-en-ciel Noirs** — Fiche 25AI0202 (section 7) : dimensions différentes : fiche « 161 x 15,5 x 5,5 cm » / fichier « 122 x 11 x 3 cm ».
- **Les Gardiens de la Terre** — Fiche 23FM0208 (section 21) : fiche regroupant 3 œuvres (23FM0208, 23DM0308, 23CM0108).
- **Les Gardiens de la Terre** — Fiche E24DM0101 (section 32) : matériaux différents : fiche « Pin douglas Acier corten » / fichier « Pin douglas Acier corten Inox ».
- **Collection Privée** — Fiche 20MBDF0301 (section 65) : référence différente entre la fiche (`20MBDF0301`) et le fichier (`20MBD0301`).
- **Collection Privée** — Fiche 20MBDF0301 (section 65) : dimensions différentes : fiche « 46 x 56 x 4 cm » / fichier « 56 x 46 x 4 ».
- **Collection Privée** — Fiche 21FM0204 (section 93) : dimensions absentes du titre de la fiche.
- **Collection Privée** — Fiche 20SBFM0111 (section 97) : référence différente entre la fiche (`20SBFM0111`) et le fichier (`20BFM0111`).
- **Evénements** — 13 titres d'événements sont des liens vers `#` (EXPOSITION PLURIEL, Salon 349 GALLERY ×2, ART Points de Vue, Maison Louis DAVID, ART & JAZZ DANS MA COUR, Exposition « La Main Est l'Outil #4 », Salon de Sculpture Terre & Flamme, Salon international d'art contemporain, Sculpture monumentale contemporaine, Galerie Paul Sibra, Salon d'art international, Nice Art Expo) : liens cassés.
- **Evénements** — Contenu périmé : le dernier événement date de novembre 2024, rien pour 2025 ni 2026 (alors que la page ART'elier montre une exposition d'août 2025).

### 🟠 P2 — Important

- **Site** — Le sitemap `oceanwp_library-sitemap.xml` expose `/?oceanwp_library=footer` (modèle OceanWP) ; l'URL redirige vers l'accueil. À exclure du sitemap Yoast.
- **Site** — 9 pages sur 11 n'ont pas de H1 : seuls l'accueil et les mentions légales en ont un.
- **Site** — Les meta descriptions sont des listes de mots-clés ; 4 pages ont exactement la même (accueil, Arcs-en-ciel Noirs, Collection Privée, Mentions légales).
- **Site** — Textes alternatifs : sur 342 images d'œuvres, une seule a un `alt` renseigné ; les logos du footer ont aussi un `alt` vide.
- **Site** — Le site applique une limite de requêtes (HTTP 429), puis une page « Test de sécurité » o2switch (HTTP 503) aux clients sans JavaScript. Les robots d'indexation et les outils d'audit peuvent être bloqués : à vérifier dans la Search Console.
- **Toutes les pages** — Footer : lien `https://jeanmichelribeyrolles.fr/#` sans texte visible. C'est le bouton « retour en haut » du thème OceanWP ; son seul intitulé est l'`aria-label` anglais « Scroll to the top of the page ».
- **Toutes les pages** — Footer : les logos (`logo-2-blanc-1024x948.png`, `AAF_LOGO_OK.png`) ont un `alt` vide ; le logo AAF n'est ni expliqué ni lié.
- **Accueil** — Le `<title>` contient une espace avant la virgule : « Jean-Michel RIBEYROLLES **,** Sculpteur-Musicien ».
- **Accueil** — Le H1 « Sculpteur - Musicien » ne contient ni le nom de l'artiste ni la spécialité (sculpture sur bois brûlé).
- **Les Arcs-en-ciel Noirs** — Fiche 25FI0907 (section 3) : numéro de vue en double : 2.
- **Les Arcs-en-ciel Noirs** — Fiche 25FI0907 (section 3) : fichiers de références différentes dans la même galerie (25FI0907, 25FI1007).
- **Les Arcs-en-ciel Noirs** — Fiche 23FMB0410 (section 16) : numéro de vue en double : 1.
- **Collection Privée / Les Miroirs d'Enigme** — doublon : référence présente 2 fois — Les Miroirs d'Enigme (section 7), Collection Privée (section 12). (22FM0407)
- **Collection Privée / Les Miroirs d'Enigme** — numérotation des vues discontinue (1, 3). (3 fiches : 24CM0604, 24CHM0403, 20SDM0311)
- **ART'elier** — Photos d'appareil photo brutes servies en pleine taille (`20250826_*.jpg`, 3468×4624 et 4624×3468 px) dans des vignettes de 314×235 px : poids de page inutile.
- **ART'elier** — 3 images sans attribut `alt` (`20250826_151856.jpg`, `20250826_151641.jpg`, `20250826_151732.jpg`) ; les autres ont des `alt` génériques en double (« Œuvre 1 », « Œuvre 2 », « Œuvre 3 » apparaissent deux fois).
- **ART'elier** — Exposition « Mémoire de Traces Oubliées – Espace Orlando » : ni date ni lieu complet.
- **Portrait** — Les 3 photos sont des miniatures de 300×200 px (`Portrait-1-300x200.jpg`…) : basse résolution pour la page de présentation de l'artiste.
- **Contact** — Deux formulaires complets dans le code (« Formulaire PC » et « Formulaire Mobile »), l'un avec Captcha, l'autre avec reCAPTCHA : le même contenu est dupliqué et maintenu deux fois.
- **Contact** — Champs sans libellé visible (placeholder seulement) et aucun champ obligatoire, y compris l'e-mail.
- **Contact** — Les numéros de téléphone ne sont pas cliquables (pas de lien `tel:`).
- **Contact** — Un `<iframe>` sans `src` dans la page.
- **Evénements** — Page absente du menu principal (seulement dans le footer).
- **Mentions légales** — Pas de politique de confidentialité alors que le site collecte des données (formulaire de contact, reCAPTCHA Google, carte Google Maps) ; pas de mention RGPD (finalité, durée de conservation, droits).

### 🟡 P3 — Finitions

- **Site** — Nommage incohérent entre menu, titre et URL : « Les Arcs-en-ciel Noirs » → `/les-arcs-en-ciel-noir/`, « Collection Privée » → `/catalogue/`, « Portrait » → `/jmir-portrait/`.
- **Site** — « Evénements » est dans le footer mais pas dans le menu principal.
- **Toutes les pages** — Footer : la navigation n'a pas les mêmes entrées que le menu principal (Evénements en plus, Mentions légales à part, sous-collections absentes).
- **Toutes les pages** — Footer : « non libres de droit » → « non libres de droits ».
- **Toutes les pages** — Chaque page commence par une section « bandeau » (image de fond CSS) sans texte ni H1 ; l'image de fond n'a pas d'équivalent textuel.
- **Accueil** — Hiérarchie des titres irrégulière : H1, puis H2 « Collections » avec des H5 pour les collections, puis un H4 « ART'elier » sans H3.
- **Accueil** — Deux liens consécutifs vers `/les-miroirs-denigme/` (2 images liées dans le même bloc).
- **Accueil** — Liens-images sans texte ni `alt` (image du haut vers `/jmir-portrait/`, vignettes des collections) : intitulé vide pour les lecteurs d'écran.
- **Accueil** — Le bloc « Collections » ne présente que 3 collections ; « Collection Privée » n'y figure pas.
- **Accueil** — Bloc « Reportage France TV » : aucune date ni source du reportage, une seule ligne de texte.
- **Collections** — Chaque collection a 2 à 4 liens vers la même page (images + bouton « Découvrir ») : liens redondants.
- **Collections** — Le nom de l'image `19MBDF0212-4-mains-…-En-duo-Nathalie-RIBEYROLLES` ne suit pas le format des autres fichiers (voir `oeuvres.md`).
- **Collection Privée / Les Arcs-en-ciel Noirs / Les Gardiens de la Terre** — coquille « Châtaigner » (→ Châtaignier). (6 fiches : 24HM0308, 24HM0208, 24HM0212, 25HM0407, 25HI0105, 25HI0601)
- **Collection Privée / Les Arcs-en-ciel Noirs / Les Gardiens de la Terre** — espace manquante après « Matière : ». (10 fiches : 24CHM0204, 23TM0508, 24CHM0202, 24FMR0303, 24FM0106, 24CHM0403, 24FM0102, 24FM0103, 24FM0203, 24FM0503)
- **Les Arcs-en-ciel Noirs** — 4 fiche(s) sur 15 ont des noms de fichiers hors format (liste dans [`oeuvres.md`](oeuvres.md#noms-de-fichiers-hors-format)).
- **Les Arcs-en-ciel Noirs** — Texte d'introduction : « jusqu'à **l‘**effacement » utilise un guillemet ouvrant (‘) au lieu d'une apostrophe (’).
- **Les Arcs-en-ciel Noirs** — Le slug `/les-arcs-en-ciel-noir/` est au singulier, le titre est au pluriel (« Noirs »).
- **Les Arcs-en-ciel Noirs** — Le `<title>` met le nom de la collection en premier (« Les Arcs-en-ciel Noirs - Jean-Michel RIBEYROLLES ») ; les autres pages de collection commencent par « Jean-Michel RIBEYROLLES - ».
- **Collection Privée / Les Gardiens de la Terre / Les Miroirs d'Enigme** — décimale avec un point (ailleurs : virgule). (4 fiches : 25BC0308, 25BI0104, 25CHI0305, 23DM0210)
- **Les Miroirs d'Enigme** — 4 fiche(s) sur 17 ont des noms de fichiers hors format (liste dans [`oeuvres.md`](oeuvres.md#noms-de-fichiers-hors-format)).
- **Les Miroirs d'Enigme** — Texte d'introduction : « coeurs » → « cœurs ».
- **Les Miroirs d'Enigme** — « Enigme » sans accent sur la majuscule (→ « Énigme ») dans le titre, le menu et le H2 ; la page ART'elier écrit « Miroirs d'énigme ».
- **Les Gardiens de la Terre** — Fiche 24103 (section 9) : référence sans lettres dans la fiche (`24103`).
- **Les Gardiens de la Terre** — Fiche 24101 (section 15) : référence sans lettres dans la fiche (`24101`).
- **Collection Privée / Les Gardiens de la Terre** — matériaux différents : fiche « Frêne / Bronze Florentin » / fichier « Frêne Métal » (le nom de fichier est plus générique : à vérifier). (2 fiches : 22FM0102, 22FM0401)
- **Les Gardiens de la Terre** — 16 fiche(s) sur 32 ont des noms de fichiers hors format (liste dans [`oeuvres.md`](oeuvres.md#noms-de-fichiers-hors-format)).
- **Collection Privée** — Fiche 24102 (section 26) : référence sans lettres dans la fiche (`24102`).
- **Collection Privée** — Fiche 252 (section 47) : référence sans lettres dans la fiche (`252`).
- **Collection Privée** — Fiche 252 (section 47) : matériaux différents : fiche « Noyer / Bronze Florentin » / fichier « Noyer Métal » (le nom de fichier est plus générique : à vérifier).
- **Collection Privée** — Fiche 23CHM0312 (section 48) : préfixe parasite « 1 - » devant les dimensions.
- **Collection Privée** — espacement irrégulier autour de « / ». (2 fiches : 20SBDM0212, 22DM0803)
- **Collection Privée** — « X » majuscule dans les dimensions. (2 fiches : 20SBFM0312, 22FM0603)
- **Collection Privée** — Fiche 21PM0110 (section 78) : coquille « Pallissandre » (→ Palissandre).
- **Collection Privée** — Fiche 21PM0110 (section 78) : matériaux différents : fiche « Pallissandre / Bronze Florentin » / fichier « Palissandre Métal » (le nom de fichier est plus générique : à vérifier).
- **Collection Privée** — Fiche 22CM0301 (section 90) : matériaux différents : fiche « Cèdre / Bronze Florentin » / fichier « Cèdre Métal » (le nom de fichier est plus générique : à vérifier).
- **Collection Privée** — Fiche 22DM0201 (section 91) : coquille « Etain » (→ Étain).
- **Collection Privée** — Fiche 22DM0201 (section 91) : matériaux différents : fiche « Douglas / Etain » / fichier « douglas Métal » (le nom de fichier est plus générique : à vérifier).
- **Collection Privée** — Fiche 21FM0204 (section 93) : coquille « laitonnél » (→ laitonné).
- **Collection Privée** — Fiche 19MBDF0212 (section 107) : mention « Collaboration » collée dans le titre (format différent des autres fiches).
- **Collection Privée** — Fiche 19B03 (section 109) : matériaux différents : fiche « Douglas / Galet » / fichier « douglas » (le nom de fichier est plus générique : à vérifier).
- **Collection Privée** — 65 fiche(s) sur 110 ont des noms de fichiers hors format (liste dans [`oeuvres.md`](oeuvres.md#noms-de-fichiers-hors-format)).
- **Collection Privée** — Nom incohérent : menu « Collection Privée », `<title>` « Collection privée », URL `/catalogue/`.
- **Collection Privée** — Une seule image a un `alt` renseigné (« 20SBFM0111 70 x 22 x 3 cm Frêne / Métal ») ; toutes les autres sont vides.
- **Collection Privée** — Page très longue (112 sections, 217 images) sans filtre, ancre ni pagination.
- **ART'elier** — 2 images du carrousel (`20250826_151641.jpg`, `20250826_151732.jpg`) n'étaient pas chargées au moment de la capture (hors écran, chargement différé) : à vérifier visuellement.
- **ART'elier** — Carrousels codés à la main dans des widgets HTML (CSS et JS en ligne) : maintenance plus difficile que des widgets Elementor.
- **ART'elier** — Livre d'or : tous les messages datent d'août/septembre 2020.
- **ART'elier** — Livre d'or (citation de visiteurs) : « nous sommes délicatement invité » → « invités ».
- **ART'elier** — Noms des collections écrits différemment du menu : « Miroirs d'énigme », « Arcs-en-ciel noirs », « Les gardiens de la Terre ».
- **Portrait** — « A côté » → « À côté ».
- **Portrait** — « la forteresse de Castelneau » : orthographe probable « Castelnau » (château de Castelnau-Bretenoux, Lot), à confirmer.
- **Portrait** — « les dégradés orangers du Douglas » → « orangés ».
- **Portrait** — Le texte est signé « Patrick Churlet » sans mention de son rôle (auteur, journaliste ?).
- **Contact** — Placeholder « Telephone » → « Téléphone ».
- **Contact** — Formats de téléphone différents de la page Mentions légales (`+33 (0)6 85 81 31 48` ici, `06.85.81.31.48` là-bas).
- **Evénements** — Orthographe du nom de page incohérente : « Evènements » (titre, H2) / « Evénements » (footer, meta description). Forme recommandée : « Événements ».
- **Evénements** — « Grandville (50) » → « Granville ».
- **Evénements** — « 9ième édition » → « 9e édition ».
- **Evénements** — « Saint Antonin Noble Val » → « Saint-Antonin-Noble-Val » ; « Saint Orens » et « Saint-Orens » coexistent.
- **Evénements** — 2020 : ordre chronologique cassé (« 7 au 14 septembre » est listé après « 29 août au 04 septembre »).
- **Evénements** — Formats de date mélangés : « 01 au 3 mars », « Du 10 au 13 novembre », « 22 octobre au 24 octobre ».
- **Mentions légales** — `<title>` « Mentions legales » sans accent.
- **Mentions légales** — Adresse « 46 400 SAINT-PAUL-DEVERN » → « 46400 Saint-Paul-de-Vern » (comme dans le footer).
- **Mentions légales** — Rubrique « Informatiques et libertés » → « Informatique et libertés ».
- **Mentions légales** — Capital de l'hébergeur au format anglais : « 10,000,000€ » → « 10 000 000 € ».
- **Mentions légales** — Le texte sur les cookies parle du « consommateur » : le site ne vend rien.

## Éléments communs à toutes les pages

- 🔴 P1 — Footer : « © 2026 Jean-Michel **Riberyrolles** » → « Ribeyrolles ». Coquille sur toutes les pages.
- 🟠 P2 — Footer : lien `https://jeanmichelribeyrolles.fr/#` sans texte visible. C'est le bouton « retour en haut » du thème OceanWP ; son seul intitulé est l'`aria-label` anglais « Scroll to the top of the page ».
- 🟠 P2 — Footer : les logos (`logo-2-blanc-1024x948.png`, `AAF_LOGO_OK.png`) ont un `alt` vide ; le logo AAF n'est ni expliqué ni lié.
- 🟡 P3 — Footer : la navigation n'a pas les mêmes entrées que le menu principal (Evénements en plus, Mentions légales à part, sous-collections absentes).
- 🟡 P3 — Footer : « non libres de droit » → « non libres de droits ».
- 🟡 P3 — Chaque page commence par une section « bandeau » (image de fond CSS) sans texte ni H1 ; l'image de fond n'a pas d'équivalent textuel.

## URL pour les redirections 301

Liste des URL publiques actuelles, à reporter dans le plan de redirection de la refonte. Les cibles proposées sont des **suggestions** à valider selon la nouvelle arborescence.

| URL actuelle | Statut actuel | Cible proposée | Remarque |
|---|---|---|---|
| https://jeanmichelribeyrolles.fr/ | 200 | `/` | Accueil, à conserver |
| https://jeanmichelribeyrolles.fr/collections-jmir/ | 200 | `/collections/` | Slug « -jmir » superflu |
| https://jeanmichelribeyrolles.fr/les-arcs-en-ciel-noir/ | 200 | `/collections/arcs-en-ciel-noirs/` | Corrige le singulier |
| https://jeanmichelribeyrolles.fr/les-miroirs-denigme/ | 200 | `/collections/miroirs-d-enigme/` | |
| https://jeanmichelribeyrolles.fr/les-gardiens-de-la-terre/ | 200 | `/collections/gardiens-de-la-terre/` | |
| https://jeanmichelribeyrolles.fr/catalogue/ | 200 | `/collections/collection-privee/` | Aligne l'URL sur le nom du menu |
| https://jeanmichelribeyrolles.fr/artelier/ | 200 | `/artelier/` | À conserver |
| https://jeanmichelribeyrolles.fr/jmir-portrait/ | 200 | `/portrait/` | |
| https://jeanmichelribeyrolles.fr/contact/ | 200 | `/contact/` | À conserver |
| https://jeanmichelribeyrolles.fr/evenements/ | 200 | `/evenements/` | À conserver |
| https://jeanmichelribeyrolles.fr/mentions-legales/ | 200 | `/mentions-legales/` | À conserver |
| https://jeanmichelribeyrolles.fr/elementor-2080/ | 200 | `/` (ou 410) | Modèle de footer exposé par erreur |
| https://jeanmichelribeyrolles.fr/?oceanwp_library=footer | redirige vers `/` | `/` | Modèle OceanWP, déjà redirigé |
| https://jeanmichelribeyrolles.fr/wp-sitemap.xml | 301 → `/sitemap_index.xml` | nouveau sitemap | Déjà en 301 |

Liste brute :

```text
https://jeanmichelribeyrolles.fr/
https://jeanmichelribeyrolles.fr/collections-jmir/
https://jeanmichelribeyrolles.fr/les-arcs-en-ciel-noir/
https://jeanmichelribeyrolles.fr/les-miroirs-denigme/
https://jeanmichelribeyrolles.fr/les-gardiens-de-la-terre/
https://jeanmichelribeyrolles.fr/catalogue/
https://jeanmichelribeyrolles.fr/artelier/
https://jeanmichelribeyrolles.fr/jmir-portrait/
https://jeanmichelribeyrolles.fr/contact/
https://jeanmichelribeyrolles.fr/evenements/
https://jeanmichelribeyrolles.fr/mentions-legales/
https://jeanmichelribeyrolles.fr/elementor-2080/
https://jeanmichelribeyrolles.fr/?oceanwp_library=footer
https://jeanmichelribeyrolles.fr/wp-sitemap.xml
```

Si les médias changent d'emplacement, il faudra aussi rediriger les URL `/wp-content/uploads/…` des images (342 images d'œuvres, plus les images ouvertes en grand dans les galeries). Elles ne sont pas listées ici.
