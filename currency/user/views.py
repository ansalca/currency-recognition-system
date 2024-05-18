import cv2
import numpy as np
from django.shortcuts import render
from keras.preprocessing import image
from keras.models import load_model
from collections import Counter

app_name = 'user'

# Create your views here.
def home(request):
    return render(request,'base.html')

def find_repeating(arr):
    counts = Counter(arr)
    most_repeating = max(counts, key=counts.get)
    return most_repeating


def predict(request):
    np.set_printoptions(suppress=True)
    model = load_model("currency_classifier.h5", compile=False)
    class_names = open("labels.txt", "r").readlines()
    camera = cv2.VideoCapture(0)
    predictions = []

    for a in range(0, 25):
        ret, img = camera.read()
        img = cv2.resize(img, (224, 224), interpolation=cv2.INTER_AREA)
        if ret:
            file = 'media\images\img' + str(a) + '.jpg'
            cv2.imwrite(file, img)
            img1 = img
            cv2.resize(img, dsize=(224, 224), interpolation=cv2.INTER_LINEAR)
            print("Image" + str(a) + " saved")
        cv2.imshow("Webcam Image", img)
        img = np.asarray(img, dtype=np.float32).reshape(1, 224, 224, 3)
        img = (img / 127.5) - 1
        prediction = model.predict(img)
        index = np.argmax(prediction)
        class_name = class_names[index]
        confidence_score = prediction[0][index]
        print("Class:", class_name[2:], end="")
        print("Confidence Score:", str(np.round(confidence_score * 100))[:-2], "%")
        predictions.append(index)
        keyboard_input = cv2.waitKey(1)
        if keyboard_input == 27:
            break

    camera.release()
    cv2.destroyAllWindows()

    print(predictions)
    a = find_repeating(predictions)
    print(a)

    if a == 0:
        k = '1Hundrednote'
        print("1Hundrednote")
    elif (a == 1):
        k = '2Hundrednote'
        print("2Hundrednote")
    elif (a == 2):
        k = '2Thousandnote'
        print("2Thousandnote")
    elif (a == 3):
        k = '5Hundrednote'
        print("5Hundrednote")
    elif (a == 4):
        k = 'Fiftynote'
        print("Fiftynote")
    elif (a == 5):
        k = 'Tennote'
        print("Tennote")
    elif (a == 6):
        k = 'Twentynote'
        print("Twentynote")
    else:
        k = 'no'
        print('background image')

    import pyttsx3
    text = ('You have', k, 'Note')

    def speak(text):
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
        engine.stop()

    speak(text)
    return render(request, 'base.html')



# def predict(request):
#     np.set_printoptions(suppress=True)
#     model = load_model("keras_model.h5", compile=False)
#     class_names = open("labels.txt", "r").readlines()
#     camera = cv2.VideoCapture(0)
#     predictions = []
#
#     for a in range(0, 25):
#         ret, img = camera.read()
#         img = cv2.resize(img, (224, 224), interpolation=cv2.INTER_AREA)
#         if ret:
#             file = 'media\images\img' + str(a) + '.jpg'
#             cv2.imwrite(file, img)
#             img1 = img
#             cv2.resize(img, dsize=(224, 224), interpolation=cv2.INTER_LINEAR)
#             print("Image" + str(a) + " saved")
#         cv2.imshow("Webcam Image", img)
#         img = np.asarray(img, dtype=np.float32).reshape(1, 224, 224, 3)
#         img = (img / 127.5) - 1
#         prediction = model.predict(img)
#         index = np.argmax(prediction)
#         class_name = class_names[index]
#         confidence_score = prediction[0][index]
#         print("Class:", class_name[2:], end="")
#         print("Confidence Score:", str(np.round(confidence_score * 100))[:-2], "%")
#         predictions.append(index)
#         keyboard_input = cv2.waitKey(1)
#         if keyboard_input == 27:
#             break
#
#     camera.release()
#     cv2.destroyAllWindows()
#
#     print(predictions)
#     a = find_repeating(predictions)
#     print(a)
#
#
#     if a == 1:
#         k = 'Tennote'
#         print("Tennote")
#     elif (a == 2):
#         k = 'Twentynote'
#         print("Twentynote")
#     elif (a == 3):
#         k = 'Fiftynote'
#         print("Fiftynote")
#     elif (a == 4):
#         k = '1Hundrednote'
#         print("1Hundrednote")
#     elif (a == 5):
#         k = '2Hundrednote'
#         print("2Hundrednote")
#     elif (a == 6):
#         k = '5Hundrednote'
#         print("5Hundrednote")
#     else:
#         k = 'no'
#         print('background image')
#
#     import pyttsx3
#     text = ('You have', k, 'Note')
#
#     def speak(text):
#         engine = pyttsx3.init()
#         engine.say(text)
#         engine.runAndWait()
#         engine.stop()
#
#     speak(text)
#     return render(request, 'base.html')



# def predict(request):
#     np.set_printoptions(suppress=True)
#     model = load_model("model_Classifier.h5", compile=False)
#     class_names = open("labels.txt", "r").readlines()
#     camera = cv2.VideoCapture(0)
#     predictions = []
#
#     for a in range(0, 25):
#         ret, img = camera.read()
#         img = cv2.resize(img, (224, 224), interpolation=cv2.INTER_AREA)
#         if ret:
#             file = 'media\images\img' + str(a) + '.jpg'
#             cv2.imwrite(file, img)
#             img1 = img
#             cv2.resize(img, dsize=(224, 224), interpolation=cv2.INTER_LINEAR)
#             print("Image" + str(a) + " saved")
#         cv2.imshow("Webcam Image", img)
#         img = np.asarray(img, dtype=np.float32).reshape(1, 224, 224, 3)
#         img = (img / 127.5) - 1
#         prediction = model.predict(img)
#         index = np.argmax(prediction)
#         class_name = class_names[index]
#         confidence_score = prediction[0][index]
#         print("Class:", class_name[2:], end="")
#         print("Confidence Score:", str(np.round(confidence_score * 100))[:-2], "%")
#         predictions.append(index)
#         keyboard_input = cv2.waitKey(1)
#         if keyboard_input == 27:
#             break
#
#     camera.release()
#     cv2.destroyAllWindows()
#
#     print(predictions)
#     a = find_repeating(predictions)
#     print(a)
#
#
#     if a == 1:
#         k = 'Fiftynote'
#         print("Fiftynote")
#     elif (a == 2):
#         k = '1Hundrednote'
#         print("1Hundrednote")
#     elif (a == 3):
#         k = 'Tennote'
#         print("Tennote")
#     elif (a == 4):
#         k = 'Twentynote'
#         print("Twentynote")
#     elif (a == 5):
#         k = '2Hundrednote'
#         print("2Hundrednote")
#     elif (a == 6):
#         k = '5Hundrednote'
#         print("5Hundrednote")
#     else:
#         k = 'no'
#         print('background image')
#
#     import pyttsx3
#     text = ('You have', k, 'Note')
#
#     def speak(text):
#         engine = pyttsx3.init()
#         engine.say(text)
#         engine.runAndWait()
#         engine.stop()
#
#     speak(text)
#     return render(request, 'base.html')
