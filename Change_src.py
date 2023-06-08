import os

def rename_images(folder_path):
    files = os.listdir(folder_path)
    num_files = len(files)
    for i, filename in enumerate(files):
        # 이미지 파일인지 확인
        if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
            # 숫자로 변경된 파일명 생성
            new_filename = 'glasses_'+str(i) +'.jpg'  # 확장자는 이미지 파일에 맞게 변경하세요
            # 파일 이동 및 이름 변경
            os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
            print(f'Renamed {filename} to {new_filename}')
    print('Renaming complete.')

# 이미지 파일들의 이름을 변경할 폴더 경로 설정
folder_path = r'C:\Users\User\myenv3\glasses-detector\train_data_2(recommand)\glasses'
rename_images(folder_path)
