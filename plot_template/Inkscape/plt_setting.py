#
#   Created by WW on 2023-12-20.
#   Updated by WW on 2024-12-08.
#   Copyright © WW. All rights reserved.
#
#   Basic plot settings
#

import matplotlib.pyplot as plt


def plt_init():
    plt.rcParams.update({
        # requires a working LaTeX installation & slower than Matplotlib's mathtext
        "text.usetex": False,
        "font.family": "Times New Roman",    # "sans-serif"
        # "font.sans-serif": "DejaVu Sans"
    })

    plt.rcParams["ps.usedistiller"] = "xpdf"    # for scalable eps file
    plt.rcParams['svg.fonttype'] = 'none'    # save svg without text as paths but embedded fonts
    
    plt.rcParams['figure.constrained_layout.use'] = True  # depends on whether you want to adjust the distance between subplots by yourself
    plt.rcParams["mathtext.fontset"] = "cm"    # change the math font to Computer Modern (TeX font)
    
    plt.rcParams['ytick.right'] = True
    plt.rcParams['xtick.top'] = True
    plt.rc('xtick', labelsize=12, direction='in')
    plt.rc('ytick', labelsize=12, direction='in')
    plt.rc('axes', labelsize=14, titlesize=14)
    plt.rc('legend', fontsize=12)
    
