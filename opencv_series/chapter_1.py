# read image
import cv2


def show_image(image, name="image"):
    cv2.imshow(name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    path = "../images/dog.jpeg"
    img = cv2.imread(path)
    print("image size:", img.shape)
    show_image(img)
