import cv2
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QSlider
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage

class MainWindow(QMainWindow):
    def __init__(self, equipment, test_folder_path, folder_name, settings):
        super().__init__()

        # Initialize camera
        self.cam = cv2.VideoCapture(int(settings['camera']))
        self.cam.set(cv2.CAP_PROP_AUTOFOCUS, 1)

        # Initialize window dimensions and resize factor
        self.width = int(settings['width'])
        self.height = int(settings['height'])
        self.resize_factor = int(settings['resize_factor'])

        # Initialize capture button and slider
        self.capture_button = QPushButton('Capture', self)
        self.capture_button.setGeometry(50, 50, 100, 50)
        self.capture_button.clicked.connect(self.capture_image)

        self.zoom_slider = QSlider(Qt.Horizontal, self)
        self.zoom_slider.setGeometry(50, 110, 100, 30)
        self.zoom_slider.setRange(1, 10)
        self.zoom_slider.setValue(self.resize_factor)
        self.zoom_slider.valueChanged.connect(self.set_resize_factor)

        self.brightness_slider = QSlider(Qt.Horizontal, self)
        self.brightness_slider.setGeometry(50, 150, 100, 30)
        self.brightness_slider.setRange(-255, 255)
        self.brightness_slider.setValue(0)
        self.brightness_slider.valueChanged.connect(self.set_brightness)

        self.contrast_slider = QSlider(Qt.Horizontal, self)
        self.contrast_slider.setGeometry(50, 190, 100, 30)
        self.contrast_slider.setRange(-127, 127)
        self.contrast_slider.setValue(0)
        self.contrast_slider.valueChanged.connect(self.set_contrast)

        # Initialize labels for displaying images and text
        self.image_label = QLabel(self)
        self.image_label.setGeometry(200, 50, self.width, self.height)

        self.equipment_label_1 = QLabel(self)
        self.equipment_label_1.setGeometry(200, 10, 200, 30)
        self.equipment_label_1.setText(f"{equipment[0]}")

        self.equipment_label_2 = QLabel(self)
        self.equipment_label_2.setGeometry(200, 30, 200, 30)
        self.equipment_label_2.setText(f"{equipment[1]}")

        # Initialize image counter
        self.img_counter = 0


def capture_image(self):
    ret, frame = self.cam.read()
    if not ret:
        print("failed to grab frame")
        return

    # Resize frame based on the zoom slider value
    resize_factor = self.resize_factor
    width = int(self.width / resize_factor)
    height = int(self.height / resize_factor)
    dim = (width, height)
    frame = cv2.resize(frame, dim, interpolation=cv2.INTER_CUBIC)

    # Apply brightness and contrast adjustments based on the slider values
    brightness = self.brightness_slider.value()
    contrast = self.contrast_slider.value()
    frame = cv2.addWeighted(frame, 1 + contrast/127, frame, 0, brightness)

    # Display captured image
    self.display_image(frame)

    # Save image to file
    img_name = f"{self.equipment[0]}_{self.equipment[1]}_{self.img_counter}.png"
    img_path = f"{self.test_folder_path}/{self.folder_name}/InternalTestResults/Pictures/{img_name}"
    cv2.imwrite(img_path, frame)
    print("{} written!".format(img_name))
    self.img_counter += 1
