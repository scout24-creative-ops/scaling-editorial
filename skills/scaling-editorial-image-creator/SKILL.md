---
name: scaling-editorial-image-creator
description: 'Erstellt redaktionelle ImmoScout24-Bildmotive aus dem fertigen Artikel und exportiert zwei 16:9-WebPs: 1920 × 1080 für Titel/große Teaser und 480 × 270 für kleine News- und Weiterlesen-Teaser. Prüft die Original-Frontify-KI-Kennzeichnung je Ausgabe. Erstellt separat beauftragte quadratische WebP-Autorenporträts. Nicht für reine Text- oder Headline-Tests. Frühere Namen: se-image-creator, scout24-editorial-imagery.'
---


# Scaling Editorial – Image Creator (MVP)

Earlier instructions may refer to this same personal skill as `se-image-creator` or `scout24-editorial-imagery`. Use the current personal edition `scaling-editorial-image-creator`; the skill identity and operational scope are unchanged. These are previous names, not other skill dependencies.

## Purpose

Generate one editorial image that fits the article and feels visually related to Scout24 / ImmoScout24 photography. Prioritize a believable, clear overall look, not perfection or strict replication of campaign photography. Use the image-generation tool already available to the agent; this skill supplies art direction, not a connection to another agent.

Use the supplied Frontify AI-label instructions and original assets for visible disclosure. Treat the remaining photographic direction as an editorial adaptation of Imagery Builder guidance, not a certified corporate-brand standard or a reproduction of that separate agent. Use the stricter Seeker campaign look as a reference, not a compulsory template for every article.

## When to run

- Run when an editorial title image, article visual or author portrait is explicitly requested, or when the host agent's own instructions require an image as part of its article output. Do not create an author portrait as part of an ordinary article assignment.
- In `HEADLINE_TEST` or other text-only tasks, do not generate an image.
- For an explicitly requested image concept, deliver the concept only; do not generate a raster or claim an export.
- Follow the host agent's article/output instructions; this skill only governs imagery.
- Before producing a Writer's title image, read the final headline, intro and complete written article, not only the topic, an earlier Story Package or a presumed previous message. Use the supplied Story Package for evidence and visual boundaries. Request an actually missing handoff instead of pretending to have read it. For a standalone image or concept request, use its explicit briefing. Do not browse for new factual claims.

## Ownership and handoff

Keep motif choice, photographic style, symbolic-image decisions, crop checks, dimensions, export, filenames and image metadata in this skill. The Writer owns the article, decides whether imagery is in scope and supplies the final text plus any actual asset or naming requirements. Read the references required for the selected branch; do not assume access to another agent or an unprovided article. A skill is not an image-generation connection.

## Minimal workflow

1. **Read the final handoff and identify the picture's job.** Apply the input requirements above. Determine whether the final text concerns a specific real property, person, location or event, even when the package contains no image warning. Apply the symbolic-imagery decision below. Define what readers should recognize at a glance; preserve the actual story angle.
2. **Choose the motif deliberately.** Apply the subject-selection rules below: consider three distinct concepts internally, then select one for its story fit and thumbnail clarity. Generate only the selected concept.
3. **Direct the photograph.** Apply the selection and style rules below. Specify a dominant subject, context, perspective, lighting, composition, palette and exclusions. For motif examples, concert/Lifestyle direction or selection evidence, read [references/editorial-style.md](references/editorial-style.md); its examples are options, not compulsory topic templates.
4. **Generate the image.** Use one unlabelled 16:9 source for the 1920 × 1080 title/large teaser and the 480 × 270 compact teaser. Keep breathing room in the lower corners. A separately requested 240 × 240 author portrait uses a square source. Generate without lettering; add the original artwork during export. Check actual raster dimensions.
5. **Check, label and export the result.** Read [references/ai-labeling.md](references/ai-labeling.md), classify the provenance and actual edit, apply the practical visual check, then complete the technical export with the required original Frontify label in the same assignment. Correct one clear visual failure when regeneration is supported; do not generate alternatives merely for variety. Retain exactly one selected unlabelled source for both exports; never generate a second scene for the teaser. A generation prompt or preview does not establish file dimensions.
6. **Deliver.** Apply the image-output contract below. Keep the completed article available if generation, file access or export fails. Name the actual missing step and never invent a file, hosted URL, successful export or verified dimensions.

