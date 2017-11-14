import os
import time

source = ['F:\\Programming\\Python\\pcode\\bytepython']

target_dir = 'F:\\Backup_Programming'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)

today_dir = target_dir + os.sep + time.strftime('%Y%m%d')
if not os.path.exists(today_dir):
    os.mkdir(today_dir)
print('today_dir:', today_dir, '\n')

now = time.strftime('%H%M%S')

comment = input('Enter a comment --> ')

# 检查是否有评论键入
if len(comment) == 0:
    target = today_dir + os.sep + now + '.zip'
else:
    target = today_dir + os.sep + now + '_' \
             + comment.replace(' ', '_') + '.zip'
    print('target:', target)

zip_command = 'zip -r -v {0} {1}'.format(target, ' '.join(source))

print('Zip command is:\n', zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('Successfully backup to', target)
else:
    print('Backup FAILED')