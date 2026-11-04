"""Build one guide from guides/<slug>.json into:
  <slug>/index.html        public web page (GitHub Pages)
  dify/<slug>.md           Dify knowledge-base Markdown (absolute image URLs)
  dify/<slug>.pdf          Dify knowledge-base PDF (printed from the web page)
  notion/<slug>.md         Notion-flavoured Markdown for the User Guide / Help Center pages

Usage: python3 tools/build.py <slug> [<slug> ...]
Inline text uses **bold** only; everything else is plain text.
"""
import html
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://marconip2026.github.io/qmas-user-guide"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

CSS = """
  :root { --bg:#F7FAFF; --card:#fff; --text:#1F2937; --muted:#6B7280; --primary:#005EFF; --line:#E5E7EB; --tip:#EEF4FF; }
  * { box-sizing:border-box; }
  body { margin:0; background:var(--bg); color:var(--text); font:15px/1.6 Roboto, -apple-system, "Segoe UI", sans-serif; }
  main { max-width:880px; margin:0 auto; padding:32px 16px 64px; }
  h1 { font-size:28px; margin:0 0 4px; }
  h2 { font-size:20px; margin:40px 0 12px; padding-top:16px; border-top:1px solid var(--line); }
  h3 { font-size:16px; margin:24px 0 8px; }
  .sub { color:var(--muted); margin:0 0 24px; }
  .meta { display:grid; grid-template-columns:max-content 1fr; gap:4px 16px; background:var(--card); border:1px solid var(--line); border-radius:8px; padding:16px; }
  .meta b { color:var(--muted); font-weight:500; }
  a { color:var(--primary); }
  ol.overview { background:var(--card); border:1px solid var(--line); border-radius:8px; padding:16px 16px 16px 36px; }
  figure { margin:12px 0 20px; }
  figure img { width:100%; border:1px solid var(--line); border-radius:8px; display:block; }
  figcaption { color:var(--muted); font-size:13px; margin-top:6px; }
  .tip { background:var(--tip); border-left:3px solid var(--primary); border-radius:4px; padding:12px 16px; margin:12px 0; }
  table { border-collapse:collapse; width:100%; background:var(--card); font-size:14px; }
  th, td { border:1px solid var(--line); padding:8px 10px; text-align:left; vertical-align:top; }
  th { background:#F3F4F6; }
  dl.faq dt { font-weight:600; margin-top:12px; }
  dl.faq dd { margin:4px 0 0; }
"""


def inline_html(text):
    out = html.escape(text)
    out = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", out)
    return re.sub(r"(https?://[^\s<]+)", r'<a href="\1">\1</a>', out)


def img_url(g, name):
    return f"{SITE}/{g['slug']}/img/{name}"


def render_html(g):
    p = [f"<!doctype html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n"
         f"<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n"
         f"<title>{html.escape(g['tab_title'])}</title>\n<style>{CSS}</style>\n</head>\n<body>\n<main>\n",
         '  <p><a href="../">← All guides</a></p>\n',
         f"  <h1>{html.escape(g['title'])}</h1>\n  <p class=\"sub\">{inline_html(g['purpose'])}</p>\n",
         '  <div class="meta">\n']
    for k, v in g["meta"]:
        p.append(f"    <b>{html.escape(k)}</b><span>{inline_html(v)}</span>\n")
    p.append("  </div>\n\n  <h2>Overview</h2>\n  <ol class=\"overview\">\n")
    p += [f"    <li>{inline_html(o)}</li>\n" for o in g["overview"]]
    p.append("  </ol>\n\n  <h2>Step-by-step</h2>\n")
    for s in g["steps"]:
        p.append(f"\n  <h3>{html.escape(s['h'])}</h3>\n")
        for block in s["body"]:
            p.append(render_block_html(g, block))
    if g.get("tips"):
        p.append("\n  <h2>Tips</h2>\n")
        p += [f'  <div class="tip">{inline_html(t)}</div>\n' for t in g["tips"]]
    if g.get("faq"):
        p.append('\n  <h2>FAQ</h2>\n  <dl class="faq">\n')
        for q, a in g["faq"]:
            p.append(f"    <dt>{inline_html(q)}</dt><dd>{inline_html(a)}</dd>\n")
        p.append("  </dl>\n")
    p.append("</main>\n</body>\n</html>\n")
    return "".join(p)


def render_block_html(g, b):
    if isinstance(b, str):
        return f"  <p>{inline_html(b)}</p>\n"
    if "list" in b:
        return "  <ul>\n" + "".join(f"    <li>{inline_html(i)}</li>\n" for i in b["list"]) + "  </ul>\n"
    if "table" in b:
        head, *rows = b["table"]
        out = "  <table>\n    <tr>" + "".join(f"<th>{inline_html(c)}</th>" for c in head) + "</tr>\n"
        out += "".join("    <tr>" + "".join(f"<td>{inline_html(c)}</td>" for c in r) + "</tr>\n" for r in rows)
        return out + "  </table>\n"
    if "img" in b:
        return (f'  <figure><img src="img/{b["img"]}" alt="{html.escape(b["caption"])}">'
                f"<figcaption>{inline_html(b['caption'])}</figcaption></figure>\n")
    raise ValueError(b)


def render_md(g, notion=False):
    """Markdown for Dify (notion=False) or Notion (notion=True)."""
    p = []
    if not notion:
        p.append(f"# {g['title']}\n\n")
    p.append(f"{g['purpose']}\n\n")
    for k, v in g["meta"]:
        p.append(f"- **{k}:** {v}\n")
    p.append(f"- **Full guide with screenshots:** {SITE}/{g['slug']}/\n\n## Overview\n\n")
    p += [f"{i}. {o}\n" for i, o in enumerate(g["overview"], 1)]
    p.append("\n## Step-by-step\n")
    for s in g["steps"]:
        p.append(f"\n### {s['h']}\n\n")
        for b in s["body"]:
            if isinstance(b, str):
                p.append(f"{b}\n\n")
            elif "list" in b:
                p.append("".join(f"- {i}\n" for i in b["list"]) + "\n")
            elif "table" in b:
                head, *rows = b["table"]
                p.append("| " + " | ".join(head) + " |\n|" + "---|" * len(head) + "\n")
                p.append("".join("| " + " | ".join(r) + " |\n" for r in rows) + "\n")
            elif "img" in b:
                p.append(f"![{b['caption']}]({img_url(g, b['img'])})\n\n")
    if g.get("tips"):
        p.append("## Tips\n\n" + "".join(f"- {t}\n" for t in g["tips"]) + "\n")
    if g.get("faq"):
        p.append("## FAQ\n\n")
        for q, a in g["faq"]:
            p.append(f"**Q: {q}**\nA: {a}\n\n")
    return "".join(p)


def build(slug):
    with open(os.path.join(ROOT, "guides", f"{slug}.json"), encoding="utf-8") as f:
        g = json.load(f)
    g["slug"] = slug
    page = os.path.join(ROOT, slug, "index.html")
    with open(page, "w", encoding="utf-8") as f:
        f.write(render_html(g))
    for folder, notion in (("dify", False), ("notion", True)):
        os.makedirs(os.path.join(ROOT, folder), exist_ok=True)
        with open(os.path.join(ROOT, folder, f"{slug}.md"), "w", encoding="utf-8") as f:
            f.write(render_md(g, notion))
    pdf = os.path.join(ROOT, "dify", f"{slug}.pdf")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={pdf}", f"file://{page}"],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print("built", slug)


if __name__ == "__main__":
    for s in sys.argv[1:]:
        build(s)
