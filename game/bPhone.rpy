#Be sure to make all the three(3) entries for the images to work.

#avatars
image unknown_pf = "/images/aPhone/unknown.png"
image haru_pf = "/images/aPhone/haru_pf.png" #this is needed do not delete or remove the .png file
image akeyuki_pf = "/images/aPhone/akeyuki_pf.png"

#phone face
image phone0 = "images/aPhone/phone0.png"
image phone1 = "images/aPhone/phone1.png"

#pointers
image send_pointer = "images/aPhone/pointer-tip-send.png"
image receive_pointer = "images/aPhone/pointer-tip-receive.png"

#message bubble
image bubble_send = "images/aPhone/bubble-send.png"
image bubble_receive = "images/aPhone/bubble-receive.png"

#define main image for full screen image
image img0 = ("images/phone images/phone image 0.png")
image img1 = ("images/phone images/phone image 1.png")
image img2 = ("images/phone images/phone image 0.png") #BadMustard being lazy
#add more here as needed increasing the numbers

#define small image to be shown on phone screen
image thumb0 = ("images/phone images/thumbs/phone image 0.png")
image thumb1 = ("images/phone images/thumbs/phone image 1.png")
image thumb2 = ("images/phone images/thumbs/phone image 0.png") #BadMustard being lazy
#add more here as needed increasing the numbers

#put everything in a python list
init python:
    closeup_page = 0
    class phoneItem:
        def __init__(self, images, thumb):
            self.images = images
            self.thumb = thumb

    phone_images = []
    phone_images.append (phoneItem(["img0"], "thumb0"))
    phone_images.append (phoneItem(["img1"], "thumb1"))
    phone_images.append (phoneItem(["img2"], "thumb2"))
    #add more here as needed increasing the numbers
