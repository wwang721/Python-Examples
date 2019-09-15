import sys
import time

def progress_bar(rate):
    """ 进度条效果

    :param rate: 进度百分比
    """
    label = ["-", "\\", "|", "/"]
    # 获取标准输出
    _output = sys.stdout
    bar = ""
    for i in range(rate // 2):
        bar = bar + "="
    for i in range(50 - rate // 2):
        bar = bar + " "
    # 输出进度条
    _output.write(f'\rProc:[{bar}][{rate:.0f}%][{label[rate%4]}]')
    if rate == 100:
        _output.write(f'\n')
    # 将标准输出一次性刷新
    _output.flush()

def main():
    for rate in range(101):
        progress_bar(rate)
        time.sleep(0.02)

if __name__ == "__main__":
    main()