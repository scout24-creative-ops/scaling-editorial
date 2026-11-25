# Scaling Editorial Publisher — Building Policy

## Contents

- Scope, canonical composition and spacing
- Article Package intake and SEO
- Category mapping and existing-entry preservation
- Reviewed author records, dates and reading time
- Global component policies
- Legacy and current editorial module contracts

## Scope and sources

For current SE UX pages, read [Current portal UX](portal-ux.md) and [Portal configuration](portal-config.json). Their website-specific targets, layout, spacing, navigation and intro-position rules supersede older global target and module-layout descriptions below. Read the Website targets and Magazine support section in contentful-integration.md before choosing a creation/update route or browser destination. Author/master-data, source, image and date requirements below remain in force; the active Publisher is draft-only with mandatory author/image intake and News plus rubric placement. Legacy layout sections apply only to explicitly retained legacy modules.

This is the canonical policy for standard LP Builder page composition, embedded-component use and module modification. `component-library.html` is the sole user-capability inventory. Complete `LP_MODULE_START` / `LP_MODULE_END` blocks define available Page Modules; complete `LP_COMPONENT_START` / `LP_COMPONENT_END` blocks define available Embedded Components or visual variants. A missing module-specific policy never removes availability.

CoreCSS and the centrally delivered LP Builder Bridge/Runtime remain the production implementation truth. The GPT-authored and stored `htmlSource` contains only LP Builder page markup. The renderer owns surrounding technical markup and loads the global Bridge/Runtime outside `htmlSource`; their presence in final renderer output is never an authoring or payload-validation requirement. Do not add their `<link>`/`<script>`, parallel CSS, arbitrary inline styles, guessed classes, tokens, assets or runtime behaviour. Approved narrow exceptions (20.11.2026) under portal-ux.md: the current article intro paragraph uses exactly `style="font-size:20px!important;line-height:30px!important;"`; the News home-lead image uses exactly `style="aspect-ratio:16/9!important;"`. These do not authorize other inline styles, page-spacing workarounds or changes to category/compact images.

Technical Design/Development references outside this GPT package are not user-capability sources: a documented token or utility is not a user capability unless it also has a complete Component Library block.

# Page Building

## Standard workflow

For every standard build or update: resolve the requested modules or template; load complete canonical Library blocks; resolve requested Embedded Components; apply this Building Policy; validate the complete page and its ending; only then Create or Update. Unknown modules, components, variants or classes are `GAP` / `ASK`, never an invitation to approximate.

Full HTML import and bypassing canonical composition are not active in this Publisher. Every build/edit requires the documented components, a complete authoritative pre-read for existing pages and the normal validation; no import exception bypasses them.

Stored `htmlSource` uses exactly one content root: `<div class="lpb-explicit-spacing">…</div>`. All Page Modules and page spacers are direct children. Embedded Components are used only inside a valid module slot and never become direct page sections merely because they have a Library block. Do not generate, require or validate a Bridge `<link>`, Runtime `<script>` or renderer wrapper inside this payload.

## Page spacing

- Page rhythm uses only `<div class="lpb-spacer lpb-spacer--{size}" aria-hidden="true"></div>` inside `lpb-explicit-spacing`. The Bridge is the technical source for spacer pixel values.
- For current UX pages use the navigation-to-content `lpb-spacer--l` exception in portal-ux.md. Other compositions use exactly one `lpb-spacer--3xl` between independent modules and directly after an initial Hero.
- Between directly consecutive `teaser-split-image-right` and `teaser-split-image-left` modules in either order, replace only that intervening `3xl` with exactly one `lpb-spacer--xxl`.
- Use `lpb-spacer--4xl` immediately before an LP Builder footer and for an explicitly requested large section transition.
- Without a footer, end `… → LAST CONTENT MODULE → spacer-4xl → END ROOT`; the closing `4xl` is the final direct child.
- With a footer, end `… → LAST CONTENT MODULE → spacer-4xl → FOOTER → END ROOT`; the footer is final and no closing spacer follows it.
- Never add an opening spacer, consecutive spacers, more than one spacer between modules, or a spacer inside a module.
- Do not simulate page rhythm with margins, padding, empty sections, content elements, custom CSS, another wrapper or `!important`. Module-internal contract spacing remains allowed.

## Page-level validation

Before Create/Update verify only the stored `htmlSource`: every Page Module has one complete canonical Library block; Embedded Components occur only in suitable module slots; module policies and runtime hooks are preserved; spacing and the terminal sequence are correct; no opening, missing, duplicate or consecutive spacer exists; no invented wrapper, class, module, variant, script or page-level spacing workaround exists. Missing renderer-owned assets are not a payload error or STOP condition.

## Layout and technical primitives

Grid, columns, breakpoints, gutters, alignment, margin, padding, gap, borders, radii and media ratios are implementation primitives, not user-selectable components. Use them only to preserve a canonical block or implement an allowed capability under this policy.

- Allowed containers/items: `grid`, `grid-flex`, `grid-item`.
- Allowed fractions: `one-whole`, `one-half`, `one-third`, `two-thirds`, `one-fourth`, `three-fourths`; never `three-quarters`.
- Allowed responsive items: `palm-one-whole`, `lap-one-half`, `desk-one-half`; approved three-column pattern: `one-third lap-one-half palm-one-whole`.
- Allowed gutters: `gutter-horizontal-l`, `gutter-vertical-s`; `align-center` is text alignment only.
- Native internal spacing utilities use `xs`, `s`, `m`, `l`, `xl`, `xxl`, `none` and documented responsive prefixes. No negative utilities, direct spacing tokens, invented utilities or arbitrary layout values.
- Builder radius roles are `lpb-radius--card` for card/teaser/callout surfaces and `lpb-radius--media` for media. Borders are used only where the canonical module/component requires them.
- Do not introduce arbitrary widths, wrappers, max-width, overflow, flex/grid/gap, border or radius values. Verified module-owned Bridge rules are the only exceptions.

# Editorial templates

Article Package default: `scaling-editorial-news-nav-categories` followed by `scaling-editorial-article-page`, under the current UX root and spacing contract.

Current category overview: `scaling-editorial-news-nav-categories` followed by `scaling-editorial-category-page`. An explicitly requested News edit uses `scaling-editorial-news-home` and its existing verified entry.

The older article-with-sidebar, category-overview, news-nav and standalone article blocks are retained for explicit legacy preservation. Keep the existing News entry; create no replacement or duplicate homepage.

# Scaling Editorial Article Package

## Recognition and authority

