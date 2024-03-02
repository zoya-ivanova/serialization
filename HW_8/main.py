import os
import json
import csv
import pickle

def get_dir_size(directory):
    total_size = 0
    for root, dirs, files in os.walk(directory):
        for name in files:
            path = os.path.join(root, name)
            total_size += os.path.getsize(path)
        for name in dirs:
            path = os.path.join(root, name)
            total_size += get_dir_size(path)
    return total_size


def traverse_directory(directory):
    results = []
    for root, dirs, files in os.walk(directory):
        for name in files:
            path = os.path.join(root, name)
            size = os.path.getsize(path)
            results.append({'Path': path, 'Type': 'File', 'Size': size})
        for name in dirs:
            path = os.path.join(root, name)
            size = get_dir_size(path)
            results.append({'Path': path, 'Type': 'Directory', 'Size': size})
    return results


def save_results_to_json(results, filename):
    with open(filename, 'w') as f:
        json.dump(results, f, indent=4)


def save_results_to_csv(results, filename):
    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['Path', 'Type', 'Size'])
        writer.writeheader()
        for result in results:
            writer.writerow(result)


def save_results_to_pickle(results, filename):
    with open(filename, 'wb') as f:
        pickle.dump(results, f)

directory = 'geekbrains'
results = traverse_directory(directory)

save_results_to_json(results, 'results.json')
save_results_to_csv(results, 'results.csv')
save_results_to_pickle(results, 'results.pkl')