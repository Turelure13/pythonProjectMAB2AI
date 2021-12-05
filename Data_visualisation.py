import pandas as pd
import matplotlib.pyplot as plt
import scipy.signal as sc


def get_data_from_csv(file):
    data = pd.read_csv(file, header=0)

    return data


def plot_TFBG(data):
    # t = data.iloc[:, 0]
    # s1 = data.iloc[:, 1]
    # s2 = data.iloc[:, 2]
    # plt.plot(t, s2)
    # plt.show()

    # create figure and axis objects with subplots()
    fig, ax = plt.subplots()
    # make a plot
    ax.plot(data.iloc[0:3600, 0], data.iloc[0:3600, 1], color="red")
    # set x-axis label
    ax.set_xlabel("time (seconds)", fontsize=14)
    # set y-axis label
    ax.set_ylabel("FHR", color="red", fontsize=14)
    # twin object for two different y-axis on the sample plot
    ax2 = ax.twinx()
    # make a plot with different y-axis using second axis object
    ax2.plot(data.iloc[0:3600, 0], data.iloc[0:3600, 2], color="blue")
    ax2.set_ylabel("UC", color="blue", fontsize=14)
    plt.show()
    # # save the plot as a file
    # fig.savefig('two_different_y_axis_for_single_python_plot_with_twinx.jpg',
    #             format='jpeg',
    #             dpi=100,
    #             bbox_inches='tight')


file_path = r"/Users/arthurlefebvre/PycharmProjects/pythonProjectMAB2AIgit/database/signals/1142.csv"
test = get_data_from_csv(file_path)

plot_TFBG(test)

print("end")
