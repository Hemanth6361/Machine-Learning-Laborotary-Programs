import pandas as pd
import numpy as np
import math

dt = pd.read_csv("Id3.csv")
print(dt)

attributes = list(dt.columns[:-1])
target = dt.columns[-1]

def entropy(data, target):
    class_counts = data[target].value_counts()
    total_rows = len(data)
    ent = 0
    for cnt in class_counts:
        p = cnt / total_rows
        ent -= p * math.log2(p)
    return ent

def attribute_entropy(data, attribute, target):
    attr_values = data[attribute].unique()
    total_ent = 0
    for val in attr_values:
        subset = data[data[attribute] == val]
        # print(subset)
        subset_ent = entropy(subset, target)
        subset_prob = len(subset) / len(data)
        total_ent += subset_prob * subset_ent
    return total_ent

def IG(data, attribute, target):
    ent = entropy(data, target)
    attr_ent = attribute_entropy(data, attribute, target)
    return ent - attr_ent

def id3(data, attributes, target):
    if len(data[target].unique()) == 1:
        return data[target].iloc[0]
    
    elif len(attributes) == 0:
        return data[target].mode()[0]
    
    else:
        info_gains = []
        for attribute in attributes:
            info_gains.append(IG(data, attribute, target))
            
        print(info_gains)    
        best_index = np.argmax(info_gains)
        best_attr = attributes[best_index]
        tree = {best_attr: {}}
        remaining_attrs = attributes.copy()
        remaining_attrs.remove(best_attr)
        
        
        for value in data[best_attr].unique():
            subset = data[data[best_attr] == value]
            if len(subset) == 0:
                tree[best_attr][value] = data[target].mode()[0]
            else:
                subtree = id3(subset, remaining_attrs, target)
                tree[best_attr][value] = subtree
        return tree

def predict(example, tree):
    # attribute = list(tree.keys())[0]
    # subtree = tree[attribute]
    for attr, subtree in tree.items():
        value = example[attr]
        if value in subtree:
            if isinstance(subtree[value], dict):
                return predict(example, subtree[value])
            else:
                return subtree[value]
        else:
            return None


def printTree(tree, indent=''):
    if isinstance(tree, dict):
        for attr, subtree in tree.items():
            print(indent + attr)
            printTree(subtree, indent + '\t')
    else:
        print(indent + '->', tree)


tree = id3(dt, attributes, target)

print("Decision Tree:")
printTree(tree)

example = {"Fever": "YES", "Cough": "YES", "Breathing issues": "NO"}
prediction = predict(example, tree)
print("Prediction:", prediction)
