import os
import time

# 1. 在列表中指定需要备份的文件与目录
source = ['"F:/Programming/Python/pcode/bytepython"', 'F:\\Programming\\Python\\byte-of-python-chinese-edition.pdf']
# source = ['/Users/swa/notes']  # Linux
print('source:', source, '\n')
# 2. 备份文件必须存储在一个主备份目录中
target_dir = 'F:\\Backup_Programming'
print('target_dir:', target_dir, '\n')
# target_dir = /Users/loren/backup  # Linux

# 3. 将备份文件打包成 .zip 文件
# 4. zip 压缩文件的文件名由当前日期与时间构成
target = target_dir + os.sep + \
         time.strftime('%Y%m%d%H%M%S') + '.zip'
print('target:', target, '\n')

# 如果目标目录还不存在，则进行创建
if not os.path.exists(target_dir):
    os.mkdir(target_dir)
    print('Create Target Directory ...')

# 5. 使用 zip 命令将文件打包成 zip 格式
zip_command = 'zip -r {0} {1}'.format(target, ' '.join(source))

# 运行备份
print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')