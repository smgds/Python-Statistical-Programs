# =============================================================================
# 
'''CPSC-51100, Summer II 2019
NAME: Amy Noyes
PROGRAMMING ASSIGNMENT #2
'''
# =============================================================================
print("\n")
print("CPSC-51100, Summer II 2019", "NAME: Amy Noyes", \
      "PROGRAMMING ASSIGNMENT #2", sep="\n")
      
print("\n")

import os

print("Input File Directory")
print(os.getcwd() + "\n")

# Read text file and convert strings to a list of floats
def get_datasets(): 
    datasets_file = open('prog2-input-data.txt', 'r'); 
    datasets = datasets_file.readlines() 
    
    datasets = [float(dataset) for dataset in datasets]
    datasets_file.close()
    return datasets

# User enters number of k clusters
k = int(input('Enter the number of clusters: '))
print("\n")

# Initializes centroids with the first k points as initial centroids \
# using a dict data structure
def initial_centroids(k, datasets):
    centroids = dict()
    for i in range(k):
        centroids[i] = datasets[i]
    return centroids

# Initializes dict clusters
def initial_clusters(k):
    clusters = dict()
    for i in range(k):
        clusters[i] = []
    return clusters

# Get closest cluster to the centroids
def get_closest(point, centroids):
    distances = []    
# Lambda = anonymous function
    get_distance = lambda A, B: abs(A - B)
    for cluster, centroid in centroids.items():
        distance = (cluster, get_distance(point, centroid))
        distances.append(distance)
    closest_cluster = min(distances, key=lambda x: x[1])[0]
    return closest_cluster

# Print each iteration
def print_clusters(iteration, clusters):
    print('Iteration', iteration)
    for cluster, datasets in clusters.items():
        print(cluster, datasets)
    print()

# K-means clustering: get centroids, loop to get new centroids
def kmeans(k, datasets):
    centroids = initial_centroids(k, datasets)
    clusters = initial_clusters(k)
    clusters_copy = None
    get_centroid = lambda points: sum(points) / len(points)

    iteration = 0
    while clusters != clusters_copy:
        iteration += 1
        clusters_copy = clusters.copy()
        clusters = initial_clusters(k)
        for dataset in datasets:
            cluster = get_closest(dataset, centroids)
            clusters[cluster].append(dataset)
        for cluster in clusters.keys():
            centroids[cluster] = get_centroid(clusters[cluster])
        print_clusters(iteration, clusters)
    return clusters

# Print output
def format_output(clusters):
    output = ''
    for cluster, datasets in clusters.items():
        for dataset in datasets:
            output += 'Point %s in cluster %s\n' % (dataset, cluster)
    return output

datasets = get_datasets()
clusters = kmeans(k, datasets)

# Print final output
output = format_output(clusters)
print(output)

# File output to Input File Directory shown by print(os.getcwd())
output_file = open('prog2-output-data.txt', 'w')
output_file.write(output)
output_file.close()
