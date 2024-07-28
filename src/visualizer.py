import matplotlib.pyplot as plt
from src.subspace_calculator import column_space, row_space, null_space, left_null_space

def visualize_subspaces(matrix):
    #creating the figure, 2*2 grid of subplots with fix size of 12*12 in
    fig,axs = plt.subplots(2,2, figsize=(12,10))
    subspaces = [column_space(matrix), row_space(matrix),
                 null_space(matrix), left_null_space(matrix)]
    
    titles = ['Column Space', 'Row Space', 'Null Space', 'Left Null Space']

    for ax, subspace, title in zip(axs.flat, subspaces, titles):
        ax.bar(['Dimension'], [subspace])
        ax.set_title(title)
        ax.set_ylim(0, max(matrix.shape))

    plt.tight_layout()
    plt.show()