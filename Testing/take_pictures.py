import cv2

def take_pictures(equipment, folder_name):
    print("loading...")
    #cam = cv2.VideoCapture(1) #for dell laptop + nokia ivcam
    cam = cv2.VideoCapture(0)
    #focus = 255
    #cam.set(28, focus)
    cam.set(cv2.CAP_PROP_AUTOFOCUS, 1)
    
   #codec = 0x47504A4D  # MJPG
    #cam.set(cv2.CAP_PROP_FPS, 30.0)
    #cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc('m','j','p','g'))
    #cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc('M','J','P','G'))
    #cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1920*2)
    #cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080*2)

    #cam.set(3, 1920)
    #cam.set(4, 900)

    img_counter = 0
    while True:
        ret, frame = cam.read()
        # describe the type of font
        # to be used.
        font = cv2.FONT_HERSHEY_SIMPLEX
  
        # Use putText() method for
        # inserting text on video
        cv2.putText(frame, 
                f"{equipment[0]}", 
                (50, 50), 
                font, 1, 
                (0, 255, 255), 
                1, 
                cv2.LINE_4)
        cv2.putText(frame, 
                f"{equipment[1]}", 
                (50, 100), 
                font, 1, 
                (0, 255, 255), 
                1, 
                cv2.LINE_4)

        # Works for surface
        width = 1500
        height = 843
        dim = (width, height)
        frame = cv2.resize(frame, dim, interpolation=cv2.INTER_CUBIC)
        
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow(f"Take Pictures for {equipment[0]}_{equipment[1]}", frame)

        k = cv2.waitKey(1)
        if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
        elif k%256 == 32:
            # SPACE pressed
            img_name = f"{equipment[0]}_{equipment[1]}_{img_counter}.png"
            cv2.imwrite(f"{folder_name}/InternalTestResults/Pictures/{img_name}", frame)
            print("{} written!".format(img_name))
            img_counter += 1

    cam.release()

    cv2.destroyAllWindows()