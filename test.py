import cv2 as cv
import numpy as np
import random
import matplotlib.pyplot as plt




flag = True
print("1. Calculate the value of the constant c \n" +
      "2.Display the images\n" +
      "3.Display histograms\n"+
      "4.Save both images")

# i Read the input image in gray-scale
input_image = cv.imread('IMG1.jpeg', cv.IMREAD_GRAYSCALE)

    
# 2. Generate a random value for gamma using my  university ID as a seed
#Modify the brightness of the input image
university_id = '11924302' 
seed = sum(ord(char) for char in university_id)
random.seed(seed)
gamma = random.uniform(0.04, 25.0)
c = 255 / (255 ** gamma)

#  i Modify the brightness of the image using the equation s = c * r^gamma
output_image = np.uint8(c * np.power(input_image.astype(float), gamma))

while flag:
    choice = int(input())
    if choice == 1:
     
      print("The value of the constant c is:", c)
    elif choice == 2:
       #print output 2 imge (before and after modification)
       combined_image = cv.hconcat([input_image, output_image])
       cv.imshow('Before and After', combined_image)
       cv.waitKey(0)
       cv.destroyAllWindows()   
    elif choice == 3:
       # histogram before and after modification 
       plt.figure(figsize=(10, 5))
       plt.subplot(1, 2, 1)
       plt.hist(input_image.ravel(),255,[0,255],color='black')
       plt.title('Before')
       plt.xlabel('Gray Level')
       plt.ylabel('Pixel Count')

       plt.subplot(1, 2, 2)
       plt.hist(output_image.ravel(),255,[0,255],color='red')
       plt.title('After')
       plt.xlabel('Gray Level')
       plt.ylabel('Pixel Count')

       plt.show()
    elif choice == 4:
        cv.imwrite(f'before_{university_id}.jpg', input_image)
        cv.imwrite(f'after_{university_id}.jpg', output_image)

  
