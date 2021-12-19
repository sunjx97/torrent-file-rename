import os
import re

torrents_src = input('请输入torrents文件夹绝对路径：')
resume_src = input('请输入resume文件夹绝对路径：')

torrent_list = os.listdir(torrents_src)
resume_list = os.listdir(resume_src)

count = 0

for torrent in torrent_list:
    # 从16位hash值开始，到后缀名结束
    # 如果是新版文件40位hash，则会截取后16位，在下面match起始位置匹配匹配失败
    pattern = torrent[-24:-8]

    for resume in resume_list:
        if re.match(pattern, resume[:-7], re.I):
            print('Ok, find the files!')
            print('torrent:', torrent)
            print('resume:', resume)
            os.rename(torrents_src+'\\'+torrent, torrents_src+'\\'+resume[:-7]+'.torrent')
            print(f'{torrent} 已更名为 {resume[:-7]}.torrent')
            print('==========================')
            count += 1

print(f'已成功命名{count}个种子文件')
