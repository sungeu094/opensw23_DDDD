import os
import cv2
import numpy as np

def tilt_image(image_path, output_path, tilt_factor):
    # 이미지 로드
    image = cv2.imread(image_path)

    # 이미지의 크기 및 중심 좌표 계산
    height, width = image.shape[:2]
    center_x = width // 2
    center_y = height // 2

    # 원근 변환을 위한 원본 점과 목표 점 좌표 설정
    original_points = np.float32([[0, 0], [width, 0], [width, height], [0, height]])
    target_points = np.float32([[center_x - tilt_factor * width, center_y], [center_x + tilt_factor * width, center_y], [width, height], [0, height]])

    # 원근 변환 행렬 계산
    perspective_matrix = cv2.getPerspectiveTransform(original_points, target_points)

    # 이미지 원근 변환
    tilted_image = cv2.warpPerspective(image, perspective_matrix, (width, height))

    # 기울어진 이미지 저장
    cv2.imwrite(output_path, tilted_image)

def tilt_images_in_folder(folder_path, output_folder, tilt_factor):
    # 폴더 내의 이미지 파일 목록 얻기
    image_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    for image_file in image_files:
        # 이미지 파일 경로 및 출력 경로 설정
        image_path = os.path.join(folder_path, image_file)
        output_path = os.path.join(output_folder, image_file)

        # 이미지 기울이기
        tilt_image(image_path, output_path, tilt_factor)

# 이미지가 저장된 폴더 경로 설정
input_folder = "train_data_2(recommand)/glasses"

# 기울이기 정도 설정 (양수: 앞으로 기울임, 음수: 뒤로 기울임)
tilt_factor = 0.7

# 출력 폴더 생성
output_folder = "train_data_2(recommand)/tilted_glasses"
os.makedirs(output_folder, exist_ok=True)

# 폴더 내의 이미지 기울이기
tilt_images_in_folder(input_folder, output_folder, tilt_factor)
