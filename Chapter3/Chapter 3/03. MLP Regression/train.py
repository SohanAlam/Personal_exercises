#import the needed libraries

import data_handler as dh           # yes, you can import your code. Cool!

# once you built your model, remember to import it!!!
# you can do it like this:
# from model import (class name)

x_train, x_test, y_train, y_test = dh.load_data("data/turkish_stocks.csv", 7)
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)

epochs = 1                          # remember to increare the epochs!

# define your optimizer and your criterion here

for epoch in range(epochs):
    
    loss_train = []                 # here you will append the train losses, it can be useful to plot them out
    loss_test = []                   # here you will append the test losses, it can be useful to plot them out


    # Define a loop so you can load the data in batches 

    x_train_batch, x_test_batch, y_train_batch, y_test_batch = dh.to_batches(x_train, x_test, y_train, y_test, 7)

    print(x_train_batch.shape, x_test_batch.shape, y_train_batch.shape, y_test_batch.shape)

    # Reset the gradients



    # Feed the model


    # Compute the loss


    # Backpropagation time


    # Update the weight

    # Remember to validate your model: with torch.no_grad() ...... model.eval .........model.train
