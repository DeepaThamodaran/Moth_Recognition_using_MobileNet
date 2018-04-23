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
