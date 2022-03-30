import os
import shutil


def collect_weight(filename):
    a = os.path.splitext(filename)[0]
    b = a.split('_')[2]
    c = float(b.split('-')[0])
    return c


def mv_file(now_path, mv_path):
    shutil.move(now_path, mv_path)


def find_file(root_path):
    for path, dirs, files in os.walk(root_path):
        for filename in files:
            ext = os.path.splitext(filename)[-1]
            if ext == '.png':
                weight = collect_weight(filename)
                if weight // 10 == 4:
                    print(path + filename)
                elif weight // 10 == 5:
                    print(path + filename)
                elif weight // 10 == 6:
                    print(path + filename)
                elif weight // 10 == 7:
                    print(path + filename)
                elif weight // 10 == 8:
                    print(path + filename)
                elif weight // 10 == 9:
                    print(path + filename)
                elif weight // 10 == 10:
                    print(path + filename)
                else:
                    print(path + filename)



if __name__ == '__main__':
    find_file('E:/seongwon/img/slice_images')
    #print(collect_weight('1234_1234_24.4-10.png'))
