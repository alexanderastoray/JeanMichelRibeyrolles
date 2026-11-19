async (page) => {
  const fn = async () => {
    for (let y = 0; y < document.body.scrollHeight; y += 700) { window.scrollTo(0, y); await new Promise(r => setTimeout(r, 150)); }
    window.scrollTo(0, 0); await document.fonts.ready;
    const P = ['font-family','font-size','font-weight','line-height','letter-spacing','color','background-color','text-transform','font-style','text-decoration-line','padding','margin','border-radius','border'];
    const st = el => { if (!el) return null; const c = getComputedStyle(el); const o = {}; P.forEach(p => o[p] = c.getPropertyValue(p)); return o; };
    const desc = el => el ? (el.tagName.toLowerCase() + (el.id ? '#' + el.id : '') + (el.className && typeof el.className === 'string' ? '.' + el.className.trim().split(/\s+/).slice(0, 3).join('.') : '')) : null;
    const txt = el => el ? el.textContent.replace(/\s+/g, ' ').trim().slice(0, 60) : null;
    const vis = el => !!(el.offsetWidth || el.offsetHeight);
    const all = (sel) => [...document.querySelectorAll(sel)].filter(vis);
    const inMain = el => !el.closest('#site-header, footer, [data-elementor-type="footer"], .elementor-location-footer');
    // group distinct styles for a selector
    const groups = (els, max = 8) => { const m = new Map(); for (const el of els) { const s = st(el); const k = JSON.stringify(s); if (!m.has(k)) m.set(k, { count: 0, style: s, examples: [] }); const g = m.get(k); g.count++; if (g.examples.length < 3) g.examples.push(desc(el) + ' « ' + txt(el) + ' »'); } return [...m.values()].sort((a, b) => b.count - a.count).slice(0, max); };
    const header = document.querySelector('#site-header');
    const footer = document.querySelector('[data-elementor-type="footer"], footer, .elementor-location-footer');
    const menuLinks = all('#site-navigation a, #site-header .main-menu a, #site-header nav a');
    const btns = all('.elementor-button, button, .button, input[type=submit], a.btn, [class*="button"]').filter(e => e.tagName !== 'DIV' || e.classList.contains('elementor-button'));
    // CSS vars
    const vars = {};
    const scan = rules => { for (const r of rules) { try { if (r.style) for (const p of r.style) if (p.startsWith('--e-global') || p.startsWith('--ocean') ) vars[p] = vars[p] || []; if (r.cssRules) scan(r.cssRules); } catch (e) {} } };
    for (const s of document.styleSheets) { try { scan(s.cssRules); } catch (e) {} }
    const rootCs = getComputedStyle(document.querySelector('.elementor-kit-' + (document.body.className.match(/elementor-kit-(\d+)/) || [])[1]) || document.body);
    const varVals = {}; Object.keys(vars).forEach(k => varVals[k] = rootCs.getPropertyValue(k).trim());
    // fonts
    const fontFaces = [...document.fonts].map(f => ({ family: f.family, weight: f.weight, style: f.style, status: f.status }));
    const fontFaceRules = []; const sheets = [];
    for (const s of document.styleSheets) { sheets.push(s.href); try { for (const r of s.cssRules) if (r.constructor.name === 'CSSFontFaceRule') fontFaceRules.push({ family: r.style.getPropertyValue('font-family'), weight: r.style.getPropertyValue('font-weight'), src: r.style.getPropertyValue('src').slice(0, 200), sheet: s.href }); } catch (e) { fontFaceRules.push({ blocked: s.href }); } }
    const fontRes = performance.getEntriesByType('resource').map(r => r.name).filter(n => /fonts\.(googleapis|gstatic)|\.woff2?|\.ttf|\.otf/.test(n));
    // colors census
    const colorCount = {}; const bgCount = {};
    for (const el of document.querySelectorAll('body *')) { if (!vis(el)) continue; const c = getComputedStyle(el); if (el.childNodes && [...el.childNodes].some(n => n.nodeType === 3 && n.textContent.trim())) colorCount[c.color] = (colorCount[c.color] || 0) + 1; if (c.backgroundColor !== 'rgba(0, 0, 0, 0)') bgCount[c.backgroundColor] = (bgCount[c.backgroundColor] || 0) + 1; }
    // spacing: sections padding / gaps
    const secs = [...document.querySelectorAll('[data-elementor-type="wp-page"] > .elementor-element, [data-elementor-type="wp-page"] > section, [data-elementor-type="wp-page"] .e-con.e-parent')].filter(vis).slice(0, 20).map(s => { const c = getComputedStyle(s); return { el: desc(s), padding: c.padding, margin: c.margin, gap: c.gap, maxWidth: c.maxWidth, width: Math.round(s.getBoundingClientRect().width), height: Math.round(s.getBoundingClientRect().height), bg: c.backgroundColor, bgImg: c.backgroundImage.slice(0, 120) }; });
    const containers = [...new Set(all('.e-con-inner, .elementor-container, #main #content-wrap, .container').map(e => getComputedStyle(e).maxWidth + ' / ' + desc(e).split('.').slice(0, 2).join('.')))].slice(0, 10);
    return {
      url: location.href, viewport: [innerWidth, innerHeight], bodyClass: document.body.className,
      body: st(document.body), html: st(document.documentElement),
      header: { el: desc(header), style: st(header), height: header ? Math.round(header.getBoundingClientRect().height) : null, inner: groups(header ? [...header.querySelectorAll('*')].filter(e => vis(e) && getComputedStyle(e).backgroundColor !== 'rgba(0, 0, 0, 0)') : [], 4) },
      menu: groups(menuLinks), menuActive: groups(all('#site-header .current-menu-item > a, #site-header .current_page_item > a')),
      h1: groups(all('h1')), h2: groups(all('h2')), h3: groups(all('h3')), h4: groups(all('h4')), h5: groups(all('h5')), h6: groups(all('h6')),
      p: groups(all('p').filter(inMain)), links: groups(all('a').filter(e => inMain(e) && !e.querySelector('img') && txt(e))),
      buttons: groups(btns),
      footer: { el: desc(footer), style: st(footer), bgChain: footer ? [...footer.querySelectorAll('*')].filter(e => vis(e) && getComputedStyle(e).backgroundColor !== 'rgba(0, 0, 0, 0)').slice(0, 5).map(e => desc(e) + ' ' + getComputedStyle(e).backgroundColor) : [], text: groups(footer ? [...footer.querySelectorAll('p, a, h1, h2, h3, h4, h5, h6, li, span')].filter(e => vis(e) && txt(e)) : [], 8) },
      cssVars: varVals, fontFaces, fontFaceRules, fontResources: fontRes, stylesheets: sheets,
      colors: Object.entries(colorCount).sort((a, b) => b[1] - a[1]), backgrounds: Object.entries(bgCount).sort((a, b) => b[1] - a[1]),
      sections: secs, containers,
    };
  };
  await page.context().addInitScript({ content: `window.__design = ${fn.toString()};` });
  return 'installed';
}
