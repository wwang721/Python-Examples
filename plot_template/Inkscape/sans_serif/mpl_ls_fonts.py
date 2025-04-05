import matplotlib.font_manager as fm

# Get all font entries known to Matplotlib
fonts = fm.fontManager.ttflist

# Create a sorted set of all font family names
font_keys = sorted(set(f"{f.name}" for f in fonts))

# Optionally, include variants (oblique, bold, etc.)
for f in fonts:
    base = f.name
    style = f.style  # 'normal', 'italic', 'oblique'
    weight = f.weight  # 400 = normal, 700 = bold
    suffix = []

    if weight >= 600:
        suffix.append("bold")
    if style in ("italic", "oblique"):
        suffix.append(style)

    key = base
    if suffix:
        key += ":" + ":".join(suffix)

    print(key)
