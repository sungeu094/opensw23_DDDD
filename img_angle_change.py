import os
import cv2

def tilt_image(image_path, output_path, tilt_angle):
    # 이미지 로드
    image = cv2.imread(image_path)

    # 이미지의 중심 좌표 계산
    height, width = image.shape[:2]
    center_x = width // 2
    center_y = height // 2

    # 이미지를 앞으로 기울이는 변환 행렬 생성
    tilt_matrix = cv2.getRotationMatrix2D((center_x, center_y), tilt_angle, 1.0)

    # 이미지 변환
    tilted_image = cv2.warpAffine(image, tilt_matrix, (width, height), flags=cv2.INTER_LINEAR)

    # 기울어진 이미지 저장
    cv2.imwrite(output_path, tilted_image)

def tilt_images_in_folder(folder_path, output_folder, tilt_angle):
    # 폴더 내의 이미지 파일 목록 얻기
    image_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    for image_file in image_files:
        # 이미지 파일 경로 및 출력 경로 설정
        image_path = os.path.join(folder_path, image_file)
        output_path = os.path.join(output_folder, image_file)

        # 이미지 기울이기
        tilt_image(image_path, output_path, tilt_angle)

# 이미지가 저장된 폴더 경로 설정
input_folder = "train_data_2(recommand)/glasses"

# 기울이기 각도 설정 (양수: 앞으로 기울임, 음수: 뒤로 기울임)
tilt_angle = -30

# 출력 폴더 생성
output_folder = "train_data_2(recommand)/angle_changeglass"
os.makedirs(output_folder, exist_ok=True)

# 폴더 내의 이미지 기울이기
tilt_images_in_folder(input_folder, output_folder, tilt_angle)
