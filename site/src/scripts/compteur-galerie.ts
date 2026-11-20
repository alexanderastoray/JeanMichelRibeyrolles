// Mobile : galerie en carrousel horizontal ; met à jour « 1 / N » au défilement.
const galerie = document.querySelector<HTMLElement>('.gallery');
const courant = document.querySelector<HTMLElement>('.gallery-count .cur');

if (galerie && courant) {
  galerie.addEventListener(
    'scroll',
    () => {
      courant.textContent = String(Math.round(galerie.scrollLeft / galerie.clientWidth) + 1);
    },
    { passive: true },
  );
}
