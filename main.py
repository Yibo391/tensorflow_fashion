import tensorflow as tf



# List available GPUs
gpus = tf.config.list_physical_devices('GPU')
if gpus:
    for gpu in gpus:
        tf.config.experimental.set_memory_growth(gpu,True)


for gpu in gpus:
    print(gpu)

    
