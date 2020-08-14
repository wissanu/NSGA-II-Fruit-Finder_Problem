import matplotlib.pyplot as plt


def plot_graph(chromosome_list, max_p_rank):

    color = ['red','blue','green','yellow','black']
    for _ in range(1,max_p_rank+1):
        # x axis values
        x = [x.fitness_cost for x in chromosome_list if x.pareto_rank == _]
        # corresponding y axis values
        y = [y.fitness_piece for y in chromosome_list if y.pareto_rank == _]

        # plotting points as a scatter plot
        plt.scatter(x, y, label="stars", color=color[_-1],
                    marker="o", s=30)

    # naming the x axis
    plt.xlabel('cost')
    # naming the y axis
    plt.ylabel('pieces')

    # giving a title to my graph
    plt.title('Pareto Front level')
    plt.legend(('F1', 'F2', 'F3', 'F4', 'F5'))

    # function to show the plot
    plt.show()
