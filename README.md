# SuperBusinessIntelligence.org

Static site for SuperBusiness Intelligence (SBI). Plain HTML and CSS. No build step or dependencies are needed to host it.

## Pages

| File | Purpose |
| --- | --- |
| `index.html` | Home: thesis, coverage tiers, links to the pillars |
| `si-watch.html` | Dated, sourced timeline of the federal AI-to-SI change |
| `outlier-watch.html` | Lead editorial pillar: the five tests and exception-first operations |
| `si-era-standard.html` | SBI's four-part SI-era classification and its guardrails |
| `about.html` | Claim labels, sourcing, AIIngestion disclosure, corrections |
| `404.html` | Not-found page |
| `assets/styles.css` | Shared styles, light and dark mode |
| `CNAME`, `sitemap.xml`, `robots.txt`, `.nojekyll` | GitHub Pages and search setup |
| `build.py` | Optional: regenerates every page from one file (`python3 build.py`) |

## Before making the site public

1. **Fill the evidence excerpts.** Every fact entry shows "Pending: verbatim excerpt…". Replace each with a short exact quote from the linked primary source (in `build.py`, then rerun it). Publishing the Truth Rule with empty excerpts undercuts the site's core claim.
2. **Set up the contact address.** `about.html` uses `editor@superbusinessintelligence.org`. Create that mailbox or forward, or change the address.
3. **Check the federal-definition date.** SI Watch expects the proposed definition about 60 days after Sept 29, 2026. Update the entry when it lands.

## Deploy on GitHub Pages

1. Create a public repository, for example `superbusinessintelligence`.
2. Upload every file in this folder to the repository root, including `.nojekyll` and `CNAME`.
3. In the repository: **Settings → Pages → Build and deployment → Source: Deploy from a branch**, branch `main`, folder `/ (root)`.
4. In **Settings → Pages → Custom domain**, enter `superbusinessintelligence.org`.
5. At your domain registrar, set DNS:
   - `A` records for `@`: `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
   - `AAAA` records for `@`: `2606:50c0:8000::153`, `2606:50c0:8001::153`, `2606:50c0:8002::153`, `2606:50c0:8003::153`
   - `CNAME` for `www`: `<your-github-username>.github.io`
6. After DNS resolves (minutes to a few hours), tick **Enforce HTTPS**.
7. Submit `https://superbusinessintelligence.org/sitemap.xml` in Google Search Console.

Recommended: verify the domain under your GitHub account settings (Settings → Pages → Verified domains) so no one else can claim it on Pages.

## Not included, by design

- No lead-capture form. GitHub Pages cannot process form submissions on its own; add a form service later only when there is an offer to capture leads for.
- No AIIngestion service pages. They stay frozen until a pilot produces measured results.
