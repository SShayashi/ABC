import numpy as np


def get_rotation_matrix(rad):
    """
    指定したradの回転行列を返す
    """
    rot = np.array([[np.cos(rad), -np.sin(rad)],
                    [np.sin(rad), np.cos(rad)]])
    return rot


def main():
    a, b, h, m = map(int, input().split())

    radis_h = np.deg2rad((360 / 12) * h + 30*(m/60))
    radis_m = np.deg2rad((360 / 60) * m)

    a_point = np.array([0, 1])
    b_point = np.array([0, 1])

    rot_a = get_rotation_matrix(radis_h)
    rot_b = get_rotation_matrix(radis_m)

    a_fin = np.dot(rot_a, a_point) * a
    b_fin = np.dot(rot_b, b_point) * b
    return np.linalg.norm(a_fin - b_fin)


print(main())
