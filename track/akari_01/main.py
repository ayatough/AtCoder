import numpy as np

def calc_th_index(temperature, humidity):
    return 0.81 * temperature + 0.01 * humidity * (0.99 * temperature - 14.3) + 46.3

def main(csv):
    altitudes = csv[:,0]
    temperatures = csv[:,1]
    humidities = csv[:,2]
    th_indices = calc_th_index(temperatures, humidities)
    al_mean = np.mean(altitudes)
    al_var = np.var(altitudes)
    th_mean = np.mean(th_indices)
    th_var = np.var(th_indices)
    cov = np.mean((altitudes - al_mean) * (th_indices - th_mean))
    pcc = cov / np.sqrt(al_var * th_var)
    print(pcc)


if __name__ == '__main__':
    import sys
    csv = np.loadtxt(sys.argv[1], delimiter=',', skiprows=1, usecols=[1, 2, 3])
    main(csv)
