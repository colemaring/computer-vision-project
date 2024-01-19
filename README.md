# Disclaimer
This is not intended for use in multiplayer games. This is purely an educational computer vision project.

# Model/Training
Player dataset is from [Roboflow](https://universe.roboflow.com/cb/cs2-vlya3/dataset/16). Trained using YOLOv8n with 400 epochs on a NVIDIA 3060ti GPU. (took about 2.5 hours)
![results](https://github.com/colemaring/symmetrical-guacamole/assets/65455664/4659e79e-87b6-4784-b7f1-41d36d8627fb)
Notice how the loss and performance metrics converge after about 300 epochs.

# Inference Performance
Frame inference latency depends on the size of the inference window. A 256x256 inference window will have a frame latency of around 7ms on a 3060ti. A CUDA-supported GPU is almost necessary for short inference times.

# Demonstration
https://github.com/colemaring/symmetrical-guacamole/assets/65455664/9cd3d39c-6d13-40df-8af6-640e2eabab7f

# Features
General:<br>
Custom in-game resolution<br>
Inference window size for player detection<br>
Bounding box confidence levels<br>
Show inference window checkbox<br>
Exit program hotkey<br>
<br>
Aim Assist:<br>
Field of View controls<br>
Y aim height offset<br>
Mouse sleep timer<br>
Mouse smoothing controls<br>
Mouse speed controls<br>
Mouse acceleration controls<br>
Aim assist hotkey<br>
<br>
Auto shoot:<br>
Triggerbot always enabled checkbox<br>
Triggerbot sensitivity controls<br>
Triggerbot click delay<br>
Triggerbot hotkey<br>



