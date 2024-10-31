from src import globals as glb


def argsInit(arg, total=0):
    for a, j in zip(glb.arguments, range(1, len(arg))):
        if float(arg[j]) <= 0:
            raise ValueError(
                "'{}' must be positive (is {})".format(
                    a, arg[j]))
        glb.arguments[a] = float(arg[j])
        if glb.arguments[a] is not glb.arguments['n']:
            glb.ordArray.append(glb.arguments[a])


def displayResult():
    print(
        "vector result: [{:.1f}, {:.1f}, {:.1f}, {:.1f}, {:.1f}]".format(
            glb.vctr[0] if round(
                glb.vctr[0], 1) != 0 else 0, glb.vctr[1] if round(
                glb.vctr[1], 1) != 0 else 0, glb.vctr[2] if round(
                    glb.vctr[2], 1) != 0 else 0, glb.vctr[3] if round(
                        glb.vctr[3], 1) != 0 else 0, glb.vctr[4] if round(
                            glb.vctr[4], 1) != 0 else 0))
    for j in range(int(glb.arguments['n'])):
        print("abscissa: {:.1f} cm\tradius: {:.1f} cm".format(
            20 / (glb.arguments['n'] - 1) * j, glb.resArray[j]))
