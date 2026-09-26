// AEC case-study deck: navigation, scaling, reveal animations and video playback.
(() => {
  const stage = document.getElementById('stage');
  const slides = [...stage.querySelectorAll('.slide')];
  const bar = document.getElementById('bar');
  const notes = document.getElementById('notes');
  const help = document.getElementById('help');
  let current = -1;

  slides.forEach((s, i) => { const n = s.querySelector('.pagenum'); if (n) n.textContent = `${String(i + 1).padStart(2, '0')} / ${slides.length}`; });

  // Scale the 1920×1080 stage to fit the window, centred and letterboxed. Refit on any
  // size change: window resize or maximise, fullscreen, browser zoom, rotation.
  const viewport = stage.parentElement;
  function fit() {
    const w = viewport.clientWidth || innerWidth, h = viewport.clientHeight || innerHeight;
    const s = Math.min(w / 1920, h / 1080);
    stage.style.transform = `translate(-50%, -50%) scale(${s})`;
  }
  fit();
  addEventListener('resize', fit);
  document.addEventListener('fullscreenchange', fit);
  if ('ResizeObserver' in window) new ResizeObserver(fit).observe(viewport);

  function go(i) {
    i = Math.max(0, Math.min(slides.length - 1, i));
    if (i === current) return;
    const prev = slides[current];
    if (prev) {
      prev.classList.remove('active', 'in');
      prev.querySelectorAll('video').forEach((v) => v.pause());
    }
    const next = slides[i];
    next.classList.add('active');
    requestAnimationFrame(() => requestAnimationFrame(() => next.classList.add('in')));
    const v = next.querySelector('video');
    if (v) { try { v.currentTime = 0; } catch (e) {} v.play().catch(() => {}); }
    current = i;
    bar.style.width = `${((i + 1) / slides.length) * 100}%`;
    notes.textContent = next.dataset.notes || '';
    history.replaceState(null, '', `#${i + 1}`);
  }

  const video = () => slides[current] && slides[current].querySelector('video');
  addEventListener('keydown', (e) => {
    if (e.metaKey || e.ctrlKey || e.altKey) return;
    const k = e.key;
    if (['ArrowRight', 'ArrowDown', 'PageDown', ' ', 'Enter'].includes(k)) { e.preventDefault(); go(current + 1); }
    else if (['ArrowLeft', 'ArrowUp', 'PageUp', 'Backspace'].includes(k)) { e.preventDefault(); go(current - 1); }
    else if (k === 'Home') go(0);
    else if (k === 'End') go(slides.length - 1);
    else if (k === 'f' || k === 'F') { document.fullscreenElement ? document.exitFullscreen() : document.documentElement.requestFullscreen().catch(() => {}); }
    else if (k === 'n' || k === 'N') notes.hidden = !notes.hidden;
    else if (k === 'm' || k === 'M') { const v = video(); if (v) v.muted = !v.muted; }
    else if (k === 'k' || k === 'K') { const v = video(); if (v) v.paused ? v.play() : v.pause(); }
    else if (k === '?' || k === 'h' || k === 'H') help.hidden = !help.hidden;
  });

  // Click to advance (left third goes back); links, videos and tiles keep their own behaviour.
  stage.addEventListener('click', (e) => {
    if (e.target.closest('a, video, button')) return;
    const r = stage.getBoundingClientRect();
    go(e.clientX < r.left + r.width / 3 ? current - 1 : current + 1);
  });
  let tx = null;
  addEventListener('touchstart', (e) => { tx = e.touches[0].clientX; }, { passive: true });
  addEventListener('touchend', (e) => { if (tx == null) return; const dx = e.changedTouches[0].clientX - tx; if (Math.abs(dx) > 50) go(current + (dx < 0 ? 1 : -1)); tx = null; });

  const start = parseInt(location.hash.slice(1), 10);
  go(Number.isFinite(start) ? start - 1 : 0);
  addEventListener('hashchange', () => { const n = parseInt(location.hash.slice(1), 10); if (Number.isFinite(n)) go(n - 1); });

  // Show the key help briefly on first load.
  help.hidden = false; setTimeout(() => { help.hidden = true; }, 4000);
})();
