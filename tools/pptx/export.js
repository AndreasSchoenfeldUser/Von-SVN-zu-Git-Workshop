// Export eines Slide-Decks nach PowerPoint (.pptx) mit editierbaren Formen und Texten.
//
// Aufruf (aus tools/pptx):  node export.js tag1   bzw.   npm run build
//
// Ablauf: Chrome rendert die erzeugten HTML-Slides (deck.json, deck.css, slides/*.html)
// mit den Web-Fonts. Aus dem berechneten Layout entstehen native PowerPoint-Elemente:
// Flächen, Texte mit Formatierung, Listen, Tabellen, Linien und Kreise der Commit-Graphen,
// Pfeile, Icons und das Logo. Überschriften liegen in Titel-Platzhaltern, Fußzeile und
// Seitenzahl im Folienlayout, Sprechernotizen in den Notizen.
//
// Optional: CHROME_CHANNEL (Standard "chrome"), CHROMIUM_PATH.

const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');
const PptxGenJS = require('pptxgenjs');

const REPO = path.resolve(__dirname, '..', '..');
const deckKey = process.argv[2];
if (!deckKey) { console.error('Aufruf: node export.js <tag1|tag2> [ausgabe.pptx]'); process.exit(1); }
const DECK_DIR = path.join(REPO, 'slides', 'decks', deckKey, 'project');
const OUT = process.argv[3] || path.join(REPO, 'slides', 'pptx', `${deckKey}.pptx`);
const LOGO_FILE = path.join(REPO, 'slides', 'assets', 'comquent-academy-logo.png');
const ICON_DIR = path.join(__dirname, 'node_modules', '@phosphor-icons', 'core', 'assets', 'regular');
const ICON_ALIAS = { Settings: 'gear' };

const PX = 144;                       // 1920 px = 13,333 in
const inch = v => +(v / PX).toFixed(4);
const pt = v => +(v * 0.5).toFixed(2); // 1 px = 0,5 pt

const THEME = {
  name: 'Comquent Academy',
  headFontFace: 'Space Grotesk',
  bodyFontFace: 'Inter',
  colors: {
    dk1: '10345A', lt1: 'FFFFFF', dk2: '4A5A6E', lt2: 'F7F4EF',
    accent1: 'EC3C5C', accent2: 'B81E3E', accent3: '1B4672', accent4: 'FBE4E9',
    accent5: 'DCD6CC', accent6: '3E6A97', hlink: '1B4672', folHlink: 'B81E3E',
  },
};

// Seite wie in tools/preview/pv.js aufbauen, ergänzt um die Web-Fonts aus deck.json.
const SHIM = `* { margin: 0 } body { font: 32px/1.2 sans-serif } body > section { width: 1920px !important; height: 1080px !important; overflow: hidden !important; box-sizing: border-box !important; position: relative; isolation: isolate } section[hidden], aside, noscript { display: none !important } h1 { font-size: 96px; font-weight: 600 } h2 { font-size: 64px; font-weight: 600 } h3 { font-size: 44px; font-weight: 600 } p, li, h1, h2, h3, td, th { overflow-wrap: break-word; text-wrap: pretty } table { width: 100%; border-collapse: separate; border-spacing: 0; border: solid #0003; border-width: 2px 0 0 2px } th, td { padding: .35em .6em; text-align: left; border: solid #0003; border-width: 0 2px 2px 0 } x-shape, x-icon, x-embed { display: block } .rise{animation:none!important} .band,.cpanel{z-index:-1}`;

