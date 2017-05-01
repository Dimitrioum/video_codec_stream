# -*- coding: utf-8 -*-
import re, subprocess, cv2

def _check_stat_cam(number):
    return cv2.VideoCapture(number).read()[0]


def _get_cameras(numbers, devices, check_stat):
    device_re = re.compile("Bus\s+(?P<bus>\d+)\s+Device\s+(?P<device>\d+).+ID\s(?P<id>\w+:\w+)\s(?P<tag>.+)$", re.I)
    n_o_c = []

    for i in devices.split('\n'):
        if i:
            info = device_re.match(i)
            if info:
                dinfo = info.groupdict()
                if int(dinfo['bus']) in numbers and 'root' not in dinfo['tag'].split(' '):
                    n_o_c.append(dinfo['tag'])

    if (check_stat):
        n_o_c.append('stationary')
        numbers.append(len(numbers)+1)

    return dict(zip([(i+1) for i in range(len(numbers))], n_o_c))


def _get_all_devices():
    df = subprocess.check_output("lsusb", shell=True)
    return df


if __name__ == '__main__':
    check_stat = _check_stat_cam(0)

    devices = _get_all_devices()
    print(devices)

    numbers = raw_input('Введите номера USB-портов видеокамер через запятую для дальнейшей работы: ').split(',')
    numbers = [int(i) for i in numbers]

    #numbers = [001, 003]
    print(_get_cameras(numbers, devices, check_stat))
