import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import pandas as pd


def find_all_peaks(y_axis):
    return find_peaks(y_axis, height=y_axis, distance=1000)


def remove_noisy_peaks(pulses, found_peaks):
    peak_heights = found_peaks[1]['peak_heights']
    peak_positions = pulses[found_peaks[0]]

    new_positions = []
    new_heights = []

    peak_mean = np.average(peak_heights)

    for i in range(0, len(peak_heights) - 1):
        if peak_heights[i] > peak_mean:
            new_heights.append(peak_heights[i])
            new_positions.append(peak_positions[i])

    return new_positions, new_heights


def draw_peaks(pulses, y_axis, peak_pos, peak_h):
    print(f"First peak position: {peak_pos[0]}, height: {peak_h[0]}")
    fig = plt.figure()
    ax = fig.subplots()
    ax.plot(pulses, y_axis)
    ax.scatter(peak_pos[0], peak_h[0], color='r', s=15, marker='D', label='Maxima')
    plt.show()


def read_xlsx_file(path, starting_column, row_number):
    df = pd.read_excel(path)
    selected_row = df.iloc[row_number - 1, starting_column:].values
    return selected_row.astype(float)


def get_pulse_data():
    file_path = input('Provide the file path: ')
    starting_col = int(input('Provide the starting column(e.g. 6, 17 etc.): '))
    selected_row = int(input('Provide the row you want to find peak(e.g. 30): '))
    yaxis = np.array(read_xlsx_file(file_path, starting_col, selected_row))

    pulses = np.array(list(range(0, len(yaxis))))
    return pulses, yaxis


if __name__ == '__main__':
    x, y = get_pulse_data()

    if x is not None and y is not None:
        peaks = find_all_peaks(y)
        peak_positions, peak_heights = remove_noisy_peaks(x, peaks)
        draw_peaks(x, y, peak_positions, peak_heights)

