#!/usr/bin/env python3
"""Génère les maquettes HTML statiques dans maquettes/ (une page par fichier).

Usage, depuis la racine du projet :  python3 scripts/maquettes/gen.py
Dépendance : Pillow (images réduites dans maquettes/img/).
Données : docs/audit/ (dimensions des titres H2) ; textes relevés sur le site en ligne.
"""
import glob, os, sys, urllib.parse
from PIL import Image

ROOT = sys.argv[1] if len(sys.argv) > 1 else os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
PH = os.path.join(ROOT, "docs/design/photos")
OUT = os.path.join(ROOT, "maquettes")
REL = "../docs/design/photos/"
# Affichage réduit (grilles, rangées) ; la lightbox charge l'original HD (-scaled).
SIZES = {"t": 900, "m": 1800}

def photo(prefix):
    m = sorted(glob.glob(os.path.join(PH, prefix + "*.jpg")))
    assert m, prefix
    return os.path.basename(m[0])

def size(fname):
    return Image.open(os.path.join(PH, fname)).size

def reduced(fname, v):
    """Crée (si besoin) la version réduite de fname et renvoie (chemin relatif, w, h)."""
    src = os.path.join(PH, fname)
    im = Image.open(src)
    w, h = im.size
    lim = SIZES[v]
    if max(w, h) <= lim:
        return REL + fname, w, h
    r = lim / max(w, h)
    nw, nh = round(w * r), round(h * r)
    rel = f"img/{v}/{fname}"
    dst = os.path.join(OUT, rel)
    if not os.path.exists(dst):
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        im.convert("RGB").resize((nw, nh), Image.LANCZOS).save(dst, "JPEG", quality=82, progressive=True, optimize=True)
    return rel, nw, nh

ARCS, MIR, GARD, PRIV = "Les Arcs-en-ciel Noirs", "Les Miroirs d’Énigme", "Les Gardiens de la Terre", "Collection Privée"
COLL = MIR

def work(ref, dims, mats, coll, v1=None, **kw):
    v1 = v1 or photo(ref + "-Vue-1")
    others = sorted(x for x in map(os.path.basename, glob.glob(os.path.join(PH, ref + "-Vue-*.jpg")))
                    if not x.startswith(ref + "-Vue-1"))
    return dict(ref=ref, dims=dims, mats=mats, coll=coll, v1=v1, views=[v1] + others, **kw)

# Données : dimensions des titres H2 (virgule décimale), matériaux du H2.
# w = largeur réelle (cm) de l'œuvre dans la photo de face ; f = part de la largeur
# de la photo occupée par l'œuvre (mesurée à l'œil, ±10 %) ; maxd = plus grande dimension.
MIROIRS = [
    # ref,        dims,                mats,                 w,  f,    maxd
    ("25SA0108", "Ø 40 × 4 cm",       ["Séquoia", "acier"],  40, .56, 40),
    ("25CC0208", "Ø 17 × 2 cm",       ["Cèdre", "cuivre"],   17, .54, 17),
    ("25CA0307", "Ø 25 × 3 cm",       ["Cèdre", "aluminium"],25, .60, 25),
    ("25BC0308", "Ø 16 × 1,5 cm",     ["Buis", "cuivre"],    16, .54, 16),
    ("22FM0407", "43 × 43 × 3 cm",    ["Frêne", "aluminium"],43, .54, 43),
    ("25DI0204", "Ø 29 × 7 cm",       ["Pin douglas", "inox"],29, .57, 29),
    ("24FM0311", "Ø 40 × 4 cm",       ["Frêne", "aluminium"],40, .57, 40),
    ("25DM0301", "Ø 42 × 4 cm",       ["Pin douglas", "inox"],42, .556, 42),
    ("24FM0112", "Ø 65 × 5 cm",       ["Frêne", "inox"],     65, .61, 65),
    ("24FM0211", "Ø 34 × 4 cm",       ["Frêne", "aluminium"],34, .61, 34),
    ("24FM0111", "Ø 34 × 4 cm",       ["Frêne", "aluminium"],34, .57, 34),
    ("24CM0604", "Ø 17 × 2 cm",       ["Cèdre", "acier"],    17, .45, 17),
    ("22FM0307", "26 × 21 × 3 cm",    ["Frêne", "acier"],    21, .46, 26),
    ("22CM0205", "41 × 34 × 4,5 cm",  ["Cèdre", "acier"],    34, .50, 41),
    ("20SFM0112", "37 × 26 × 3 cm",   ["Frêne", "métal"],    26, .31, 37),
    ("22TM0112", "32 × 3 cm",         ["Tsuga", "acier"],    32, .44, 32),
    ("19MBD0111", "43 × 5,5 cm",      ["Douglas"],           43, .40, 43),
]
M = {ref: work(ref, dims, mats, MIR, w=w, f=f, maxd=maxd) for ref, dims, mats, w, f, maxd in MIROIRS}

