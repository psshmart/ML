import math
from enum import Enum
import random
from sklearn import datasets
import matplotlib.pyplot as plt


class IrisDatasetEnum(Enum):
    IrisS = 0
    IrisVersColour = 1
    IrisVerg = 2


class Iris:
    def __init__(self, sep_length, sep_width, pet_length, pet_width, iris_class):
        self.sep_length = sep_width
        self.sep_width = sep_width
        self.pet_length = pet_length
        self.pet_width = pet_width
        self.iris_class = iris_class


def load_dataset():
    iris_dataset = datasets.load_iris()
    data = []

    for k in range(len(iris_dataset.data)):
        data.append(
            Iris(
                iris_dataset.data[k][0],
                iris_dataset.data[k][1],
                iris_dataset.data[k][2],
                iris_dataset.data[k][3],
                iris_dataset.target[k]
            )
        )

    return data


def shuffled_data(data):
    shuffled = []

    while len(data) > 0:
        index = random.randint(0, len(data) - 1)
        shuffled.append(data.pop(index))

    return shuffled


def regulate_data(data):
    min = [math.inf, math.inf, math.inf, math.inf]
    max = [-1, -1, -1, -1]
    regulated_data = []
    for piece in data:
        if piece.sep_length > max[0]:
            max[0] = piece.sep_length
        if piece.sep_length < min[0]:
            min[0] = piece.sep_length

        if piece.sep_width > max[1]:
            max[1] = piece.sep_width
        if piece.sep_width < min[1]:
            min[1] = piece.sep_width

        if piece.pet_length > max[2]:
            max[2] = piece.pet_length
        if piece.pet_length < min[2]:
            min[2] = piece.pet_length

        if piece.pet_width > max[3]:
            max[3] = piece.pet_width
        if piece.pet_width < min[3]:
            min[3] = piece.pet_width

    for piece in data:
        regulated_data.append(
            Iris(
                (piece.sep_length - min[0]) / (max[0] - min[0]),
                (piece.sep_width - min[1]) / (max[1] - min[1]),
                (piece.pet_length - min[2]) / (max[2] - min[2]),
                (piece.pet_width - min[3]) / (max[3] - min[3]),
                piece.iris_class
            )
        )
    return (min, max, regulated_data)


def get_color(iris):
    if iris == IrisDatasetEnum.IrisS.value:
        return "green"
    elif iris == IrisDatasetEnum.IrisVerg.value:
        return "yellow"
    else:
        return "red"


def make_projections(data, regulated_data):
    f, a = plt.subplots(4, 4)

    a[0, 1].scatter(x=[iris.sep_length for iris in data],
                    y=[iris.sep_width for iris in data],
                    c=[get_color(iris.iris_class) for iris in data]
                    )
    a[0, 1].set_xlabel('sep_length')
    a[0, 1].set_ylabel('sep_width')

    a[0, 2].scatter(x=[iris.sep_length for iris in data],
                    y=[iris.pet_length for iris in data],
                    c=[get_color(iris.iris_class) for iris in data]
                    )
    a[0, 2].set_xlabel('sep_length')
    a[0, 2].set_ylabel('pet_length')

    a[0, 3].scatter(x=[iris.sep_length for iris in data],
                    y=[iris.pet_width for iris in data],
                    c=[get_color(iris.iris_class) for iris in data]
                    )
    a[0, 3].set_xlabel('sep_length')
    a[0, 3].set_ylabel('pet_width')

    a[1, 2].scatter(x=[iris.sep_width for iris in data],
                    y=[iris.pet_length for iris in data],
                    c=[get_color(iris.iris_class) for iris in data]
                    )
    a[1, 2].set_xlabel('sep_width')
    a[1, 2].set_ylabel('pet_length')

    a[1, 3].scatter(x=[iris.sep_width for iris in data],
                    y=[iris.pet_width for iris in data],
                    c=[get_color(iris.iris_class) for iris in data]
                    )
    a[1, 3].set_xlabel('sep_width')
    a[1, 3].set_ylabel('pet_width')

    a[2, 3].scatter(x=[iris.pet_length for iris in data],
                    y=[iris.pet_width for iris in data],
                    c=[get_color(iris.iris_class) for iris in data]
                    )
    a[2, 3].set_xlabel('pet_length')
    a[2, 3].set_ylabel('pet_width')

    a[1, 0].scatter(x=[iris.sep_length for iris in regulated_data],
                    y=[iris.sep_width for iris in regulated_data],
                    c=[get_color(iris.iris_class) for iris in regulated_data]
                    )
    a[1, 0].set_xlabel('sep_length')
    a[1, 0].set_ylabel('sep_width')

    a[2, 0].scatter(x=[iris.sep_length for iris in regulated_data],
                    y=[iris.pet_length for iris in regulated_data],
                    c=[get_color(iris.iris_class) for iris in regulated_data]
                    )
    a[2, 0].set_xlabel('sep_length')
    a[2, 0].set_ylabel('pet_length')

    a[2, 1].scatter(x=[iris.sep_length for iris in regulated_data],
                    y=[iris.pet_width for iris in regulated_data],
                    c=[get_color(iris.iris_class) for iris in regulated_data]
                    )
    a[2, 1].set_xlabel('sep_length')
    a[2, 1].set_ylabel('pet_width')

    a[3, 0].scatter(x=[iris.sep_width for iris in regulated_data],
                    y=[iris.pet_length for iris in regulated_data],
                    c=[get_color(iris.iris_class) for iris in regulated_data]
                    )
    a[3, 0].set_xlabel('sep_width')
    a[3, 0].set_ylabel('pet_length')

    a[3, 1].scatter(x=[iris.sep_width for iris in regulated_data],
                    y=[iris.pet_width for iris in regulated_data],
                    c=[get_color(iris.iris_class) for iris in regulated_data]
                    )
    a[3, 1].set_xlabel('sep_width')
    a[3, 1].set_ylabel('pet_width')

    a[3, 2].scatter(x=[iris.pet_length for iris in regulated_data],
                    y=[iris.pet_width for iris in regulated_data],
                    c=[get_color(iris.iris_class) for iris in regulated_data]
                    )
    a[3, 2].set_xlabel('pet_length')
    a[3, 2].set_ylabel('pet_width')

    f.set_figwidth(16)
    f.set_figheight(16)

    plt.show()


