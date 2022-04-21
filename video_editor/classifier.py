import os
import shutil


def collect_weight(filename):
    a = os.path.splitext(filename)[0]
    print(filename)
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
                try:
                    if weight // 10 == 4:
                        mv_file(f'{path}\\{filename}',f'E:\\seongwon\\img\\class_origin\\{str(weight)[0]}0\\')
                    elif weight // 10 == 5:
                        mv_file(f'{path}\\{filename}', f'E:\\seongwon\\img\\class_origin\\{str(weight)[0]}0\\')
                    elif weight // 10 == 6:
                        mv_file(f'{path}\\{filename}',f'E:\\seongwon\\img\\class_origin\\{str(weight)[0]}0\\')
                    elif weight // 10 == 7:
                        mv_file(f'{path}\\{filename}',f'E:\\seongwon\\img\\class_origin\\{str(weight)[0]}0\\')
                    elif weight // 10 == 8:
                        mv_file(f'{path}\\{filename}',f'E:\\seongwon\\img\\class_origin\\{str(weight)[0]}0\\')
                    elif weight // 10 == 9:
                        mv_file(f'{path}\\{filename}',f'E:\\seongwon\\img\\class_origin\\{str(weight)[0]}0\\')
                    elif weight // 10 == 10:
                        mv_file(f'{path}\\{filename}',f'E:\\seongwon\\img\\class_origin\\100\\')
                    elif weight // 10 == 11:
                        mv_file(f'{path}\\{filename}',f'E:\\seongwon\\img\\class_origin\\110\\')
                    elif weight // 10 == 12:
                        mv_file(f'{path}\\{filename}',f'E:\\seongwon\\img\\class_origin\\120\\')
                    else:
                        mv_file(f'{path}\\{filename}',f'E:\\seongwon\\img\\class_origin\\120+\\')
                except:
                    continue


if __name__ == '__main__':
    find_file('E:\\seongwon\\img\\mun-3')
    #print(collect_weight('1234_1234_24.4-10.png'))
