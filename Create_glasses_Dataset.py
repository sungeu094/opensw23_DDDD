import dlib
import cv2
import numpy as np
from PIL import Image, ImageFile
import os

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

without_dir = os.path.join('train_data_2(recommand)/noglass_zoom/')
print('total training without glasses images:', len(os.listdir(without_dir)))
withoutimgnum = len(os.listdir(without_dir))
without_files = os.listdir(without_dir)


for k in range(300,500):
    count = k
    img = cv2.imread('train_data_2(recommand)/noglass_zoom/' + without_files[k], 1)

    rows, cols = img.shape[:2]
    rects = detector(img, 1)
    if len(rects) > 0:
        for i, rect in enumerate(rects):
            shape = predictor(img, rect)


            for j in range(68):
                x, y = shape.part(j).x, shape.part(j).y

                color = (0, 255, 0)
                if (j == 0):
                    color = (0, 0, 255)
                    left = np.array([x, y])
                elif (j == 28):
                    color = (0, 0, 255)
                    chin = np.array([x, y])
                elif (j == 15):
                    color = (0, 0, 255)
                    right = np.array([x, y])
                elif (j == 22):
                    color = (0, 0, 255)
                    nose = np.array([x, y])
                cv2.putText(img, str(j), (x, y), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 0.3, color)


        def get_distance_from_point_to_line(point, line_point1, line_point2):
            distance = np.abs((line_point2[1] - line_point1[1]) * point[0] +
                              (line_point1[0] - line_point2[0]) * point[1] +
                              (line_point2[0] - line_point1[0]) * line_point1[1] +
                              (line_point1[1] - line_point2[1]) * line_point1[0]) / \
                       np.sqrt((line_point2[1] - line_point1[1]) * (line_point2[1] - line_point1[1]) +
                               (line_point1[0] - line_point2[0]) * (line_point1[0] - line_point2[0]))
            return int(distance)


        img2 = Image.open('train_data_2(recommand)/noglass_zoom/' + without_files[k])
        glasses_img = Image.open('glasses/glass_down2.png')
        width = glasses_img.width
        height = glasses_img.height
        width_ratio = 1.2
        new_height = int(np.linalg.norm(left - right))

        # left
        glasses_left_img = glasses_img.crop((0, 0, width // 2, height))
        glasses_left_width = get_distance_from_point_to_line(left, nose, chin)
        glasses_left_width = int(glasses_left_width * width_ratio)
        glasses_left_img = glasses_left_img.resize((glasses_left_width, new_height))

        # right
        glasses_right_img = glasses_img.crop((width // 2, 0, width, height))
        glasses_right_width = get_distance_from_point_to_line(right, nose, chin)
        glasses_right_width = int(glasses_right_width * width_ratio)
        glasses_right_img = glasses_right_img.resize((glasses_right_width, new_height))

        # merge glasses
        size = (glasses_left_img.width + glasses_right_img.width, new_height)
        glasses_img = Image.new('RGBA', size)
        glasses_img.paste(glasses_left_img, (0, 0), glasses_left_img)
        glasses_img.paste(glasses_right_img, (glasses_left_img.width, 0), glasses_right_img)

        # rotate glasses
        angle = np.arctan2(chin[1] - nose[1], chin[0] - nose[0])
        rotated_glasses_img = glasses_img.rotate(angle, expand=True)

        # calculate glasses location
        center_x = (nose[0] + chin[0]) // 2
        center_y = (nose[1] + chin[1]) // 2

        offset = glasses_img.width // 2 - glasses_left_img.width
        radian = angle * np.pi / 180
        box_x = center_x + int(offset * np.cos(radian)) - rotated_glasses_img.width // 2
        box_y = center_y + int(offset * np.sin(radian)) - rotated_glasses_img.height // 2

        img2.paste(rotated_glasses_img, (box_x, box_y), rotated_glasses_img)

        file_name_path = 'train_data_2(recommand)/glasses/' + str(count) + '.jpg' # your own repository path
        
        img2.save(file_name_path)
        print(count)
    else:
        print("not detected")
