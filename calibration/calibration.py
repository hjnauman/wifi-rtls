from math import log10

DELIM = ' | '

def calculate_path_loss_exponent():
    """
    Cancel c from the equation to get all mean formulas in terms of n, then use the average values
    to calculate the n value.
    rssi(d) = -10n log_10(d) - c
    """

    multiplicand = 1
    n_calculation_list = []

    with open('calibration/distance_rssi_measurements_means.txt', 'r') as f:
        lines = f.readlines()

        for line in lines:
            line = line.strip('\n')
            distance = int(line.split(DELIM)[0])
            rssi = int(line.split(DELIM)[1])

            n_calculation_list.append([(rssi*multiplicand), (multiplicand*-10)*log10(distance)])

            multiplicand *= -1

        total_rssi = 0
        total_n_multiplicand = 0
        for i in n_calculation_list:
            total_rssi += i[0]
            total_n_multiplicand += i[1]

        n = float(total_rssi / total_n_multiplicand)

        return n

def calculate_mean_environmental_loss(n):
    """
    Calculate c for each reading and then average the c value across the board.
    rssi(d) = -10n log_10(d) - c
    """

    c_calculation_list = []

    with open('calibration/distance_rssi_measurements.txt', 'r') as f:
        lines = f.readlines()

        for line in lines:
            line = line.strip('\n')
            distance = int(line.split(DELIM)[0])
            rssi = int(line.split(DELIM)[1])

            c_calculation_list.append((rssi + (-10.0*n) * log10(distance)) * -1)

        total_c = 0
        for c_calculation in c_calculation_list:
            total_c += c_calculation

        mean_c = total_c / len(c_calculation_list)

        return mean_c

        print()

n = calculate_path_loss_exponent()
mean_c = calculate_mean_environmental_loss(n)

print(f'Calculated n value to be : {n}')
print(f'Calculated average c value to be : {mean_c}')
