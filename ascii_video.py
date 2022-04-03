import cv2

#27 chars ordered by density
density = "Ñ@#W$9876543210?!abc;:+=-,_"
  
vid = cv2.VideoCapture(0)
  
while(True):

    #Dimensions
    dim = (170, 50)    
          
    ret, frame = vid.read()
    
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    grey = cv2.resize(grey, dim, interpolation =cv2.INTER_AREA)
    img = ""
    for i in range(grey.shape[0]): #height
        for j in range(grey.shape[1]):#width
            k = grey[i,j] #row, column
            char_pos = int(k // (255/ 26))
            char = density[-char_pos] #change sign of position to alter gray scale. (Nice details)
            img = img + char
        img = img + "\n"        
    cv2.imshow('', grey)
    print(img)
    if cv2.waitKey(1) & 0xFF == ord('q'): #Exit w/ "q" key (when camera window selected.)
        break

vid.release()

cv2.destroyAllWindows()