W = {  # autres collections : œuvres dont la photo est disponible dans docs/design/photos
    # Arcs-en-ciel Noirs (15 œuvres)
    "24HM0212": work("24HM0212", "178 × 21 × 5 cm", ["Châtaignier", "inox"], ARCS),
    "25CHI411": work("25CHI411", "65 × 40 × 5 cm", ["Chêne", "inox"], ARCS),
    "24CHM0710": work("24CHM0710", "134 × 35 × 4 cm", ["Chêne", "acier"], ARCS,
                      v1="24CHM0710-Vue-1-134-x-35-x-4-cm-Chene-Acier-scaled.jpg"),
    "25FI0907": work("25FI0907", "130 × 60 × 5 cm", ["Frêne", "inox"], ARCS, v1=photo("25FI0907-et-25FI1007-Vue-1")),
    "25AI0202": work("25AI0202", "161 × 15,5 × 5,5 cm", ["Charme", "inox"], ARCS),
    "24FM0107": work("24FM0107", "74 × 59 × 5 cm", ["Frêne", "acier"], ARCS),
    # Gardiens de la Terre (32 œuvres)
    "25FI58": work("25FI58", "73 × 31 × 4 cm", ["Frêne", "inox"], GARD),
    "24103": work("24103", "190 × 22 × 5 cm", ["Chêne", "inox"], GARD),
    "25CHA311": work("25CHA311", "58 × 43 × 5 cm", ["Chêne", "acier"], GARD),
    "22FM0208": work("22FM0208", "174 × 28 × 3 cm", ["Frêne", "acier"], GARD),
    "25BI0505": work("25BI0505", "57 × 10 × 3 cm", ["Buis", "inox"], GARD),
    "E24DM0101": work("E24DM0101", "188 × 50 × 6 cm", ["Pin douglas", "acier corten"], GARD,
                      v1=photo("E24DM0101-188")),
    "23DM0205": work("23DM0205", "127 × 15 × 5,5 cm", ["Pin douglas", "acier"], GARD, w=15, f=.16),
    # Collection Privée (110 œuvres)
    "25SA0207": work("25SA0207", "53 × 38 × 3 cm", ["Séquoia", "acier"], PRIV),
    "25SP0405": work("25SP0405", "Ø 33 × 3 cm", ["Séquoia", "pyrite"], PRIV),
    "24BM0310": work("24BM0310", "55 × 7 × 3 cm", ["Buis", "acier"], PRIV),
    "23FM0212": work("23FM0212", "Ø 36 × 34 × 3 cm", ["Frêne", "acier"], PRIV),
    "24FM0203": work("24FM0203", "65 × 47 × 4 cm", ["Frêne", "acier"], PRIV, w=47, f=.84),
    "23CHMB0610": work("23CHMB0610", "29 × 29 × 3 cm", ["Chêne", "acier"], PRIV),
    "22DM0803": work("22DM0803", "24 × 23 × 2,5 cm", ["Pin douglas", "aluminium"], PRIV),
    "24FM0210": work("24FM0210", "80 × 37 × 4 cm", ["Frêne", "acier"], PRIV),
    "23CM0307": work("23CM0307", "20 × 3 cm", ["Cèdre", "acier"], PRIV),
}

# Textes des collections : retours à la ligne d'origine (relevés sur le site en ligne), en romain.
VERSES = {
    ARCS: ["Qui révélera l’énigme des origines du noir,",
           "lorsque dans un temps enfoui, les sept couleurs de l’arc-en-ciel",
           "emportées dans un mouvement insensé",
           "roulèrent les unes contre les autres,",
           "jusqu’à l’effacement, la nudité absolue,",
           "pour rendre au noir toute sa clarté, sa puissance sauvage,",
           "pour l’affranchir de son exil."],
    MIR: ["Il y a quelque 3000 ans des hommes et des femmes entreprenaient des",
          "voyages périlleux pour se retrouver seuls avec les Miroirs d’Énigme."],
    GARD: ["Les Gardiens de la Terre sont des messagers bienveillants et",
           "protecteurs, sans âge ni origine, porteurs de l’histoire de",
           "l’humanité."],
}

def verse(coll):
    # un vers = une ligne ; s'il ne tient pas, la suite est en retrait (retrait suspendu)
    return "".join(f'<span class="l">{l}</span>' for l in VERSES[coll])

def mats_txt(o):
    m = o["mats"]
    return m[0] if len(m) == 1 else ", ".join([m[0]] + [x.lower() for x in m[1:]])

def mats_alt(o):
    m = [x.lower() for x in o["mats"]]
    return m[0] if len(m) == 1 else ", ".join(m[:-1]) + " et " + m[-1]

def alt(o, detail=False):
    s = f"{o['coll']} : sculpture en {mats_alt(o)}, {o['dims']}"
    return s + (", détail" if detail else "")

def fiche(o):
    return "oeuvre.html" if o["ref"] == "24FM0112" else "#"

def cartel(o, short=False, link=False):
    ref = f'<a class="ref" href="{fiche(o)}">{o["ref"]}</a>' if link else f'<span class="ref">{o["ref"]}</span>'
    if short:
        return f'<p class="cartel">{ref}</p>'
    return (f'<p class="cartel">{ref}<span class="sep">·</span>'
            f'<span class="dims">{o["dims"]}</span><span class="sep mat-sep">·</span><span class="mat">{mats_txt(o)}</span></p>')