- Treat a complete Article Package supplied by the user as the current input as the draft-intake order. A Writer-generated package in the same conversation is only a handoff until the user requests CMS implementation. Read the full package and first obtain the mandatory personal author choice and two hosted WebP image-role URLs under required-inputs-and-placement.md and image-roles.md; do not add a general creation-confirmation question.
- A complete package normally contains `Auftrag`, `Rubrik`, `Themen-Tags`, `Platzierung`, a slug proposal or explicit update target, author information, `Veröffentlichungsdatum`, `Status`, image URL, headline, intro, article, sources, title-image alt text, caption, AI label and optional open checks. New packages may supply `Autor-ID`; legacy packages may still supply `Autor` and `Rolle`. Use the current personal selection of Inga or Julia and the confirmed hosted role URLs under image-roles.md; package values alone do not replace that selection. Ask only genuinely missing other requirements.
- Default to a new unpublished article Draft. Update only when the package explicitly identifies one existing article unambiguously; a matching slug alone never authorises overwriting a different article. Preserve an existing update target's slug unless a change is explicitly requested.
- A slug proposal is unverified. Apply the normal duplicate preflight and lifecycle contract from `contentful-integration.md`. Package status never authorises publication.

## Image-role handoff

Follow [image-roles.md](image-roles.md) for new standard intake: the same motif has a shared 1920 × 1080 title/large/medium WebP and a 480 × 270 compact WebP for small News and Weiterlesen. Accept the Article Package’s `Bild-URL` and `Listenteaser-Bild-URL` fields in the package, but obtain the required current personal confirmation. Older packages remain usable after only the missing role URLs are supplied. Preserve exact author/title/caption/credits and the visible AI mark on both files; downloads and placeholders are not hosted URLs. Keep the role map on the existing article root and run its scoped preflight/read-back check. This authorizes no asset upload, CDN transformation, CSS change, bulk retrofit or Discover metadata injection.

## Editorial SEO handoff

Accept the Article Package's separate `SEO` section with `SEO-Titel (seoTitle)` and `Meta Description (metaDescription)`, and an optional `Interne Linkvorschläge` section. Keep older packages without these additions draft-capable; report missing SEO metadata without inventing a finished implementation.

- The selected editorial headline remains the visible H1, teaser headline and ordinary `mainTitle`. A supplied `seoTitle` is separate metadata, never an alternative selected headline or a reason to overwrite public copy. Receive it without a publication suffix; any future supported title renderer adds the agreed suffix once. The project targets of 50–60 total title characters including the suffix and 140–160 description characters are guidelines, not draft-storage blockers.
- Preserve supplied SEO values exactly when reporting them. Flag a materially conflicting claim or ambiguous field; do not rewrite the article or manufacture missing evidence. Source URLs, author assignment, dates and image metadata keep their existing rules.
- Before storing metadata, inspect the actual native schema for dedicated supported fields. The current MCP create/update operations expose no verified `seoTitle` or `metaDescription` fields. Report each supplied value as `nicht im CMS gespeichert — kein unterstütztes Feld` in the completion result. Keeping it in the package/report is not CMS persistence or a rendered meta tag. Do not overload `mainTitle`, visible intro, body, caption or unrelated fields to hide it.
- Technical `<title>`, description, canonical, robots, Open Graph, JSON-LD, image preloads and responsive image delivery belong to the frontend/integration. This handoff does not authorize injecting head tags/scripts into stored body HTML, inventing fields, deploying runtime changes or claiming production SEO acceptance.
- Internal link suggestions are source data, not new research authority. Use only supplied/verified existing targets and anchor labels, in their supplied suitable context. If a suggestion lacks an unambiguous insertion point, retain it in the result for review rather than silently rewriting the body. Link suggestions do not independently authorize editing another page or inventing a recommendation destination.
- For new article HTML and a requested update to that article's source list, apply `rel="nofollow"` to external public source links under the supplied project editorial policy. Preserve complete original hrefs and any existing `noopener`, `noreferrer` or other required rel tokens. Links to `immobilienscout24.de` and its actual subdomains remain normal followed internal links; a name merely containing that domain is external. Before writing, run `python3 <skill-root>/scripts/check_source_links.py --html <complete-input.html>` against the final complete payload. Fix missing tokens and rerun. After full CMS read-back run the same check on the saved HTML, adding `--expected-html <complete-input.html>` to compare the source hrefs and required rel tokens. This read-only helper inspects only canonical source lists; it never changes HTML or contacts a service. If Python is unavailable, perform the same per-link checks on the complete input and read-back with another available parser and identify that method; never claim the helper ran. If no reliable check is possible, report it as unverified and stop dependent placements. A failed check also stops dependent placements. Preserve the existing entry identity and re-read before a scoped correction. For a narrow unrelated edit leave the source list untouched; the check does not expand the write scope. Explicit historical non-linked demo exceptions remain unchanged and cannot be reported as a successful real-source check. This is an editorial implementation policy, not a universal Google requirement.
- A dedicated author-profile destination, actual publication time/timezone and image credit can only come from supplied or reviewed data. Preserve allowed open draft states and report missing inputs for review. Do not construct an author-profile page, invent midnight/timezone or rename a Contentful system modification time as an editorial event.

## Category overview lookup

For the mandatory rubric placement of a new article, resolve all seven internal categories through `displayGroups` and `sites[selectedSite].placementTargets` in [Portal configuration](portal-config.json). The six non-Lifestyle categories group under Immobilienmarkt; Lifestyle retains its own group. Magazine is the default for new SE work. Use its configured category identities and verify them by fresh reads; null or mismatch never authorizes a www fallback or invented target. Resolve both required overview targets before the first article write. The existing www overview identities remain in sites.www for explicitly requested work there. Keep the original internal category; verify the target's actual site and grouped display identity. News placement is also mandatory for new Magazine articles under required-inputs-and-placement.md; no extra request is needed.

### Retained legacy overview inventory

The following entries remain intact for existing-page preservation and explicitly identified legacy-target requests. Their existence does not make them default placement destinations. Never delete, replace or bulk-synchronize these pages as a consequence of the routing change.

| Category | Existing Contentful slug | Known Entry ID |
|---|---|---|
| Immobilienmarkt | `dev-scaling-editorial-immobilienmarkt-mvp` | — |
| Mieten | `dev-scaling-editorial-mieten-mvp` | — |
| Kaufen & Verkaufen | `dev-scaling-editorial-kaufen-verkaufen-mvp` | — |
| Finanzen | `dev-scaling-editorial-finanzen-mvp` | — |
| Recht & Politik | `dev-scaling-editorial-wohnrecht-mvp` | `22O849wA6VAVgxOYVT9zvB` |
| Wohnen & Architektur | `dev-scaling-editorial-wohnen-architektur-mvp` | — |
| Lifestyle | `dev-scaling-editorial-lifestyle-mvp` | — |

