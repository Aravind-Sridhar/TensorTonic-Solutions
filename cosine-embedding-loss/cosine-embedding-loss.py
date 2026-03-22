def cosine_embedding_loss(x1, x2, label, margin):
    """
    Compute cosine embedding loss for a pair of vectors.
    label: 1 (similar), -1 (dissimilar)
    """
    x1_mag = (sum(val**2 for val in x1)) ** 0.5
    x2_mag = (sum(val**2 for val in x2)) ** 0.5

    dot = sum(a * b for a, b in zip(x1, x2))
    cos = dot / (x1_mag * x2_mag)

    if label == 1:
        return 1 - cos
    else:
        return max(0, cos - margin)