def img(fname, alt_txt, cls="", loading="lazy", v="t", style=""):
    if v:
        src, w, h = reduced(fname, v)
    else:
        (w, h), src = size(fname), REL + fname
    c = f' class="{cls}"' if cls else ""
    s = f' style="{style}"' if style else ""
    return f'<img{c}{s} src="{src}" width="{w}" height="{h}" alt="{alt_txt}" loading="{loading}" decoding="async">'

def hd(fname, label, inner, cls=""):
    """Lien vers le fichier HD, ouvert dans la lightbox PhotoSwipe."""
    w, h = size(fname)
    c = f' class="{cls}"' if cls else ""
    return (f'<a{c} href="{REL}{fname}" data-pswp-width="{w}" data-pswp-height="{h}" '
            f'aria-label="{label}">{inner}</a>')

NAV = [("collections.html", "Collections"), ("#", "ART'elier"), ("portrait.html", "Portrait"), ("#", "Contact")]

def header(current):
    items = "\n".join(
        f'        <li><a href="{h}"{" aria-current=\"page\"" if l == current else ""}>{l}</a></li>' for h, l in NAV)
    return f'''<header class="site-header">
  <div class="bar">
    <a class="logo" href="accueil.html">Jean-Michel RIBEYROLLES</a>
    <button class="menu-toggle" type="button" aria-label="Ouvrir le menu" aria-expanded="false" aria-controls="menu">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M3 6h18M3 12h18M3 18h18"/></svg>
    </button>
    <nav class="nav" id="menu" aria-label="Menu principal">
      <button class="menu-toggle menu-close" type="button" aria-label="Fermer le menu">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M5 5l14 14M19 5L5 19"/></svg>
      </button>
      <ul>
{items}
      </ul>
    </nav>
  </div>
</header>'''

FOOTER = f'''<footer class="site-footer">
  <div class="cols">
    <div class="f-brand">
      <img src="{REL}logo-2-blanc.png" width="1643" height="1521" alt="JmiR, signature de Jean-Michel Ribeyrolles" loading="lazy">
      <p>© 2026<br>Jean-Michel Ribeyrolles</p>
    </div>
    <div class="f-info">
      <h2>Information</h2>
      <p>ART'elier Samonteil<br>115 impasse de Samonteil<br>46400 Saint-Paul-de-Vern<br>France</p>
      <p><a href="tel:+33685813148">06 85 81 31 48</a><br><a href="tel:+33678387857">06 78 38 78 57</a></p>
    </div>
    <div class="f-legal">
      <h2>Mentions légales</h2>
      <p>© Photos de Yoann Portejoie et Benoît Frété, non libres de droits</p>
      <p>Site réalisé par Alexander Astoray</p>
      <p><a href="#">Mentions légales</a></p>
    </div>
    <div class="f-nav">
      <h2>Navigation</h2>
      <ul>
        <li><a href="collections.html">Collections</a></li>
        <li><a href="#">ART'elier</a></li>
        <li><a href="portrait.html">Portrait</a></li>
        <li><a href="#">Contact</a></li>
      </ul>
    </div>
    <div class="f-aaf">
      <a href="https://www.ateliersdart.com/" rel="noopener"><img src="{REL}AAF_LOGO_OK.png" width="369" height="391" alt="Membre des Ateliers d'Art de France" loading="lazy"></a>
    </div>
  </div>
</footer>
<script>
  (function () {{
    var header = document.querySelector('.site-header');
    var nav = document.getElementById('menu');
    var open = document.querySelector('.bar > .menu-toggle');
    var close = nav.querySelector('.menu-close');
    open.addEventListener('click', function () {{ nav.classList.add('is-open'); open.setAttribute('aria-expanded', 'true'); close.focus(); }});
    close.addEventListener('click', function () {{ nav.classList.remove('is-open'); open.setAttribute('aria-expanded', 'false'); open.focus(); }});

    // Header : réduit à 64 px une fois la page défilée ; masqué en descendant, visible en remontant.
    var last = window.scrollY, ticking = false;
    function update() {{
      var y = window.scrollY, dy = y - last;
      header.classList.toggle('is-scrolled', y > 8);
      if (Math.abs(dy) > 4) {{
        var hide = dy > 0 && y > 160 && !nav.classList.contains('is-open') && !header.contains(document.activeElement);
        header.classList.toggle('is-hidden', hide);
        last = y;
      }}
      ticking = false;
    }}
    window.addEventListener('scroll', function () {{
      if (!ticking) {{ ticking = true; requestAnimationFrame(update); }}
    }}, {{ passive: true }});
    update();
  }})();
</script>'''

