from Visualiser import Visualise
from Sorting import sortAlgo
import random

def generate(n = 50):
        return random.sample(range(1, n + 1), n)

if __name__ == '__main__':

    n = 40

    array = generate(n)

    screen = Visualise(1280, 720, n)

    #process = sortAlgo(array).insertion_Sort()
    #process = sortAlgo(array).bubble_Sort()
    process = sortAlgo(array).selection_Sort()
    #process = sortAlgo(array).binary_insertion_Sort()
    #quick sort, merge sort (are currently not working for graphical use)

    #speed : fast or normal speed (normal : ..)
    screen.update(process,'fast')