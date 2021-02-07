# headerfile
import linecache
import os
import shutil

def movefile(origin_folder_path, new_folder_path):
    if not (os.path.isfile(origin_folder_path+'origin.c')):                                    # origin 폴더에 origin.c가 없으면
        print("Error : ther is no origin.c in", origin_folder_path)
    else:                                                                   # origin 폴더에 origin.c 가 있으면
        src = origin_folder_path + 'origin.c'                               # origin.c 위치
        dst = new_folder_path + 'New.c'                                     # New.c 위치
        shutil.copy(src, dst)                                               # src 를 dst로 복사
        os.chdir(new_folder_path)                                           # dst 로 이동
        if (os.path.isfile(dst)):                                           
            print("File already exist\nDo you want remove exist file?")
            while 1:
                answer = input("Enter yes(y) or no(n)")
                if (answer.lower() in ["yes", "y"]):                        # lower()는 모두 소문자로 취급하겠다는 거
                    os.remove(new_folder_path + "New.c")                    # 기존에 있던 New.c 삭제
                    os.rename('origin.c', 'New.c')                          # origin.c를 New.c로 이름 변경  (origin_file_folder에 new.c가 있으면 실행)
                    print("Exist file removed and Job Done!")
                    os.remove(new_folder_path + "origin.c")
                    break
                elif (answer.lower() in ["no", "n"]):
                    print("Error : File already exist")
                    break
                else:
                    print("Error : Please enter yes or no")
        else:
            shutil.copy(src, dst)                                               # src 를 dst로 복사
            os.chdir(new_folder_path)                                           # dst 로 이동
            os.rename('origin.c', 'New.c')                                      # origin.c를 New.c로 이름 변경  (origin_file_folder에 new.c가 있으면 실행)
            # os.chdir(very_top_dir + "/new_file_folder")                         # new_file_folder에 작업 끝났다는 확인용 txt 만들기
            # f = open('파일 옮기기 완료!.txt', 'w')
            # f.write("Done!")
            # f.close

def fileopen(fname, target):
    with open(fname,'r',encoding='UTF8') as file:
        text = file.read()
        if target in text   :
            flag = True
            splitdata = text.split()
        else :
            flag = False
            splitdata = None
    return flag, splitdata

def filefind(fname, target):
    with open(fname,'r',encoding='UTF8') as file:
        text = file.read()                                          # list로 내용 받기
        tempindex = -1                                              # find의 반환값이 -1이면 못찾은거
        index = []
        while 1:
            tempindex = text.find(target, tempindex + 1)            # list에서 target 찾기
            if tempindex == -1:
                break
            else:
                index.append(tempindex)
        # print(text)
        # print(index)
    return index

''' Todo '''
def changecontents(바꿀 파일 path , targetindex, 바꿀내용)