import cv2
import numpy as np

def clock_generation(max_len):

    random_sequence = ""
    true_sequence = []

    # takes a photo
    cap = cv2.VideoCapture(0)  # 1 - HD web 3000
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

    sequence_length = 0

    while sequence_length < max_len:

        ret, frame = cap.read()
        img = frame

        # convert to HSV
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv)

        # create mask for blue color
        # lower_blue = (85, 50, 160) #lower HSV value for blue color
        lower_blue = (85, 50, 100)  # lower HSV value for blue color
        upper_blue = (255, 200, 255)  # lower HSV value for blue color
        mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)

        # count non-zero (white) pixels in mask
        blue_count = np.count_nonzero(mask_blue)
        print('blue:', blue_count)

        # create mask for green color
        # lower HSV value for green color
        # lower_green = (40, 80, 100)
        lower_green = (50, 45, 100)
        upper_green = (80, 255, 255)  # upper HSV value for green color
        mask_green = cv2.inRange(hsv, lower_green, upper_green)

        # count non-zero (white) pixels in mask
        green_count = np.count_nonzero(mask_green)
        print('green:', green_count)

        n = sequence_length % 13

        # generate number depending on sequence length
        if n <= 5:
            num = min([blue_count, green_count])
            word = str(num)[1:]
        else:
            num = max([blue_count, green_count])
            word = str(num)[1:]

        if word == "":
            word = "0"

        while word[0] == "0" and len(word) > 1:
            word = word[1:]
            true_sequence.append(0)
            random_sequence += "0"
        word = int(word)

        binary = bin(word)[2:-1]
        sequence_length += len(binary)
        random_sequence += binary
        true_sequence.append(int(word))

        print(true_sequence)
        print(f"Bin sequence len: {sequence_length}")

        # show webcam real image and masks
        cv2.imshow('mask_blue', mask_blue)
        cv2.imshow('mask_green', mask_green)
        cv2.imshow('real_photo', frame)

        key = cv2.waitKey(1)
        if key == 27:
            break

        if sequence_length >= max_len or input("Continue? (blank if yes): "):
            break

    print("\nProgram end")

    # save sequence
    with open("sequence.txt", "w") as file:
        if sequence_length > max_len:
            random_sequence = random_sequence[:max_len]
        file.write(random_sequence)
        print("File writen successfully")

    print(f"Bin sequence: {random_sequence}")
    print(f"Len: {len(random_sequence)}")
    cap.release()  # turn of the web camera

    cv2.destroyAllWindows()
