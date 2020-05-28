def imageTruncation(image, threshold):
    for i in range(len(image)):
        for j in range(len(image[i])): image[i][j] = min(image[i][j], threshold)
    return image
