async (page) => {
  const fn = async () => {
    for (let y = 0; y < document.body.scrollHeight; y += 600) { window.scrollTo(0, y); await new Promise(r => setTimeout(r, 200)); }
    window.scrollTo(0, 0); await new Promise(r => setTimeout(r, 1500));
    const txt = e => e ? e.textContent.replace(/\s+/g, ' ').trim() : '';
    const vis = e => !!(e.offsetWidth || e.offsetHeight);
    const zone = el => el.closest('#site-header') ? 'header' : el.closest('footer, [data-elementor-type="footer"], .elementor-location-footer, #footer') ? 'footer' : el.closest('#mobile-fullscreen, #mobile-dropdown') ? 'mobile-menu' : 'main';
    const main = document.querySelector('[data-elementor-type="wp-page"]') || document.querySelector('#main, main') || document.body;
    let tops = [...main.querySelectorAll(':scope > .elementor-element, :scope > .elementor-section-wrap > .elementor-element, :scope > section, :scope > .e-con')];
    if (!tops.length) tops = [...main.children];
    const nav = performance.getEntriesByType('navigation')[0];
    const res = performance.getEntriesByType('resource').filter(r => r.responseStatus >= 400).map(r => [r.responseStatus, r.name]);
    return {
      url: location.href, status: nav ? nav.responseStatus : null, title: document.title,
      metaDescription: document.querySelector('meta[name=description]')?.content ?? null,
      robots: document.querySelector('meta[name=robots]')?.content ?? null,
      canonical: document.querySelector('link[rel=canonical]')?.href ?? null,
      ogTitle: document.querySelector('meta[property="og:title"]')?.content ?? null,
      ogDescription: document.querySelector('meta[property="og:description"]')?.content ?? null,
      lang: document.documentElement.lang,
      h1: [...document.querySelectorAll('h1')].map(h => ({ text: txt(h), visible: vis(h), zone: zone(h) })),
      h2: [...document.querySelectorAll('h2')].map(h => ({ text: txt(h), visible: vis(h), zone: zone(h) })),
      sections: tops.map((s, i) => ({ index: i + 1, visible: vis(s),
        headings: [...s.querySelectorAll('h1,h2,h3,h4,h5,h6')].map(h => h.tagName + ': ' + txt(h)).filter(h => h.length > 4),
        widgets: [...new Set([...s.querySelectorAll('[data-widget_type]')].map(w => w.dataset.widget_type.replace(/\.default$/, '')))],
        images: s.querySelectorAll('img').length, text: txt(s).slice(0, 1200) })),
      images: [...document.querySelectorAll('img')].map(img => { const src = img.currentSrc || img.getAttribute('data-src') || img.src; const a = img.closest('a');
        return { zone: zone(img), file: (src || '').split('/').pop().split('?')[0], src, linkHref: a ? a.href : null,
          natural: [img.naturalWidth, img.naturalHeight], attr: [img.getAttribute('width'), img.getAttribute('height')],
          hasAlt: img.hasAttribute('alt'), alt: img.getAttribute('alt'), title: img.getAttribute('title'),
          caption: txt(img.closest('figure')?.querySelector('figcaption')), loaded: img.complete && img.naturalWidth > 0, visible: vis(img) }; }),
      bgImages: [...new Set([...document.querySelectorAll('.elementor-element, [style*="background"]')].map(e => getComputedStyle(e).backgroundImage).filter(b => b && b.includes('url(')))],
      links: [...document.querySelectorAll('a')].map(a => ({ zone: zone(a), text: txt(a) || a.getAttribute('aria-label') || a.querySelector('img')?.getAttribute('alt') || '', href: a.getAttribute('href'), abs: a.href, target: a.target || null })),
      forms: [...document.querySelectorAll('form')].map(f => ({ id: f.id, action: f.getAttribute('action'), fields: [...f.querySelectorAll('input,textarea,select')].filter(i => i.type !== 'hidden').map(i => ({ type: i.type || i.tagName.toLowerCase(), name: i.name, label: i.labels?.[0] ? txt(i.labels[0]) : null, placeholder: i.placeholder || null, required: i.required })) })),
      iframes: [...document.querySelectorAll('iframe')].map(f => f.src),
      badResources: res,
      bodyText: txt(main).slice(0, 15000),
      footerText: txt(document.querySelector('[data-elementor-type="footer"], footer, .elementor-location-footer')),
    };
  };
  await page.context().addInitScript({ content: `window.__audit = ${fn.toString()};` });
  return 'installed';
}