## Visible AI disclosure

- Read [references/ai-labeling.md](references/ai-labeling.md) before any raster export. Apply **AI created** to newly generated images or imagery whose visual core is substantially AI-created, including generated portraits. Apply **AI modified** to substantial AI changes to a pre-existing human-made image. Use no label for unchanged authentic images or only minor technical corrections; do not remove the generated classification from an already AI-created image.
- Apply the supplied original Frontify mark separately after sizing each WebP when the source qualifies. The compact News/Weiterlesen file is labeled too; there is no small-slot exception. Use the approved positive or negative artwork on a suitable corner with margin. Keep an existing correct mark without duplicating it if only a marked source survives; note small-size legibility limits.
- Preserve required captions and factual symbolic-image clarifications. Record the visible label status separately in the existing `Kennzeichnung` field. Treat a missing or unchecked label as an unfinished step, not a completed export.
- Keep final imagery as a human-review draft. Implement the supplied labeling instructions now; do not defer them wholesale to the editorial team or claim legal compliance from applying an asset.

## Technical export after generation

- Obtain the actual raster file from the image-tool result or available files. Do not assume that the native preview is the final upload file, or invent a source path. If a newly generated file is not exposed to code execution, report that specific gap; success exporting a reattached file does not prove this handoff works.
- With the actual source and Pillow, run [scripts/export_editorial_image.py](scripts/export_editorial_image.py) once with `--kind title` and once with `--kind compact`, both to distinct `.webp` paths. Use `--kind avatar` only for an expressly requested portrait (240 × 240 lossless WebP). Default editorial quality is 85. Use `--label modified` or `--label none` only with a truthful `--label-reason`; never suppress a required mark.
- Verify two actual WebP files and identical source checksum and 16:9 crop box. The exporter adds the original artwork after sizing each output. Inspect framing, edges, compression, disclosure and bytes; a contrast estimate is not visual proof. Report uncovered legibility issues without claiming publication approval.
- Reuse the one labelled 1920 × 1080 file for the title and all large/medium teasers; reuse the one labelled 480 × 270 file for small News and article-side Weiterlesen (128 × 72 display each). Do not create another size or a separate labelled/unlabelled compact variant.
- Export only the selected source file; do not call image generation during resizing, renaming or delivery. A technical export can change cropping, resolution and the prescribed disclosure overlay; keep people, objects and the depicted scene unchanged. If the source cannot be identified unambiguously, report the gap rather than choosing an arbitrary file. Align alt text and caption with the selected final image.
- Select the filename using the naming convention below. Keep the original image; the script refuses overwriting. Deliver exactly the verified title/compact pair for an ordinary article image, one file for an explicitly requested portrait or narrower single-role export. No third size, alternative motif, repeated download links or preview sheets unless requested. Earlier generation drafts may remain in chat history; when a correction occurred, briefly identify the final download as the corrected selection. Do not export the discarded draft as another final asset.
- If code execution, Pillow, source-file access or downloadable export is missing, state what is missing and that technical preparation remains open. Preserve the generated original and the full text output. Do not claim publishing-ready dimensions or silently substitute a text placeholder.

## Teaser roles and fixed page design

- Apply the two-file mapping above to every current Magazine slot, including News, Immobilienmarkt and Lifestyle.
- Both editorial files are 16:9. Do not stretch the scene or change the article layout.
- Inspect the large file at hero and card sizes and the compact file at 128 × 72. Keep the complete mark within the frame and do not let it dominate; state if it is too small to read comfortably.
- Return the two actual filenames, dimensions, bytes and disclosure statuses. Hosting is separate; never invent a hosted URL.