def get_dist(iris_1, iris_2):
    return math.sqrt(math.pow(iris_1.sep_length - iris_2.sep_length, 2) +
                     math.pow(iris_1.sep_width - iris_2.sep_width, 2) +
                     math.pow(iris_1.pet_length - iris_2.pet_length, 2) +
                     math.pow(iris_1.pet_width - iris_2.pet_width, 2))


def get_opt_k(data):
    min_k = int(math.sqrt(len(data)) / 2)
    max_k = int(math.sqrt(len(data)) * 2)

    data_test = []
    for i in range(int(len(data) * 0.3)):
        data_test.append(data.pop(0))

    exact_k = []

    for k in range(min_k, max_k + 1):
        total = 0
        right_count = 0

        for t_item in data_test:
            # Ищем k ближайших соседей
            dist_class = []
            for item in data:
                if len(dist_class) < k:
                    dist_class.append((get_dist(t_item, item), item.iris_class))
                else:
                    max_dist_class_index = -1
                    max_dist_class = dist_class[0]
                    for i in range(len(dist_class)):
                        if dist_class[i][0] > max_dist_class[0]:
                            max_dist_class = dist_class[i]
                            max_dist_class_index = i

                    current_distance = get_dist(t_item, item)
                    if current_distance < max_dist_class[0]:
                        dist_class[max_dist_class_index] = (current_distance, item.iris_class)

            predicted = IrisDatasetEnum.IrisS
            verginica_count = 0
            setosa_count = 0
            versicolour = 0
            for item in dist_class:
                if item[1] == IrisDatasetEnum.IrisVerg.value:
                    verginica_count += 1
                elif item[1] == IrisDatasetEnum.IrisS.value:
                    setosa_count += 1
                else:
                    versicolour += 1

            if verginica_count >= setosa_count and verginica_count >= versicolour:
                predicted = IrisDatasetEnum.IrisVerg
            elif setosa_count >= verginica_count and setosa_count >= versicolour:
                predicted = IrisDatasetEnum.IrisS
            else:
                predicted = IrisDatasetEnum.IrisVersColour

            if predicted.value == t_item.iris_class:
                right_count += 1
            total += 1

        exact_k.append((right_count / total, k))

    max_accuracy = exact_k[0]
    for item in exact_k:
        if item[0] > max_accuracy[0]:
            max_accuracy = item

    return max_accuracy[1]


def classification(min, max, data, k):
    sep_length = (float(input('Input sep_length')) - min[0]) / (max[0] - min[0])
    sep_width = (float(input('Input sep_width')) - min[1]) / (max[1] - min[1])
    pet_length = (float(input('Input pet_length')) - min[2]) / (max[2] - min[2])
    pet_width = (float(input('Input pet_width')) - min[3]) / (max[3] - min[3])

    iris = Iris(sep_length, sep_width, pet_length, pet_width, IrisDatasetEnum.IrisVersColour)

    dist_class = []
    for i in data:
        if len(dist_class) < k:
            dist_class.append((get_dist(iris, i), i.iris_class))
        else:
            max_dist_class_index = -1
            max_dist_class = dist_class[0]
            for k in range(len(dist_class)):
                if dist_class[k][0] > max_dist_class[0]:
                    max_dist_class = dist_class[k]
                    max_dist_class_index = k

            curr_dist = get_dist(iris, i)
            if curr_dist < max_dist_class[0]:
                dist_class[max_dist_class_index] = (curr_dist, i.iris_class)

    verginica_c = 0
    setosa_c = 0
    versicolour_c = 0
    for i in dist_class:
        if i[1] == IrisDatasetEnum.IrisVerg.value:
            verginica_c += 1
        elif i[1] == IrisDatasetEnum.IrisS.value:
            setosa_c += 1
        else:
            versicolour_c += 1

    if verginica_c >= setosa_c and verginica_c >= versicolour_c:
        print('Verginica')
    elif setosa_c >= verginica_c and setosa_c >= versicolour_c:
        print('Setosa')
    else:
        print('Versicolour')


data = load_dataset()
shuffled = shuffled_data(data)
regulated_data = regulate_data(shuffled)
make_projections(shuffled, regulated_data[2])
k = get_opt_k(regulated_data[2])
classification(regulated_data[0], regulated_data[1], regulated_data[2], k)