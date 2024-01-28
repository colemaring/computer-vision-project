import os
from ultralytics import YOLO

def main():
    # Print the current working directory
    print(f'Current working directory: {os.getcwd()}')

    # If necessary, change the working directory to the directory of the script
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    model = YOLO('yolov8n.pt')  
    model.train(data='config.yaml', epochs = 400, imgsz=640)

if __name__ == '__main__':
    main()