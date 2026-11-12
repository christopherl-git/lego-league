# Team Logo (digital copy)

Alexis's winning logo ([vote results](../logo-vote/results-2026-11-10.md)), digitized from the photo [alexis-logo-winner.jpg](../logo-vote/alexis-logo-winner.jpg) on 2026-11-10.

## Clean copy

- [look-its-a-giraffe-logo.png](look-its-a-giraffe-logo.png): 2400 × 2400 px with a transparent background outside the circle. Use it for t-shirts, the banner, the poster and slides.
- [look-its-a-giraffe-logo.jpg](look-its-a-giraffe-logo.jpg): the same image on white.
- [look-its-a-giraffe-logo.svg](look-its-a-giraffe-logo.svg): full-color vector (100 mm wide; scales to any size).

**What changed from the drawing:**
- The hand-drawn circle is now a perfect circle.
- The light-blue background is solid instead of marker strokes.
- The white outline around the letters and face is an even width, and the gaps in the stars are filled.
- Very thin pen lines are slightly thicker.
- Alexis's signature at the bottom right is left out. **(confirm)** with Alexis, since we can add it back.

## 3D print files (Bambu, PLA, iron-on, printed face down)

All files are in [print/](print/). The design is a **100 mm circle**, **0.2 mm thick** (two layers of 0.1 mm). It prints **face down**: the colors go in the first layer, against the plate, so the smooth plate side becomes the front. Every file is already **mirrored**, so the design reads correctly once you flip it over. Don't mirror it again in Bambu Studio.

| File (STL and SVG) | Type in Bambu Studio | Height | Filament | What it is |
|---|---|---|---|---|
| `logo-1-cyan-body` | Part | 0.0 to 0.2 mm | Cyan | The full circle |
| `logo-2-blue-modifier` | Modifier | 0.0 to 0.1 mm (layer 1) | Blue | Ring and stars |
| `logo-3-yellow-modifier` | Modifier | 0.0 to 0.1 mm (layer 1) | Yellow | Letters and face |
| `logo-4-cocoa-brown-modifier` | Modifier | 0.0 to 0.1 mm (layer 1) | Cocoa Brown | Face shading |
| `logo-5-black-modifier` | Modifier | 0.0 to 0.1 mm (layer 1) | Black | Outlines, hatching, eyes |
| `logo-6-yellow-head-backing-modifier` | Modifier | 0.1 to 0.2 mm (layer 2) | Yellow | Solid yellow behind the giraffe's head, so cyan doesn't show through gaps in layer 1 |

- **Head backing:** it is the head's outline pulled in 0.3 mm, so it stays hidden behind the black outline.
- **Eyes:** the backing has the eyes cut out, so the area behind the eyes stays cyan and the cyan eye highlights stay true cyan.
- **Cyan areas:** everywhere layer 1 has no modifier (the light-blue background, the white outlines and the eye highlights), the cyan body shows.

[logo-print-preview.png](print/logo-print-preview.png) shows layer 1 as it sits on the plate, then layer 2, then the finished front.

**Printing in Bambu Studio (use the STLs):**
1. **Import all six STLs together.** Use **File → Import → Import 3MF/STL/STEP/SVG/OBJ/AMF**, select all six, and answer **Yes** to "Load these files as a single object with multiple parts?". This keeps everything lined up.
2. **Turn the colors into modifiers.** In the **Objects** list, expand the object, then right-click each of parts 2 to 6 and choose **Change type → Modifier**. Leave `logo-1-cyan-body` as a Part.
3. **Set the filaments.** The body is Cyan. The modifiers are Blue, Yellow, Cocoa Brown, Black, and Yellow for the head backing.
4. **Set the layer heights.** Under **Process → Quality**, set **Layer height 0.1 mm** and **Initial layer height 0.1 mm**. The default first layer is 0.2 mm, which would merge both layers into one.
5. **Check the slice preview.**
   - **Layer 1:** all four colors, with the text reading backwards.
   - **Layer 2:** cyan, with a yellow head that has two eye holes.
   - **Thin lines:** the finest black lines are about 0.45 mm wide. If any go missing with a 0.4 mm nozzle, scale the object up to about 120 mm.

**SVG files:** the six print SVGs match the STLs (mirrored, same 100 × 100 mm canvas), so they line up in tools that keep the canvas, such as Inkscape. Bambu Studio may re-center each SVG when importing, so use the STLs for printing. For a version that isn't mirrored, use the full-color [look-its-a-giraffe-logo.svg](look-its-a-giraffe-logo.svg).
