import cv2
import os

def rotate_images(folder_path, angle):
    files = os.listdir(folder_path)
    for filename in files:
        if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
            img_path = os.path.join(folder_path, filename)
            img = cv2.imread(img_path)
            height, width = img.shape[:2]
            center = (width // 2, height // 2)
            matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
            rotated_img = cv2.warpAffine(img, matrix, (width, height))
            rotated_filename = filename
            rotated_img_path = os.path.join(folder_path, rotated_filename)
            cv2.imwrite(rotated_img_path, rotated_img)
            print(f"Rotated {filename} and saved as {rotated_filename}")

# 이미지 파일들을 회전시킬 폴더 경로와 회전각(angle) 설정
folder_path = r'C:\Users\User\myenv3\COVID-19-Face-mask-detector\train_data_3(glass)\glasses_dataset'
angle = -25  # 회전각을 원하는 각도로 설정

rotate_images(folder_path, angle)
