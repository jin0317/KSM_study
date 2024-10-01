# -*- coding:utf-8 -*-

import os 

import sys 

import matplotlib as mpl

from matplotlib import font_manager 



# 폰트매니저 리빌드

# font_manager._rebuild() 



# 설치되어 있는 폰트 리스트 가져오기 

if sys.platform=='win32':

    #시스템 글꼴 목록을 리스트로 가져오기 

    font_list=font_manager.findSystemFonts() 

    

    # 이름순정렬

    font_list.sort() 

    

    # 리스트탐색반복

    for file_path in font_list:

        #폰트 파일의 경로를 사용하여 폰트 속성 객체 가져오기

        fp=font_manager.FontProperties(fname=file_path) 

        

        # 폰트 속성을 통해 파이썬에 설정해야 하는 폰트 이름 조회 

        font_name=fp.get_name() 

        

        # 폰트 파일 경로와 폰트 이름 출력하기

        print("%s >> %s" %(file_path,font_name))

else:
    # else 부분은 mac에서 작동한다
    # 설정 파일의 위치 조회

    conf_file_path = mpl.matplotlib_fname() 

    print('설정 파일 위치:' + conf_file_path)

    

    # 설정 파일이 들어 있는 폴더

    conf_file_dir=os.path.dirname(conf_file_path) 

    print('설정 폴더 위치:' +conf_file_dir)

    

    # 설정파일의 폴더 하위에 폰트 파일이 위치해야 하는 폴더 경로 조합

    font_path=conf_file_dir+"/fonts/ttf" 

    print('폰트 폴더 위치:' + font_path) 

    

    # 폰트 폴더를 열기 위한 명령어 수행 

    command='open '+font_path 

    os.system(command) 