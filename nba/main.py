import numpy as np
import pandas as pd


def main():
    symptoms = pd.read_csv("symptom.csv", sep=";")
    diseases = pd.read_csv("disease.csv", sep=";")
    init_symptoms = np.random.randint(0,2, symptoms.shape[0])
    probability = np.zeros(diseases.shape[0])
    for i in range(len(probability) - 1):
        for j in range(len(init_symptoms)):
            if init_symptoms[j] == 1:
                if probability[i] == 0:
                    probability[i] += 1
                probability[i] *= symptoms.iloc[j][i + 1]
        probability[i] *= diseases.iloc[i][1] / diseases.iloc[len(diseases)-1][1]
    max_prob = probability.max()
    print(max_prob)
    print(probability)
    disease_index = np.where(probability == max_prob)
    print(disease_index)
    print("Название болезни: " + diseases.iloc[int(disease_index[0])][0])

if __name__ == '__main__':
    main()