import tfcoreml as tf_converter

tf_model_path = 'demo/retrained_graph.pb'
mlmodel_path = 'demo/MobileNet.mlmodel'

mlmodel = tf_converter.convert(
                               tf_model_path = tf_model_path,
                               mlmodel_path = mlmodel_path,
                               output_feature_names = ['final_training_ops/Wx_plus_b/add:0'],
                               input_name_shape_dict = {'input:0':[1,224,224,3]},
                               image_input_names = ['input:0'],
                               class_labels='demo/retrained_labels.txt',
                               red_bias = -1,
                               green_bias = -1,
                               blue_bias = -1,
                               image_scale = 2.0/255.0)
