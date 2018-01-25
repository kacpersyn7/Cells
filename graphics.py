import matplotlib.pyplot as plt
import mpl_toolkits.axes_grid1 as axes_grid1
import numpy as np


def show_and_save_target_function(iterated, target_f, name='target_func.png'):
    fig_target = plt.figure()
    plt.title('Target value, max=' + str(target_f[-1]) + 'in:' + str(iterated[-1]) + 'iterations')
    plt.plot(iterated, target_f, 'ro')
    plt.savefig(name, bbox_inches='tight', pad_inches=0.0)
    plt.show()
    return fig_target


def show_and_save_accesspoints(bitmap, name='aps.png'):
    fig_aps = plt.figure()
    x, y = np.where(bitmap[1] == 1)
    fig_aps.suptitle('Accesspoints')
    plt.plot(x, y, 'ro', label="Typ 0")
    plt.axis([0, bitmap.shape[1] - 1, 0, bitmap.shape[2] - 1])
    x, y = np.where(bitmap[0] == 1)
    plt.plot(x, y, 'bx', label="Typ 1")
    plt.axis([0, bitmap.shape[1] - 1, 0, bitmap.shape[2] - 1])
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.savefig(name, bbox_inches='tight', pad_inches=0.0)
    plt.show()
    return fig_aps


def show_and_save_power(people, heatmap, name='power_png'):
    fig_power = plt.figure()
    # fig_power.suptitle('Moc', fontsize=12)
    grid = axes_grid1.AxesGrid(
        fig_power, 111, nrows_ncols=(1, 2), axes_pad=1, cbar_location="right",
        cbar_mode="each", cbar_size="5%", cbar_pad="5%", )
    im1 = grid[0].imshow(people, cmap='plasma', interpolation='nearest')
    grid.cbar_axes[0].colorbar(im1)
    im2 = grid[1].imshow(heatmap, cmap='plasma', interpolation='nearest', vmax=np.max(people))
    grid.cbar_axes[1].colorbar(im2)

    plt.savefig(name, bbox_inches='tight', pad_inches=0.0, dpi=500)
    plt.show()
    return fig_power
