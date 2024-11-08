import torch
from smplx import SMPL
import trimesh
import pyrender
import numpy as np
import tkinter as tk

# Load the SMPL model
model_path = r"C:\Users\migzuu\Downloads\SMPL_python_v.1.1.0 (1)\SMPL_python_v.1.1.0\smpl\models\basicmodel_m_lbs_10_207_0_v1.1.0.pkl"
smpl = SMPL(model_path=model_path, gender='neutral')

# Initial values for the shape and pose parameters
betas = torch.zeros(1, 10)  # Start with neutral betas
body_pose = torch.zeros(1, 69)  # Neutral body pose
global_orient = torch.tensor([[0, 0, np.pi / 2]], dtype=torch.float32)  # Neutral global orientation

# Generate the initial 3D mesh from SMPL
output = smpl(betas=betas, body_pose=body_pose, global_orient=global_orient)
vertices = output.vertices.detach().cpu().numpy().squeeze()
faces = smpl.faces
joints = output.joints.detach().cpu().numpy().squeeze()

# Create a Trimesh object for visualization
mesh = trimesh.Trimesh(vertices, faces, process=False)

# Initialize Pyrender scene and viewer
scene = pyrender.Scene()
mesh_pyrender = pyrender.Mesh.from_trimesh(mesh)
node = scene.add(mesh_pyrender)
viewer = pyrender.Viewer(scene, use_raymond_lighting=True, run_in_thread=True)

# Create a simple GUI with tkinter for beta adjustments
root = tk.Tk()
root.title("Adjust Beta Parameters for 3D Model")

# Function to update the Pyrender scene and reflect beta changes
def update_model():
    global betas, smpl, scene, node

    try:
        # Update betas based on input fields
        for i in range(10):
            betas[0, i] = float(beta_entries[i].get())

        # Update global orientation based on input
        new_orient_x = float(orient_x.get())
        new_orient_y = float(orient_y.get())
        new_orient_z = float(orient_z.get())
        global_orient = torch.tensor([[new_orient_x, new_orient_y, new_orient_z]], dtype=torch.float32)

        # Print the current orientation and betas
        print(f"Current orientation (x, y, z): {new_orient_x}, {new_orient_y}, {new_orient_z}")
        print("Current beta values:", betas.numpy().squeeze())

        # Regenerate the 3D mesh from SMPL with the updated orientation and betas
        output = smpl(betas=betas, body_pose=body_pose, global_orient=global_orient)
        vertices = output.vertices.detach().cpu().numpy().squeeze()

        # Update mesh in the Pyrender scene
        new_mesh = trimesh.Trimesh(vertices, faces, process=False)
        new_mesh_pyrender = pyrender.Mesh.from_trimesh(new_mesh)

        # Use the Pyrender context to safely update the scene
        scene.remove_node(node)
        node = scene.add(new_mesh_pyrender)

    except ValueError as ve:
        print(f"Invalid input: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Create tkinter inputs for orientation adjustment
orient_x = tk.Entry(root)
orient_x.insert(0, "0.0")
orient_y = tk.Entry(root)
orient_y.insert(0, "0.0")
orient_z = tk.Entry(root)
orient_z.insert(0, "0.0")

# Pack the orientation inputs in the GUI
tk.Label(root, text="Orientation X:").pack()
orient_x.pack()
tk.Label(root, text="Orientation Y:").pack()
orient_y.pack()
tk.Label(root, text="Orientation Z:").pack()
orient_z.pack()

# Create and pack beta input fields with body part labels
beta_labels = [
    "Beta 0 (Overall Size/Height)",
    "Beta 1 (Chest/Bust)",
    "Beta 2 (Waist)",
    "Beta 3 (Hips)",
    "Beta 4 (Leg Length)",
    "Beta 5 (Shoulder Width)",
    "Beta 6 (Arm Thickness)",
    "Beta 7 (Torso Depth)",
    "Beta 8 (Thigh Size)",
    "Beta 9 (Calf Size)"
]

beta_entries = []
for i in range(10):
    label = tk.Label(root, text=beta_labels[i])
    label.pack()
    entry = tk.Entry(root)
    entry.insert(0, "0.0")  # Initial value
    entry.pack()
    beta_entries.append(entry)

# Create a button to update and print the model's current position
button = tk.Button(root, text="Update and Print Model Position", command=update_model)
button.pack()

# Run the tkinter main loop
mesh.export('model.glb')
root.mainloop()