PSWP_CSS = '\n<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/photoswipe@5.4.4/dist/photoswipe.css">'
PSWP_JS = '''
<script type="module">
  import PhotoSwipeLightbox from 'https://cdn.jsdelivr.net/npm/photoswipe@5.4.4/dist/photoswipe-lightbox.esm.min.js';
  const lightbox = new PhotoSwipeLightbox({
    gallery: '[data-pswp-gallery]',
    children: 'a[data-pswp-width]',
    pswpModule: () => import('https://cdn.jsdelivr.net/npm/photoswipe@5.4.4/dist/photoswipe.esm.min.js'),
    bgOpacity: 1,
    padding: { top: 56, bottom: 104, left: 16, right: 16 },
    imageClickAction: 'zoom',      // clic : zoom / dézoom
    tapAction: 'toggle-controls',  // mobile : tap = interface, pincement et double tap = zoom
    doubleTapAction: 'zoom',
    maxZoomLevel: 4,
    closeTitle: 'Fermer (Échap)', zoomTitle: 'Zoomer', arrowPrevTitle: 'Précédente', arrowNextTitle: 'Suivante',
    errorMsg: 'L’image n’a pas pu être chargée.',
    indexIndicatorSep: ' / ',
  });
  // Légende : cartel de l'œuvre (+ lien vers la fiche sur la page collection)
  lightbox.on('uiRegister', () => {
    lightbox.pswp.ui.registerElement({
      name: 'cartel', order: 9, isButton: false, appendTo: 'root', html: '',
      onInit: (el, pswp) => {
        pswp.on('change', () => {
          const a = pswp.currSlide.data.element;
          const cap = a && a.parentElement.querySelector('.pswp-cap');
          el.innerHTML = cap ? cap.innerHTML : '';
        });
      },
    });
  });
  lightbox.init();
</script>'''

def page(title, desc, current, body, extra="", head="", body_cls=""):
    cls = f' class="{body_cls}"' if body_cls else ""
    return f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&family=Swanky+and+Moo+Moo&display=swap">{head}
<link rel="stylesheet" href="styles.css">
</head>
<body{cls}>
{header(current)}
<main>
{body}
</main>
{FOOTER}{extra}
</body>
</html>
'''

def write(name, html):
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as fh:
        fh.write(html)
    print("écrit", name)

def breadcrumb(*items):
    parts = [f'<a href="{h}">{l}</a>' if h else f'<span aria-current="page">{l}</span>' for h, l in items]
    return ('<nav class="breadcrumb" aria-label="Fil d’Ariane">'
            + '<span class="sep">/</span>'.join(parts) + '</nav>')

# --------------------------------------------------------------------------- accueil
def coll_block(name, o, href):
    w, h = size(o["v1"])
    return f'''    <article class="coll">
      <figure class="coll-media"><a href="{href}">{img(o["v1"], alt(o), "portrait" if h > w else "landscape", v="m")}</a></figure>
      <div class="coll-text">
        <h3>{name}</h3>
        <p class="verse">{verse(name)}</p>
        {cartel(o)}
        <p><a class="link-arrow" href="{href}">Découvrir la collection</a></p>
      </div>
    </article>'''

accueil = f'''<section class="hero">
  {img("ACCUEIL.jpg", "", loading="eager", v=None)}
  <div class="hero-text">
    <h1><span class="accroche">Sculpteur – Musicien</span>
      <span class="h1-sub">Jean-Michel Ribeyrolles<span>Sculpture sur bois brûlé · ART'elier Samonteil, Lot</span></span></h1>
  </div>
</section>

<section class="section collections" aria-labelledby="t-coll">
  <div class="wrap">
    <h2 class="section-title" id="t-coll">Collections</h2>
{coll_block(ARCS, W["24FM0203"], "#")}
{coll_block(MIR, W["23CM0307"], "collection.html")}
{coll_block(GARD, W["23DM0205"], "#")}
    <p class="all-colls"><a class="link-arrow" href="collections.html">Toutes les collections</a></p>
  </div>
</section>

<section class="section artelier" aria-labelledby="t-art">
  <div class="wrap">
    <article class="coll coll--media-first">
      <figure class="coll-media">{img("2020-09-Exposition-ephemere-1.jpg", "Exposition éphémère à l’ART’elier Samonteil, septembre 2020 : sculptures murales et sur socle", "landscape", v="m")}</figure>
      <div class="coll-text">
        <h2 id="t-art">ART'elier Samonteil</h2>
        <p>Invitation à découvrir l’univers d’un sculpteur-musicien à l’ART’elier Samonteil. Venez vous évader au milieu de ses œuvres réalisées seul ou à « 4 mains » et de ses instruments de musique.</p>
        <p>Jean-Michel vous recevra dans une atmosphère musicale concoctée sur le moment, au gré de ses inspirations.</p>
        <p class="cartel infos">Saint-Paul-de-Vern, Lot<span class="sep">·</span>juin à octobre<span class="sep">·</span>sur rendez-vous</p>
        <p><a class="link-arrow" href="#">Préparer sa visite</a></p>
      </div>
    </article>
  </div>
</section>

