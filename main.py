import mymodule
import os

# os.chdir("C:/98_Git/Python_file_overwrite/origin_file_folder")        # directory 이동
# os.chdir("../")                                                       # 상위 directory로 이동

very_top_dir = os.getcwd()                                              # 현재 경로
origin_folder_path = very_top_dir + "/origin_file_folder/"
origin_file_path = very_top_dir + "/origin_file_folder/origin.c"
new_folder_path = very_top_dir + "/new_file_folder/"
new_file_path = very_top_dir + "/new_file_folder/New.c"
TargetText = "printf"

# mymodule.movefile(origin_folder_path, new_folder_path)

# flag, splitdata = mymodule.fileopen(origin_file_path, TargetText)          # split 기준 : 띄어쓰기
# print(flag,splitdata)
# print(mymodule.filefind(origin_file_path, TargetText))

print(mymodule.filefind(origin_file_path, TargetText))                      # origin_file_path file에 있는 target text의 index
                                                                            # index는 target text의 시작 위치를 의미
