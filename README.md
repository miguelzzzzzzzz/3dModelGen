

# 3D Model Generator

This repository contains a Python script that allows you to adjust and generate a 3D model using the SMPL (Skinned Multi-Person Linear) model. The script uses Pyrender for visualization and Tkinter for creating a simple GUI for adjusting the model's parameters.

## Prerequisites

- Python 3.x
- PyTorch
- SMPL model files (download from [here](https://download.is.tue.mpg.de/download.php?domain=smpl&sfile=SMPL_python_v.1.1.0.zip))
- Pyrender
- Trimesh
- Tkinter

## Installation

1. Clone this repository:

```bash
https://github.com/miguelzzzzzzzz/3dModelGen.git
```

2. Install the required Python packages:

```bash
pip install -r requirements.txt
```

3. Download the SMPL model files and extract them. Update the `model_path` variable in the script with the path to the `.pkl` file of the desired model.
https://download.is.tue.mpg.de/download.php?domain=smpl&sfile=SMPL_python_v.1.1.0.zip
## Usage

Run the script:

```bash
python main.py
```

The script will open a GUI window. You can adjust the shape and orientation of the 3D model using the input fields provided. Click the "Update and Print Model Position" button to see the changes in the visualization.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [SMPL](https://smpl.is.tue.mpg.de/) model by Loper et al.
- [Pyrender](https://github.com/mmatl/pyrender) for 3D visualization.
- [Trimesh](https://github.com/mikedh/trimesh) for mesh processing.
- [Tkinter](https://docs.python.org/3/library/tkinter.html) for creating the GUI.
