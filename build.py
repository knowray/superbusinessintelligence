import pathlib
SITE="https://superbusinessintelligence.org"
NAV=[("index.html","Home"),("si-watch.html","SI Watch"),("outlier-watch.html","Outlier Watch"),("si-era-standard.html","SI-era standard"),("about.html","Method and disclosures")]
def page(fn,title,desc,body):
    nav="".join(f'<li><a href="{h}"{" aria-current=\"page\"" if h==fn else ""}>{t}</a></li>' for h,t in NAV)
    canon=SITE+"/" if fn=="index.html" else f"{SITE}/{fn}"
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canon}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="{canon}">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'><rect width='32' height='32' fill='%231F5F7A'/><text x='16' y='22' font-family='Arial' font-weight='700' font-size='14' fill='white' text-anchor='middle'>SBI</text></svg>">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Familjen+Grotesk:wght@400;600;700&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/styles.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="mast"><div class="wrap">
<a class="brand" href="index.html">SuperBusiness Intelligence<small>Business intelligence for the SI era</small></a>
<nav aria-label="Main"><ul>{nav}</ul></nav>
</div></header>
<main id="main" class="wrap">
{body}
</main>
<footer><div class="wrap">
<p>SuperBusinessIntelligence.org is an independent research publication. It is operated by the same owner as AIIngestion.com, the ingestion engine that powers this site's source ledger. That relationship is disclosed on every page and explained in <a href="about.html">Method and disclosures</a>.</p>
<p>"SI-era" is SBI's own editorial classification, not the US federal definition of super intelligence and not a certification.</p>
</div></footer>
</body>
</html>
'''
def ledger(rows,pending=False):
    cls="ledger pending" if pending else "ledger"
    dl="".join(f"<dt>{k}</dt><dd{' class=\"excerpt\"' if k=='Excerpt' else ''}>{v}</dd>" for k,v in rows)
    return f'<aside class="{cls}" aria-label="Evidence"><dl>{dl}</dl></aside>'
PENDING="Pending: verbatim excerpt to be captured from the primary source before launch."
EO_URL="https://www.whitehouse.gov/president-actions/2026/09/inaugurating-the-era-of-super-intelligence/"

home=f'''
<div class="hero">
<h1>Every claim on this site shows where it came from.</h1>
<p class="lede">SuperBusiness Intelligence tracks how the newest generation of AI systems changes the way businesses work, and backs each factual statement with its source, date and supporting excerpt.</p>
</div>
<div class="claim">
<p>On September 29, 2026, an executive order directed US federal agencies to use "super intelligence" and "SI" in place of "artificial intelligence" in official communications. <span class="status fact">Fact</span></p>
{ledger([("Source",f'<a href="{EO_URL}">White House: Executive Order 14434</a>'),("Published","Sept 29, 2026"),("Checked","Oct 8, 2026"),("Excerpt",PENDING)],True)}
</div>
<p>This is the format for everything SBI publishes: the claim, the source, when it was published and checked, and the passage that supports it. Statements are labeled as fact, analysis or exception so you always know what you are reading.</p>

<section>
<h2>What SBI covers</h2>
<p>SBI sorts business technology into three tiers so readers can tell proven tools from frontier claims.</p>
<div class="tiers">
<div class="tier"><h3>Useful now</h3><p>Proven AI-era tools still worth using: document intelligence, automation, customer operations and decision support.</p></div>
<div class="tier"><h3>SI era</h3><p>Deployed systems that meet the <a href="si-era-standard.html">SI-era standard</a>: event-aware workflows, exception-first operations and processes that no longer need to exist.</p></div>
<div class="tier"><h3>Frontier</h3><p>What substantially more capable systems could change about companies and business models. Always labeled as analysis.</p></div>
</div>
</section>

<section>
<h2>Outlier Watch</h2>
<p>Most businesses try to automate the steps they already have. Outlier Watch asks a harder question: which of those steps only exist because older software needed someone to type, copy or re-check information the business could already observe?</p>
<p><a href="outlier-watch.html">Read the framework and the five tests</a></p>
</section>

