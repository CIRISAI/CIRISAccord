#!/usr/bin/env python3
"""Build the CIRIS Accord PDF from the canonical accord/ markdown.

Reading order is deliberately "cold open": readers meet Book I (Section 1)
first; the introduction / foreword / genesis prose is moved to the back as
front-matter-as-appendix. Output: ciris_accord.pdf (repo root).

Deps: `markdown` + `weasyprint`.  Run:  python3 build_pdf.py
"""
import os, re
import markdown
from weasyprint import HTML

ROOT = os.path.dirname(os.path.abspath(__file__))
ACC = os.path.join(ROOT, "accord")

# Main content first (Book I → IX, supporting material, annexes), then the
# moved-to-back prose, then the backmatter end-piece.
MAIN = [
    "03_book_I", "04_book_II", "05_book_III", "06_book_IV", "07_book_V",
    "08_book_VI", "09_book_VII", "10_book_VIII", "11_book_IX",
    "90_formulas", "91_addenda",
    "annexes/00_overview",
    *[f"annexes/annex_{x}" for x in "ABCDEFGHIJ"],
]
BACK_PROSE = ["00_introduction", "01_foreword", "02_genesis"]
BACKMATTER = ["92_backmatter"]

MD_EXT = ["tables", "fenced_code", "sane_lists", "attr_list", "md_in_html"]


def render(stem):
    text = open(os.path.join(ACC, stem + ".md"), encoding="utf-8").read()
    # normalise the NBSP-after-### headings the canonical uses in some annexes
    text = re.sub(r"(?m)^(#{1,6}) *", r"\1 ", text)
    html = markdown.markdown(text, extensions=MD_EXT, output_format="html5")
    return f'<section class="doc">{html}</section>'


def title_page():
    intro = open(os.path.join(ACC, "00_introduction.md"), encoding="utf-8").read()
    title = re.search(r"(?m)^#\s+(CIRIS Accord Version.*)$", intro)
    title = title.group(1) if title else "CIRIS Accord"
    sub = re.search(r"(?m)^>\s*(CIRIS [0-9].*)$", intro)
    sub = sub.group(1) if sub else ""
    issued = re.search(r"(?m)^##\s*Issued\s*\n+(.*)$", intro)
    issued = issued.group(1).strip() if issued else ""
    return f"""
    <section class="title-page">
      <div class="brand">CIRIS</div>
      <h1 class="title">{title}</h1>
      <p class="subtitle">{sub}</p>
      <p class="issued">{issued}</p>
      <p class="note">The framing prose (Introduction, Foreword, Genesis) follows
      the specification at the back of this document, so that readers meet Book I
      first.</p>
    </section>
    """


def divider(label):
    return f'<section class="divider"><h1>{label}</h1></section>'


CSS = """
@page {
  size: A4; margin: 22mm 20mm 20mm 20mm;
  @bottom-center { content: counter(page); font: 9pt Georgia, serif; color: #555; }
  @top-center { content: "CIRIS Accord 1.3-RC2"; font: 8pt Georgia, serif; color: #999; }
}
@page :first { @top-center { content: none; } @bottom-center { content: none; } }
html { font-family: Georgia, "Times New Roman", serif; font-size: 10.5pt; color: #1a1a1a; line-height: 1.5; }
.title-page { height: 100%; display: flex; flex-direction: column; justify-content: center; text-align: center; page-break-after: always; }
.title-page .brand { font: 700 14pt Georgia, serif; letter-spacing: .4em; color: #2563eb; margin-bottom: 1.5em; }
.title-page .title { font-size: 22pt; line-height: 1.25; margin: 0 0 .6em; }
.title-page .subtitle { font-size: 11pt; color: #444; max-width: 30em; margin: 0 auto 2em; font-style: italic; }
.title-page .issued { color: #666; font-size: 10pt; }
.title-page .note { margin-top: 3em; color: #888; font-size: 9pt; max-width: 26em; margin-left: auto; margin-right: auto; }
.divider { page-break-before: always; text-align: center; padding-top: 35vh; }
.divider h1 { font-size: 18pt; color: #2563eb; border: none; }
.doc { page-break-before: always; }
h1 { font-size: 17pt; border-bottom: 2px solid #2563eb; padding-bottom: .2em; margin-top: 0; }
h2 { font-size: 13pt; margin-top: 1.4em; color: #111; }
h3 { font-size: 11.5pt; margin-top: 1.1em; color: #333; }
h4 { font-size: 10.5pt; color: #444; }
p { margin: .5em 0; orphans: 2; widows: 2; }
blockquote { border-left: 3px solid #cbd5e1; margin: .8em 0; padding: .2em 0 .2em 1em; color: #475569; font-style: italic; }
code { font-family: "DejaVu Sans Mono", monospace; font-size: 9pt; background: #f1f5f9; padding: .05em .3em; border-radius: 3px; }
pre { background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 4px; padding: .7em 1em; overflow-wrap: anywhere; white-space: pre-wrap; font-size: 8.5pt; }
pre code { background: none; padding: 0; }
table { border-collapse: collapse; width: 100%; margin: .8em 0; font-size: 9pt; page-break-inside: avoid; }
th, td { border: 1px solid #cbd5e1; padding: .35em .5em; text-align: left; vertical-align: top; }
th { background: #eef2ff; }
hr { border: none; border-top: 1px solid #e2e8f0; margin: 1.5em 0; }
a { color: #2563eb; text-decoration: none; }
ul, ol { margin: .4em 0 .4em 1.2em; }
li { margin: .2em 0; }
"""


def main():
    parts = [title_page()]
    parts += [render(s) for s in MAIN]
    parts.append(divider("Front Matter"))
    parts += [render(s) for s in BACK_PROSE]
    parts += [render(s) for s in BACKMATTER]
    html = (
        "<!doctype html><html><head><meta charset='utf-8'>"
        f"<style>{CSS}</style></head><body>" + "".join(parts) + "</body></html>"
    )
    out = os.path.join(ROOT, "ciris_accord.pdf")
    HTML(string=html, base_url=ROOT).write_pdf(out)
    size = os.path.getsize(out)
    print(f"wrote {out} ({size//1024} KB)")


if __name__ == "__main__":
    main()
