# Installing TensorFlow on Manjaro Linux with RTX 3070
To leverage the full power of your RTX 3070 GPU with TensorFlow, you need to ensure that your system is properly set up with NVIDIA drivers, CUDA, and cuDNN. Follow these steps to prepare your Manjaro Linux system and install TensorFlow.
```
my pc ➜  same_tree pip --version 
pip 24.0 from /usr/lib/python3.11/site-packages/pip (python 3.11)
➜  same_tree neofetch  
██████████████████  ████████   yibo@yibo-blade14rz090370 
██████████████████  ████████   ------------------------- 
██████████████████  ████████   OS: Manjaro Linux x86_64 
██████████████████  ████████   Host: Blade 14 - RZ09-0370 1.04 
████████            ████████   Kernel: 6.6.19-1-MANJARO 
████████  ████████  ████████   Uptime: 2 hours, 2 mins 
████████  ████████  ████████   Packages: 1248 (pacman) 
████████  ████████  ████████   Shell: zsh 5.9 
████████  ████████  ████████   Resolution: 2560x1440 
████████  ████████  ████████   DE: GNOME 45.4 
████████  ████████  ████████   WM: Mutter 
████████  ████████  ████████   WM Theme: Space-master 
████████  ████████  ████████   Theme: Space-master [GTK2/3] 
████████  ████████  ████████   Icons: Bibata-Original-Amber [GTK2/3] 
                               Terminal: gnome-terminal 
                               CPU: AMD Ryzen 9 5900HX with Radeon Graphics (16 
                               GPU: NVIDIA GeForce RTX 3070 Mobile / Max-Q 
                               GPU: AMD ATI Radeon Vega Series / Radeon Vega Mo 
                               Memory: 8813MiB / 15392MiB 
```
## 1. Update Your System
First, ensure your system is up-to-date:
```shell
sudo pacman -Syu
```

## 2. Install NVIDIA Drivers
Manjaro provides a convenient way to install NVIDIA drivers:
```shell

sudo mhwd -a pci nonfree 0300
```
This command automatically installs the best driver for your system.

## 3. Install CUDA and cuDNN
Install CUDA and cuDNN from the Manjaro repositories:
```shell

sudo pacman -S cuda cudnn
```
## 4. Set Up Environment Variables

```

export PATH=/opt/cuda/bin:$PATH
export LD_LIBRARY_PATH=/opt/cuda/lib64:$LD_LIBRARY_PATH

```
Add these lines to your .zshrc or .bashrc file and apply the changes:

## 5. Install TensorFlow
```

pip install tensorflow
```

