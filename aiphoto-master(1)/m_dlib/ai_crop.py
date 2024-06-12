import m_dlib.face_marks as fmarks
from PIL import Image


def crop_photo(path, target, target_size):
    shape, d = fmarks.predictor_face(path)

    if d is None:
        print("No face detected.")
        return

    face_width = d.right() - d.left()
    face_height = d.bottom() - d.top()

    im = Image.open(path)  # 加载图像
    crop_width = min(face_width , face_height , target_size[0])  # 增加裁剪框的大小
    crop_height = min(face_width  , face_height , target_size[1])  # 增加裁剪框的高度
    
    crop_left = max(0, d.left() - face_width)  # 左
    crop_top = max(0, d.top() - face_height)  # 上
    crop_right = min(d.right() + face_width, im.size[0])  # 右
    crop_bottom = min(d.bottom() + face_height, im.size[1])  # 下
    # 计算增加的裁剪框边界
    expand_horizontal = min(face_width // 4, (im.size[0] - (crop_right - crop_left)) // 2)

# 调整裁剪框边界
    crop_left = max(0, d.left() - face_width +1.5* expand_horizontal)  # 左移裁剪框
    crop_right = min(d.right() + face_width - 1.5*expand_horizontal, im.size[0])  # 右移裁剪框


    # 裁剪图像
    im = im.crop((crop_left, crop_top, crop_right, crop_bottom))
    im.save(target)  # 保存裁剪后的图像
