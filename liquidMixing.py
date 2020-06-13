def liquidMixing(densities):
    result = [densities[0]]
    for i in range(1, len(densities)):
        for j in range(i + 1):
            if densities[i] <= densities[j]:
                tmp = densities[i]
                for k in range(i, j, -1):
                    densities[k] = densities[k - 1]
                densities[j] = tmp
                if i % 2 == 1:
                    result.append((densities[(i + 1) // 2] +
                                  densities[i // 2]) / 2)
                else:
                    result.append(densities[i // 2])
                break
    return result
