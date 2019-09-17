from recorder import set_and_record
from plotting import plotter
from util import algorithm, compare_with_median


if __name__ == "__main__":
	set_and_record()
	distances = algorithm()
	clap_times = compare_with_median(distances)
	plotter(clap_times)