<section class="section reportage" aria-labelledby="t-tv">
  <div class="wrap">
    <h2 class="section-title" id="t-tv">Reportage France TV</h2>
    <div class="player">
      <video controls preload="none" poster="../docs/design/videos/reportage-vignette.jpg" width="1280" height="720">
        <source src="../docs/design/videos/reportage-france-tv.mp4" type="video/mp4">
      </video>
      <p class="caption">Des sculptures inspirées du néolithique</p>
    </div>
  </div>
</section>'''
write("accueil.html", page("Jean-Michel Ribeyrolles, sculpteur sur bois brûlé et musicien",
                           "Jean-Michel Ribeyrolles sculpte le bois brûlé à l’ART’elier Samonteil, dans le Lot : sculptures murales et sur socle, collections et visites de juin à octobre.",
                           None, accueil, body_cls="home"))

# --------------------------------------------------------------------------- collections (vue d'ensemble)
# Œuvres choisies par l'artiste : celles de la page Collections du site actuel
# (docs/audit/collections-jmir.md). Dimensions et matériaux des titres H2 (docs/audit/catalogue.md…).
PICKS = {
    "24FMR0303": work("24FMR0303", "80 × 30 × 3 cm", ["Frêne", "acier"], ARCS),
    "24FM0503": work("24FM0503", "55 × 37 × 4 cm", ["Frêne", "acier"], ARCS),
    "21CM0109": work("21CM0109", "38 × 48 × 4 cm", ["Cèdre", "métal"], MIR),
    "23CM0307": work("23CM0307", "20 × 3 cm", ["Cèdre", "acier"], MIR),
    "23FM0112": work("23FM0112", "Ø 36 × 34 × 3 cm", ["Frêne", "acier"], MIR),
    "22DM0206": work("22DM0206", "47 × 38 × 4 cm", ["Pin douglas", "acier"], MIR),
    "23CM0408": work("23CM0408", "75 × 25 × 4,8 cm", ["Cèdre", "acier"], GARD),
    "23DM0101": work("23DM0101", "115 × 32 × 4 cm", ["Pin douglas", "acier"], GARD),
    "21DM0305": work("21DM0305", "110 × 40 × 2,5 cm", ["Douglas", "métal"], PRIV),
    "22FM0305": work("22FM0305", "36 × 31 × 3 cm", ["Frêne", "acier"], PRIV),
    "19MBDF0212": work("19MBDF0212", "42 × 78 × 5 cm", ["Douglas", "frêne"], PRIV,
                       v1=photo("19MBDF0212-4-mains-Vue-1"), duo="à 4 mains avec Nathalie Ribeyrolles"),
}
# Composition de la page Collections actuelle (docs/design/captures/collections-jmir-1440.png) :
# grille de 2 colonnes ; « pairs » = photos 2 par 2, « mosaic » = 1re photo à gauche sur toute
# la hauteur, les 2 suivantes empilées à droite.
OVERVIEW = [
    (ARCS, "#", "pairs", ["24FMR0303", "24FM0503"], None),
    (MIR, "collection.html", "pairs", ["21CM0109", "23CM0307", "23FM0112", "22DM0206"], None),
    (GARD, "#", "pairs", ["23CM0408", "23DM0101"], None),
    (PRIV, "#", "mosaic", ["21DM0305", "22FM0305", "19MBDF0212"],
     "Les sculptures présentées dans ce catalogue appartiennent à des collectionneurs privés en France et à l’étranger."),
]

def ocell(r, cls="cell"):
    """Photo cliquable (lightbox HD) + légende de la lightbox."""
    o = PICKS[r]
    a = alt(o) + (", " + o["duo"] if o.get("duo") else "")
    return (f'<div class="{cls}">{hd(o["v1"], f"Agrandir la photo de {o["ref"]}", img(o["v1"], a, v="m"))}'
            f'<div class="pswp-cap" hidden>{cartel(o)}</div></div>')

def cblock(i, name, href, layout, refs, intro):
    if layout == "mosaic":
        cells = (f'      {ocell(refs[0], "cell cell--tall")}\n'
                 f'      <div class="stack">{"".join(ocell(r) for r in refs[1:])}</div>')
    else:
        cells = "\n".join(f"      {ocell(r)}" for r in refs)
    lines = VERSES.get(name, [])
    text = (f'<p class="intro-line">{intro}</p>' if intro
            else '<p class="verse">' + "".join(f'<span class="l">{l}</span>' for l in lines) + '</p>')
    return f'''<section class="cblock" aria-labelledby="c{i}">
  <div class="wrap">
    <h2 class="section-title" id="c{i}">{name}</h2>
    {text}
    <div class="cgrid{" cgrid--mosaic" if layout == "mosaic" else ""}" data-pswp-gallery>
{cells}
    </div>
    <p class="more"><a class="link-arrow" href="{href}">Découvrir<span class="sr-only"> : {name}</span></a></p>
  </div>
</section>'''

collections = f'''<section class="banner banner--colls">
  {img("Bandeau-COLLECTIONS.jpg", "", loading="eager", v=None)}
  <h1>Collections</h1>
</section>

