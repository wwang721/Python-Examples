#
#   Created by WW on 2023-12-20.
#   Updated by WW on 2025-04-05.
#   Copyright © WW. All rights reserved.
#
#   Basic plot settings
#

import matplotlib.pyplot as plt


def plt_init():
    plt.rcParams.update({
        # requires a working LaTeX installation & slower than Matplotlib's mathtext
        "text.usetex": False,
        "font.family": "Helvetica",    # or other sans-serif font like Arial
        # "font.sans-serif": "DejaVu Sans"
    })
    plt.rcParams["mathtext.fontset"] = "custom"    
    plt.rcParams["mathtext.rm"] = "Helvetica"  # change the math font to Helvetica
    plt.rcParams["mathtext.cal"] = "DejaVu Serif Display"  # use the dejavusans version \mathcal{}

    plt.rcParams['svg.fonttype'] = 'none'    # save svg with embedded fonts instead of converting text to paths
    plt.rcParams["ps.usedistiller"] = "xpdf"    # for scalable eps file
    
    plt.rcParams['figure.constrained_layout.use'] = False  # depends on whether you want to adjust the distance between subplots by yourself
    # You can always add bbox_inches='tight' when save figures
    
    plt.rcParams['ytick.right'] = True
    plt.rcParams['xtick.top'] = True
    plt.rc('xtick', labelsize=12, direction='in')
    plt.rc('ytick', labelsize=12, direction='in')
    plt.rc('axes', labelsize=14, titlesize=14)
    plt.rc('legend', fontsize=12)
    
