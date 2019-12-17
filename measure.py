from datetime import datetime as dt
from collections import OrderedDict
import sys

filename = sys.argv[1]
distance = int(sys.argv[2])

if __name__ == '__main__':

    odic = OrderedDict()

    fr = open(filename,'r')
    line = fr.readline()
    header = line.rstrip().split(',')
    header.append('speed')

    print(','.join(header))

    while line:
        elements = line.rstrip().split(',')
        id = elements[3]

        if id in odic:
            pre_dt_str = odic[id][0]
            crr_dt_str = elements[0]

            pre_format = '%Y-%m-%d %H:%M:%S' if len(pre_dt_str) == 19 else '%Y-%m-%d %H:%M:%S.%f'
            crr_format = '%Y-%m-%d %H:%M:%S' if len(crr_dt_str) == 19 else '%Y-%m-%d %H:%M:%S.%f'

            pre_dt = dt.strptime(pre_dt_str, pre_format)
            crr_dt = dt.strptime(crr_dt_str, crr_format)
            tdelta = (crr_dt - pre_dt).total_seconds()

            kmh = round((distance/5)/(tdelta/18),1)
            elements.append(str(kmh))

            print(','.join(elements))

        else:
            odic[id] = elements

        if len(odic) > 1000:
            odic.popitem(last=False)

        line = fr.readline()

    fr.close()