- The category-overview slug identifies the existing overview and is never the new article's slug. Apply the technical leading-slash request convention from `contentful-integration.md` when reading it, but preserve the existing stored overview slug unchanged.
- Resolve the requested target through the selected site's placement configuration, then read its exact slug/known Entry ID and verify its actual site and displayed group identity. For an explicitly identified legacy target use the legacy inventory and its internal category instead. Preserve the complete existing content. A missing Entry ID does not block a supported unambiguous slug-based read; a null site-specific target remains unresolved.
- `Recht & Politik` groups under Immobilienmarkt for a requested rubric placement within the selected site. The existing www Wohnrecht Entry `22O849wA6VAVgxOYVT9zvB` is used only for an explicit request to that legacy target; preserve its identity and contents. Verify any configured known Entry ID and expected site against the returned result; a contradiction stops the dependent write.
- Never create a replacement overview automatically. An unknown category, missing mapping, ambiguous identity, not-found response or mismatch between the mapped slug, returned Entry and visible category is a targeted `ASK` or concrete read error.
- The article slug identifies the article only. Validate and use the package proposal under existing slug conventions. If it is absent, derive a suitable article slug from the supplied headline, then run the normal duplicate preflight. Topic tags determine neither the category-overview slug nor necessarily the article slug.
- A collision never authorises overwriting an existing article. Update only an explicitly and unambiguously identified existing article; otherwise stop and clarify identity.

## Article mapping

- Use `scaling-editorial-article-page` and the current three-entry UX navigation under portal-ux.md. Preserve the package headline, intro and Markdown article content verbatim in meaning and order while mapping paragraphs and heading levels to the canonical article structure.
- The package intro is the article subline exactly once directly after the complete author/meta block and before the complete title-media figure/caption, outside the headline header and meta block; use the exact same text in its large category teaser. Its approved current-article typography is 20/30 px with unchanged inherited colour under portal-ux.md. No Google preference, bottom statistics or SuchenPlus on current article pages. Preserve the terminal direct 4xl spacer. Production instructions, slug notes and open checks never enter the public article body. Historical standalone/legacy module ordering below does not override this current article-page contract; never shorten supplied text automatically.
- Accept only the seven internal categories present in portal-config.json displayGroups. An unknown category is `ASK`; never silently rename or create one.
- Accept only topic names from the `scaling-editorial-article` taxonomy. For Article Package work, do not render topic tags in the article or any teaser. Store them only in an appropriate already exposed metadata field. If none exists, do not overload another field or create one; preserve the unstored tags in the completion report.
- Resolve author data and article-specific date/reading-time data through the canonical author contract below. Never infer the author from the ChatGPT account, category, topic or prior article, and never assign a test author as a fallback.
- Preserve the supplied publication date. Never derive it from the current date, a Contentful timestamp or the requested status.
- Obtain the actual personally selected hosted image URL before implementation under required-inputs-and-placement.md. Use that same image in the article and both required teasers. No automatic grey image, TEXT_TEST fallback or unresolved placeholder URL, even for drafts/tests. A local download is not hosting. Preserve actual matching alt text, caption, credit and confirmed AI status; clarify concrete metadata conflicts. Intended title-image size is 1920×1080; independent downloading/pixel proof is not a prerequisite. Never invent an asset.
- Map supplied title-image alt text and confirmed AI status according to the `scaling-editorial-article` hero-caption rule. Use the canonical `lpb-editorial-article__media--with-caption` structure with its media frame and one `figcaption` when a caption or AI label is present; never infer an AI claim.
- Render every public source with its supplied publisher and short source title, optionally followed by its supplied publication date. Preserve the complete verified original HTTPS URL unchanged in `href`, including its query and fragment; never display the full URL as the label. Missing publisher/title data needs targeted clarification, never an invented attribution. Missing or unsafe required source URLs are `ASK`; the non-linked demo-source exception applies only to explicitly labelled demo content.

## Overview and consistency

- Resolve and read the matching existing category overview through the canonical lookup, place the new or updated article first as the lead in its featured area and preserve all unrelated existing articles and information. In a current UX category page, demote the old lead into the existing grids while preserving remaining article information and order and deduplicating identities across sections. The former two-compact-slot layout applies only to a retained legacy category-overview module. Replace an empty state when the first valid article is added; never duplicate the same article identity, destination or Entry.
- Use only the actual article destination returned by the Contentful workflow. Existing navigation, layout and other categories remain unchanged. For an update, keep existing links to that exact article consistent without rewriting unrelated portal Pages.
- Build sidebar recommendations only from existing verified articles, excluding the current article. Do not invent recommendations; use fewer only when the canonical module and supplied inventory allow it, otherwise report the gap before writing.
- After article and overview mutations, apply the normal read-back, version, integrity and Draft checks. Preserve package open checks in the result report and distinguish storage verification from any visual check that was not actually performed.

## Author registry and Article Package contract

This is the single deployed author-registry snapshot available to the LP Builder. Real-author master data were refreshed from the published central register at `https://wiki.scout24.com/spaces/product-intelligence/pages/68902/autorenregister` on 19.11.2026 (revision `2c3fc9c34a852cf115acf0d98457edbfd44ddc478940537c715a13bbdb8e1ef4`). The LP Builder does not infer or scrape author data at build time. The two real authors below require explicit per-article assignment; their presence is not an assignment, style instruction or publication approval. Retained test profiles are separate legacy records, never fallbacks for the real authors.

| Author ID | Public display name | Confirmed role / expertise | Portrait URL | Verified profile URL | Status |
|---|---|---|---|---|---|
| `inga-ervig` | Inga Ervig | Freie Autorin | `https://www.static-immobilienscout24.de/statpic/scaling-editorial/c2e67242abf8f7858ad7ee881a9abbf7_scaling-editorial-portraet-inga-ervig-v02.webp` | `https://threadmedia.de/about-inga-ervig/` | Real author; confirm assignment per article |
| `julia-walter` | Julia Walter | Freie Autorin | `https://www.static-immobilienscout24.de/statpic/scaling-editorial/460d851cbbd183a405ec8785a4dfd928_scaling-editorial-portraet-julia-walter-v02.webp` | `https://www.canva.com/design/DAFIcfHGL7s/4sOKkOHP5gmxoZz_jJxzTw/view?utm_content=DAFIcfHGL7s&utm_campaign=designshare&utm_medium=link&utm_source=editor` | Real author; confirm assignment per article |
| `test-autor-1` | Maria Müller | Expertin für Immobilien | `https://www.static-immobilienscout24.de/fro/_/_/sclaing-editorial-author-avatar-1.png` | — | Historischer Testdatensatz – keine Neuzuweisung |
| `test-autor-2` | Elisabeth König | Expertin für Immobilien | `https://www.static-immobilienscout24.de/fro/_/_/sclaing-editorial-author-avatar-2.png` | — | Historischer Testdatensatz – keine Neuzuweisung |