## Subject selection and variety

- **Show the story's subject.** Start with an observable object, building, spatial situation or relevant action that expresses the actual angle. For heating costs, consider heating equipment or a reading situation before a person thinking about a bill. For an abstract policy story, choose a clear housing connection without inventing an affected household.
- **Consider three genuinely different concepts internally.** Use different approaches where suitable: an object/detail, a building/environment, or a meaningful human action. Select the strongest story fit, then visual clarity and distinctiveness. Do not output the shortlist or generate three images unless asked. Honor a supplied motif when it passes the factual-reference check; otherwise preserve its thematic purpose with a clearly generic alternative.
- **Compose for small news teasers first.** Make one subject or meaningful action visually dominant, with few supporting details and clear separation from the background. Prefer a close detail or medium view when it carries the story. Choose a wide view when space, architecture or scale is essential and still legible; proximity is a starting preference, not a universal close-up rule. A collection of tiny people, objects or buildings is not a substitute for a focal point.
- **Give people a useful action.** Include them when what they do explains the topic. Choose credible casting for that action; age, gender or a concerned expression alone is not a picture concept. Papers at a kitchen table are one possible scene, not the default for finance, legal or service stories.
- **Create curiosity through specificity.** Use a revealing detail, plausible action, spatial relationship or interesting perspective. Preserve the actual story promise; avoid exaggerated distress, staged mystery and unsupported visual contrasts.
- **Keep style consistent and motifs flexible.** Treat examples as possibilities, not fixed topic-to-image assignments. When recent images or motif notes are supplied, vary subject, setting or framing meaningfully; changing clothing or gender alone is insufficient. Without that context, do not claim knowledge of earlier generations or guaranteed cross-chat variety. Do not require a motif history before producing an image.

## Specific real subjects and symbolic imagery

- **Decide autonomously before generation.** When an article concerns a specific real building, person, location or event, distinguish the documented subject from a generated scene. Choose a thematically relevant generic motif that works without being mistaken for that subject. Do this even when the Writer or Story Package has not flagged the issue. Original-photo requests and human approval of each motif are not prerequisites for this fallback.
- **Show the underlying theme.** Prefer an observable detail, ordinary residential situation or meaningful generic action. For a named building's heating concept, consider sunlight entering a generic living room rather than an invented exterior, interior, resident or technical installation attributed to the project. Keep the photographic style and vary the motif according to the actual story; this example is not a fixed template.
- **Keep the scene truthful on its own.** Do not create a photorealistic reconstruction or lookalike of the specific subject, including from a reference photograph, and pass it off as project documentation. Avoid invented project-specific architecture, equipment, conditions, measurements or witness scenes. A caption cannot rescue a misleading motif: change the motif first. Keep explicitly requested author portraits under the separate portrait rules.
- **Make the distinction visible in the caption.** For a named real case using a generated symbol image, use the short `Bildunterschrift` clarification `KI-generiertes Symbolbild – keine Aufnahme des beschriebenen [Gebäudes/Orts/Ereignisses/der Person].` Adapt its grammar and reference; a note only in alt text or internal metadata is insufficient. Preserve it in the Writer handoff and wherever a caption accompanies the image. Use the image-output contract for the remaining metadata and delivery.
- **Complete the normal delivery.** Select one motif, generate one final image and apply the existing export, naming and download rules. Do not introduce an original-image procurement step, additional variants or an extra image approval gate. For general-topic articles, retain the ordinary symbolic-image labeling without adding an irrelevant named-project disclaimer.

## Celebrity and event news in the current MVP

