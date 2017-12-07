#
# スクレイピングの繰り返し実行用
#

from subprocess import call
import os
import time
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)


while True:
    call(["scrapy", "runspider", "yahoospider.py"], cwd=dir_path)
    print('run spider')
    time.sleep(30)