Real-profile resolution:
- Resolve `Inga` / `Inga Ervig` to `inga-ervig`, and `Julia` / `Julia Walter` to `julia-walter` only after the user explicitly assigns that author for the specific article. Use exactly the reviewed public name, fixed role, portrait and profile URL above; do not derive authorship from category, style profile, account or an earlier article.
- Use the existing canonical author component with `data-lpb-author-status="assigned"` for that confirmed real assignment. This is a draft assignment, not a claim of editorial/publication approval. Profile links use only the exact reviewed supplied URL.
- The portrait filename `author-julia-fraese.png` is the historical filename for public author Julia Walter; use her verified WebP from the current register. Do not rename the public author or reconstruct an asset URL from the public name. The register's provisional style-profile discussion does not change these stable master records.
- Preserve newer unrelated existing author content during partial updates. These rows are for confirmed new assignments, not authority to migrate old article identities or rewrite a source register.

Separation:
- Author master data are stable Author ID, public display name, editorially confirmed role/expertise, portrait URL, verified profile URL and author status. Resolve them only from this registry or a future explicitly supplied, reviewed replacement; never rewrite the role per article.
- Add or change an author once in the reviewed central register and this single deployed snapshot. Both article variants resolve the same `scaling-editorial-author` component by Author ID; never duplicate an author record or create an author-specific article template.
- Article data are assigned Author ID, first publication date, optional actual editorial-update date and reading time calculated from the final article body. Do not copy article-specific values into the registry.
- New Article Packages use one `Autor-ID` value. A known ID resolves the complete master record. A contradictory supplied `Autor`, `Rolle`, portrait or profile value is `ASK` / STOP, not an override.

Missing or conflicting author data:
- Before implementation ask the user to select exactly one of Inga Ervig or Julia Walter for this article. Current explicit answers for that same article need not be repeated. Package placeholders or account/category/previous-article guesses are not assignment.
- Resolve only the two confirmed real records above for new assignments. Missing choice, unknown ID, conflicting master data or either test profile stops the write; no unassigned Draft fallback is active. Existing unrelated legacy author content is preserved, not automatically migrated.
- Test profiles above remain historical master records for identifying/preserving existing legacy content, not selectable options or publication exceptions. There is no technical-pilot publishing route in this Publisher. Preserve an existing explicitly scoped pilot notice during a partial edit, but it grants no authority.
- Render the confirmed real author with the canonical component and its exact reviewed role/portrait/profile. Author ID, name, fixed role and selected image must be consistent across article and both required teasers, subject to each canonical teaser's visible fields.
- Publication, deletion and other lifecycle actions remain unavailable under this MVP regardless of package status or historic pilot ID.

Profile and portrait output:
- Preserve the registered portrait URL exactly. The two supplied test URLs deliberately contain `sclaing`; do not correct that spelling or substitute another asset.
- Use the complete safe portrait URL from the resolved author registry record. The intended portrait production size is 240×240 pixels; no independent file or pixel verification is required before a Contentful Action. A missing, incomplete or unsafe portrait URL or an unresolved placeholder address remains `ASK`; never replace a portrait with the article title image. Missing or unassigned author data now stops the Publisher intake; do not omit the confirmed real portrait as a fallback.
- Without a verified profile URL, render the author name as a non-interactive `span`. Only a complete supplied and verified safe HTTPS profile URL may change that `span` to `a[href]`; never invent a profile page or use `href="#"`.
- Informative portraits use a meaningful alt in the form `Porträt von {display name}`. An unassigned author state is not permitted for a new Publisher implementation.

Dates:
- For a **new article**, resolve one intended publication date before writing: an explicit current user date takes precedence; otherwise retain a valid supplied editorial date. When neither exists, obtain the actual current calendar date in `Europe/Berlin` with an available clock/date tool. Use that day automatically, without an extra date-confirmation question. An open Writer value such as „noch festzulegen“ is missing input, not a user override. An explicitly requested open date remains open; contradictory or invalid dates require targeted clarification. If the current date cannot be reliably obtained, report it as unresolved rather than guessing.
- Render the resolved date as `Veröffentlicht: TT.MM.JJJJ` in the existing component and copy the same date to the two corresponding teasers. In the result identify it as the **intended** publication date, including whether it came from the user, package or current-day default. A stored draft/display date proves no publication; it must be checked again before actual publication, which remains outside this Publisher's scope.
- For an **existing article**, preserve its original first-publication date, including an existing open state, unless the user explicitly requests a date correction. Never replace it with today's date because of an edit. On resume or a later teaser-placement step, reuse the date already resolved and stored for that article, even after midnight; do not default it again. The first publication date never appears as `Aktualisiert`.
- Render `Aktualisiert: TT.MM.JJJJ` only when the package or explicit update supplies a distinct actual editorial-update date and identifies the corresponding substantive content update. Keep it as optional secondary date information alongside the first-publication label; never relabel an update date as `Veröffentlicht` or replace a known first-publication fact.
- `02.11.2026` is explicitly supplied only for the existing author-module layout test. Never copy it to another article or derive an update date from Contentful status, modification time or the current date.
- Format the resolved ISO date mechanically as `TT.MM.JJJJ` and retain the ISO value in `time[datetime]`. An explicitly open or unresolved date remains `Veröffentlicht: noch festzulegen` in a Draft and is reported. Never use Contentful creation/modification timestamps or another article's date. The current-day default above applies only to a new article.
- The primary visible date label is `Veröffentlicht:`. Add `, HH:mm Uhr` only when the editorial metadata explicitly supplies that clock time with an unambiguous display context; never invent midnight, a timezone or a converted time. Preserve the supplied ISO value in `time[datetime]`. A date-only value stays date-only. No additional Contentful field is required.

Reading time:
- Calculate only after the final article HTML is complete. Count Unicode word sequences in visible editorial `p`, `h2`, `h3` and list-item text inside `.lpb-editorial-article__body`; include internal apostrophes and hyphens as part of a word.
- Exclude the complete sources aside, author/header metadata, tags, title-image and diagram captions, SVG accessibility text and any non-editorial technical labels. Divide the resulting word count by 200 and round up to the next whole minute; a non-empty body has a minimum of one minute.
- Render exactly `Lesezeit: 1 Minute` or `Lesezeit: {N} Minuten`. Recalculate after any body-content change. If the final body is unavailable or an exact mechanical count cannot be completed, render `Lesezeit: noch zu bestimmen`, report the open check and make no publication-ready claim; never guess.

# Global Component Policies

## Typography

The Component Library defines the available visual headline and body/text variants. Semantic `h1`–`h6`, paragraph, label and other HTML roles are independent of visual size: changing a visual class never changes the semantic heading level or document outline.

