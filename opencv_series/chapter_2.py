# edge detection
import cv2


def show_image(image, name="image"):
    cv2.imshow(name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def canny_det(image_path):
    img = cv2.imread(image_path)
    canny_img = cv2.Canny(img, 100, 200)
    return canny_img

def sobel_det(image_path):
    img = cv2.imread(image_path)

    yuan_x_64 = cv2.Sobel(img, cv2.CV_64F, dx=1, dy=0)
    # 这一步将默认的uint8数据类型更改为float64，以便能够保存负数的边缘强度

    # 将Sobel水平边缘检测结果的负数值转换为正数
    yuan_x_full = cv2.convertScaleAbs(yuan_x_64)
    # 这一步将负数值转换为其绝对值，以便在显示时产生正确的视觉效果

    # 使用Sobel算子进行垂直边缘检测
    yuan_y_64 = cv2.Sobel(img, cv2.CV_64F, dx=0, dy=1)
    # 这一步将默认的uint8数据类型更改为float64，以便能够保存负数的边缘强度

    # 将Sobel垂直边缘检测结果的负数值转换为正数
    yuan_y_full = cv2.convertScaleAbs(yuan_y_64)
    # 这一步将负数值转换为其绝对值，以便在显示时产生正确的视觉效果

    # 使用addWeighted函数将水平和垂直边缘检测结果叠加，创建合并的边缘检测图像

    img_xy_full = cv2.addWeighted(yuan_x_full, 1, yuan_y_full, 1, 0)

    return img_xy_full


if __name__ == "__main__":
    path = "../images/dog.jpeg"
    canny_img = canny_det(path)
    print("image size:", canny_img.shape)
    show_image(canny_img)