{chr(10).join(cblock(i, *c) for i, c in enumerate(OVERVIEW))}'''
write("collections.html", page("Collections · Jean-Michel Ribeyrolles",
                               "Les quatre collections de Jean-Michel Ribeyrolles : Les Arcs-en-ciel Noirs, Les Miroirs d’Énigme, Les Gardiens de la Terre et la Collection Privée.",
                               "Collections", collections, PSWP_JS, PSWP_CSS))

# --------------------------------------------------------------------------- collection
def card(o, lightbox=True):
    detail = o["views"][1] if len(o["views"]) > 1 else None
    d = img(detail, alt(o, True), "detail") if detail else ""
    inner = f'{img(o["v1"], alt(o), "main")}{d}'
    if not lightbox:
        return f'''      <li class="card">
        <a href="{fiche(o)}">
          <div class="frame">{inner}</div>
          {cartel(o)}
        </a>
      </li>'''
    return f'''      <li class="card">
        {hd(o["v1"], f"Agrandir la photo de {o['ref']}", inner, "frame")}
        {cartel(o, link=True)}
        <div class="pswp-cap" hidden>{cartel(o)}<a class="link-arrow" href="{fiche(o)}">Voir la fiche</a></div>
      </li>'''

cards = "\n".join(card(M[r[0]]) for r in MIROIRS)
collection = f'''<section class="banner">
  {img("Bandeau-COLLECTION-MURALE.jpg", "", loading="eager", v=None)}
  <h1>Les Miroirs d’Énigme</h1>
</section>

<div class="wrap">{breadcrumb(("collections.html", "Collections"), (None, MIR))}</div>

<section class="section section--tight">
  <div class="wrap coll-intro">
    <p>Il y a quelque 3000 ans des hommes et des femmes entreprenaient des<br>
voyages périlleux pour se retrouver seuls avec les Miroirs d’Énigme.<br>
On ne sait dans quels cœurs a germé l’utopie poétique des Miroirs.</p>
    <p>On ne sait quelles mains ont donné corps et matière à ce qui pourrait<br>
n’être qu’un mirage de l’inconscient collectif&nbsp;?</p>
    <p>Nul ne sait qui a protégé les Miroirs, ni quel fut leur périple à travers<br>
le chaos des temps&nbsp;?</p>
    <p class="to-scale"><a class="link-arrow" href="echelle.html">Voir les Miroirs à l’échelle</a></p>
  </div>
</section>

<section class="section" style="padding-top:0" aria-labelledby="t-oeuvres">
  <div class="wrap">
    <h2 class="sr-only" id="t-oeuvres">Les 17 œuvres</h2>
    <ul class="grid" data-pswp-gallery>
{cards}
    </ul>
  </div>
</section>'''
write("collection.html", page("Les Miroirs d’Énigme · Jean-Michel Ribeyrolles",
                              "Les Miroirs d’Énigme : 17 sculptures murales rondes en bois brûlé et métal de Jean-Michel Ribeyrolles.",
                              "Collections", collection, PSWP_JS, PSWP_CSS))

# --------------------------------------------------------------------------- oeuvre
o = M["24FM0112"]
order = [r[0] for r in MIROIRS]
i = order.index("24FM0112")
prev, nxt = M[order[i - 1]], M[order[i + 1]]
slides = "\n".join(
    f'      <li>{hd(v, f"Agrandir la vue {k + 1} sur {len(o["views"])}", img(v, alt(o, k > 0), loading="eager" if k == 0 else "lazy", v="m"))}'
    f'<div class="pswp-cap" hidden>{cartel(o)}</div></li>'
    for k, v in enumerate(o["views"]))
related = "\n".join(card(M[r], lightbox=False) for r in ["25SA0108", "24FM0311", "25DM0301", "24FM0211", "24FM0111", "22TM0112"])
subject = urllib.parse.quote(f"Œuvre {o['ref']} – {COLL}")
oeuvre = f'''<div class="wrap">
  <div class="oeuvre">
    <div class="oeuvre-media">
      <ul class="gallery" aria-label="Photos de l’œuvre" data-pswp-gallery>
{slides}
      </ul>
      <p class="gallery-count" aria-live="polite"><span class="cur">1</span> / {len(o["views"])}</p>
    </div>

    <aside class="oeuvre-info">
      {breadcrumb(("collections.html", "Collections"), ("collection.html", COLL))}
      <p class="ref">{o["ref"]}</p>
      <h1>{COLL}</h1>
      <dl class="specs">
        <div><dt>Dimensions</dt><dd>{o["dims"]}<br><small style="color:var(--text-2)">diamètre × épaisseur</small></dd></div>
        <div><dt>Matériaux</dt><dd>{mats_txt(o)}</dd></div>
        <div><dt>Collection</dt><dd><a href="collection.html">{COLL}</a></dd></div>
      </dl>
      <div class="actions">
        <a class="btn" href="mailto:artelier-samonteil@orange.fr?subject={subject}">Me contacter à propos de cette œuvre</a>
        <a class="link-arrow" href="echelle.html#oeuvre-{o["ref"]}">Voir à l’échelle</a>
      </div>
      <nav class="prevnext" aria-label="Œuvres voisines">
        <a class="prev" href="#">{img(prev["v1"], "")}<span>Précédente<strong>{prev["ref"]}</strong></span></a>
        <a class="next" href="#">{img(nxt["v1"], "")}<span>Suivante<strong>{nxt["ref"]}</strong></span></a>
      </nav>
    </aside>
  </div>
