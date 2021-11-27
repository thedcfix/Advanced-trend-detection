import pandas
import functions
import json
import numpy
import pickle
import stockpicking_functions as sp

data = pandas.read_csv("data.csv")
recreateModel = True
n_cluster = 25

with open('data.txt') as json_file:
    sequences = json.load(json_file)
    sequences = numpy.array(sequences)

values = functions.normalize(data["close"].values)

# splits data in blocks of 30 days going back up to 90 days. Returns an array of arrays
months = functions.splitData(values, 30, 90)

if recreateModel:
    model = functions.createClusteringModel(n_cluster, 20, 400, "full")
    model = functions.trainModel(model, sequences)

    # saving the model to file for reusage
    outfile = open("model.pkl",'wb')
    pickle.dump(model, outfile)
    outfile.close()
else:
    infile = open("model.pkl",'rb')
    model = pickle.load(infile)
    infile.close()

prediction = functions.predict(model, months[2])

print(prediction)

centroids = functions.getCentroids(model, showdata=False)

for centroid in centroids:
    print("Variance: ", sp.variance(centroid))
    print("Max: ", sp.max(centroid))
    print("Min: ", sp.min(centroid))
    print("Average: ", sp.average(centroid))
    print("Max Delta: ", sp.maxDelta(centroid))
    print("Delta Sequence: ", sp.deltaSequence(centroid))
    print("Growth %: ", sp.growth(centroid), "%\n")

functions.viewAdvancedCentroids(model, 0.005)