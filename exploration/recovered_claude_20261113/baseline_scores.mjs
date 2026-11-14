/* Plan-side calibration only (exact BigInt). Baseline single-diagonal inequality
     sum_{d>0} (n-d-18*cap(n,d)) a_d <= n a_0,   cap = 24 if n-1-d >= 425 else 23
   External inputs G(24)>=425, G(25)>=480; valid for n<=480.
   This is NOT a proof artifact and NOT the PR #6 joint-capacity certificate. */
const corr = w => w.map((_, d) => { let s = 0n; for (let i = 0; i + d < w.length; i++) s += w[i] * w[i + d]; return s; });
const cap = (n, d) => (n - 1 - d >= 425 ? 24 : 23);
/* r8 = uniform per-class cap reduction in eighths of a mark; the score is scaled by 8. */
function score8(n, w, r8 = 0) {
  const a = corr(w); let s = 0n;
  for (let d = 1; d < w.length; d++) s += BigInt(8 * (n - d) - 18 * (8 * cap(n, d) - r8)) * a[d];
  return [s - 8n * BigInt(n) * a[0], a[0]];
}
const tent = h => Array.from({ length: 2 * h - 1 }, (_, k) => BigInt(Math.min(k + 1, 2 * h - k - 1)));
const para = L => Array.from({ length: L - 1 }, (_, k) => BigInt((k + 1) * (L - k - 1)));
const show = (nm, w) => { const o = {}; for (let n = 462; n <= 466; n++) o[n] = (score8(n, w)[0] / 8n).toString(); console.log(nm, JSON.stringify(o)); };
show("tent47", tent(47)); show("para86", para(86));
function best(n, r8) {
  let b = null;
  for (let L = 20; L <= 160; L++) {
    const [s, a0] = score8(n, para(L), r8); const q = Number(s) / Number(a0);
    if (!b || q > b.q) b = { q, L, pos: s > 0n };
  }
  return b;
}
for (const n of [464, 463, 462, 460, 455, 450, 440, 430, 420, 400, 380]) {
  let r = 0; while (!best(n, r).pos) r++;
  const b = best(n, r);
  console.log(n, "min uniform per-class cap reduction (marks):", r / 8, "parabola L:", b.L, "fraction of 24:", (r / 8 / 24).toFixed(3));
}