</div>

<section class="section related" aria-labelledby="t-rel">
  <div class="wrap">
    <h2 id="t-rel">Dans la même collection</h2>
    <ul class="row">
{related}
    </ul>
  </div>
</section>'''
oeuvre_js = '''
<script>
  (function () {
    var g = document.querySelector('.gallery'), cur = document.querySelector('.gallery-count .cur');
    if (!g || !cur) return;
    g.addEventListener('scroll', function () {
      cur.textContent = Math.round(g.scrollLeft / g.clientWidth) + 1;
    }, { passive: true });
  })();
</script>''' + PSWP_JS
write("oeuvre.html", page(f"{o['ref']} · {COLL} · Jean-Michel Ribeyrolles",
                          f"{COLL}, {o['ref']} : sculpture murale en {mats_alt(o)}, {o['dims']}.",
                          "Collections", oeuvre, oeuvre_js, PSWP_CSS))

# --------------------------------------------------------------------------- échelle
def pw(o):
    return round(o["w"] / o["f"], 1)

def ph(o):
    w, h = size(o["v1"])
    return round(pw(o) * h / w, 1)

HAND = '''<svg class="hand" viewBox="0 0 10 19" fill="none" stroke="currentColor" stroke-width=".18" aria-hidden="true">
  <path d="M2.2 19 V12.2 L0.6 8.6 Q0.3 7.7 1.1 7.5 Q1.7 7.4 2.1 8.1 L2.9 9.6 V3.4 Q2.9 2.6 3.7 2.6 Q4.4 2.6 4.4 3.4 V8.4 V1.4 Q4.4 0.6 5.2 0.6 Q6 0.6 6 1.4 V8.4 V2 Q6 1.2 6.8 1.2 Q7.6 1.2 7.6 2 V8.6 V3.6 Q7.6 2.9 8.3 2.9 Q9 2.9 9 3.6 V12.4 Q9 14.4 8 15.6 V19"/>
</svg>'''

lineup_items = ['''      <li>
        ''' + HAND + '''
        <p class="cartel">Main · 19 cm</p>
      </li>''']
for ref in sorted(M, key=lambda r: (M[r]["maxd"], r)):
    m = M[ref]
    lineup_items.append(f'''      <li id="oeuvre-{ref}" style="--pw:{pw(m)}">
        {img(m["v1"], alt(m), "ph")}
        <p class="cartel"><span class="ref">{ref}</span><br>{m["dims"]}</p>
      </li>''')

PERSON = '''<svg class="person" style="--x:18" viewBox="0 0 50 175" fill="currentColor" fill-opacity=".55" aria-hidden="true">
  <circle cx="25" cy="10" r="10"/>
  <path d="M16 23 H34 V98 L33 175 H26.6 L25.6 104 H24.4 L23.4 175 H17 L16 98 Z"/>
  <path d="M14.8 23 V94 H11.2 Q9.6 94 9.6 92 V28 Q9.6 23 14 23 Z"/>
  <path d="M35.2 23 V94 H38.8 Q40.4 94 40.4 92 V28 Q40.4 23 36 23 Z"/>
</svg>'''

# x = bord gauche (cm), y = bas de la photo (cm, depuis le sol)
WALL = [
    (W["23DM0205"], 92, 0, True),
    (W["24FM0203"], 214, None, False),   # centrée à 150 cm
    (M["24FM0112"], 292, None, False),
    (M["24CM0604"], 327, 62, False),
    (M["25SA0108"], 420, 152, False),
    (M["22TM0112"], 420, 82, False),
]
wall_items = []
for w_o, x, y, floor in WALL:
    if y is None:
        y = round(150 - ph(w_o) / 2, 1)
    wall_items.append(f'''      <div class="item{" on-floor" if floor else ""}" id="oeuvre-{w_o["ref"]}" style="--x:{x};--y:{y};--pw:{pw(w_o)}">
        {img(w_o["v1"], alt(w_o))}
        {cartel(w_o, short=True)}
      </div>''')
legend = "\n".join("      " + cartel(w_o) for w_o, *_ in WALL)

echelle = f'''<section class="section" aria-labelledby="t-a">
  <div class="wrap">
    <h1 class="section-title" id="t-a">Les Miroirs d’Énigme à l’échelle</h1>
    <p class="scale-note">échelle approximative</p>
    <p class="scale-lead">Les 17 Miroirs à leur taille relative réelle, du plus petit au plus grand. Une main sert de repère.</p>
    <ul class="lineup">
{chr(10).join(lineup_items)}
    </ul>
  </div>
</section>

