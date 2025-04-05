# Using sans-serif fonts in Matplotlib

Use the default **DejaVu Sans** or download other sans-serif fonts like **Arial** and **Helvetica**, etc (need to install for Matplotlib, see [how](README.md#how-to-install-fonts-for-matplotlib)).

For `mathtext`, you can set it to `'dejavusans'` (default) and `'stixsans'`, see [Matplotlib documentation](https://matplotlib.org/stable/users/explain/text/mathtext.html#fonts).

If you want to be consistent with the text fonts, you can set it to `'custom'` and then set the specific fonts one by one, see the [documentation](https://matplotlib.org/stable/users/explain/text/mathtext.html#custom-fonts).

* Since `\mathcal{}` is less frequently used, it can be repurposed as a workaround for applying a different font locally. For example, if you want to render Greek letters (e.g., \alpha $\alpha$) using the Computer Modern font, you can set `mathtext.cal` = `'cmmi10'` and write `\mathcal{\alpha}` in your plot string.
* As there are a few fonts in each font family, you can use [mpl_ls_fonts.py](sans_serif/mpl_ls_fonts.py) to list all keys available for those fonts.
