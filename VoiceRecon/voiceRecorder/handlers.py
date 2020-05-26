from .models import Author
from . import pyfil
import numpy as np


def matchAuthor(author):
    try:
        currentAuthor = Author.objects.get(author=author)
        print(author + ' recognised')
    except Author.DoesNotExist:
        print("New author is here: " + author)
        currentAuthor = Author(author=author)
        currentAuthor.save()

    result = currentAuthor.pk
    return result


def trainingHandler(files, author):
    authorID = matchAuthor(author)
    authorID = np.array([authorID], dtype=np.float64)
    for file in files:
        print('received file:')
        print(file)
        data = pyfil.Voice2Data(file)
        print(type(data[0]))
        print(type(authorID))
        data = np.append(data, authorID)
        # print(data)
        print(len(data))
        data = data.reshape(1, data.shape[0])
        f = open('datos.csv', 'ab')
        np.savetxt(f, data, delimiter=',')
        # f.close()
        print('Successfully added record')


def resultHandler(file):
    data = pyfil.Voice2Data(file)
    data = data.reshape(1, data.shape[0])

    f = open('guess.csv', 'w')
    np.savetxt(f, data, delimiter=',')
    f.close()
