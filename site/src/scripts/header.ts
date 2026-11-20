// Menu mobile plein écran + header réduit à 64 px une fois la page défilée,
// masqué en descendant, visible en remontant (comportement des maquettes).

const header = document.querySelector<HTMLElement>('.site-header');
const nav = document.getElementById('menu');
const openBtn = document.querySelector<HTMLButtonElement>('.bar > .menu-toggle');
const closeBtn = nav?.querySelector<HTMLButtonElement>('.menu-close');

if (header && nav && openBtn && closeBtn) {
  const setOpen = (open: boolean): void => {
    nav.classList.toggle('is-open', open);
    openBtn.setAttribute('aria-expanded', String(open));
    document.documentElement.style.overflow = open ? 'hidden' : '';
    (open ? closeBtn : openBtn).focus();
  };

  openBtn.addEventListener('click', () => setOpen(true));
  closeBtn.addEventListener('click', () => setOpen(false));
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && nav.classList.contains('is-open')) setOpen(false);
  });

  let last = window.scrollY;
  let ticking = false;
  const update = (): void => {
    const y = window.scrollY;
    const dy = y - last;
    header.classList.toggle('is-scrolled', y > 8);
    if (Math.abs(dy) > 4) {
      const hide =
        dy > 0 && y > 160 && !nav.classList.contains('is-open') && !header.contains(document.activeElement);
      header.classList.toggle('is-hidden', hide);
      last = y;
    }
    ticking = false;
  };
  window.addEventListener(
    'scroll',
    () => {
      if (!ticking) {
        ticking = true;
        requestAnimationFrame(update);
      }
    },
    { passive: true },
  );
  update();
}
