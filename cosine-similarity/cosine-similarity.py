import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    # Write code here
    mag_a = np.linalg.norm(a)
    mag_b = np.linalg.norm(b)

    print(mag_a, mag_b)

    if mag_a == 0 or mag_b ==0:
        return float(0)

    return float((np.dot(a,b)) / (mag_a * mag_b ))