<section class="section" style="background:var(--bg);padding-top:0" aria-labelledby="t-b">
  <div class="wrap">
    <h2 class="section-title" id="t-b">Sur un mur</h2>
    <p class="scale-note">échelle approximative · silhouette de 1,75 m</p>
  </div>
  <div class="wall-scroll">
    <div class="wall" role="img" aria-label="Mur de 5,2 m sur 2,6 m : une silhouette de 1,75 m à côté de 23DM0205 (127 cm, posée au sol), de 24FM0203 (65 × 47 cm) et de quatre Miroirs d’Énigme accrochés autour de 1,50 m">
      {PERSON}
      <span class="cote" style="--x:72">1,75 m</span>
{chr(10).join(wall_items)}
    </div>
  </div>
  <div class="wrap wall-legend">
{legend}
  </div>
</section>'''
write("echelle.html", page("Les Miroirs d’Énigme à l’échelle · Jean-Michel Ribeyrolles",
                           "Les Miroirs d’Énigme de Jean-Michel Ribeyrolles à leur taille relative, et en situation sur un mur à côté d’une silhouette de 1,75 m.",
                           "Collections", echelle))

# --------------------------------------------------------------------------- portrait
# Texte de la page /jmir-portrait/ (relevé sur le site en ligne), avec les corrections de
# l'audit : « À côté », « Castelnau » (à confirmer), « dégradés orangés ».
portrait = f'''<section class="banner">
  {img("bandeau-portrait.jpg", "", loading="eager", v=None)}
  <h1>Messager du néolithique</h1>
</section>

<section class="section portrait" aria-label="Portrait de Jean-Michel Ribeyrolles">
  <div class="wrap">
    <article class="coll">
      <figure class="coll-media">{img("Portrait-1.jpg", "Jean-Michel Ribeyrolles à l’atelier, penché sur une pièce de bois", "landscape", v="m")}</figure>
      <div class="coll-text prose">
        <p>La sculpture et la musique ont fait irruption dans la vie de Jean-Michel Ribeyrolles il y a longtemps. Les deux s’accordent et se répondent en parfaite complicité. Quand le sculpteur expose ses œuvres, il arrive que le musicien improvise quelques notes à l’accordéon ou au violon.</p>
        <p class="quote">« Musique et sculpture c’est pour moi la même chose, la liberté d’improvisation, la créativité à l’état pur. »</p>
      </div>
    </article>
    <article class="coll">
      <figure class="coll-media">{img("Portrait-2.jpg", "Tronçonneuse entamant une planche de bois, à l’atelier", "landscape", v="m")}</figure>
      <div class="coll-text prose">
        <p>L’univers de <strong>JmiR</strong> est profondément inspiré par le monde néolithique, les représentations grand format des premières traces de l’homme, les dolmens, les statues menhirs ou les imposants cairns. Qui sont ces bâtisseurs, avec quelles techniques et connaissances ont-ils pu créer ces formes&nbsp;? C’est tout le champ libre laissé par le silence à ces questions qui est source d’inspiration, de dialogue, de recherches.</p>
        <p>Les sculptures de <strong>JmiR</strong> forment une constellation de points, comme un arc tendu qui nous relie à ces origines insondables, à la nature, à l’espace.</p>
        <p class="quote">« Quand j’attaque une pièce je me laisse guider par des impulsions. La sculpture se construit au fur et à mesure. Je cherche toujours à créer de la transparence, des effets de lumière en jouant avec le noir du bois brûlé, les dégradés orangés du Douglas, les reflets argentés du fer. »</p>
      </div>
    </article>
    <article class="coll">
      <figure class="coll-media">{img("Portrait-3.jpg", "Gouges et ciseaux à bois alignés sur un râtelier de l’atelier", "landscape", v="m")}</figure>
      <div class="coll-text prose">
        <p>À côté de son atelier qui plonge dans les vallons du Lot bordés par les tours du château de Saint-Laurent et la masse ocre de la forteresse de Castelnau, <strong>JmiR</strong> a aménagé une pièce claire et nue où il installe ses sculptures avec lesquelles il continue de dialoguer.</p>
        <p class="quote">« Cette pièce est un espace de vérité. Quand je passe devant les sculptures, quand je les regarde, il doit se passer quelque chose, des émotions, des sensations, comme un courant magnétique. Si je ne ressens rien, je les détruis. La sculpture est terminée quand elle trouve sa place, son équilibre dans l’espace. »</p>
        <p>Dans son musée imaginaire sur le causse du Ségala, <strong>JmiR</strong> rêve au jour naissant qui dévoile des sculptures où vibrent les matières ancestrales de l’humanité, bois, fer, pierre. Dans l’ombre profonde d’un dolmen, un violoniste improvise…</p>
        <p class="cartel">Texte de Patrick Churlet</p>
      </div>
    </article>
  </div>
</section>'''
write("portrait.html", page("Portrait · Jean-Michel Ribeyrolles",
                            "Jean-Michel Ribeyrolles, sculpteur sur bois brûlé et musicien, inspiré par le néolithique : portrait de l’artiste à l’ART’elier Samonteil.",
                            "Portrait", portrait))
