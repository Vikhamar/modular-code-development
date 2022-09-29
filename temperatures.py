import pandas as pd
from matplotlib import pyplot as plt
import pytest
import click

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


@click.command()
@click.option('--num-measurements', type=int, help='Number of measurements.')
@click.option('--input-file', help='Input file.')
@click.option('--output-file', help='Output file.')

def main(num_measurements, input_file, output_file):
    temperatures = read_data(input_file, num_measurements)
    mean = compute_mean(temperatures)
    plot_data(temperatures, mean, output_file)

if __name__ == "__main__":
    main()