<section>
<h2>SI Watch</h2>
<p>A dated, sourced record of how the US government's switch from "AI" to "SI" is being applied: the federal definition, agency adoption, procurement language and vendor relabeling.</p>
<p><a href="si-watch.html">Open the SI Watch timeline</a></p>
</section>
'''

siwatch=f'''
<div class="hero">
<h1>SI Watch</h1>
<p class="lede">A dated record of the US federal shift from "artificial intelligence" to "super intelligence," with every entry tied to its source.</p>
</div>
<div class="notice"><p><strong>What SI means in federal usage.</strong> Under Executive Order 14434, SI currently refers to the same technologies covered by the existing statutory definition of AI. It is a change of name, not a claim about capability. SBI uses a narrower <a href="si-era-standard.html">SI-era classification</a> of its own.</p></div>
<ol class="timeline">
<li><time datetime="2026-09-22">September 22, 2026</time>
<div class="claim"><p>Speaking at the UN General Assembly, President Trump said US government documents would use "super intelligence" instead of "artificial intelligence." <span class="status fact">Fact</span></p>
{ledger([("Source",'<a href="https://letsdatascience.com/news/trump-proposes-super-intelligence-name-for-ai-fd1370d6">Let\'s Data Science</a>'),("Published","Sept 2026"),("Checked","Oct 8, 2026"),("Excerpt",PENDING)],True)}</div></li>
<li><time datetime="2026-09-23">September 23, 2026</time>
<div class="claim"><p>The State Department told diplomats in its international organizations bureau to use "super intelligence," in an email titled "Change in Nomenclature AI to SI." <span class="status fact">Fact</span></p>
{ledger([("Source",'<a href="https://www.adn.com/nation-world/2026/09/23/us-diplomats-told-to-say-super-intelligence-not-artificial-intelligence-after-trumps-call/">AP via Anchorage Daily News</a>'),("Published","Sept 23, 2026"),("Checked","Oct 8, 2026"),("Excerpt",PENDING)],True)}</div></li>
<li><time datetime="2026-09-29">September 29, 2026</time>
<div class="claim"><p>Executive Order 14434 directed federal agencies to use "super intelligence" and "SI" in official correspondence, public communications and non-statutory policy documents. <span class="status fact">Fact</span></p>
{ledger([("Source",f'<a href="{EO_URL}">White House</a>'),("Published","Sept 29, 2026"),("Checked","Oct 8, 2026"),("Excerpt",PENDING)],True)}</div>
<div class="claim"><p>The order defines SI, for now, as the technologies already covered by the statutory AI definition, and gives the President's science and technology assistant 60 days to propose legislative language for a new definition. <span class="status fact">Fact</span></p>
{ledger([("Source",f'<a href="{EO_URL}">White House</a>'),("Published","Sept 29, 2026"),("Checked","Oct 8, 2026"),("Excerpt",PENDING)],True)}</div></li>
<li><time datetime="2026-11-28">Expected late November 2026</time>
<div class="claim"><p>The proposed federal SI definition is due about 60 days after the order. SBI will record what is proposed, when, and by whom. <span class="status analysis">Analysis</span></p></div></li>
</ol>
<section>
<h2>What SI Watch does not do</h2>
<p>SI Watch records how the term is used. It does not argue for or against the policy, and it does not count a press mention as adoption. An entry is added only when a primary document or a named source shows the change.</p>
</section>
'''

outlier='''
<div class="hero">
<h1>Outlier Watch</h1>
<p class="lede">The best systems ask people for less. Outlier Watch looks for business routines that only exist because older software needed someone to type, copy or re-check what the business already knew.</p>
</div>
<p><span class="status analysis">Analysis</span> This page is SBI's own framework, not a report of established fact.</p>
<h2>From keyboard-driven to event-driven</h2>
<div class="flow">
<p class="old">Keyboard-driven: something happens, a person notices, opens software, types it in, someone checks it, the business reacts later.</p>
<p>Event-driven: something happens, the system records it and gathers permitted context, proposes a next step, and a person handles only the exceptions.</p>
</div>
<p>This is not a claim that forms, keyboards or human judgment are disappearing. The point is narrower: a system should ask for human input only when that input adds judgment, permission, correction, relationship value or accountability.</p>
<section>
<h2>The five tests</h2>
<p>Each Outlier Watch analysis runs a workflow through the same five questions, in order.</p>
<ol class="tests">
<li><div><strong>Event</strong><p>What real-world or digital event proves this process has started?</p></div></li>
<li><div><strong>Information</strong><p>What does the business already know that people are re-entering today?</p></div></li>
<li><div><strong>Inference</strong><p>What can be safely classified, predicted or pre-filled?</p></div></li>
<li><div><strong>Cue</strong><p>What is the smallest prompt, choice or confirmation a person actually needs to give?</p></div></li>
<li><div><strong>Exception</strong><p>When must the system stop and hand control to a responsible person?</p></div></li>
</ol>
</section>
<section>
<h2>Exception-first operations</h2>
<p>An exception-first system handles the routine path on its own and brings a person in when something is uncertain, unusual, costly or sensitive. The person's time goes to judgment and relationships instead of data entry.</p>
<div class="notice"><p><span class="status exception">Exception</span> Safety issues, legal matters, pricing exceptions, unusual payments and decisions about people always go to a person. Exception-first does not mean unsupervised.</p></div>
</section>
<section>
<h2>Coming next</h2>
<p>The first Outlier Watch case study will be published once a real pilot has before-and-after measurements. SBI does not publish hypothetical results as case studies.</p>
</section>
'''

standard='''
<div class="hero">
<h1>The SI-era standard</h1>
<p class="lede">The US government now uses "SI" for all AI. SBI uses the term more narrowly, for deployed systems that can do bounded knowledge work on their own and know when to stop.</p>
</div>
<p>An SI-era system is a deployed model-and-workflow system that can carry out a bounded knowledge-work process across multiple steps, use approved tools and sources, adapt when intermediate results change the path, and escalate material uncertainty or exceptions to a person.</p>
<h2>The four requirements</h2>
<p>A system is classified SI-era only if published evidence or SBI's own documented use shows all four.</p>
<ol class="criteria">
<li><strong>Multi-step execution.</strong> It plans and completes a bounded workflow involving more than one decision or action.</li>
<li><strong>Tool use and adaptation.</strong> It uses approved tools or data sources, incorporates their results, and changes course when the results require it.</li>
<li><strong>Evidence-grounded work.</strong> Its outputs trace to the specific source passages or records that support them.</li>
<li><strong>Exception discipline.</strong> It identifies uncertainty, conflicts, missing evidence or out-of-policy conditions and routes them to a person rather than guessing.</li>
</ol>
<section>
<h2>What the classification is not</h2>
<ul class="criteria">
<li>It is SBI's editorial classification, not a universal or official definition of SI.</li>
<li>It is not a certification or a badge vendors can claim. SBI does not run a testing program for vendor systems.</li>
<li>It does not claim any model is superhuman or scientifically superintelligent.</li>
<li>Qualifying does not mean a system is autonomous, reliable in every setting, or suitable for high-impact decisions without human accountability.</li>
</ul>
<p>SBI reviews classifications every quarter as capabilities and practical reliability change. Systems that no longer meet the standard remain AI but leave the SI tier.</p>
</section>
'''

about='''
<div class="hero">
<h1>Method and disclosures</h1>
<p class="lede">How SBI decides what to publish, how it labels what you read, and who is behind it.</p>
</div>
<h2>How claims are labeled</h2>
<p><span class="status fact">Fact</span> A statement supported by a named source, with its publication date, the date SBI checked it, and the supporting passage.</p>
<p><span class="status analysis">Analysis</span> SBI's own interpretation or framework. It may be well reasoned, but it is not a reported fact.</p>
<p><span class="status exception">Exception</span> A case where a person, not a system, must make the decision.</p>
<section>
<h2>Sources and evidence</h2>
<p>SBI prefers primary sources: official orders, agency documents, company announcements and published research. Each factual claim links to its source and quotes only the short passage needed to support it. If a source changes or is withdrawn, the entry is updated and the change is noted.</p>
</section>
<section>
<h2>Commercial relationships</h2>
<p>SuperBusinessIntelligence.org and AIIngestion.com have the same owner. AIIngestion builds the ingestion engine that collects and organizes this site's sources. Where SBI discusses AIIngestion, it says so.</p>
<p>SBI does not accept payment to include, rank or describe any product. Any future sponsorship or referral relationship will be labeled where it appears.</p>
</section>
<section>
<h2>Corrections</h2>
<p>If something here is wrong, please report it with the page and the source that shows the error. Corrections are made on the page and dated.</p>
<p>Contact: <a href="mailto:editor@superbusinessintelligence.org">editor@superbusinessintelligence.org</a></p>
</section>
'''

notfound='''
<div class="hero">
<h1>This page isn't here.</h1>
<p class="lede">The address may have changed. Start from the <a href="index.html">home page</a> or open <a href="si-watch.html">SI Watch</a>.</p>
</div>
'''
pages=[("index.html","SuperBusiness Intelligence: business intelligence for the SI era","Evidence-cited research on how frontier AI and the US federal shift to super intelligence (SI) change the way businesses work.",home),
("si-watch.html","SI Watch: tracking the federal shift from AI to super intelligence | SBI","A dated, sourced timeline of the US federal change from artificial intelligence (AI) to super intelligence (SI), including Executive Order 14434.",siwatch),
("outlier-watch.html","Outlier Watch: business processes that should not exist | SBI","A framework for finding business routines that exist only because of old software, and redesigning them around events and exceptions.",outlier),
("si-era-standard.html","The SI-era standard: SBI's classification for frontier AI systems | SBI","How SuperBusiness Intelligence decides which deployed AI systems count as SI-era, and what the classification does not claim.",standard),
("about.html","Method and disclosures | SBI","How SuperBusiness Intelligence labels claims, handles sources and corrections, and discloses its relationship with AIIngestion.",about),
("404.html","Page not found | SBI","This page could not be found.",notfound)]
for fn,t,d,b in pages: pathlib.Path(fn).write_text(page(fn,t,d,b))
sm="".join(f"<url><loc>{SITE}/{'' if fn=='index.html' else fn}</loc><lastmod>2026-10-08</lastmod></url>" for fn,*_ in pages if fn!="404.html")
pathlib.Path("sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{sm}</urlset>\n')
pathlib.Path("robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
pathlib.Path("CNAME").write_text("superbusinessintelligence.org\n")
pathlib.Path(".nojekyll").write_text("")
