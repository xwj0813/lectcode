# -*- coding:utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from ftplib import FTP
import os
import argparse
#####################
# FTP info #
#####################
# '10.10.50.158', 31333, 'yzg', 'yzg', FLAGS.dataset_dir, 'xinhao.zip'
"""只能下载一级目录"""


def get_code(address, port, user, passwd, dataset_dir, file_name):
    ftp = FTP()  # ���ñ���
    timeout = 30
    ftp.connect(address, port, timeout)
    ftp.login(user, passwd)
    if not os.path.exists(dataset_dir):
        # os.mkdir(dataset_dir)
        os.makedirs(dataset_dir)
    os.chdir(dataset_dir)

    def _downloaddir(dirname):
        if not os.path.exists(dirname):
            # os.mkdir(dirname)
            os.makedirs(dataset_dir)
        os.chdir(dirname)
        print("dirname", dirname)
        ftp.cwd(dirname)  # 设置FTP当前操作的路径
        filelines = []
        ftp.dir(filelines.append)
        filelines_bk = ftp.nlst()
        for i in range(len(filelines)):
            file = filelines[i]
            file_name = filelines_bk[i]
            if 'd' in file.split()[0]:
                _downloaddir(file_name)
                ftp.cwd('..')
                os.chdir('..')
            else:
                with open(file_name, 'wb') as f:
                    download_cmd = 'RETR ' + file_name
                    ftp.retrbinary(download_cmd, f.write)
            print(file_name + ' download done....')
    _downloaddir(file_name)
    ftp.quit()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir', default='./code', type=str)

    parser.add_argument('--ftp_addr', default='10.10.50.158',  type=str)
    parser.add_argument('--ftp_port', default=31333, type=int)
    parser.add_argument('--debug', action='store_true')
    parser.add_argument('--ftp_user', default='SuperAdmin', type=str)
    parser.add_argument('--ftp_passwd', default='hello', type=str)

    parser.add_argument('--ftp_file', default='/code/textsim', type=str)  # 要下载的目录
    args = parser.parse_args()
    get_code(args.ftp_addr, args.ftp_port, args.ftp_user, args.ftp_passwd, args.data_dir, args.ftp_file)


if __name__ == '__main__':
    main()
