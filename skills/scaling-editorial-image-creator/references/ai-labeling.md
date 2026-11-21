# Frontify AI labels

Use the supplied ImmoScout24 Frontify guidance and original artwork for visible AI disclosure. Read this reference before any raster export, including edits and requested author portraits.

## Source and scope

Source: user-supplied screenshot of [Frontify: AI Label](https://brand.immoscout24.de/document/417#/-/ai-label), supplied 19 November 2026, page last modified 11 August 2026, and its six-asset download package `Assets 2026-11-19.zip`.

Apply these as the supplied brand instructions. Do not turn the screenshot's legal introduction or the earlier Slack dates into an independently verified legal claim or a date-based switch. Apply the label now when the image qualifies. Use these more specific Frontify instructions for asset selection and layout.

## Decide from provenance and the actual edit

| Image origin / edit | Visible label | Example |
| --- | --- | --- |
| Newly generated or visual core substantially created using generative AI | AI created | Generated editorial symbol image, generated author portrait, newly generated scene based on an AI reference |
| Pre-existing human-made content substantially altered with AI, changing its interpretation | AI modified | AI furnishings added to an authentic empty-apartment photo; substantial realistic changes to a real scene |
| Only minor technical changes to existing human-made content | None | Colour correction, retouching, background removal; simple layout extension that does not materially change the depicted scene |
| Unchanged authentic photo | None | Supplied original photograph |
| Unknown provenance or uncertain extent of modification | Resolve from supplied inputs before a final labeling claim | Do not silently classify an unknown original as human-made |

Keep an already AI-created image classified as `created` after cropping, resizing, colour correction or later edits. The minor-adjustment exception does not erase its generated origin. Do not use `modified` merely because a generated image was resized. Preserve an existing appropriate disclosure; avoid placing a second label on top of it. Export from the identified unlabelled source when adding or repositioning the label; never invent that source or erase an existing mark blindly.

## Select original artwork

Use `assets/ai-labels/ai-{created|modified}-{positive|negative|negative-transparent}.svg`. All six supplied SVGs are bundled byte-for-byte with ASCII filenames. Each has a transparent PNG derivative at 10× its SVG viewBox size, rendered from those paths for Pillow-only execution. Preserve the SVG aspect ratio and artwork, including the AI-in-the-heart icon and word. Do not recreate it with a font, generate it inside the scene, recolor, distort, add a shadow/box, or substitute a generic watermark.

| Variant | Use |
| --- | --- |
| positive | Dark artwork on a light background |
| negative | White artwork on a dark background |
| negative-transparent | Supplied translucent artwork on a background where it remains clearly visible; never an automatic choice |

## Place and inspect

- Place the complete label at the bottom, preferably a corner, with sufficient edge spacing. Keep it subtle, clearly legible and separate from faces or important details. Choose the other bottom corner if necessary.
- Use the full icon-and-word lockup when space allows. No separate icon-only asset is provided; do not invent one for small formats.
- Add the label **after the final crop and resize**, using the supplied artwork. Caption, alt text and metadata remain required where applicable and do not replace this visible label.
- Treat the exporter's 192 px artwork width and 24 px margin for 1920 × 1080 heroes (88 px and 8 px for 240 × 240 portraits) as adjustable implementation defaults, not Frontify-specified minimums. Inspect the actual result. `--label-width`, `--margin`, `--corner` and `--label-style` permit adjustments without changing the scene.
- Check contrast over the whole mark at the intended display size. Automatic light/dark selection estimates contrast from pixels beneath the artwork; it cannot verify visual legibility. On busy backgrounds, choose the other corner or a legible original variant/size. Do not invent a new logo treatment.
- Check the reopened labeled PNG at full size and a realistic article display size. Inspect teaser crops too. A bottom label on a 16:9 master can be clipped by a centered 16:7 crop or become unreadable at 120 × 80 / 80 × 56. Do not promise one baked-in mark survives every derivative. Keep the unlabelled master internally; require the CMS/publishing step to apply the same original label **after each actual crop/resize** at a readable size. Keep these as downstream handoff instructions, not extra deliverables or a publication operation. If the small format cannot accommodate a legible full lockup, report that placement gap rather than inventing an icon or claiming a passed check.

## Export examples

Resolve the actual skill root, identified unlabelled source and final destination first. Keep the original and deliver only the selected final asset.

```bash
python <skill-root>/scripts/export_editorial_image.py <source> <final>.png --kind title
python <skill-root>/scripts/export_editorial_image.py <source> <final>.png --kind title --label modified --label-reason 'Original human-made photo; AI furnishings added' --corner bottom-left
python <skill-root>/scripts/export_editorial_image.py <source> <final>.png --kind title --label none --label-reason 'Authentic original; only colour correction'
```

The default is `created`; explicitly justify `modified` or `none` from actual provenance. Read the JSON result for `ai_label.type`, asset, style, placement and checksum. Confirm technical success and visually inspect the file before reporting the mark as checked. If the original asset, source access or compositing capability is missing, keep the article and original image, report `AI-Label ausstehend`, and do not call the image publishing-ready. Do not substitute a caption-only disclosure or an AI-drawn approximation.
