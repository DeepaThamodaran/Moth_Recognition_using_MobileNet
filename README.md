# Moth_Recognition_using_MobileNet
This repository walks-through how to identify moth species at Real-time using Tensorflow - MobileNet model. It shows how to take our own images organize into folders by category, and use them to quickly retrain the top layer of the 
MobileNet neural network to recognize those image categories. The training process outputs the retrained graph as retrained_graph.pb, which can be used to validate the model. This deep learning classifier can be used to train any object of our interest.

# Operational Procedure in Terminal window
  
Step-1 Create Virtual Environment using Anaconda3:

> conda create -n MothReg_Desktop_MobileNet pip python=2.7

> source activate MothReg_Desktop_MobileNet

Step-2 Install TensorFlow:

> pip install --ignore-installed --upgrade \
https://storage.googleapis.com/tensorflow/mac/cpu/tensorflow-1.7.0-py2-none-any.whl

Step-3 Move to code repository:

> cd Moth_Recognition_using_MobileNet

Step-4 Train the neural network:

Parameters:

> IMAGE_SIZE=224

> ARCHITECTURE="mobilenet_0.50_${IMAGE_SIZE}"

To Run tensorboard at background:

> tensorboard --logdir tf_files/training_summaries &

To understand all supported arguments:

> python -m scripts.retrain –h

To Train:

> python -m scripts.retrain \
--bottleneck_dir=tf_files/bottlenecks \
--how_many_training_steps=500 \
--model_dir=tf_files/models/ \
--summaries_dir=tf_files/training_summaries/"${ARCHITECTURE}" \
--output_graph=tf_files/retrained_graph.pb \
--output_labels=tf_files/retrained_labels.txt \
--architecture="${ARCHITECTURE}" \
--image_dir=tf_files/moth_photos

Step-5 Validate the network:

> python -m scripts.label_image \
--graph=tf_files/retrained_graph.pb  \
--image=tf_files/moth_photos/lunamoth/luna_040.jpg

![alt text](https://github.com/DeepaThamodaran/Moth_Recognition_using_MobileNet/blob/master/MobileNet_Image_validation.png)

Step-6 Deactivate virtual environment:

> source deactivate

# Mobile App in iOS:

Step-1 Basic Requirements

- You’ll need an iOS device like iPhone or iPad.
- You’ll need to download and launch latest Xcode.
- To execute the code in iOS device, you’ll need to enroll in the Apple iOS developer program which is $99/year and register your iPhone/iPad under ‘Accounts’ tab.

Step-2 Virtual Environment Setup:

> virtualenv -p /usr/bin/python2.7 env

> source env/bin/activate

> pip install tensorflow

> pip install keras==1.2.2

> pip install coremltools

Step-3 Clone necessary repositories:

Create a folder as iOS under main folder and clone below repositories inside

> git clone -b master https://github.com/tf-coreml/tf-coreml

  This will create a folder like Moth_Recognition_using_MobileNet/iOS/tf-coreml/

> git clone -b master https://github.com/hollance/MobileNet-CoreML

  This will create a folder like Moth_Recognition_using_MobileNet/iOS/MobileNet-CoreML

Step-4 CoreML model conversion

- create a folder named "demo" under Moth_Recognition_using_MobileNet/iOS/tf-coreml/
- Copy the generated retrained_labels.txt and retrained_graph.pb from /tf_files folder to /iOS/tf-coreml/demo/ folder
- Move the Moth_Recognition_using_MobileNet/demo_MobileNet.py file to Moth_Recognition_using_MobileNet/iOS/tf-coreml/ folder
- Execute below command:

> cd Moth_Recognition_using_MobileNet/iOS/tf-coreml/tf-coreml

> python demo_MobileNet.py

- Copy the newly generated MobileNet.mlmodel from /iOS/tf-coreml/demo/ to /iOS/MobileNet-CoreML 

Step-5 Open MobileNetCamera.xcodeproj in Xcode

Step-6 Build the Project:

Run and compile the code using iPhone/iPad device. You will receive the message of ‘Build Successful’ and app will get launched in iPhone/iPad accessing your device camera.

Step-7 Validation:

Point the iPhone/iPad camera to any trained moth picture/image, you will see the moth labels and its confidence level of close resemblance.

![alt text](https://github.com/DeepaThamodaran/Moth_Recognition_using_MobileNet/blob/master/MobileNet_Image_validation.png)


Step-8 Cleanup:

Close the app and disconnect the device from Xcode.

# Disclaimer:

This project uses code from:

https://github.com/thtrieu/darkflow: for the real-time object detections and classifications.

https://github.com/tf-coreml/tf-coreml: for tensorFlow to CoreML convertion

https://github.com/hollance/MobileNet-CoreML: for iOS implementation of MobileNet using CoreML

Please follow the links to get an understanding of all the features of each project.

# Citation:

Yolov2 :

  @article{redmon2016yolo9000,
  title={YOLO9000: Better, Faster, Stronger},
  author={Redmon, Joseph and Farhadi, Ali},
  journal={arXiv preprint arXiv:1612.08242},
  year={2016}
  }
