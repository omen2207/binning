import csv
import numpy as np

def read_csv_data(file_path):
    data = []
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  
        for row in csv_reader:
            data.append(float(row[1]))  
    return data

def create_bins(data, bin_size):
    bins = []
    for i in range(0, len(data), bin_size):
        bin = data[i:i + bin_size]  
        bins.append(bin)  
    return bins

def binning_by_mean(bins):
    smoothed_data = []
    for bin in bins:
        mean_value = sum(bin) / len(bin)
        smoothed_data.append([mean_value] * len(bin))  
    return smoothed_data

def binning_by_median(bins):
    smoothed_data = []
    for bin in bins:
        median_value = sorted(bin)[len(bin) // 2]  
        smoothed_data.append([median_value] * len(bin))  
    return smoothed_data

def binning_by_boundaries(bins):
    smoothed_data = []
    for bin in bins:
        min_value = min(bin)
        max_value = max(bin)
        smoothed_bin = []
        for value in bin:
            if abs(value - min_value) < abs(value - max_value):
                smoothed_bin.append(min_value)  
            else:
                smoothed_bin.append(max_value)
        smoothed_data.append(smoothed_bin)
    return smoothed_data

def binning_data(file_path, bin_size):
    data = read_csv_data(file_path)
    data.sort()  
    bins = create_bins(data, bin_size)
    mean_smoothed = binning_by_mean(bins)
    median_smoothed = binning_by_median(bins)
    boundary_smoothed = binning_by_boundaries(bins)

    print("\nOriginal Data:", data)
    print("Bins:")
    for bin in bins:
        print(f"[{', '.join(map(str, bin))}]")

    print("\nBinning by Mean:")
    for bin in mean_smoothed:
        print(f"[{', '.join(map(str, bin))}]")

    print("\nBinning by Median:")
    for bin in median_smoothed:
        print(f"[{', '.join(map(str, bin))}]")

    print("\nBinning by Boundaries:")
    for bin in boundary_smoothed:
        print(f"[{', '.join(map(str, bin))}]")

file_path = r'C:\Users\bhilw\OneDrive\Documents\DM\iris.csv'
bin_size = int(input('Enter bin size: '))
binning_data(file_path, bin_size)
