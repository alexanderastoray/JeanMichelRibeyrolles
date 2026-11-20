// Lightbox PhotoSwipe (npm, MIT). Chargée uniquement par les pages qui incluent <Lightbox />.
// Galeries : éléments [data-pswp-gallery] ; diapositives : liens a[data-pswp-src].
// Légende : contenu du .pswp-cap (caché) le plus proche du lien.
import PhotoSwipeLightbox from 'photoswipe/lightbox';
import 'photoswipe/style.css';

const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

const lightbox = new PhotoSwipeLightbox({
  gallery: '[data-pswp-gallery]',
  children: 'a[data-pswp-src]',
  pswpModule: () => import('photoswipe'),
  bgOpacity: 1,
  padding: { top: 56, bottom: 104, left: 16, right: 16 },
  imageClickAction: 'zoom', // clic : zoom / dézoom
  tapAction: 'toggle-controls', // mobile : tap = interface, pincement et double tap = zoom
  doubleTapAction: 'zoom',
  maxZoomLevel: 4,
  showHideAnimationType: reduceMotion ? 'none' : 'zoom',
  closeTitle: 'Fermer (Échap)',
  zoomTitle: 'Zoomer',
  arrowPrevTitle: 'Précédente',
  arrowNextTitle: 'Suivante',
  errorMsg: 'L’image n’a pas pu être chargée.',
  indexIndicatorSep: ' / ',
});

lightbox.on('uiRegister', () => {
  lightbox.pswp?.ui?.registerElement({
    name: 'cartel',
    order: 9,
    isButton: false,
    appendTo: 'root',
    html: '',
    onInit: (el, pswp) => {
      pswp.on('change', () => {
        const lien = pswp.currSlide?.data.element;
        const cap = lien?.closest('li')?.querySelector('.pswp-cap');
        el.innerHTML = cap ? cap.innerHTML : '';
      });
    },
  });
});

lightbox.init();