// Läuft im Browser: zerlegt jede Slide in zeichenbare Elemente mit absoluten Koordinaten.
function extract() {
  const INLINE = new Set(['SPAN', 'B', 'STRONG', 'I', 'EM', 'A', 'BR', 'CODE', 'SMALL', 'SUB', 'SUP']);
  const parseColor = s => {
    const m = s && s.match(/rgba?\(([^)]+)\)/);
    if (!m) return null;
    const p = m[1].split(/[ ,/]+/).filter(Boolean).map(Number);
    return { r: p[0], g: p[1], b: p[2], a: p.length > 3 ? p[3] : 1 };
  };
  const hex = (c, under) => {
    if (!c) return null;
    let { r, g, b, a } = c;
    if (a < 1) { const u = under || { r: 247, g: 244, b: 239 }; r = r * a + u.r * (1 - a); g = g * a + u.g * (1 - a); b = b * a + u.b * (1 - a); }
    return [r, g, b].map(v => Math.round(v).toString(16).padStart(2, '0')).join('').toUpperCase();
  };
  const visible = c => c && c.a > 0.01;
  const family = f => f.split(',')[0].replace(/["']/g, '').trim();

  const out = [];
  for (const sec of document.querySelectorAll('body > section')) {
    const S = sec.getBoundingClientRect();
    const box = el => { const r = el.getBoundingClientRect(); return { x: r.left - S.left, y: r.top - S.top, w: r.width, h: r.height }; };
    const secBg = parseColor(getComputedStyle(sec).backgroundColor);
    const items = [];

    const runStyle = (el) => {
      const cs = getComputedStyle(el);
      return {
        color: hex(parseColor(cs.color)), bold: +cs.fontWeight >= 600, italic: cs.fontStyle === 'italic',
        font: family(cs.fontFamily), size: parseFloat(cs.fontSize),
        spacing: cs.letterSpacing === 'normal' ? 0 : parseFloat(cs.letterSpacing),
        upper: cs.textTransform === 'uppercase',
      };
    };
    // Inline-Inhalt eines Blocks als Liste von Absätzen aus Runs.
    const runsOf = (el) => {
      const paras = [[]];
      const pre = /pre|nowrap/.test(getComputedStyle(el).whiteSpace) && getComputedStyle(el).whiteSpace !== 'nowrap';
      const walk = (node, style) => {
        for (const n of node.childNodes) {
          if (n.nodeType === 3) {
            let t = n.textContent;
            if (!pre) t = t.replace(/[ \t\n\r]+/g, ' ');
            if (style.upper) t = t.toUpperCase();
            if (t) paras[paras.length - 1].push({ text: t, ...style });
          } else if (n.nodeType === 1) {
            if (n.tagName === 'BR') paras.push([]);
            else if (getComputedStyle(n).display !== 'none') walk(n, runStyle(n));
          }
        }
      };
      walk(el, runStyle(el));
      for (const p of paras) {   // Leerraum an Absatzgrenzen entfernen wie im Browser
        while (p.length && !p[0].text.replace(/^ +/, '')) p.shift();
        if (p.length) p[0].text = p[0].text.replace(/^ +/, '');
        while (p.length && !p[p.length - 1].text.replace(/ +$/, '')) p.pop();
        if (p.length) p[p.length - 1].text = p[p.length - 1].text.replace(/ +$/, '');
      }
      return paras;
    };
    const isTextBlock = el => {
      if (!el.textContent.trim()) return false;
      for (const c of el.children) if (!INLINE.has(c.tagName)) return false;
      return true;
    };
    const contentBox = (el) => {
      const b = box(el), cs = getComputedStyle(el);
      const l = parseFloat(cs.paddingLeft) + parseFloat(cs.borderLeftWidth), r = parseFloat(cs.paddingRight) + parseFloat(cs.borderRightWidth);
      const t = parseFloat(cs.paddingTop) + parseFloat(cs.borderTopWidth), bo = parseFloat(cs.paddingBottom) + parseFloat(cs.borderBottomWidth);
      return { x: b.x + l, y: b.y + t, w: b.w - l - r, h: b.h - t - bo };
    };
    const textProps = (el) => {
      const cs = getComputedStyle(el);
      return {
        align: cs.textAlign === 'center' ? 'center' : cs.textAlign === 'right' || cs.textAlign === 'end' ? 'right' : 'left',
        lineHeight: cs.lineHeight === 'normal' ? null : parseFloat(cs.lineHeight),
        nowrap: cs.whiteSpace === 'nowrap',
      };
    };
    const bgUnder = (el) => {
      for (let e = el; e && e !== document.body; e = e.parentElement) {
        const c = parseColor(getComputedStyle(e).backgroundColor);
        if (visible(c)) return c;
      }
      return secBg;
    };

    const drawBox = (el) => {
      const cs = getComputedStyle(el);
      if (el === sec) return;
      const b = box(el);
      if (b.w < 0.5 || b.h < 0.5) return;
      const bg = parseColor(cs.backgroundColor);
      const bw = ['Top', 'Right', 'Bottom', 'Left'].map(s => cs[`border${s}Style`] === 'none' ? 0 : parseFloat(cs[`border${s}Width`]));
      const uniform = bw.every(v => v === bw[0]) && bw[0] > 0;
      const radius = parseFloat(cs.borderTopLeftRadius) || 0;
      if (visible(bg) || uniform) {
        items.push({
          type: 'rect', ...b, radius,
          fill: visible(bg) ? hex(bg, bgUnder(el.parentElement)) : null,
          line: uniform ? { w: bw[0], color: hex(parseColor(cs.borderTopColor), bgUnder(el)), dash: cs.borderTopStyle === 'dashed' } : null,
        });
      }
      if (!uniform && bw[3] > 0) items.push({ type: 'rect', x: b.x, y: b.y, w: bw[3], h: b.h, radius: 0, fill: hex(parseColor(cs.borderLeftColor)), line: null });
    };

    const visit = (el) => {
      const cs = getComputedStyle(el);
      if (cs.display === 'none' || el.tagName === 'ASIDE') return;
      const tag = el.tagName;
      if (tag === 'svg') {
        const o = box(el);
        for (const n of el.children) {
          const a = k => parseFloat(n.getAttribute(k) || 0);
          if (n.tagName === 'line') items.push({ type: 'line', x1: o.x + a('x1'), y1: o.y + a('y1'), x2: o.x + a('x2'), y2: o.y + a('y2'), color: (n.getAttribute('stroke') || '#000').slice(1).toUpperCase(), w: a('stroke-width') || 1, dash: !!n.getAttribute('stroke-dasharray') });
          else if (n.tagName === 'circle') {
            const fill = n.getAttribute('fill'), stroke = n.getAttribute('stroke');
            items.push({ type: 'oval', x: o.x + a('cx') - a('r'), y: o.y + a('cy') - a('r'), w: 2 * a('r'), h: 2 * a('r'), fill: fill && fill !== 'none' ? fill.slice(1).toUpperCase() : null, line: stroke ? { w: a('stroke-width') || 1, color: stroke.slice(1).toUpperCase() } : null });
          }
        }
        return;
      }
      if (tag === 'IMG') {
        const b = box(el), nw = el.naturalWidth || 1, nh = el.naturalHeight || 1;
        let w = b.w, h = b.h;
        if (cs.objectFit === 'contain') { const s = Math.min(b.w / nw, b.h / nh); w = nw * s; h = nh * s; }
        items.push({ type: 'img', cls: el.className, x: b.x + (b.w - w) / 2, y: b.y + (b.h - h) / 2, w, h, alt: el.alt });
        return;
      }
      if (tag === 'X-ICON') { items.push({ type: 'icon', name: el.getAttribute('name'), color: hex(parseColor(cs.color)), ...box(el) }); return; }
      if (tag === 'X-SHAPE') { items.push({ type: 'shape', kind: el.getAttribute('kind'), fill: hex(parseColor(cs.backgroundColor)), ...box(el) }); return; }

      drawBox(el);

      if (tag === 'TABLE') {
        const rows = [...el.rows].map(tr => [...tr.cells].map(td => {
          const c = getComputedStyle(td);
          return {
            paras: runsOf(td), fill: hex(bgUnder(td)),
            pad: [c.paddingTop, c.paddingRight, c.paddingBottom, c.paddingLeft].map(parseFloat),
            border: { top: parseFloat(c.borderTopWidth), right: parseFloat(c.borderRightWidth), bottom: parseFloat(c.borderBottomWidth), left: parseFloat(c.borderLeftWidth), color: hex(parseColor(c.borderRightColor), bgUnder(td)) },
            ...textProps(td),
          };
        }));
        const tc = getComputedStyle(el);
        items.push({
          type: 'table', ...box(el), rows,
          colW: [...el.rows[0].cells].map(td => td.getBoundingClientRect().width),
          rowH: [...el.rows].map(tr => tr.getBoundingClientRect().height),
          outer: { top: parseFloat(tc.borderTopWidth), left: parseFloat(tc.borderLeftWidth), color: hex(parseColor(tc.borderTopColor), secBg) },
        });
        return;
      }
      if (tag === 'UL' || tag === 'OL') {
        const lis = [...el.children].filter(c => c.tagName === 'LI');
        items.push({
          type: 'list', ordered: tag === 'OL', ...box(el), indent: parseFloat(cs.paddingLeft),
          paras: lis.map(li => runsOf(li).flat()), ...textProps(el),
        });
        return;
      }
      if (el.classList.contains('pageno')) { items.push({ type: 'pageno', ...box(el), ...runStyle(el) }); return; }
      if (isTextBlock(el)) {
        items.push({ type: 'text', tag, cls: el.className, ...contentBox(el), paras: runsOf(el), ...textProps(el) });
        return;
      }
      for (const c of el.children) visit(c);
    };

    for (const c of sec.children) visit(c);
    const aside = sec.querySelector(':scope > aside');
    out.push({ id: sec.id, cls: sec.className.trim().split(/\s+/)[0], bg: hex(secBg), notes: aside ? aside.textContent.trim() : '', items });
  }
  return out;
}

async function renderIcons(browser, names) {
  const page = await browser.newPage({ viewport: { width: 512, height: 512 } });
  const icons = {};
  for (const key of names) {
    const [name, color] = key.split('|');
    const file = (ICON_ALIAS[name] || name.replace(/([a-z0-9])([A-Z])/g, '$1-$2').toLowerCase()) + '.svg';
    const p = path.join(ICON_DIR, file);
    if (!fs.existsSync(p)) { console.warn(`Icon nicht gefunden: ${name}`); continue; }
    const svg = fs.readFileSync(p, 'utf8').replace('<svg ', `<svg width="512" height="512" style="color:#${color};display:block" `);
    await page.setContent(`<html><body style="margin:0;background:transparent">${svg}</body></html>`);
    const buf = await page.locator('svg').screenshot({ omitBackground: true });
    icons[key] = 'image/png;base64,' + buf.toString('base64');
  }
  await page.close();
  return icons;
}

async function load() {
  const deck = JSON.parse(fs.readFileSync(path.join(DECK_DIR, 'deck.json'), 'utf8'));
  const body = deck.order.map(id => fs.readFileSync(path.join(DECK_DIR, 'slides', id + '.html'), 'utf8')).join('\n');
  const fonts = Object.values(deck.faces || {}).map(f => `<link rel="stylesheet" href="${f.href}">`).join('');
  const html = `<!doctype html><html><head><meta charset="utf-8"><style>${SHIM}</style>${fonts}<link rel="stylesheet" href="/project/deck.css"></head><body>${body}</body></html>`;

  const browser = await chromium.launch(process.env.CHROMIUM_PATH ? { executablePath: process.env.CHROMIUM_PATH } : { channel: process.env.CHROME_CHANNEL || 'chrome' });
  const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
  await page.route('**/*', r => {
    const u = new URL(r.request().url());
    if (u.hostname === 'deck.local') {
      if (u.pathname === '/') return r.fulfill({ body: html, contentType: 'text/html' });
      if (u.pathname.startsWith('/project/')) return r.fulfill({ path: path.join(DECK_DIR, u.pathname.slice('/project/'.length)) });
      if (u.pathname.startsWith('/_blob/')) return r.fulfill({ path: LOGO_FILE, contentType: 'image/png' });
      return r.abort();
    }
    if (u.hostname === 'fonts.googleapis.com' || u.hostname === 'fonts.gstatic.com') return r.continue();
    return r.abort();
  });
  await page.goto('http://deck.local/', { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  const missing = await page.evaluate(() => ['Space Grotesk', 'Inter', 'JetBrains Mono'].filter(f => !document.fonts.check(`700 32px "${f}"`)));
  if (missing.length) console.warn('Web-Fonts nicht geladen, Layout weicht ab:', missing.join(', '));
  const slides = await page.evaluate(extract);
  const iconKeys = [...new Set(slides.flatMap(s => s.items.filter(i => i.type === 'icon').map(i => `${i.name}|${i.color}`)))];
  const icons = await renderIcons(browser, iconKeys);
  await browser.close();
  return { deck, slides, icons };
}

// ---------- PowerPoint aufbauen ----------

function scheme(pres, hex) {
  if (!hex) return hex;
  const C = pres.SchemeColor;
  const map = { [THEME.colors.dk1]: C.text1, [THEME.colors.lt2]: C.background2, [THEME.colors.dk2]: C.text2,
    [THEME.colors.accent1]: C.accent1, [THEME.colors.accent2]: C.accent2, [THEME.colors.accent3]: C.accent3,
    [THEME.colors.accent4]: C.accent4, [THEME.colors.accent5]: C.accent5, [THEME.colors.accent6]: C.accent6 };
  return map[hex] || hex;
}

// Space Grotesk und Inter bleiben erhalten; fehlen sie, setzt PowerPoint Calibri ein.
// Für Code ist ein proportionaler Ersatz unbrauchbar, daher Consolas (in Office enthalten).
const CODE_FONT = process.env.PPTX_CODE_FONT || 'Consolas';
const FONT_FACE = f => (f === 'JetBrains Mono' ? CODE_FONT : f);

function runOpts(pres, r) {
  const o = { fontFace: FONT_FACE(r.font), fontSize: pt(r.size), color: scheme(pres, r.color), bold: r.bold };
  if (r.italic) o.italic = true;
  if (r.spacing) o.charSpacing = pt(r.spacing);
  return o;
}

function paraRuns(pres, paras, extra = {}) {
  const arr = [];
  paras.forEach((p, i) => {
    if (!p.length) p = [{ text: '', size: 24, font: 'Inter', color: '10345A' }];
    p.forEach((r, j) => {
      const o = { ...runOpts(pres, r), ...extra };
      if (j === p.length - 1 && i < paras.length - 1) o.breakLine = true;
      arr.push({ text: r.text, options: o });
    });
  });
  return arr;
}

// Etwas Breitenreserve, damit PowerPoint bei abweichender Laufweite nicht früher umbricht.
function slack(it) {
  const extra = Math.max(8, it.w * 0.03);
  let x = it.x, w = it.w + extra;
  if (it.align === 'center') x -= extra / 2;
  else if (it.align === 'right') x -= extra;
  x = Math.max(0, x); w = Math.min(w, 1920 - x);
  return { x, w };
}

function textBoxOpts(it) {
  const { x, w } = it.nowrap ? { x: it.x, w: it.w } : slack(it);
  const o = { x: inch(x), y: inch(it.y), w: inch(w), h: inch(Math.max(it.h, 1)), margin: 0, valign: 'top', align: it.align, isTextBox: true, fit: 'none' };
  if (it.nowrap) o.wrap = false;
  if (it.lineHeight) o.lineSpacing = pt(it.lineHeight);
  return o;
}

function addItem(pres, slide, it, ctx) {
  switch (it.type) {
    case 'rect': {
      const rounded = it.radius > 0.5;
      const o = { x: inch(it.x), y: inch(it.y), w: inch(it.w), h: inch(it.h) };
      o.fill = it.fill ? { color: scheme(pres, it.fill) } : { type: 'none' };
      o.line = it.line ? { color: scheme(pres, it.line.color), width: pt(it.line.w), dashType: it.line.dash ? 'dash' : 'solid' } : { type: 'none' };
      if (rounded) o.rectRadius = inch(Math.min(it.radius, it.w / 2, it.h / 2));
      slide.addShape(rounded ? pres.ShapeType.roundRect : pres.ShapeType.rect, o);
      break;
    }
    case 'oval':
      slide.addShape(pres.ShapeType.ellipse, {
        x: inch(it.x), y: inch(it.y), w: inch(it.w), h: inch(it.h),
        fill: it.fill ? { color: scheme(pres, it.fill) } : { type: 'none' },
        line: it.line ? { color: scheme(pres, it.line.color), width: pt(it.line.w) } : { type: 'none' },
      });
      break;
    case 'line': {
      const dx = it.x2 - it.x1, dy = it.y2 - it.y1;
      slide.addShape(pres.ShapeType.line, {
        x: inch(Math.min(it.x1, it.x2)), y: inch(Math.min(it.y1, it.y2)), w: inch(Math.abs(dx)), h: inch(Math.abs(dy)),
        flipV: dx * dy < 0, line: { color: scheme(pres, it.color), width: pt(it.w), dashType: it.dash ? 'dash' : 'solid' },
      });
      break;
    }
    case 'shape':
      slide.addShape(it.kind === 'arrow-left' ? pres.ShapeType.leftArrow : pres.ShapeType.rightArrow, {
        x: inch(it.x), y: inch(it.y), w: inch(it.w), h: inch(it.h), fill: { color: scheme(pres, it.fill) }, line: { type: 'none' },
      });
      break;
    case 'img':
      slide.addImage({ path: LOGO_FILE, x: inch(it.x), y: inch(it.y), w: inch(it.w), h: inch(it.h), altText: it.alt });
      break;
    case 'icon': {
      const data = ctx.icons[`${it.name}|${it.color}`];
      if (data) slide.addImage({ data, x: inch(it.x), y: inch(it.y), w: inch(it.w), h: inch(it.h), altText: it.name });
      break;
    }
    case 'text':
      slide.addText(paraRuns(pres, it.paras), textBoxOpts(it));
      break;
    case 'list': {
      const arr = [];
      it.paras.forEach((p, i) => {
        p.forEach((r, j) => {
          const o = { ...runOpts(pres, r), bullet: it.ordered ? { type: 'number', indent: pt(it.indent) } : { indent: pt(it.indent) } };
          if (j === p.length - 1 && i < it.paras.length - 1) o.breakLine = true;
          arr.push({ text: r.text, options: o });
        });
      });
      slide.addText(arr, textBoxOpts(it));
      break;
    }
    case 'table': {
      const b = c => ({ type: 'solid', pt: pt(c), color: null });
      const rows = it.rows.map((row, ri) => row.map((c, ci) => {
        const border = [
          ri === 0 ? { type: 'solid', pt: pt(it.outer.top), color: it.outer.color } : { type: 'none' },
          { type: 'solid', pt: pt(c.border.right), color: c.border.color },
          { type: 'solid', pt: pt(c.border.bottom), color: c.border.color },
          ci === 0 ? { type: 'solid', pt: pt(it.outer.left), color: it.outer.color } : { type: 'none' },
        ];
        return {
          text: paraRuns(pres, c.paras),
          options: { fill: { color: scheme(pres, c.fill) }, border, margin: c.pad.map(inch), align: c.align, valign: 'top', lineSpacing: c.lineHeight ? pt(c.lineHeight) : undefined },
        };
      }));
      slide.addTable(rows, { x: inch(it.x), y: inch(it.y), w: inch(it.w), colW: it.colW.map(inch), rowH: it.rowH.map(inch), autoPage: false });
      break;
    }
  }
}

// Folienlayouts: Titel, Trennfolie, Statement, Inhalt. Geometrie der Titel-Platzhalter
// wird aus der ersten Slide des jeweiligen Typs übernommen.
const KINDS = { cover: { layout: 'Titel', titleTag: 'H1' }, divider: { layout: 'Trennfolie', titleTag: 'H2' },
  statement: { layout: 'Statement', titleTag: 'H1' }, content: { layout: 'Inhalt', titleTag: 'H2' } };

function titleOf(s) {
  const k = KINDS[s.cls];
  return k && s.items.find(i => i.type === 'text' && i.tag === k.titleTag);
}

function defineLayouts(pres, slides) {
  const defs = {};
  for (const s of slides) {
    const k = KINDS[s.cls];
    if (!k || defs[k.layout]) continue;
    const t = titleOf(s);
    const objects = [];
    let slideNumber;
    if (s.cls === 'content') {
      for (const it of s.items) {
        if (it.type === 'img' && it.cls === 'footlogo') objects.push({ image: { path: LOGO_FILE, x: inch(it.x), y: inch(it.y), w: inch(it.w), h: inch(it.h), altText: it.alt } });
        if (it.type === 'text' && it.cls === 'foot') objects.push({ text: { text: it.paras.flat().map(r => r.text).join(''), options: { ...runOpts(pres, it.paras[0][0]), ...textBoxOpts(it) } } });
        if (it.type === 'pageno') slideNumber = { x: inch(it.x + it.w - 240), y: inch(it.y), w: inch(240), h: inch(it.h), align: 'right', valign: 'top', margin: 0, fontFace: FONT_FACE(it.font), fontSize: pt(it.size), color: scheme(pres, it.color), bold: it.bold };
      }
    }
    if (t) {
      const r = t.paras[0][0];
      const box = slack(t);
      objects.push({ placeholder: { options: {
        name: 'title', type: 'title', x: inch(box.x), y: inch(t.y), w: inch(box.w), h: inch(t.h),
        fontFace: FONT_FACE(r.font), fontSize: pt(r.size), color: scheme(pres, r.color), bold: r.bold, align: t.align, valign: 'top', margin: 0,
        lineSpacing: t.lineHeight ? pt(t.lineHeight) : undefined,
      }, text: '' } });
    }
    pres.defineSlideMaster({ title: k.layout, background: { color: scheme(pres, s.bg) }, objects, slideNumber });
    defs[k.layout] = { title: t };
  }
  return defs;
}

// Nacharbeiten an den Titel-Platzhaltern, die pptxgenjs nicht abdeckt:
// - Position je Folie (pptxgenjs übernimmt stets die Layoutposition; Überschriften auf
//   Trennfolien sind aber vertikal zentriert und stehen je nach Inhalt unterschiedlich hoch),
// - kein Innenabstand, Ausrichtung oben, keine automatische Verkleinerung (wie im HTML).
const TITLE_SP = /<p:sp>(?:(?!<\/p:sp>)[\s\S])*?<p:ph\b[^>]*type="title"[\s\S]*?<\/p:sp>/;
const TITLE_BODY = '<a:bodyPr wrap="square" lIns="0" tIns="0" rIns="0" bIns="0" anchor="t" rtlCol="0"><a:noAutofit/></a:bodyPr>';
const fixBody = sp => sp.replace(/<a:bodyPr\b[^>]*?(?:\/>|>[\s\S]*?<\/a:bodyPr>)/, TITLE_BODY);

async function placeTitles(file, boxes) {
  const JSZip = require(require.resolve('jszip', { paths: [require.resolve('pptxgenjs')] }));
  const zip = await JSZip.loadAsync(fs.readFileSync(file));
  for (const name of Object.keys(zip.files).filter(n => /^ppt\/slideLayouts\/slideLayout\d+\.xml$/.test(n))) {
    zip.file(name, (await zip.file(name).async('string')).replace(TITLE_SP, fixBody));
  }
  for (const [n, [x, y, cx, cy]] of Object.entries(boxes)) {
    const name = `ppt/slides/slide${n}.xml`;
    let xml = await zip.file(name).async('string');
    if (!TITLE_SP.test(xml)) throw new Error(`${name}: Titel-Platzhalter nicht gefunden`);
    xml = xml.replace(TITLE_SP, sp => fixBody(
      sp.replace(/<a:off x="\d+" y="\d+"\/>\s*<a:ext cx="\d+" cy="\d+"\/>/, `<a:off x="${x}" y="${y}"/><a:ext cx="${cx}" cy="${cy}"/>`)));
    zip.file(name, xml);
  }
  for (const p of Object.keys(zip.files)) if (zip.files[p].dir) delete zip.files[p]; // Ordnereinträge stören beim Öffnen aus Cloud-Diensten
  fs.writeFileSync(file, await zip.generateAsync({ type: 'nodebuffer', compression: 'DEFLATE' }));
}

async function build() {
  const { deck, slides, icons } = await load();
  const pres = new PptxGenJS();
  pres.layout = 'LAYOUT_WIDE';
  pres.theme = { headFontFace: THEME.headFontFace, bodyFontFace: THEME.bodyFontFace };
  pres.title = deck.title;
  pres.author = 'Comquent Academy';
  pres.company = 'Comquent GmbH';

  const layouts = defineLayouts(pres, slides);
  const sectionAt = {};
  // Abschnittsname: Beschreibung bis zum Gedankenstrich; lange Namen auf „Kopf: erstes Wort“ kürzen.
  const sectionName = d => {
    let n = d.split(' – ')[0];
    if (n.length > 40 && n.includes(': ')) { const [h, rest] = n.split(': '); n = `${h}: ${rest.split(' ')[0].replace(/[,;.]$/, '')}`; }
    return n;
  };
  for (const s of Object.values(deck.sections || {})) if (s.start) sectionAt[s.start] = sectionName(s.description);
  let section;
  let slideNo = 0;
  const titleBoxes = {};

  for (const s of slides) {
    if (sectionAt[s.id]) { section = sectionAt[s.id]; pres.addSection({ title: section }); }
    slideNo++;
    const k = KINDS[s.cls];
    const slide = pres.addSlide({ masterName: k ? k.layout : undefined, sectionTitle: section });
    if (!k) slide.background = { color: scheme(pres, s.bg) };
    const title = titleOf(s);
    if (title) {
      const b = slack(title);
      titleBoxes[slideNo] = [b.x, title.y, b.w, title.h].map(v => Math.round(v / PX * 914400));
    }
    for (const it of s.items) {
      if (s.cls === 'content' && ((it.type === 'img' && it.cls === 'footlogo') || (it.type === 'text' && it.cls === 'foot') || it.type === 'pageno')) continue;
      if (it === title) {
        slide.addText(paraRuns(pres, it.paras).map(r => ({ text: r.text, options: { breakLine: r.options.breakLine } })), { placeholder: 'title' });
        continue;
      }
      addItem(pres, slide, it, { icons });
    }
    if (s.notes) slide.addNotes(s.notes);
  }

  fs.mkdirSync(path.dirname(OUT), { recursive: true });
  await pres.writeFile({ fileName: OUT });
  const { applyTheme } = require('./apply_theme.js');
  await applyTheme(OUT, THEME);
  await placeTitles(OUT, titleBoxes);
  console.log(`${slides.length} Slides -> ${path.relative(REPO, OUT)}`);
}

build().catch(e => { console.error(e); process.exit(1); });
