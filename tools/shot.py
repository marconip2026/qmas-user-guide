"""Save a browser screenshot into the guide and blur private data.

Usage: python3 tools/shot.py <capture.jpg> <guide>/img/<name>.jpg [x0,y0,x1,y1 ...]
Always blurs the top-right account block (company name + email). Add boxes for names, emails, Created By / Team columns.
The unblurred original is kept in ../user-guide-raw/ (outside the public repo). Needs Pillow.
"""
import sys, shutil, os
from PIL import Image, ImageFilter
src, dest, boxes = sys.argv[1], sys.argv[2], sys.argv[3:]
os.makedirs(os.path.dirname(dest), exist_ok=True)
raw = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "user-guide-raw", os.path.basename(os.path.dirname(os.path.dirname(dest))), os.path.basename(dest))
os.makedirs(os.path.dirname(raw), exist_ok=True)
shutil.copy(src, raw)
im = Image.open(src).convert("RGB")
w, h = im.size
regions = [(int(w*0.86), 0, w, int(h*0.085))] + [tuple(int(v) for v in b.split(",")) for b in boxes]
for b in regions:
    im.paste(im.crop(b).filter(ImageFilter.GaussianBlur(7)), b)
im.save(dest, quality=92)
print("saved", dest)