- Use an independently generated, clearly generic thematic symbol image when no original image is supplied. Generic performers, fans and other people are allowed; a real person's name in the article is not a request to depict that person. Do not introduce image purchasing, licensing research or an original-photo request as a prerequisite.
- For a named singer, a generic performer seen from behind, a non-identifiable silhouette or a meaningful microphone/performance detail can carry the music angle. Choose a clear foreground subject and supporting stage atmosphere. These are options, not a fixed concert motif.
- Consider the image beside the actual headline before accepting it. If a generic face would be read as the named celebrity, change viewpoint, identifiability or motif. Avoid lookalikes, recognizable recreations of performances, invented project-specific scenes and an anonymous frontal portrait presented as a substitute celebrity photo. Keep the required symbolic-image clarification visible in the caption.
- Keep event scale, staging and atmosphere compatible with the supplied evidence. Do not infer a stadium or enormous crowd from celebrity fame, and do not turn a substantial concert into a village-festival scene. Prefer a closer composition that does not assert an unsupported venue or audience size.
- If the story's promise requires showing the actual person, costume, room or event, report that image gap and preserve the article. Offer a neutral thematic/layout placeholder as a temporary option without silently presenting it as documentation or changing the article to fit an invented image. A gray technical placeholder is used only when explicitly authorized.

## Default ImmoScout24 editorial photographic direction

- **Image character:** Photorealistic, documentary-style lifestyle or architecture photography; human, observant, calm, believable. A lived-in European housing context when relevant. Show an actual situation rather than a vague mood.
- **Colors:** Natural, controlled saturation and realistic material/skin tones. Neutral-to-cool daylight is a housing reference, not a compulsory blue-green cast. Use credible stage colors or evening tones when the Lifestyle scene calls for them; avoid a generic golden filter.
- **Lighting:** Match the actual selected scene: plausible window/sky light, indoor practical light or concert lighting, with believable shadows and balanced exposure. No excessive HDR or artificial glow.
- **Camera:** Use natural, non-distorted perspective and believable depth. Follow the close/medium/wide decision above; no fixed lens requirement. Leave crop room around the dominant subject, not so much empty space that the subject disappears in a teaser.
- **People, if useful:** Normal people engaged in an ordinary task, not staring into the lens or presenting a product. Credible age, clothing, appearance, posture and surroundings. Never recreate real or reference individuals.
- **Homes:** Believably inhabited or maintained, with modest lived-in details and believable German/European architecture. Not showroom-perfect and not unnecessarily derelict.
- **Avoid the generic AI look:** No picturesque postcard panoramas as the default for complex market stories, supersaturated greens, glowing skies, over-ordered facades, fantasy architecture, flawless stock models, plastic skin, excessive bokeh, aggressive sharpening, impossible layouts, or contradictory shadows.
- **No generated lettering:** Keep visible text, numbers, signage, paper documents with text, logos, UI, watermarks, stickers and overlays out of the generated scene. Add only the required original Frontify AI disclosure during technical export; do not generate or imitate branded graphics. If a device is present, show its screen turned away or unreadable. No extra screens on device backs or reflections.
- **Truthfulness:** Apply the specific-subject decision above. For public-policy, finance, demographics or statistical stories, choose a generic, truthful residential scene. Avoid visual claims of vacancy, decay, danger, or prosperity not supported by the article.

## Practical visual check

- Check the selected image against the final headline and article: subject, atmosphere and implied facts must support the same story. A caption cannot fix an invented factual scene.
- Inspect the same 16:9 composition at hero, larger teaser and 128 × 72 compact sizes. The subject and complete mark should survive viewport display; do not change the factual scene to rescue a crop.
- Verify realism, anatomy, objects, materials, light and geometry, absence of fabricated visible writing, and the final hero crop. Correct one clear failure when supported; do not require formal scoring or endless iterations.
- If raster inspection or temporary previews are unavailable, state that the small-teaser/crop check is unverified. A written plan or source-pixel count is not proof of visual quality. Reopen the final export to verify its actual dimensions and the selected original AI label, corner, spacing and legibility. Check the label at realistic display sizes. Report downstream crop/size placement gaps: a centered 16:7 crop can remove a bottom label, so require the publishing step to reapply the original artwork after each actual crop/resize. Do not treat source-level labeling as proof that all CMS derivatives are labeled.