Normal visible LP copy, list copy and normal visible link labels use `font-body-large-regular`. Medium and smaller body variants are only for secondary, legal, metadata, technical, annotation or compact UI/status roles. Never shrink text merely to fit. Preserve a module-specific typography lock when one exists. No free inline typography CSS or new typography class; the exact current-article intro-only 20/30 px exception is defined above and in portal-ux.md.

## Buttons and CTA

Only Component Library button variants may be selected. An existing CTA slot may switch among those variants unless its module policy locks the variant. A variant switch does not authorise a new CTA slot, movement of a CTA, extra buttons, a semantic change or a runtime change. Buttons remain content-width; the documented mobile-full variant is opt-in only. Do not invent button classes.

Do not use deprecated `button-primary`, `button-secondary`, `ai-button`, `button-filled-*` or `button-outline-*` classes.

## Links

Use semantic `a[href]` for internal, external, fragment, `mailto` and `tel` links. Use `target="_blank" rel="noopener noreferrer"` only when a new tab is explicitly requested. Fragment targets must be unique and present. A Chevron Link is only a directional standalone action and retains its canonical icon structure; it is not an inline-link style. Do not invent link classes.

Do not use deprecated `ai-textlink`, `teaser-grid__*` or other unlisted link classes.

## Lists

Plain unordered, ordered, nested, bullet and checkmark variants are Embedded Components, never standalone Page Modules. Use semantic `ul/li` or `ol/li`; nest only for real hierarchy. `list-bullet` is for deliberate short bullet/benefit lists. `checkmark-list` is only for short positive benefit/feature lists, not sequential or mixed-status content. Preserve its item/icon/text structure.

## Media

Teaser/card media is 4:3 with 800×600 or larger recommended. Hero/stage media is 16:9 with 960×540 or larger recommended; 1920×1080 is a high-quality option. `lpb-image--responsive` provides containment only and must not become an automatic crop/upscale system.

Scaling Editorial has two separate image roles with intended production sizes: title image 1920×1080 pixels; author portrait 240×240 pixels. Never substitute one role for the other. Adopt complete safe image URLs from the Article Package or author registry. HTML `width`/`height` attributes describe the intended image dimensions and layout, not a claim that a file inspection occurred.

For image URLs, do not require a download, decoding, independent pixel measurement, reachability probe or another image-verification step before Contentful Actions. Do not require ZIP files, image checksums or substitute evidence. An execution-environment DNS or network failure is not evidence of a faulty image and is not a Draft or publication blocker; report an unperformed visual check accurately without inventing a successful inspection. Missing, incomplete or unsafe URLs and unresolved placeholder addresses still require clarification; automatic TEXT_TEST or placeholder selection is not active in this Publisher. These image rules do not relax the Contentful HTML transport, read-back or integrity checks in `contentful-integration.md`.

Informative images require meaningful supplied alt text; decorative images use `alt=""`. Missing safe context is `ASK`. For the B2B Handbook Draft only, an informative source screenshot with a supplied safe image URL but without verified alt may use the documented mechanical fallback from its directly associated heading or exact source text; retain `ALT REVIEW REQUIRED`, report it and do not claim publish readiness. A confirmed missing source asset is `ASSET GAP`; an execution-environment DNS or network failure does not establish such a gap, and no image fetch is required to establish URL usability.

Do not invent crop/object-fit, aspect-ratio, `srcset`/`sizes`/`picture`/`source` or background-image systems unless a canonical module owns that verified exception.

## Colors and surfaces

The Component Library defines the selectable LPB accent colors, neutrals, text colors and surfaces. All shown variants are user/developer capabilities, but selection never overrides a module-specific locked color, required contrast, readable focus state or accessibility rule. Use only the exact Library classes; no free hex, RGB, inline color, arbitrary token, deprecated background or invented accent-text class.

## Icons

Keep the current safe icon model. Use only an exact class from `cosma-icons-static.md` or an icon/SVG/asset already protected by a canonical module/component. Canonical names include the `s24-icons-s24_` prefix; never shorten or generate names by pattern. The host centrally loads the icon font; do not add `@font-face`, a stylesheet or font assets.

Compact LP icons use a genuine `_24` glyph plus `lpb-icon--24`; benefit/feature/value/large marketing icons use a genuine `_48` glyph plus `lpb-icon--48`. `_16` glyphs are product-UI/small-control reference only and no `lpb-icon--16` exists. Never mix glyph and adapter sizes, scale icons, expose the full inventory as a free user library, substitute a protected module asset automatically or invent SVGs. Existing inline SVGs, external SVGs and component-specific Chevrons remain allowed only in their validated canonical blocks. Icons inherit `currentColor`; decorative icons use `aria-hidden="true"`, and meaningful icons need visible text or another accessible name. Missing fit is `VERIFY` / `ICON GAP`.

# Editorial module policies

## scaling-editorial-article-teaser

Use:
- Use this Embedded Component inside the featured or lower-grid slots of `scaling-editorial-category-overview`. The same card structure can later serve a mixed-category overview; this does not authorise creating a homepage now.
- It never becomes a Top-Level Page Module and its outer `div[data-lpb-component="scaling-editorial-article-teaser"]` remains inside the consuming module.

Required:
- One 16:9 image, one visible primary-category line and one H2 title. Use `lpb-editorial-teaser--lead` for the first article, `lpb-editorial-teaser--compact` for the next up to two and `lpb-editorial-teaser--card` for all remaining articles, on the existing `article` element.
- A real lead requires the linked article's complete intro verbatim. Compact and lower-grid cards omit the intro paragraph from their HTML; keep the original intro in the article data for later promotion. Never independently rewrite a teaser summary, truncate text or hide overflow.
- Publication date is optional: preserve a supplied editorial date using `time[datetime]` in the existing date paragraph; omit the paragraph if missing. Never derive a date from the current day, draft timestamp or Contentful update time.
- Do not show author names, subcategories or topic tags in a teaser.
- For internal MVP overview placeholders follow the category-overview contract: visibly recognizable Lorem-ipsum text and accessible placeholder name, without an image badge. Other demo media/copy retains its applicable labeling.

Links:
- Without a complete supplied and verified destination URL, render no anchor, button or simulated link affordance.
- Once a complete safe destination exists, the complete teaser may gain one semantic link wrapper without changing its internal media, metadata, title or summary order.

Locked:
- Preserve the component wrapper, `article`, media, content and typography structure.
- This first local slice uses the verified IS24 placeholder image URL. Never use a Data URI or invent an external asset URL.

## scaling-editorial-more-articles

Use:
- Use this Embedded Component only in the sidebar slot of a Scaling Editorial portal Page Module.
- It never becomes a Top-Level Page Module.

