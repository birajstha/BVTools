from cv2 import VideoCapture, CAP_PROP_AUTOFOCUS,FONT_HERSHEY_SIMPLEX, \
    putText, resize, imshow, imwrite, waitKey, destroyAllWindows, \
    LINE_4, INTER_CUBIC, CAP_PROP_FRAME_HEIGHT, CAP_PROP_FRAME_WIDTH, CAP_V4L2

def take_pictures(equipment,test_folder_path, folder_name, settings):
    print("loading...")
    #cam = cv2.VideoCapture(1) #for dell laptop + nokia ivcam
    cam = VideoCapture(int(settings['camera']))

    #cam.set(CAP_PROP_AUTOFOCUS, 1)
    

    #cam.set(3, 1920)
    #cam.set(4, 1080)

    img_counter = 0
    while True:
        ret, frame = cam.read()

        font = FONT_HERSHEY_SIMPLEX

        putText(frame, 
                f"{equipment[0]}", 
                (50, 50), 
                font, 1, 
                (0, 255, 255), 
                1, 
                LINE_4)
        putText(frame, 
                f"{equipment[1]}", 
                (50, 100), 
                font, 1, 
                (0, 255, 255), 
                1, 
                LINE_4)
        
        if not ret:
            print("failed to grab frame")
            break
        
        imshow(f"Take Pictures for {equipment[0]}_{equipment[1]}", frame)

        k = waitKey(1)
        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif (k%256 == 32 or k%256 == 174):
            # SPACE pressed
            img_name = f"{equipment[0]}_{equipment[1]}_{img_counter}.png"
            imwrite(f"{test_folder_path}/{folder_name}/InternalTestResults/Pictures/{img_name}", frame)
            print("{} written!".format(img_name))
            img_counter += 1

    cam.release()

    destroyAllWindows()

    

"""

    from cv2 import * 

def take_pictures(equipment,test_folder_path, folder_name, settings):
    print("loading...")
    cam = VideoCapture(int(settings['camera']))
    cam.set(CAP_PROP_AUTOFOCUS, 1)
    cam.get()
    
    # Get the camera's maximum resolution
    width = int(cam.get(CAP_PROP_FRAME_WIDTH))
    height = int(cam.get(CAP_PROP_FRAME_HEIGHT))
    aspect_ratio = width/height
    print (width, height)
    
    # Set the camera's resolution to its maximum
    cam.set(CAP_PROP_FRAME_WIDTH, width)
    cam.set(CAP_PROP_FRAME_HEIGHT, height)

    img_counter = 0
    while True:
        ret, frame = cam.read()
        font = FONT_HERSHEY_SIMPLEX
        putText(frame, 
                f"{equipment[0]}", 
                (50, 50), 
                font, 1, 
                (0, 255, 255), 
                1, 
                LINE_4)
        putText(frame, 
                f"{equipment[1]}", 
                (50, 100), 
                font, 1, 
                (0, 255, 255), 
                1, 
                LINE_4)

        # Resize the frame for display purposes
        #display_width = int(settings['width'])
        #display_height = int(settings['height'])
        #dim = (display_width, display_height)
        #frame = resize(frame, dim, interpolation=INTER_CUBIC)
        
        if not ret:
            print("failed to grab frame")
            break
        imshow(f"Take Pictures for {equipment[0]}_{equipment[1]}", frame)

        k = waitKey(1)
        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif (k%256 == 32 or k%256 == 174):
            # SPACE pressed
            img_name = f"{equipment[0]}_{equipment[1]}_{img_counter}.png"
            imwrite(f"{test_folder_path}/{folder_name}/InternalTestResults/Pictures/{img_name}", frame)
            print("{} written!".format(img_name))
            img_counter += 1

    cam.release()

    destroyAllWindows()
    """