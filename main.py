import shutil
import os

# os.chdir("C:/98_Git/Python_file_overwrite/origin_file_folder")        # directory 이동
# os.chdir("../")                                                       # 상위 directory로 이동

very_top_dir = os.getcwd()                                              # 현재 경로
# print(os.getcwd())                                                    # 현재 경로
origin_path = very_top_dir + "/origin_file_folder/origin.c"
new_path = very_top_dir + "/origin_file_folder/New.c"

os.chdir(very_top_dir + "/origin_file_folder")                          # origin_file_folder 로 이동
if not(os.path.isfile(origin_path)):                                    # file 존재 여부 확인
    os.rename('New.c', 'origin.c',)                                     # New.c를 origin.c로 이름 변경  (origin_file_folder에 origin.c가 있으면 실행)
else:
    os.rename('origin.c', 'New.c')                                      # origin.c를 New.c로 이름 변경  (origin_file_folder에 new.c가 있으면 실행)
    src = new_path                                                      # New.c 위치
    dst = very_top_dir + "/new_file_folder"                             # New.c 복붙할 위치
    shutil.copy(src, dst)                                               # src 를 dst로 복사

os.chdir(very_top_dir + "/new_file_folder")                             # new_file_folder에 작업 끝났다는 확인용 txt 만들기
f = open('파일 옮기기 완료!.txt', 'w')
f.write("Done!")
f.close

# 두번정도 눌러보면 origin_file_folder에 origin.c가 존재할 경우 이름을 New.c로 바꾸고 new_file_folder로 붙여넣기(덮어쓰기) 한걸 볼 수 있다.