Required:
- Preserve the `aside` landmark, visible `Weitere Artikel` H2 and semantic list.
- Each item is a vertical card: one 16:9 image spanning the complete sidebar width, one small muted primary-category label in `.lpb-editorial-more-articles__meta` above one readable H3 headline, and optionally the supplied editorial publication date beneath the headline in `.lpb-editorial-more-articles__date.font-body-small-regular` with `time[datetime]`. Omit that whole date paragraph when the date is missing; never derive it from a Contentful timestamp or the current date.
- Do not show intros, author names, subcategories or topic tags in sidebar cards. Category, headline, image and optional publication date come from the recommended article's supplied data, not the currently opened article.
- Presentation target: up to three distinct existing recommendations in supplied order; show fewer when fewer valid articles are available, and omit the sidebar component when none exist. Never invent an article to reach three. Local canonical examples contain up to three explicitly marked demo items and do not claim verified article identities.
- Exclude the current article when real article data is introduced.

Links:
- For real recommendations, require the existing verified article destination and wrap the complete image and content in exactly one direct `a[href]` child of the list item; preserve the actual URL. No nested anchors, buttons or partial separate links. Exclude a recommendation without a verified target rather than inventing a URL. Only the clearly marked local canonical demo may remain unlinked, without simulated link affordance.
- Keep keyboard access and the shared visible focus outline on the complete card. Keep the current article excluded by verified article identity/Entry ID or its existing destination, not just by headline.

Locked:
- Preserve the outer Embedded Component `div`, `aside`, list and complete-item structure.
- Selection and order come from one supplied editorial dataset; do not independently rewrite duplicated teaser or sidebar facts.

## scaling-editorial-news-nav-categories

Use:
- Use this Page Module for the first category-overview MVP without a News homepage.
- It is a separate canonical module so the existing `scaling-editorial-news-nav` and its article test Page remain unchanged.

Required:
- Preserve the `nav` landmark, accessible label, inner container and list structure.
- Render no Home item or Home icon.
- Exactly one category item carries both `lpb-news-nav__item--active` and `aria-current="page"`.
- Preserve this ordered taxonomy exactly: `Immobilienmarkt`, `Mieten`, `Kaufen & Verkaufen`, `Finanzen`, `Recht & Politik`, `Wohnen & Architektur`, `Lifestyle`.
- Exactly one item matches the supplied primary article or overview category and carries the active state.

Links:
- Keep an item as a non-interactive `span` until its destination Page exists and a complete safe URL has been supplied and verified.
- Only then may that complete item element change from `span` to `a` with its verified `href`. Never emit `href="#"`, an invented slug or another placeholder destination.

Locked:
- Preserve the single `lpb-news-nav` root and existing item classes. Do not hide a Home item with CSS; the Home list item is absent from this module's HTML.
- Full-bleed background, 1200 px host-grid alignment and horizontal mobile overflow remain Bridge-owned. Both News navigation variants share a white background, Charcoal `#333333` text, a single thin bottom separator, the existing turquoise active-item underline and a visible dark keyboard-focus outline; preserve active state, semantic links, existing item sizes, spacing and alignment. This is a color inversion, not a navigation redesign.

Runtime:
- Static HTML and Bridge CSS only; no JavaScript or additional runtime dependency.

## scaling-editorial-category-overview

Use the category overview after the home-free category navigation. Preserve one H1, the category header, actual category identity and every existing real article's data/link/order. Filter to the exact category and deduplicate real article identities. This overview has no recommendations sidebar.

The approved internal MVP layout uses one shared three-column base on desktop: first article as lead spanning two columns, next up to two as compact cards stacked in column three, then three equal-width cards per lower row. Use `lpb-editorial-overview-featured lpb-editorial-overview-featured--three-columns` and `lpb-editorial-overview-grid lpb-editorial-overview-grid--three-columns`. The renderer-owned Bridge already implements these variants. At 900 px and below all cards follow DOM order in one column. Preserve the host container, 32-px horizontal gutters and module-owned spacing; no inline CSS/loaders.

For the current internal MVP, render all existing ordered real articles and fill free display slots up to six with the canonical neutral placeholder teaser. With no real articles, show six placeholders in the same 1+2+3 composition. A placeholder lead has no invented journalistic intro. When there are more than six real articles, retain them all and continue the lower rows; do not silently drop articles or duplicate the lead. Recompute slots from real article data: an arriving real article replaces a placeholder rather than becoming an extra duplicate. Ignore placeholders when identifying articles and building recommendations, signal records or article counts.

Placeholders use only the existing light-grey IS24 image URL, empty decorative alt text, `aria-label="Platzhalter-Teaser"`, exact Lorem-ipsum headline and the actual category label. They have no visible image badge, link, author, date or article Entry. This explicitly approved layout filler is confined to internal MVP overviews. Preserve draft/demo status; it is not authorization to publish placeholders as journalism. An explicitly requested sparse/public overview requires a separate appropriate layout decision, not an automatic carry-over of demo filler.

Keep real lead intro verbatim from the linked article; compact/lower cards omit intros. Recover the full intro from the actual article when promoting a card. Preserve real image, headline, category, optional supplied date and verified destination. One real card may have one whole-card anchor, no nested links. Placeholder cards remain unlinked.

The module and its embedded teaser wrappers stay inside one `lpb-explicit-spacing` root with the canonical ending. Use the library's complete module/component structure. No extra homepage, client router or runtime dependency.

## scaling-editorial-article-with-sidebar

Use:
- Use this composed Page Module for one Scaling Editorial article detail page with recommendations after `scaling-editorial-news-nav-categories`.
- The module owns one shared two-column portal layout, one complete internal Article V2 structure in the main slot and one `scaling-editorial-more-articles` component in the sidebar slot.

Required:
- Preserve `lpb-editorial-portal-layout`, its main and sidebar slots and the complete internal `.lpb-editorial-article` structure.
- The preceding `scaling-editorial-news-nav-categories` module marks the article's supplied category as its single active item; all seven taxonomy items retain the existing verified-link upgrade path from that navigation policy.
- The internal article follows every content, heading, media, source and demo-safety rule from `scaling-editorial-article`, including exactly one H1, 16:9 media, a maximum 720 px reading column and verified HTTPS sources for real editorial content.
- Preserve one complete `scaling-editorial-author` component with resolved or explicit Draft-state author master data plus the article-specific date and reading time. Ordinary article work may show applicable central-taxonomy tags; Article Package work follows its explicit non-visible tag rule.
- For an explicitly requested, visibly labelled internal demo article, the narrow non-linked demo-source exception from `scaling-editorial-article` applies unchanged.
- An explicitly requested safe `static-inline-svg-diagram` may be placed as a complete content unit inside the internal `.lpb-editorial-article__body`; apply its full component policy without changing the article or portal layout.
- Use one complete `scaling-editorial-more-articles` component with up to three available entries; the local canonical slice contains three demo items. Exclude the current article, use fewer when fewer valid recommendations exist and omit the sidebar component when none exist. Never invent a recommendation to fill the count.

