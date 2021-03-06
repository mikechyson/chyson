import matplotlib.pyplot as plt
from chyson.parse.model_net_40_to_graph import *


def plot(off_file, sep=' '):
    # 3D show
    from mpl_toolkits.mplot3d import Axes3D

    # 3D config
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    plt.axis('off')

    # read file
    fh = open(off_file, 'r', encoding=encoding)
    lines = fh.read().rstrip().split('\n')

    # vertices faces edges
    vfe = lines[1].rstrip()

    num_vertices = int(vfe.split(off_sep)[0])
    vertices = lines[vertex_start:vertex_start + num_vertices]
    faces = lines[vertex_start + num_vertices:]

    vertex_dict = index_position(vertices, sep)

    # plot vertices
    arr = []
    for v in vertex_dict.values():
        arr.append(v)
    arr = np.array(arr)
    x = arr[:, 0]
    y = arr[:, 1]
    z = arr[:, 2]
    ax.scatter(x, y, z, color='red')

    # plot edges
    all_edge = []
    for face in faces:
        lst = face.split(off_sep)
        num_edges = int(lst[0])
        polygon = lst[1:]

        sub_edge = []
        for e in range(num_edges):
            idx1 = int(polygon[e])
            idx2 = int(polygon[(e + 1) % num_edges])

            sub_edge.append([vertex_dict[idx1][0], vertex_dict[idx1][1], vertex_dict[idx1][2]])
            sub_edge.append([vertex_dict[idx2][0], vertex_dict[idx2][1], vertex_dict[idx2][2]])

        all_edge.append(sub_edge)

    for edge in all_edge:
        edge = np.array(edge)
        x = edge[:, 0]
        y = edge[:, 1]
        z = edge[:, 2]
        ax.plot(x, y, z, color='black')

    plt.show()
