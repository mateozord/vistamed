import base64, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent
ASSETS = ROOT / "assets"
FONTS_DIR = ASSETS / "fonts"
OUT = ROOT / "vistamed_redesign.html"

sys.path.insert(0, str(FONTS_DIR))
from fonts_b64 import FONTS

def b64(name, mime):
    data = (ASSETS / name).read_bytes()
    return f"data:{mime};base64,{base64.b64encode(data).decode()}"

def font_uri(key):
    return f"data:font/woff2;base64,{FONTS[key]}"

ICON = b64("icon_360.png", "image/png")
HERO = b64("hero_doctor.jpg", "image/jpeg")
UNIT_SC = b64("unit_saocaetano.jpg", "image/jpeg")
UNIT_SP = b64("unit_saopaulo.jpg", "image/jpeg")

FRAUNCES500 = font_uri("FRAUNCES500")
FRAUNCES600 = font_uri("FRAUNCES600")
FRAUNCES500I = font_uri("FRAUNCES500I")
PLEX400 = font_uri("PLEX400")
PLEX600 = font_uri("PLEX600")
PLEX700 = font_uri("PLEX700")
PLEXMONO500 = font_uri("PLEXMONO500")

HTML = """<meta charset="utf-8" />
<title>Vistamed — Proposta de Redesign</title>
<meta name="viewport" content="width=device-width, initial-scale=1" />
<style>
  @font-face { font-family: 'Fraunces'; font-style: normal; font-weight: 500; font-display: swap; src: url("__FRAUNCES500__") format('woff2'); }
  @font-face { font-family: 'Fraunces'; font-style: normal; font-weight: 600; font-display: swap; src: url("__FRAUNCES600__") format('woff2'); }
  @font-face { font-family: 'Fraunces'; font-style: italic; font-weight: 500; font-display: swap; src: url("__FRAUNCES500I__") format('woff2'); }
  @font-face { font-family: 'Plex Sans'; font-style: normal; font-weight: 400; font-display: swap; src: url("__PLEX400__") format('woff2'); }
  @font-face { font-family: 'Plex Sans'; font-style: normal; font-weight: 600; font-display: swap; src: url("__PLEX600__") format('woff2'); }
  @font-face { font-family: 'Plex Sans'; font-style: normal; font-weight: 700; font-display: swap; src: url("__PLEX700__") format('woff2'); }
  @font-face { font-family: 'Plex Mono'; font-style: normal; font-weight: 400 700; font-display: swap; src: url("__PLEXMONO500__") format('woff2'); }

  :root {
    --bg: #FFFFFF;
    --bg-alt: #F7F9FB;
    --surface: #FFFFFF;
    --text: #1C2430;
    --muted: #667085;
    --ink: #123A66;
    --ink-deep: #0B2747;
    --on-ink: #F3F7FC;
    --accent: #2B6EBF;
    --accent-contrast: #FFFFFF;
    --line: #E3E8EF;
    --focus: #2B6EBF;
    --shadow: 0 20px 44px -28px rgba(18, 40, 80, 0.28);
    --font-display: 'Fraunces', 'Iowan Old Style', Georgia, serif;
    --font-body: 'Plex Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    --font-mono: 'Plex Mono', 'SF Mono', Consolas, 'Courier New', monospace;
  }
  @media (prefers-color-scheme: dark) {
    :root {
      --bg: #0B1420; --bg-alt: #101B2A; --surface: #16222F; --text: #EDF1F7; --muted: #9BAAC0;
      --ink: #5B9CE0; --ink-deep: #060B12; --on-ink: #F3F7FC;
      --accent: #78B0EE; --accent-contrast: #071522;
      --line: #2E4056; --focus: #78B0EE;
      --shadow: 0 20px 48px -22px rgba(0, 0, 0, 0.6);
    }
  }
  :root[data-theme="dark"] {
    --bg: #0B1420; --bg-alt: #101B2A; --surface: #16222F; --text: #EDF1F7; --muted: #9BAAC0;
    --ink: #5B9CE0; --ink-deep: #060B12; --on-ink: #F3F7FC;
    --accent: #78B0EE; --accent-contrast: #071522;
    --line: #2E4056; --focus: #78B0EE;
    --shadow: 0 20px 48px -22px rgba(0, 0, 0, 0.6);
  }
  :root[data-theme="light"] {
    --bg: #FFFFFF; --bg-alt: #F7F9FB; --surface: #FFFFFF; --text: #1C2430; --muted: #667085;
    --ink: #123A66; --ink-deep: #0B2747; --on-ink: #F3F7FC;
    --accent: #2B6EBF; --accent-contrast: #FFFFFF;
    --line: #E3E8EF; --focus: #2B6EBF;
    --shadow: 0 20px 44px -28px rgba(18, 40, 80, 0.28);
  }

  * { box-sizing: border-box; }
  html, body { margin: 0; padding: 0; }
  body {
    background: var(--bg); color: var(--text); font-family: var(--font-body);
    font-size: 16px; line-height: 1.6; -webkit-font-smoothing: antialiased;
  }
  img { display: block; max-width: 100%; }
  a { color: inherit; }
  a:focus-visible, button:focus-visible, summary:focus-visible { outline: 2px solid var(--focus); outline-offset: 3px; }
  h1, h2, h3 { font-family: var(--font-display); font-weight: 600; text-wrap: balance; margin: 0; }
  p { margin: 0; }
  .wrap { max-width: 1140px; margin: 0 auto; padding: 0 28px; }

  .ribbon {
    background: var(--ink-deep); color: var(--on-ink); font-family: var(--font-mono);
    font-size: 0.7rem; letter-spacing: 0.05em; text-align: center; padding: 8px 16px;
    border-bottom: 1px solid color-mix(in srgb, var(--accent) 45%, transparent);
  }
  .ribbon strong { color: var(--accent); font-weight: 700; }

  header.site {
    position: sticky; top: 0; z-index: 30; padding: 18px 0;
    background: color-mix(in srgb, var(--bg) 90%, transparent);
    backdrop-filter: blur(10px);
    border-bottom: 1px solid var(--line);
  }
  .nav { display: flex; align-items: center; justify-content: space-between; gap: 24px; }
  .brand { display: flex; align-items: center; gap: 11px; text-decoration: none; }
  .brand img { width: 34px; height: auto; border-radius: 3px; }
  .brand-word { font-family: var(--font-display); font-weight: 600; font-size: 1.32rem; letter-spacing: 0.01em; color: var(--text); }
  .brand-word b { color: var(--accent); font-weight: 600; }
  .navlinks { display: flex; align-items: center; gap: 28px; list-style: none; margin: 0; padding: 0; }
  .navlinks a {
    position: relative; text-decoration: none; font-size: 0.85rem; letter-spacing: 0.03em; text-transform: uppercase;
    color: var(--muted); font-weight: 600; padding-bottom: 3px;
  }
  .navlinks a::after {
    content: ""; position: absolute; left: 0; right: 100%; bottom: 0; height: 1px; background: var(--accent);
    transition: right 0.2s ease;
  }
  .navlinks a:hover { color: var(--text); }
  .navlinks a:hover::after { right: 0; }
  .cta-btn {
    display: inline-flex; align-items: center; gap: 8px; background: var(--ink); color: var(--on-ink);
    padding: 11px 19px; border-radius: 3px; text-decoration: none; font-size: 0.84rem; font-weight: 700;
    letter-spacing: 0.02em; white-space: nowrap; border: 1px solid transparent;
    transition: filter 0.15s ease, transform 0.15s ease;
  }
  .cta-btn.on-ink { background: var(--accent); color: var(--accent-contrast); }
  .cta-btn.outline {
    background: color-mix(in srgb, var(--bg) 60%, transparent);
    color: var(--text); border: 1.5px solid var(--accent);
    backdrop-filter: blur(6px); -webkit-backdrop-filter: blur(6px);
  }
  .cta-btn.outline:hover { background: color-mix(in srgb, var(--bg) 80%, transparent); }
  .cta-btn:hover { filter: brightness(1.08); transform: translateY(-1px); }

  /* ---------- hero ---------- */
  .hero { position: relative; background: var(--bg); overflow: hidden; padding: 0; }
  .hero::before {
    content: ""; position: absolute; inset: 0;
    background-image: url("__HERO__");
    background-size: cover; background-position: 68% 30%;
  }
  .hero::after {
    content: ""; position: absolute; inset: 0;
    background: linear-gradient(100deg,
      var(--bg) 0%,
      color-mix(in srgb, var(--bg) 90%, transparent) 32%,
      color-mix(in srgb, var(--bg) 50%, transparent) 56%,
      color-mix(in srgb, var(--bg) 10%, transparent) 78%);
  }
  .hero-inner { position: relative; z-index: 2; padding: 100px 0 148px; max-width: 640px; }
  .eyebrow {
    font-family: var(--font-mono); font-size: 0.74rem; letter-spacing: 0.14em; text-transform: uppercase;
    color: var(--accent); margin: 0 0 18px; font-weight: 600;
  }
  .hero h1 { font-size: clamp(2.3rem, 4.4vw, 3.4rem); line-height: 1.1; color: var(--text); }
  .hero .lede { margin-top: 22px; max-width: 46ch; color: var(--muted); font-size: 1.06rem; }
  .hero-ctas { display: flex; gap: 14px; margin-top: 34px; flex-wrap: wrap; }

  /* ---------- stats (floating overlap card) ---------- */
  .stats-wrap { position: relative; z-index: 3; margin-top: -72px; margin-bottom: 8px; }
  .stats-float { box-shadow: var(--shadow); }
  .stats-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 1px; background: var(--line); }
  .stat { background: var(--surface); padding: 6px 22px; }
  .stat .n { font-family: var(--font-display); font-weight: 600; font-size: 1.9rem; color: var(--ink); font-variant-numeric: tabular-nums; }
  .stat .l { font-size: 0.82rem; color: var(--muted); margin-top: 5px; }

  section { padding: 104px 0; }
  .section-head { max-width: 640px; margin-bottom: 46px; }
  .section-head .eyebrow { color: var(--accent); }
  .section-head h2 { font-size: clamp(1.7rem, 2.6vw, 2.3rem); }
  .section-head p { margin-top: 14px; color: var(--muted); font-size: 1rem; }

  .tick-card {
    background: var(--surface); padding: 30px; border: 1px solid var(--line);
    background-image:
      linear-gradient(to right, var(--accent) 2px, transparent 2px),
      linear-gradient(to right, var(--accent) 2px, transparent 2px),
      linear-gradient(to left, var(--accent) 2px, transparent 2px),
      linear-gradient(to left, var(--accent) 2px, transparent 2px),
      linear-gradient(to bottom, var(--accent) 2px, transparent 2px),
      linear-gradient(to bottom, var(--accent) 2px, transparent 2px),
      linear-gradient(to top, var(--accent) 2px, transparent 2px),
      linear-gradient(to top, var(--accent) 2px, transparent 2px);
    background-repeat: no-repeat; background-size: 16px 16px;
    background-position: top left, bottom left, top right, bottom right, top left, top right, bottom left, bottom right;
  }

  .svc-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 22px; }
  .svc-card h3 { font-size: 1.2rem; font-weight: 600; color: var(--text); font-family: var(--font-body); }
  .svc-card .tag { display: inline-block; font-family: var(--font-mono); font-size: 0.68rem; letter-spacing: 0.06em; color: var(--muted); text-transform: uppercase; margin-bottom: 10px; }
  .svc-list { list-style: none; margin: 16px 0 0; padding: 0; display: grid; gap: 8px; }
  .svc-list li { font-size: 0.92rem; padding-left: 16px; position: relative; }
  .svc-list li::before { content: ""; position: absolute; left: 0; top: 0.6em; width: 6px; height: 1px; background: var(--accent); }
  details.more { margin-top: 16px; }
  details.more summary { cursor: pointer; font-size: 0.82rem; font-weight: 700; color: var(--ink); list-style: none; display: flex; align-items: center; gap: 6px; }
  :root[data-theme="dark"] details.more summary { color: var(--accent); }
  @media (prefers-color-scheme: dark) { details.more summary { color: var(--accent); } }
  details.more summary::-webkit-details-marker { display: none; }
  details.more summary::after { content: "→"; transition: transform 0.15s ease; }
  details.more[open] summary::after { transform: rotate(90deg); }
  details.more .svc-list { margin-top: 14px; padding-top: 14px; border-top: 1px dashed var(--line); }

  /* ---------- quote band: centered pull-quote ---------- */
  .band { background: var(--bg-alt); text-align: center; }
  .band-inner { max-width: 700px; margin: 0 auto; }
  .band-inner .mark { width: 38px; height: 38px; margin: 0 auto 28px; }
  .band .eyebrow { justify-content: center; }
  .band blockquote {
    margin: 0; font-family: var(--font-display); font-style: italic; font-weight: 500;
    font-size: clamp(1.6rem, 3.2vw, 2.3rem); line-height: 1.4; color: var(--text);
  }
  .band cite { display: block; margin-top: 20px; font-style: normal; font-family: var(--font-mono); font-size: 0.72rem; letter-spacing: 0.08em; color: var(--accent); text-transform: uppercase; }

  .why { background: var(--bg-alt); border-top: 2px dashed var(--line); }
  .why-flag {
    font-family: var(--font-mono); font-size: 0.72rem; letter-spacing: 0.04em; text-align: center;
    color: var(--muted); margin-bottom: 36px;
  }
  .why-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 1px; background: var(--line); border: 1px solid var(--line); }
  .why-item { background: var(--surface); padding: 24px 26px; display: grid; grid-template-columns: 1fr 1fr; gap: 18px; }
  .why-col .k { font-family: var(--font-mono); font-size: 0.66rem; letter-spacing: 0.08em; text-transform: uppercase; color: var(--muted); font-weight: 600; }
  .why-col p { margin-top: 8px; font-size: 0.88rem; }
  .why-col.after .k { color: var(--accent); }

  /* ---------- sobre: faixa escura fixa (missão / visão / valores) ---------- */
  .about-section {
    background:
      radial-gradient(640px circle at 12% -10%, color-mix(in srgb, var(--accent) 16%, transparent), transparent 60%),
      var(--ink-deep);
    color: var(--on-ink);
  }
  .about-section .eyebrow { color: var(--accent); }
  .about-section .section-head h2 { color: var(--on-ink); }
  .about-section .section-head p { color: color-mix(in srgb, var(--on-ink) 70%, transparent); }

  .value-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 22px; }
  .value-card {
    padding: 30px; border-radius: 4px;
    background: color-mix(in srgb, var(--on-ink) 7%, var(--ink-deep));
    border: 1px solid color-mix(in srgb, var(--on-ink) 14%, transparent);
    border-top: 2px solid var(--accent);
  }
  .value-card .icon { width: 28px; height: 28px; color: var(--accent); margin-bottom: 18px; }
  .value-card h3 {
    font-family: var(--font-body); font-size: 1.05rem; font-weight: 600;
    color: var(--on-ink); letter-spacing: 0.01em;
  }
  .value-card p {
    margin-top: 12px; font-size: 1rem; line-height: 1.65;
    color: color-mix(in srgb, var(--on-ink) 78%, transparent);
  }
  .value-list { margin: 14px 0 0; padding: 0; }
  .value-list > div { padding: 12px 0; border-top: 1px solid color-mix(in srgb, var(--on-ink) 10%, transparent); }
  .value-list > div:first-child { border-top: none; padding-top: 2px; }
  .value-list dt {
    font-family: var(--font-body); font-weight: 600; font-size: 0.95rem;
    color: var(--accent); letter-spacing: 0.01em;
  }
  .value-list dd {
    margin: 6px 0 0; font-size: 0.92rem; line-height: 1.6;
    color: color-mix(in srgb, var(--on-ink) 78%, transparent);
  }

  .value-card { transition: transform 0.22s ease, box-shadow 0.22s ease, border-color 0.22s ease; }
  .value-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 14px 28px -20px rgba(0, 0, 0, 0.5);
    border-color: color-mix(in srgb, var(--accent) 40%, transparent);
  }
  @media (prefers-reduced-motion: reduce) { .value-card { transition: none; } }
  @media (prefers-reduced-motion: no-preference) {
    .value-card:nth-child(1) { transition-delay: 0ms; }
    .value-card:nth-child(2) { transition-delay: 70ms; }
    .value-card:nth-child(3) { transition-delay: 140ms; }
  }
  @media (max-width: 980px) and (min-width: 641px) {
    .value-grid { grid-template-columns: repeat(2, 1fr); }
  }
  @media (max-width: 640px) {
    .value-grid { grid-template-columns: 1fr; }
    .value-card { padding: 28px 24px; }
  }

  .chip-grid { display: flex; flex-wrap: wrap; gap: 9px; }
  .chip { font-size: 0.8rem; padding: 7px 13px; border: 1px solid var(--line); background: var(--surface); border-radius: 2px; }
  .chip.solo { border-color: var(--accent); color: var(--accent); font-weight: 700; }

  .unit-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 22px; }
  .unit-card { background: var(--surface); border: 1px solid var(--line); overflow: hidden; }
  .unit-photo { aspect-ratio: 4 / 3; overflow: hidden; background: var(--bg-alt); }
  .unit-photo img { width: 100%; height: 100%; object-fit: cover; display: block; }
  .unit-body { padding: 24px; }
  .unit-card h3 { font-size: 1.15rem; font-family: var(--font-body); font-weight: 700; }
  .unit-card .addr { margin-top: 10px; font-size: 0.9rem; color: var(--muted); }
  .unit-card .hours { margin-top: 14px; font-family: var(--font-mono); font-size: 0.78rem; display: flex; justify-content: space-between; border-top: 1px dashed var(--line); padding-top: 12px; }
  .unit-card .cta-btn { margin-top: 18px; width: 100%; justify-content: center; }

  .svc-card, .unit-card {
    transition: transform 0.22s ease, box-shadow 0.22s ease;
  }
  .svc-card:hover, .unit-card:hover {
    transform: translateY(-4px); box-shadow: var(--shadow);
  }
  @media (prefers-reduced-motion: reduce) {
    .svc-card, .unit-card { transition: none; }
  }

  .fab-whatsapp {
    position: fixed; right: 22px; bottom: 22px; z-index: 40;
    width: 54px; height: 54px; border-radius: 50%; background: var(--accent); color: var(--accent-contrast);
    display: flex; align-items: center; justify-content: center; text-decoration: none;
    box-shadow: var(--shadow); transition: transform 0.18s ease, opacity 0.18s ease;
  }
  .fab-whatsapp.is-hidden { opacity: 0; transform: scale(0.7); pointer-events: none; }
  .fab-whatsapp:hover { transform: scale(1.06); }

  footer { background: var(--ink-deep); color: color-mix(in srgb, var(--on-ink) 85%, transparent); padding: 58px 0 28px; }
  .foot-grid { display: grid; grid-template-columns: 1.3fr 1fr 1fr; gap: 36px; }
  .foot-brand { display: flex; align-items: center; gap: 11px; }
  .foot-brand img { width: 36px; }
  footer h4 { font-size: 0.76rem; letter-spacing: 0.08em; text-transform: uppercase; color: var(--accent); margin: 0 0 14px; font-weight: 700; }
  footer p, footer a { font-size: 0.88rem; text-decoration: none; color: inherit; }
  footer .social { display: flex; gap: 14px; margin-top: 16px; }
  footer .social a { border: 1px solid color-mix(in srgb, var(--on-ink) 30%, transparent); padding: 8px; border-radius: 3px; display: inline-flex; }
  .foot-bottom { margin-top: 44px; padding-top: 20px; border-top: 1px solid color-mix(in srgb, var(--on-ink) 16%, transparent); display: flex; justify-content: space-between; flex-wrap: wrap; gap: 10px; font-size: 0.74rem; color: color-mix(in srgb, var(--on-ink) 55%, transparent); font-family: var(--font-mono); }

  @media (max-width: 860px) {
    .svc-grid, .unit-grid, .foot-grid, .why-item { grid-template-columns: 1fr; }
    .stats-grid { grid-template-columns: repeat(2, 1fr); }
    .navlinks { display: none; }
    .hero-inner { max-width: 100%; }
    .hero::after { background: linear-gradient(180deg, var(--bg-alt) 38%, color-mix(in srgb, var(--bg-alt) 55%, transparent) 62%, color-mix(in srgb, var(--bg-alt) 15%, transparent) 100%); }
  }
  @media (prefers-reduced-motion: no-preference) {
    .reveal { opacity: 0; transform: translateY(14px); transition: opacity 0.5s ease, transform 0.5s ease; }
    .reveal.in { opacity: 1; transform: none; }
  }
</style>

<div class="ribbon"><strong>PROPOSTA DE REDESIGN</strong> — versão conceitual para apresentação interna · não é o site oficial vistamed.com.br</div>

<header class="site" id="siteHeader">
  <div class="wrap nav">
    <a class="brand" href="#topo" aria-label="Vistamed">
      <img src="__ICON__" alt="" />
      <span class="brand-word">VISTA<b>MED</b></span>
    </a>
    <ul class="navlinks">
      <li><a href="#sobre">Sobre</a></li>
      <li><a href="#servicos">Serviços</a></li>
      <li><a href="#convenios">Convênios</a></li>
      <li><a href="#unidades">Unidades</a></li>
      <li><a href="#trabalhe">Trabalhe Conosco</a></li>
    </ul>
    <a class="cta-btn on-ink" href="https://api.whatsapp.com/send?l=pt&amp;phone=5511963392596" target="_blank" rel="noopener">Agendar no WhatsApp</a>
  </div>
</header>

<main id="topo">
  <section class="hero">
    <div class="wrap hero-inner">
      <p class="eyebrow">Hospital de Olhos · São Paulo e São Caetano do Sul</p>
      <h1>33 anos cuidando da visão de São Paulo com técnica e dignidade humana.</h1>
      <p class="lede">Consultas, exames e cirurgias oftalmológicas em duas unidades na Grande São Paulo. Atendimento particular e por convênio — agendamento direto pelo WhatsApp, sem burocracia.</p>
      <div class="hero-ctas">
        <a class="cta-btn on-ink" href="https://api.whatsapp.com/message/L24UNJQUC3OQN1?autoload=1&amp;app_absent=0" target="_blank" rel="noopener">Agendar — Unidade São Paulo</a>
        <a class="cta-btn outline" href="https://wa.me/message/NQ7S5W4PJ763P1" target="_blank" rel="noopener">Agendar — Unidade São Caetano</a>
      </div>
    </div>
  </section>

  <div class="stats-wrap">
    <div class="wrap">
      <div class="stats-float tick-card reveal">
        <div class="stats-grid">
          <div class="stat"><div class="n">1993</div><div class="l">Fundação — 33 anos de história</div></div>
          <div class="stat"><div class="n">2</div><div class="l">Unidades na Grande São Paulo</div></div>
          <div class="stat"><div class="n">30+</div><div class="l">Convênios e seguros aceitos</div></div>
          <div class="stat"><div class="n">45+</div><div class="l">Exames, consultas e cirurgias</div></div>
        </div>
      </div>
    </div>
  </div>

  <section id="servicos">
    <div class="wrap">
      <div class="section-head">
        <p class="eyebrow">Serviços</p>
        <h2>Consultas, exames e cirurgias oftalmológicas</h2>
        <p>Da rotina de checkup aos procedimentos cirúrgicos mais complexos, sob um único teto.</p>
      </div>
      <div class="svc-grid">
        <div class="tick-card svc-card reveal">
          <span class="tag">Diagnóstico</span>
          <h3>Consultas, Exames e Procedimentos a Laser</h3>
          <ul class="svc-list">
            <li>Refração e adaptação de lente de contato</li>
            <li>Campo Visual Computadorizado</li>
            <li>Mapeamento e Retinografia de Retina</li>
            <li>OCT — Tomografia de Coerência Óptica</li>
            <li>Topografia Corneana / Ceratoscopia</li>
            <li>Fotocoagulação de Retina</li>
          </ul>
          <details class="more">
            <summary>Ver todos os 30 exames</summary>
            <ul class="svc-list">
              <li>Angiofluoresceinografia</li>
              <li>Biometria Ultrassônica</li>
              <li>Biomicroscopia de Fundo</li>
              <li>Capsulectomia com laser</li>
              <li>Curva Tensional</li>
              <li>Eletroretinografia</li>
              <li>Eletrooculograma</li>
              <li>Exame sob narcose</li>
              <li>Fundoscopia</li>
              <li>Gonioscopia</li>
              <li>Iridectomia (Yag Laser)</li>
              <li>Microscopia Especular de Córnea</li>
              <li>Paquimetria Ultrassônica</li>
              <li>PAM (Acuidade Visual com Laser)</li>
              <li>Potencial Visual Evocado</li>
              <li>Senso Cromático / Teste de Daltonismo</li>
              <li>Teste de Ishihara</li>
              <li>Teste Ortóptico</li>
              <li>Teste de Schirmer</li>
              <li>Teste de Teller</li>
              <li>Tonometria de Aplanação</li>
              <li>Ultrassonografia Ocular</li>
              <li>Visão Sub-normal</li>
            </ul>
          </details>
        </div>
        <div class="tick-card svc-card reveal">
          <span class="tag">Cirurgia</span>
          <h3>Procedimentos Cirúrgicos</h3>
          <ul class="svc-list">
            <li>Catarata com Lente Intra-ocular</li>
            <li>Correção com Excimer Laser (Cirurgia Refrativa)</li>
            <li>Glaucoma</li>
            <li>Transplante de Córnea</li>
            <li>Estrabismo</li>
            <li>Retina e Vítreo</li>
          </ul>
          <details class="more">
            <summary>Ver todos os procedimentos</summary>
            <ul class="svc-list">
              <li>Aplicação Intra-Vítreo de Anti-Angiogênico</li>
              <li>Aplicação Intra-Vítreo de Polímero de Liberação Controlada</li>
              <li>Ciclofotocoagulação Endoscópica</li>
              <li>Conjuntiva</li>
              <li>Astigmatismo, Hipermetropia e Miopia (Excimer Laser)</li>
              <li>Crosslink</li>
              <li>Implante de Anel de Ferrara</li>
              <li>Plástica Ocular</li>
              <li>Vias Lacrimais</li>
            </ul>
          </details>
        </div>
      </div>
    </div>
  </section>

  <section class="band">
    <div class="wrap band-inner">
      <svg class="mark" viewBox="0 0 40 40" aria-hidden="true">
        <circle cx="20" cy="20" r="18" fill="none" stroke="var(--ink)" stroke-width="2"/>
        <circle cx="20" cy="20" r="11" fill="none" stroke="var(--accent)" stroke-width="2"/>
        <circle cx="20" cy="20" r="4" fill="var(--ink)"/>
      </svg>
      <p class="eyebrow">Nossa visão</p>
      <blockquote>“Ser referência como serviço de saúde oftalmológico em nossa sociedade.”</blockquote>
      <cite>Vistamed — Hospital de Olhos</cite>
    </div>
  </section>

  <section id="sobre" class="about-section">
    <div class="wrap">
      <div class="section-head">
        <p class="eyebrow">Sobre a Vistamed</p>
        <h2>Missão, visão e valores</h2>
        <p>Os princípios que guiam cada atendimento, desde 1993.</p>
      </div>
      <div class="value-grid">
        <article class="value-card reveal">
          <svg class="icon" viewBox="0 0 28 28" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true">
            <circle cx="14" cy="14" r="10"/>
            <circle cx="14" cy="14" r="5.5"/>
            <circle cx="14" cy="14" r="1.4" fill="currentColor" stroke="none"/>
          </svg>
          <h3>Missão</h3>
          <p>Executar com dignidade humana, ética e técnica, serviços médicos oftalmológicos, buscando a satisfação dos clientes independentemente de posição social, raça ou credo.</p>
        </article>
        <article class="value-card reveal">
          <svg class="icon" viewBox="0 0 28 28" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true">
            <path d="M2 14C5 8 10 5 14 5s9 3 12 9c-3 6-8 9-12 9S5 20 2 14Z"/>
            <circle cx="14" cy="14" r="3.4"/>
          </svg>
          <h3>Visão</h3>
          <p>Ser referência como serviço de saúde oftalmológico em nossa sociedade.</p>
        </article>
        <article class="value-card reveal">
          <svg class="icon" viewBox="0 0 28 28" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true">
            <path d="M5 22V13M14 22V6M23 22V13M2 22h24"/>
          </svg>
          <h3>Valores</h3>
          <dl class="value-list">
            <div>
              <dt>Humildade</dt>
              <dd>O crescimento do ser humano está diretamente relacionado à sua capacidade de ser humilde.</dd>
            </div>
            <div>
              <dt>Solidariedade</dt>
              <dd>Trabalhos sociais devem fazer parte de nossas conquistas.</dd>
            </div>
            <div>
              <dt>Competência</dt>
              <dd>A evolução da ciência deve nortear nossas atitudes éticas.</dd>
            </div>
          </dl>
        </article>
      </div>
    </div>
  </section>

  <section id="convenios">
    <div class="wrap">
      <div class="section-head">
        <p class="eyebrow">Convênios</p>
        <h2>Planos de saúde e seguradoras</h2>
        <p>Atendimento também particular, sem necessidade de convênio.</p>
      </div>
      <div class="chip-grid">
        <span class="chip">AFRESP / AMAFRESP</span>
        <span class="chip">Allianz</span>
        <span class="chip">Amil</span>
        <span class="chip">Blue Saúde</span>
        <span class="chip">Care Plus</span>
        <span class="chip">Cassi</span>
        <span class="chip">Cruz Azul</span>
        <span class="chip">Economus</span>
        <span class="chip">Gama Saúde</span>
        <span class="chip">Itaú</span>
        <span class="chip">Life Empresarial Saúde</span>
        <span class="chip">Mediservice</span>
        <span class="chip">Metrus Saúde</span>
        <span class="chip">Nova Saúde</span>
        <span class="chip">Omint</span>
        <span class="chip">Pessoal Saúde</span>
        <span class="chip">Porto Seguro Saúde</span>
        <span class="chip">Postal Saúde</span>
        <span class="chip">PROASA</span>
        <span class="chip">Petrobras Saúde</span>
        <span class="chip">Santa Casa de Mauá</span>
        <span class="chip">Saúde Caixa</span>
        <span class="chip">Select Saúde</span>
        <span class="chip">Sepaco</span>
        <span class="chip">Sobam / APS</span>
        <span class="chip">Soc. União Operária SCS</span>
        <span class="chip">Sul América Saúde</span>
        <span class="chip">Total MedCare</span>
        <span class="chip">Unimed — Central Nacional</span>
        <span class="chip">Unimed — Intercâmbio</span>
        <span class="chip">Unimed Seguros</span>
        <span class="chip">Usisaúde</span>
        <span class="chip">Vivest — Fundação CESP</span>
        <span class="chip solo">+ Particular</span>
      </div>
    </div>
  </section>

  <section id="unidades">
    <div class="wrap">
      <div class="section-head">
        <p class="eyebrow">Unidades</p>
        <h2>Onde estamos</h2>
        <p>Vistamed — cuidado que reflete em seus olhos.</p>
      </div>
      <div class="unit-grid">
        <div class="unit-card reveal">
          <div class="unit-photo"><img src="__UNIT_SC__" alt="Fachada da unidade São Caetano do Sul" /></div>
          <div class="unit-body">
            <h3>Unidade São Caetano do Sul</h3>
            <p class="addr">Rua Amazonas, 2426 — Cerâmica<br>São Caetano do Sul — SP</p>
            <div class="hours"><span>Segunda à sexta</span><span>7h às 18h</span></div>
            <a class="cta-btn" href="https://wa.me/message/NQ7S5W4PJ763P1" target="_blank" rel="noopener">(11) 96339-2596 · WhatsApp</a>
          </div>
        </div>
        <div class="unit-card reveal">
          <div class="unit-photo"><img src="__UNIT_SP__" alt="Prédio da unidade São Paulo" /></div>
          <div class="unit-body">
            <h3>Unidade São Paulo</h3>
            <p class="addr">Rua Prof. Aprígio Gonzaga, 78 — Salas 47 e 48<br>São Judas — São Paulo — SP</p>
            <div class="hours"><span>Segunda à sexta</span><span>7h às 17h</span></div>
            <a class="cta-btn" href="https://api.whatsapp.com/message/L24UNJQUC3OQN1?autoload=1&amp;app_absent=0" target="_blank" rel="noopener">(11) 96339-2619 · WhatsApp</a>
          </div>
        </div>
      </div>
    </div>
  </section>
</main>

<footer id="trabalhe">
  <div class="wrap foot-grid">
    <div>
      <div class="foot-brand">
        <img src="__ICON__" alt="" />
        <span class="brand-word" style="color:var(--on-ink)">VISTA<b>MED</b></span>
      </div>
      <p style="margin-top:14px; max-width:34ch; color:color-mix(in srgb, var(--on-ink) 70%, transparent);">Hospital de Olhos com unidades em São Paulo e São Caetano do Sul. Consultas, exames e cirurgias oftalmológicas, particular e por convênio, desde 1993.</p>
      <div class="social">
        <a href="https://www.facebook.com/VistaMedHospital" target="_blank" rel="noopener" aria-label="Facebook">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/></svg>
        </a>
        <a href="https://www.instagram.com/vistamedhospital/" target="_blank" rel="noopener" aria-label="Instagram">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1"/></svg>
        </a>
      </div>
    </div>
    <div>
      <h4>Trabalhe Conosco</h4>
      <p style="color:color-mix(in srgb, var(--on-ink) 70%, transparent)">Vagas abertas: Médico Oftalmologista e Recepção.</p>
      <p style="margin-top:10px;">Envie seu currículo: <a href="mailto:deptopessoal@vistamed.com.br" style="text-decoration:underline;">deptopessoal@vistamed.com.br</a></p>
    </div>
    <div>
      <h4>Contato</h4>
      <p>Central: (11) 4229-1522</p>
      <p style="margin-top:6px;">WhatsApp São Caetano: (11) 96339-2596</p>
      <p style="margin-top:6px;">WhatsApp São Paulo: (11) 96339-2619</p>
    </div>
  </div>
  <div class="wrap foot-bottom">
    <span>© 2026 VISTAMED — HOSPITAL DE OLHOS</span>
    <span>MOCKUP CONCEITUAL PARA APRESENTAÇÃO INTERNA · NÃO É O SITE OFICIAL</span>
  </div>
</footer>

<section class="why" id="nota-interna">
  <div class="wrap">
    <p class="why-flag">↓ A partir daqui: nota interna para a reunião — não faz parte do site em si ↓</p>
    <div class="section-head">
      <p class="eyebrow">Por que propor essa mudança</p>
      <h2>O conteúdo já é forte. A apresentação não acompanha.</h2>
      <p>Nada aqui inventa serviços novos — é o mesmo Vistamed, com a informação organizada para ser encontrada.</p>
    </div>
    <div class="why-grid">
      <div class="why-item">
        <div class="why-col before"><div class="k">Hoje</div><p>Menu em caixa alta sem hierarquia; botão de agendamento perdido no meio do texto.</p></div>
        <div class="why-col after"><div class="k">Proposta</div><p>Navegação enxuta com CTA de WhatsApp sempre visível no topo.</p></div>
      </div>
      <div class="why-item">
        <div class="why-col before"><div class="k">Hoje</div><p>Lista de ~50 exames e cirurgias despejada em bloco corrido de texto.</p></div>
        <div class="why-col after"><div class="k">Proposta</div><p>Serviços agrupados por categoria, com destaque dos mais buscados e lista completa sob demanda.</p></div>
      </div>
      <div class="why-item">
        <div class="why-col before"><div class="k">Hoje</div><p>Nenhuma foto real da equipe ou da estrutura aparece na home.</p></div>
        <div class="why-col after"><div class="k">Proposta</div><p>Fotografia real das unidades e do atendimento (mesmas imagens já usadas no site) tratadas com identidade visual própria.</p></div>
      </div>
      <div class="why-item">
        <div class="why-col before"><div class="k">Hoje</div><p>Layout de template genérico (Criador de Sites Locaweb), tipografia padrão do sistema.</p></div>
        <div class="why-col after"><div class="k">Proposta</div><p>A mesma identidade branco/cinza/azul da marca, com tipografia própria e hierarquia clara.</p></div>
      </div>
    </div>
  </div>
</section>

<a class="fab-whatsapp" id="fabWhatsapp" href="https://api.whatsapp.com/send?l=pt&amp;phone=5511963392596" target="_blank" rel="noopener" aria-label="Agendar pelo WhatsApp">
  <svg width="26" height="26" viewBox="0 0 24 24" fill="currentColor"><path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.45 1.33 4.95L2 22l5.28-1.38c1.44.79 3.06 1.2 4.71 1.2h.01c5.46 0 9.91-4.45 9.91-9.91C21.91 6.45 17.5 2 12.04 2zm5.8 14.02c-.24.68-1.4 1.32-1.93 1.4-.5.08-1.12.11-1.8-.11-.42-.13-.96-.31-1.65-.6-2.9-1.25-4.79-4.17-4.94-4.36-.14-.19-1.18-1.57-1.18-3 0-1.42.75-2.12 1.02-2.41.26-.28.58-.35.77-.35h.55c.18 0 .42-.03.65.5.24.56.81 1.95.88 2.09.07.14.12.31.02.5-.09.19-.14.31-.28.47-.14.16-.29.36-.42.48-.14.13-.28.28-.12.55.16.28.72 1.19 1.55 1.93 1.06.95 1.96 1.24 2.24 1.38.28.14.44.12.6-.07.16-.19.68-.79.86-1.06.18-.28.36-.23.6-.14.24.09 1.55.73 1.82.86.27.14.45.2.51.32.07.12.07.66-.17 1.34z"/></svg>
</a>

<script>
  var fabEl = document.getElementById('fabWhatsapp');
  var footEl = document.getElementById('trabalhe');
  if (fabEl && footEl) {
    var fabIo = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        fabEl.classList.toggle('is-hidden', e.isIntersecting);
      });
    }, { rootMargin: '0px 0px -10px 0px' });
    fabIo.observe(footEl);
  }

  if (window.matchMedia('(prefers-reduced-motion: no-preference)').matches) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
      });
    }, { threshold: 0.15 });
    document.querySelectorAll('.reveal').forEach(function (el) { io.observe(el); });
  } else {
    document.querySelectorAll('.reveal').forEach(function (el) { el.classList.add('in'); });
  }
</script>
"""

HTML = (HTML
    .replace("__ICON__", ICON)
    .replace("__HERO__", HERO)
    .replace("__UNIT_SC__", UNIT_SC)
    .replace("__UNIT_SP__", UNIT_SP)
    .replace("__FRAUNCES500__", FRAUNCES500)
    .replace("__FRAUNCES600__", FRAUNCES600)
    .replace("__FRAUNCES500I__", FRAUNCES500I)
    .replace("__PLEX400__", PLEX400)
    .replace("__PLEX600__", PLEX600)
    .replace("__PLEX700__", PLEX700)
    .replace("__PLEXMONO500__", PLEXMONO500)
)
OUT.write_text(HTML, encoding="utf-8")
print("written", OUT, len(HTML), "chars")
