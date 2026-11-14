/* Plan-side calibration only (exact BigInt arithmetic, parabola/tent weight families only).
   Inequality: sum_{d>0} (n-d-3*U_d) a_d <= n a_0 with U_d = total same-colour pair capacity at distance d.
   Scenarios give the smallest n at which SOME weight in the scanned family has positive margin.
   A scanned family is not an optimal dual; true thresholds can only be equal or lower. */
const corr = w => w.map((_, d) => { let s = 0n; for (let i = 0; i + d < w.length; i++) s += w[i] * w[i + d]; return s; });
const para = L => Array.from({ length: L - 1 }, (_, k) => BigInt((k + 1) * (L - k - 1)));
const tent = h => Array.from({ length: 2 * h - 1 }, (_, k) => BigInt(Math.min(k + 1, 2 * h - k - 1)));
const fams = []; for (let L = 20; L <= 170; L++) fams.push(["para" + L, para(L)]);
for (let h = 10; h <= 85; h++) fams.push(["tent" + h, tent(h)]);
const pre = fams.map(([nm, w]) => [nm, corr(w)]);
function positive(n, U) {
  for (const [nm, a] of pre) {
    let s = -BigInt(n) * a[0];
    for (let d = 1; d < a.length; d++) s += BigInt(n - d - 3 * U(n, d)) * a[d];
    if (s > 0n) return nm;
  }
  return null;
}
function threshold(U) { let n = 480, last = null; while (n > 200) { const r = positive(n, U); if (!r) break; last = [n, r]; n--; } return last; }
const base = (n, d) => 6 * (n - 1 - d >= 425 ? 24 : 23);
const scen = {
  "S0 baseline caps 6*(24|23)": base,
  "S1 at most ONE 24-mark class per distance (others 23)": (n, d) => (n - 1 - d >= 425 ? 6 * 23 + 1 : 6 * 23),
  "S2 no 24-mark class at all (all caps 23)": () => 6 * 23,
  "S3 every class loses one mark (23|22)": (n, d) => base(n, d) - 6,
  "S4 every class loses two marks (22|21)": (n, d) => base(n, d) - 12,
  "S5 per-colour cap 45 where 48 (Round-3 conditional shape), 46 kept": (n, d) => (n - 1 - d >= 425 ? 3 * 45 : 6 * 23),
  "S6 every class loses three marks (21|20)": (n, d) => base(n, d) - 18,
};
for (const [k, U] of Object.entries(scen)) { const t = threshold(U); console.log(k, "=> smallest n with positive margin in scanned family:", t ? t[0] : "none<=480", t ? t[1] : ""); }
