# Feedforward Neural Network Model

>ML Learning Note-4
>The basis of feedforward neural network

## Overview

In this network, the information moves in only one direction, forward, from the input nodes, through the hidden nodes (if any) and to the output nodes.

![](https://upload.wikimedia.org/wikipedia/en/5/54/Feed_forward_neural_net.gif)

The submodel between each layers is a Generalized Linear Model. So we can also call feedforward neutral network as `Stacked Generalized Linear Model  `

## Single Layer Unit

```mermaid
graph LR
i["input"]-->|"x"|x1((x))
subgraph single layer
w1{ }-->|"W"|x1
-->|"z"|f1((f))
end
f1-->|"y"|o{output}
linkStyle 0,1,2,3 stroke:gray
```

