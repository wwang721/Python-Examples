#
#   Created by WW on 2023-12-20.
#   Copyright © WW. All rights reserved.
#
#   Basic plot settings
#

import matplotlib.pyplot as plt


def plt_init():
    plt.rcParams.update({
        # requires a working LaTeX installation & slower than Matplotlib's mathtext
        "text.usetex": True,
        "font.family": "sans-serif",
        "font.sans-serif": "DejaVu Sans"
    })

    plt.rcParams['figure.constrained_layout.use'] = True
    plt.rcParams['ytick.right'] = True
    plt.rcParams['xtick.top'] = True
    plt.rc('xtick', labelsize=12, direction='in')
    plt.rc('ytick', labelsize=12, direction='in')
    plt.rc('axes', labelsize=14, titlesize=14)
    plt.rc('legend', fontsize=12)
