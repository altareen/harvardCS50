# The Experimentation Process

One of the first strategies I attempted was to add different quantities of 2D convolution layers to the sequential model. I started out with one convolution layer, then tried adding several of them, and viewing the results each time. Finally, I settled with 4 convolution layers, because it seemed to work well. I also implemented 2 maximum pooling layers. In the middle of my model, I added a hidden dense layer, followed by a dropout layer set at a rate of 0.5. Just before the dense output layer, I placed a global maximum pooling layer. At the dense output layer, I tried using a ReLU activation, but I found that a sigmoid activation produced better results.

I tried to place a flatten layer throughout the model, but for some reason, it just didn't work. Also, I tried adjusting the filter quantities of the layers, and found that an amount of 32 works well in general.