Composition:
- This Page Module is one direct child of `lpb-explicit-spacing`; the internal article structure and Embedded Component remain inside its slots.
- The internal `.lpb-editorial-article` is structure, not a nested `LP_MODULE` block. Never add `LP_MODULE` markers, Page spacers, another Page Module, a second navigation or a global header/footer inside this module.
- Keep the internal Article V2 structure synchronized with the canonical `scaling-editorial-article` module without changing that existing module.
- Desktop uses the existing Bridge-owned portal grid and sticky 320 px sidebar. At 900 px and below, the sidebar follows the article in DOM order.

Links and content:
- Article and sidebar facts come from one supplied editorial dataset and remain consistent for the same article identity.
- Without complete supplied and verified destination URLs, sidebar items remain non-interactive. Never invent a slug, external URL or `href="#"`.
- Demo text and placeholder images remain visibly labelled and must never be presented as journalism.

Runtime:
- Static HTML and existing Bridge CSS only; no client router, page script or additional Runtime behaviour.

## scaling-editorial-news-nav

Use:
- Use this Page Module as the reusable secondary navigation for Scaling Editorial News pages. It is separate from the article so the same navigation can be used on the News start page, category pages and article detail pages.

Required:
- Preserve the `nav` landmark, accessible label, one Home item and the ordered category items `Immobilienmarkt`, `Finanzen` and `Wohnrecht`.
- Exactly one item carries both `lpb-news-nav__item--active` and `aria-current="page"`. The active item is configured per page and must represent the current News destination or article category.

Links:
- Keep an item as the canonical non-interactive `span` until its destination page exists and a complete safe URL has been supplied and verified.
- Only then may that complete item element change from `span` to `a` with its verified `href`; preserve its classes, content and active state. Never emit `href="#"`, an invented slug or another placeholder destination.

Locked:
- Preserve the single `lpb-news-nav` root, inner container, list order, Home icon structure and item class names. Do not add a second global header, footer, logo or main navigation.
- Full-bleed background and horizontal mobile overflow are Bridge-owned. The inner navigation follows the 1200 px Contentful host grid with responsive inner spacing of 16 px, 24 px and 32 px.
- Use the same white surface, Charcoal `#333333` text, thin bottom separator, existing turquoise active underline and dark keyboard-focus outline as `scaling-editorial-news-nav-categories`; preserve item sizes, spacing and alignment, with no additional panel, shadow or global header.

Runtime:
- Static HTML and Bridge CSS only; no JavaScript or additional runtime dependency.

## scaling-editorial-article

Use:
- Use this Page Module for a complete Scaling Editorial article detail page. The named `Scaling Editorial Article Template` composes it after `scaling-editorial-news-nav`.

Required:
- One non-empty category in `data-lpb-article-category`, exactly one H1 headline followed by exactly one preserved subline in the header, one complete `scaling-editorial-author` component after that header and before the title media, one title image using the supplied complete safe URL and intended production size of 1920×1080 pixels with its optional single caption, at least one article paragraph and at least one complete source entry. No file inspection or independent pixel proof is a prerequisite.
- Preserve this visible article order in both variants: H1 → subline → author component → complete title-media figure including its caption → article body. Keep the author component in the article's metadata block outside the header and body. The category may remain before the H1 according to the existing navigation/badge rule. When topic tags are rendered outside Article Package work, place their single list after the article body so it does not interrupt this sequence.
- Article headings follow semantic order: article chapters use H2; an H3 is allowed only beneath a preceding H2. The sources heading is an H2.
- Use only the supplied primary category from the ordered taxonomy `Immobilienmarkt`, `Mieten`, `Kaufen & Verkaufen`, `Finanzen`, `Recht & Politik`, `Wohnen & Architektur`, `Lifestyle`.
- Topic labels use only applicable names from the central taxonomy: `Kaufpreise`, `Mietpreise`, `Bezahlbarkeit`, `Angebot & Nachfrage`, `Neubau`, `Wohnungssuche`, `Nebenkosten`, `Umzug`, `Baufinanzierung`, `Bauzinsen`, `Förderung`, `Mietrecht`, `Wohnungspolitik`, `Energie & Sanierung`, `Besondere Immobilien`, `Einrichtung`, `Wohntrends`.
- Topic labels remain non-interactive until a complete verified destination exists. Do not treat locations, story formats or technical analysis terms as topic tags.

Counts:
- Exactly one `scaling-editorial-article` module per Page; do not combine it with marketing Page Modules in the MVP.

Editable and repeatable:
- Category, headline, subline, title-image URL, `alt`, optional caption and optional AI label, article paragraphs, H2/H3 headings, source labels and safe source URLs.
- The subline remains the exact intro used by the corresponding large category teaser; placing it after the H1 never authorises rewriting or duplicating it.
- Editorial recommendation for newly written intros: 1–2 complete sentences, approximately 180–260 characters including spaces (roughly 25–40 words), giving the reader the subject and its relevance. This is guidance, not a validation limit: preserve supplied longer or shorter intros in full; never truncate, line-clamp, hide overflow or append an automatic ellipsis.
- The existing ImmoScout24 font family and canonical typography classes remain. Bridge-owned article-only hierarchy is H1 36/44 px, intro 22/32 px, body 18/28 px, H2 28/36 px and H3 22/30 px on desktop; at 668 px and below H1 is 28/36 px, intro 20/30 px, body 18/28 px, H2 24/32 px and H3 20/28 px. Captions are 14/20 px. The intro is regular-weight Charcoal, larger than the body; these overrides never become global typography variants.
- Add or remove complete article paragraphs and H2/H3 content units as required by the supplied article. Add or remove complete source-list items without changing the surrounding module structure.
- When explicitly requested, add or remove a complete safe `static-inline-svg-diagram` content unit inside `.lpb-editorial-article__body`; never place it in the article header, title-media or sources structure.
- Without the News navigation, render the category in `.lpb-editorial-article__category`. When the preceding News navigation already marks the same category as active, add `lpb-editorial-article--with-news-nav` to the article root so the badge is hidden while the category remains in `data-lpb-article-category`.

