import matplotlib.pyplot as plt
from generate_datasets import Generate, DATA_TYPE

def plot_datasets(obj: Generate):
    fig, axs = plt.subplots(2,2)
    fig.tight_layout(h_pad=2)

    X_1, y_1 = Generate.get_dataset(obj, DATA_TYPE.CIRCLES)
    X_2, y_2 = Generate.get_dataset(obj, DATA_TYPE.MOONS)
    X_3, y_3 = Generate.get_dataset(obj, DATA_TYPE.BLOBS)

    axs[0,0].set_title("Circles")
    axs[0,0].scatter(X_1[:, 0], X_1[:, 1], marker="o", c=y_1, s=40, edgecolor="k")

    axs[0,1].set_title("Moons")
    axs[0,1].scatter(X_2[:, 0], X_2[:, 1], marker="o", c=y_2, s=40, edgecolor="k")

    axs[1,0].set_title("Blobs")
    axs[1,0].scatter(X_3[:, 0], X_3[:, 1], marker="o", c=y_3, s=40, edgecolor="k")

    fig.suptitle('Datasets', fontsize=22)
    plt.subplots_adjust(top=0.85)

    plt.show()