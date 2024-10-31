from src import globals as glb


def calculate():
    x = 6 * (glb.arguments['r10'] - 2 * glb.arguments['r5'] + glb.arguments['r0']) / 50
    y = 6 * (glb.arguments['r15'] - 2 * glb.arguments['r10'] + glb.arguments['r5']) / 50
    z = 6 * (glb.arguments['r20'] - 2 * glb.arguments['r15'] + glb.arguments['r10']) / 50
    glb.vctr[2] = (y - (x + z) / 4) * 4 / 7
    glb.vctr[1] = x / 2 - 0.25 * glb.vctr[2]
    glb.vctr[3] = z / 2 - 0.25 * glb.vctr[2]
    for i in range(int(glb.arguments['n'])):
        X = 20 / (glb.arguments['n'] - 1) * i
        i = int((X - 0.01) / 5) + 1
        r = (- glb.vctr[i - 1] / 30 * pow(X - glb.absArray[i], 3)
                   + glb.vctr[i] / 30 * pow(X - glb.absArray[i - 1], 3)
                   - (glb.ordArray[i - 1] / 5 - 5 / 6 * glb.vctr[i - 1])
                   * (X - glb.absArray[i])
                   + (glb.ordArray[i] / 5 - 5 / 6 * glb.vctr[i])
                   * (X - glb.absArray[i - 1]))
        glb.resArray.append(r)
