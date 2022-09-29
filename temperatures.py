import pandas as pd
from matplotlib import pyplot as plt
import pytest

def read_data(filename, num_measurements):
    # read data from file
    data = pd.read_csv(filename, nrows=num_measurements)
    temperatures = data["Air temperature (degC)"]
    return temperatures
    
def compute_mean(data):
    # compute statistics
    return sum(data) / len(data)

def plot_data(temperatures, mean, filename):
    # plot results
    plt.title("temperatures in Helsinki")
    plt.xlabel("measurements")
    plt.ylabel("air temperature (deg C)")
    plt.plot(temperatures, "r-")
    plt.axhline(y=mean, color="b", linestyle="--")
    plt.show()
    plt.savefig(filename)
    plt.clf()

def test_compute_mean():
    result = compute_mean([1.0, 2.0, 3.0, 4.0])
    assert result == pytest.approx(2.5)

def main():
    for num_measurements in [25, 100, 500]:
        temperatures = read_data("temperatures.csv", num_measurements)
        mean = compute_mean(temperatures)
        plot_data(temperatures, mean, str(num_measurements) + ".png")

if __name__ == "__main__":
    main()