## Article image filenames

- Use `scaling-editorial-[article-slug]-titelbild-v01.webp` and `scaling-editorial-[article-slug]-listenteaser-v01.webp`, with matching revision. Use the supplied slug, lower-case ASCII and no timestamps. Separate author portraits also use `.webp`.
- Use `v01` for a first version and increment for a known replacement. Do not claim knowledge of filenames or versions from other chats. Do not change the article slug or headline just to produce a filename.
- Where the host emits an Article Package, include the proposed name as `Dateiname` under `Titelbild`. Follow the host's output format and keep this asset metadata separate from the article body and alt text.
- Verify the real WebP format, dimensions and filename, not just the file suffix.
- A native ChatGPT image preview or download can retain an application-generated name. A naming instruction alone is not proof of a renamed file. If actual export/renaming is unavailable, provide the desired filename and briefly state that manual renaming remains necessary. Keep the article output available; never invent a successful export, download link or hosted URL.

## Output and publishing boundary

- Deliver **one selected motif in exactly two files**, or one file for an expressly requested portrait or single-role export.
- Do not change the article or headline just to suit the picture.
- Keep all output a human-review draft; apply and check the prescribed visible AI label within this skill. Leave final rights approval, CMS derivative implementation and publication suitability to the editorial team. Do not claim these are already validated.
- If source style and article truth conflict, article truth wins.

## Image-output contract

- Return the selected image's `Dateiname`, `Alt-Text`, `Bildunterschrift` and `Kennzeichnung`. Describe only the visible final motif in the alt text. For generated symbol images about general topics, use only `KI-generiertes redaktionelles Symbolbild` as the caption. For a named real case using a generated symbol image, use only the short symbolic-image clarification specified above, without an extra thematic sentence. For generated symbol images, keep `KI-generiertes redaktionelles Symbolbild` as the base metadata value. Append the actual visible disclosure status within the same `Kennzeichnung` field, e.g. `KI-generiertes redaktionelles Symbolbild; Bildlabel: AI created, unten rechts, negative; geprüft`. Use `AI-Label ausstehend` or `Sichtprüfung offen` when appropriate; never claim a check from the script alone. For a substantially AI-modified authentic image, use a truthful caption and `KI-bearbeitetes redaktionelles Bild; Bildlabel: AI modified, [actual placement/style/status]`; for an authentic image with only minor technical corrections, state that fact and the justified absence of an AI label. Do not call those images AI-generated symbol images. For requested generated portraits, describe the portrait and its generated origin, using `AI created`, without applying a symbol-image caption. Include any unresolved CMS crop/size labeling gap in this field, without adding alternate motifs or a third file. Also return `Listenteaser-Dateiname`, `Listenteaser-Abmessungen`, `Listenteaser-Dateigröße` and `Listenteaser-Kennzeichnung` for the shared compact file from the actual export. Keep both files clearly separated; shared alt text/caption must still describe the same selected motif.
- In a Writer assignment, place these fields inside its `Titelbild` section and preserve the Writer's overall Article Package format. Keep the technical download separate from the hosted `Bild-URL`: an export is not a hosted URL, and no URL may be invented.
- Return two verified image downloads when available: `Titelbild und große Teaser – WebP, 1920 × 1080` and `Kleine Teaser und Weiterlesen – WebP, 480 × 270`. An expressly requested portrait or single-role export gets one link. No duplicate downloads.
- Do not embed a second preview of the export, show temporary inspection crops, or offer discarded files or sizes beyond the selected two-file set. Automatic image-generator previews may remain; do not claim control over them. A concept-only response has no image download or generated-image claim.