Hero captions:
- For a confirmed AI-generated hero illustrating a general topic, render exactly one visible caption span: `KI-generiertes redaktionelles Symbolbild`. Omit additional descriptive or thematic caption text; keep the meaningful supplied alt text for accessibility. Deduplicate identical caption and AI-label metadata rather than printing the label twice.
- For a specific real building, person, place or event, retain the shortest necessary non-documentary clarification after the AI label, for example `KI-generiertes redaktionelles Symbolbild – keine Aufnahme des beschriebenen Gebäudes.` Omit an optional introductory thematic sentence. Preserve required factual credits for other image types and the visible technical-placeholder notice when that exception applies.
- This display rule applies to article hero images in both variants. It does not shorten chart source captions, remove source evidence or change the image or its alt text.

Sources:
- For every real editorial article, each source-list item requires a semantic `a[href]` with a complete verified `https` URL before a Contentful Draft.
- Use the exact visible H2 `Quellen`. Keep the aside unboxed with no surface class or grey background, one thin muted top divider, no horizontal padding, and a marker-free list aligned to the same left text edge as the body. Bridge typography is 18/26 px for the heading and 14/22 px for entries on desktop and mobile. Every entry remains visible; no disclosure, accordion, clipping or hidden list.
- Link text is `{supplied publisher} – {short supplied source title}`, optionally with the supplied publication date. Do not expose full URLs as labels or shorten/change the actual `href`. Preserve all existing destination URLs exactly; retain factual supplied dates and qualifiers. Never infer publisher or title from an unverified URL or invent source details; clarify missing labels. The existing narrow non-linked demo exception below remains applicable.
- Narrow demo exception: only when the user explicitly requests an internal demo article and the entire article is visibly marked as demo, preserve `.lpb-editorial-article__sources`, its sources H2, `.lpb-editorial-article__sources-list` and at least one `li`. A demo source entry may contain `<span>Keine redaktionellen Quellen – Demo-Inhalt, noch nicht zur Veröffentlichung freigegeben.</span>` instead of `a[href]`.
- This exception never applies to real editorial articles. It does not relax their verified-HTTPS source requirement.
- `href="#"` remains forbidden for every Contentful Draft, including demo Drafts.

Locked:
- Preserve the single `lpb-editorial-article` section, header, 16:9 media, subline, body and sources structures and their class names. Never duplicate the H1, subline, title image or figcaption while applying the canonical order.
- Preserve the supplied title-image URL and intended production size of 1920×1080 pixels with canonical HTML `width="1920" height="1080"`; these attributes do not claim a completed file check. Do not require independent image verification before draft writing; this Publisher never publishes. Without caption data preserve the original media structure. With supplied caption or AI-label data use only the canonical `lpb-editorial-article__media--with-caption` structure; do not add sharing controls, sidebar, recommendations, navigation or footer inside this module.
- Use meaningful supplied alt text when the image conveys information. Use `alt=""` only for a genuinely decorative image; missing safe context is `ASK`.

Runtime:
- Static HTML and Bridge CSS only; no JavaScript or additional runtime dependency.

## scaling-editorial-pilot-notice

Use:
- Optional Embedded Component for a Scaling Editorial article section in either `scaling-editorial-article` or `scaling-editorial-article-with-sidebar`. Never a Top-Level Page Module, page spacer or part of the author component.

Required and locked:
- Preserve exactly `<div data-lpb-component="scaling-editorial-pilot-notice" role="note"><p class="font-body-medium-regular margin-top-none margin-bottom-l">Technischer Pilot – fiktives Autorenprofil</p></div>`.
- Insert exactly once as the first child of `.lpb-editorial-article`, immediately before `.lpb-editorial-article__header`, outside `.lpb-editorial-article__body` and `.lpb-editorial-author`. Do not hide it or abbreviate its text.
- Preserve the sequence after the notice: H1 → subline → author component → title-media figure including caption → article body. Keep the existing category/badge rule. The notice is outside the reading-time count and must not be copied into the intro or large teaser.
- This is a preserved legacy component, not a publication exception. Preserve an existing explicitly scoped notice during partial edits; do not automatically add it to regular new articles with confirmed real authors.

Runtime:
- Existing typography and spacing utilities only; no new CSS, scripts, fields or runtime dependency.

## scaling-editorial-author

Use:
- Use this Embedded Component only in the article metadata block after the headline/intro header and before the title media of a Scaling Editorial article structure.
- It never becomes a Top-Level Page Module.

Required:
- Preserve the single `.lpb-editorial-author` wrapper, `data-lpb-author-id`, `data-lpb-author-status`, content wrapper, name, role/expertise, facts, date and reading-time hooks. In both Scaling Editorial article variants place this same component after the headline and intro and before the complete title-media figure, outside the article header.
- A resolved author contains the exact complete safe registered portrait URL and non-empty master-data name and role/expertise. The intended portrait production size is 240×240 pixels; retain HTML `width="240" height="240"` without claiming a file check or requiring independent pixel proof. Bridge CSS alone controls its smaller visible size. Apply the central author registry and Article Package contract; never invent or alter identity, expertise, portrait, profile, dates or reading time.
- The name is a `span` when no verified profile URL exists. It may be an `a[href]` only for a complete verified safe HTTPS profile URL. Preserve identical typography and DOM position for either element.
- A verified date uses `time[datetime]`; an open Draft value remains plain text. Use only the canonical `Veröffentlicht:` / `Aktualisiert:` labels and reading-time forms.
- Bridge presentation uses a round portrait at 48 px on desktop and 40 px at 668 px and below, a bold 14/20 px name followed by the registered 14/20 px role/expertise, and a secondary 12/18 px facts row for the supplied publication date, optional supplied time/update date and calculated reading time. Identity and facts wrap naturally; never hide missing author data by substituting another profile or an invented date.
- An unassigned sample in the canonical library is historical demonstration markup, not an allowed intake fallback. New assignments require the confirmed real Inga/Julia record and complete canonical author component; invent no alternative component or modifier class.

Locked:
- This existing static component has no biography, social links, author selector, automatic account lookup, Wiki request, client script or Runtime behaviour. The optional scaling-editorial-author-dialog variant is governed exclusively by author-dialog.md; it is not yet a released CMS default and does not authorize per-page scripts.
- Do not render author status as visible copy inside this component. In particular omit `(Platzhalter)`, `Test-Schwerpunkt:` and `Testplatzhalter – nicht veröffentlichen`; their safety meaning remains in the registry, `data-lpb-author-status` and publication checks. The separately scoped pilot notice belongs before the article header, never inside this component.
- Keep author master data separate from article-specific facts. The Bridge owns only responsive presentation and never resolves, calculates or mutates author data.


## scaling-editorial-author-dialog

Optional Embedded Component in the same metadata slot, not a Page Module or an automatic replacement. Read author-dialog.md in full before any related work; it defines release evidence, user-approved biography, exact markup, fallback and testing. Existing static author rules and the current article layout remain active outside an explicitly authorized, technically ready overlay installation.
