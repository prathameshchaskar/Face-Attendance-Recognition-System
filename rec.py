import cv2
import numpy as np
from PIL import ImageGrab

# name = 'out' + '.mp4'
codec = cv2.VideoWriter_fourcc( 'X','V','I','D')
out = cv2.VideoWriter("rec.avi", codec, 8, (1900, 1000))
# out= cv2.VideoWriter('out.avi', cv2.VideoWriter_fourcc(*'MP42'),5, (800,600))

while True:
    img = ImageGrab.grab(bbox=(0,0,1900,1000))

    img_np = np.array(img)

    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)

     #write it to the output file
    out.write(frame)

    ##display the recording screen
    cv2.imshow("LIVE", frame)

    ##stop recording when we press 'q'
    if cv2.waitKey(1) == 27:
        break

#release the video writer
out.release()

#destroy all windows
cv2.destroyAllWindows()



