from u_2_net import my_u2net_test
from to_background import to_background
from to_background import to_standard_trimap
from m_dlib import ai_crop

def deal(img_path, color, size1, size2, size3):
    org_img = img_path
    alpha_img = "img\meinv_alpha.png"
    alpha_resize_img = "img\meinv_alpha_resize.png"
    
    # 通过u_2_net 获取 alpha
    my_u2net_test.seg_trimap(org_img, alpha_img, alpha_resize_img)
    
    print("-----------------------------")
    
    # 通过alpha 获取 trimap
    trimap = "img\meinv_trimap_resize.png"
    to_standard_trimap.to_standard_trimap(alpha_resize_img, trimap)
    
    # 证件照添加蓝底纯色背景
    id_image = "img\meinv_id.png"
    to_background.to_background(org_img, trimap, id_image, color)
    
    # 将 size1 和 size2 组合成一个元组，作为目标图像的尺寸
    target_size = (size1, size2)
    
    # 调整参数传递方式，使其与 crop_photo 函数的定义相匹配
    ai_crop.crop_photo(id_image, "last.jpg", target_size)
