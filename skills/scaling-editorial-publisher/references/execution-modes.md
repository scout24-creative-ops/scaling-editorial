# Publisher execution modes

## Standalone scope

Use the supplied finished Article Package and the actual current user order. This skill owns its complete local CMS rules and component library; no separate publisher, LP Builder, coordinator or Production Records skill is required. It does not start upstream research, writing, image or chart work. No scheduled execution is configured.

A new Magazine article includes its draft plus News and matching rubric teasers under required-inputs-and-placement.md, unless the current user explicitly narrows the scope. A package produced by a Writer in the same conversation is only an artifact until the user requests implementation. An already-active coordinator may pass its explicit CMS scope without being called recursively.

## Required personal decisions

For an implementation, obtain exactly one confirmed real author (Inga Ervig / Julia Walter) and the user-selected full hosted image URL before CMS calls or HTML construction. Existing explicit answers for this exact article need not be repeated. Read-only setup/review and HTML-only preparation retain their limited endpoints and do not authorize writes.

No unassigned author, test author or automatic TEXT_TEST/grey-image fallback is active. A draft/test request does not bypass intake. Keep the selected actual image and supplied matching alt/caption/credit/disclosure in article and both teasers. A generated/downloaded PNG is not a hosted URL; this adapter cannot upload image assets. Missing/unsafe/ambiguous URLs require concrete clarification. Do not generate, fetch or upload replacement images just to fill the input.

The component library contains historical demo media and author examples. They demonstrate markup, not new article defaults. Preserve existing unrelated legacy content and notices on partial updates; do not copy fixture identities, dates or placeholder media into a regular new article.

## Resume, partial outcomes and records

Inspect an identified existing draft before resuming a creation. Keep the confirmed article ID, site, slug and current personal choices; never create another article to repair a missing overview placement. Check an uncertain write by reading the exact target before retrying. Complete only missing/unverified article, News or rubric operations; deduplicate the article separately within each overview.

Report the three CMS outcomes separately with actual IDs, internal slugs, returned preview links and concrete gaps. Full success requires all requested outcomes stored and read back. No atomic transaction, rollback, deletion or publication is implied.

For the current user-ordered new Magazine intake, maintain its production record and Signalregister entry directly through Scout Wiki under wiki-production-records.md. Reuse the complete selected TF/SC/Writer packages actually available in this chat or readable inputs; no separate records skill or coordinator is needed. An explicit CMS-only instruction opts out. Read-only checks and HTML preparation never write to either system. Narrow existing-page edits do not trigger retrospective package collection. Missing Wiki rights or upstream packages remain separately reported documentation gaps, not invented archives or a blanket block on independently valid CMS work.

Keep all five requested outcomes distinct: article, News teaser, rubric teaser, full Wiki record, registry entry. CMS and Wiki have no shared transaction. An incomplete Wiki step does not authorize another CMS create or resetting a previously confirmed identity. Resume the same record, reserved Signal-ID and exact CMS entry; preserve older package versions and other editors' work. The parent Produktionsakten index remains unchanged.

## Allowed operations

For CMS work only native get_lp_builder_page, create_lp_builder_page and update_lp_builder_page of Contentful Landing Page Builder MCP, with explicit site on every call. For the specifically authorized Wiki work only Scout Wiki operations under wiki-production-records.md. No Dev adapter, uploads, forms, Storybook actions, lifecycle calls or parallel backend. A missing creation capability blocks creation, not an independently requested supported existing-entry update. For safe inline-HTML limits and full pre-/post-read requirements use contentful-integration.md. Never treat optional technical availability as authority.
