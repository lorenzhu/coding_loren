import os
import time

source = ['"F:/Programming/Python/pcode/bytepython"',
           'F:\\Programming\\Python\\byte-of-python-chinese-edition.pdf']

target_dir = 'F:\\Backup_Programming'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)
    print('Create target_dir:', target_dir, '\n')

# 4. 将当前日期作为主备份目录下的子目录名称
today = target_dir + os.sep + time.strftime('%Y%m%d')
print('today directory:', today, '\n')

# 将当前时间作为 zip 文件的文件名
now = time.strftime('%H%M%S')

# zip 文件名称格式
target = today + os.sep + now + '.zip'
print('target:', target, '\n')

if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory:', today, '\n')

zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))

print('Zip command is:', zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successfully backup to', target)
else:
    print('Backup FAILED')