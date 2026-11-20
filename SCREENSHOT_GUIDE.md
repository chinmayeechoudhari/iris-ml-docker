# SCREENSHOT_GUIDE.md
## MLOps Assignment 6 – Manual Screenshot Capture Guide

This guide provides exact, step-by-step instructions for executing and capturing all required screenshots for your assignment submission.

---

## Summary of Screenshots to Capture

| # | Step / Subject | Command / Action | Expected Output in Terminal | Recommended Filename |
|---|----------------|-------------------|-----------------------------|----------------------|
| **1** | Docker Desktop & Engine Status | `docker version` and `docker info` | Docker client & server v29.9.3 details, WSL2 engine | `01_docker_status.png` |
| **2** | Project Directory Structure | `dir` or `tree /F` in project folder | Lists `train_model.py`, `app.py`, `requirements.txt`, `Dockerfile` | `02_project_structure.png` |
| **3** | Model Training Execution | `python train_model.py` | Accuracy 100%, classification report, `model.joblib` confirmation | `03_model_training.png` |
| **4** | Model Artifact Verification | `dir model.joblib` | Shows `model.joblib` file size (~182 KB) | `04_model_artifact.png` |
| **5** | Local Inference Execution | `python app.py` | Input `5.1, 3.5, 1.4, 0.2` -> `PREDICTED SPECIES: setosa` | `05_local_prediction.png` |
| **6** | Docker Image Build | `docker build -t iris-ml-model .` | Multi-step build logs, layer caching, `naming to ... iris-ml-model:latest done` | `06_docker_build.png` |
| **7** | Docker Image Verification | `docker images iris-ml-model` | Repository: `iris-ml-model`, Tag: `latest`, Size: ~575MB | `07_docker_images.png` |
| **8** | Container Interactive Run (Setosa) | `docker run --rm -it iris-ml-model` | Terminal prompt, enter `5.1, 3.5, 1.4, 0.2` -> `setosa` | `08_container_prediction_setosa.png` |
| **9** | Container Second Sample (Virginica/Versicolor) | `docker run --rm -it iris-ml-model` | Enter `6.3, 3.3, 6.0, 2.5` -> `virginica` | `09_container_prediction_virginica.png` |
| **10**| Container Lifecycle & `docker ps` | Run detached demo, run `docker ps`, remove demo | `docker ps` showing active container `iris-verification-demo` | `10_docker_ps_verification.png` |
| **11**| Input Error Handling | `docker run --rm -it iris-ml-model` with bad input | Enter `bad, input, values` -> clear validation error message | `11_error_handling.png` |

---

## Detailed Step-by-Step Instructions

### Step 1: Docker Desktop and Engine Verification
1. Open PowerShell or Windows Terminal.
2. Ensure Docker Desktop is running (green status icon in system tray).
3. Execute:
   ```powershell
   docker version
   docker info
   ```
4. **Capture**: Ensure the output showing `Server: Docker Desktop` and `Kernel Version: ...-WSL2` is visible.
5. **Save as**: `01_docker_status.png`

---

### Step 2: Project Directory Structure
1. Navigate to the project directory:
   ```powershell
   cd "C:\Users\Chinmayee\.gemini\antigravity\scratch\iris-ml-docker"
   ```
2. Execute:
   ```powershell
   Get-ChildItem
   ```
3. **Capture**: Show the files: `train_model.py`, `app.py`, `requirements.txt`, `Dockerfile`, `README.md`.
4. **Save as**: `02_project_structure.png`

---

### Step 3: Model Training Execution
1. In the project directory, execute:
   ```powershell
   python train_model.py
   ```
2. **Capture**: The terminal output showing:
   - Dataset loading (150 samples)
   - 80:20 train/test split
   - RandomForestClassifier training
   - Accuracy: `1.0000 (100.00%)`
   - Classification report table
   - Model artifact confirmed: `model.joblib`
3. **Save as**: `03_model_training.png`

---

### Step 4: Model Artifact Verification
1. Check the generated model artifact on disk:
   ```powershell
   Get-Item model.joblib
   ```
2. **Capture**: File listing showing `model.joblib` with size (~186,897 bytes / 182 KB).
3. **Save as**: `04_model_artifact.png`

---

### Step 5: Local Prediction Execution
1. Run `app.py` directly in Python:
   ```powershell
   python app.py
   ```
2. When prompted:
   ```text
   Measurements > 5.1, 3.5, 1.4, 0.2
   ```
3. **Capture**: The terminal output showing:
   - `Input Vector: [5.1, 3.5, 1.4, 0.2]`
   - `Predicted Class: 0`
   - `PREDICTED SPECIES: setosa`
4. **Save as**: `05_local_prediction.png`

---

### Step 6: Docker Image Build
1. Build the Docker image:
   ```powershell
   docker build -t iris-ml-model .
   ```
2. **Capture**: The build output showing steps `[1/6]` through `[6/6]`, exporting layers, and `naming to docker.io/library/iris-ml-model:latest done`.
3. **Save as**: `06_docker_build.png`

---

### Step 7: Docker Image Verification
1. List Docker images to confirm creation:
   ```powershell
   docker images iris-ml-model
   ```
2. **Capture**: The output line displaying:
   `REPOSITORY: iris-ml-model | TAG: latest | IMAGE ID: ... | SIZE: ~575MB`
3. **Save as**: `07_docker_images.png`

---

### Step 8: Container Interactive Run (Sample 1 – Setosa)
1. Run the container interactively:
   ```powershell
   docker run --rm -it iris-ml-model
   ```
2. Enter the required sample measurements:
   ```text
   Measurements > 5.1, 3.5, 1.4, 0.2
   ```
3. **Capture**: The container starting, accepting input, and displaying `PREDICTED SPECIES: setosa`.
4. **Save as**: `08_container_prediction_setosa.png`

---

### Step 9: Container Interactive Run (Sample 2 – Virginica)
1. Run the container again for a different species:
   ```powershell
   docker run --rm -it iris-ml-model
   ```
2. Enter:
   ```text
   Measurements > 6.3, 3.3, 6.0, 2.5
   ```
3. **Capture**: The container output showing `PREDICTED SPECIES: virginica`.
4. **Save as**: `09_container_prediction_virginica.png`

---

### Step 10: Container Lifecycle & `docker ps` Verification
1. Demonstrate the container lifecycle and `docker ps` behavior:
   ```powershell
   # Launch a background verification container
   docker run -d --name iris-verification-demo iris-ml-model sleep 30

   # Run docker ps to show active container
   docker ps

   # Clean up
   docker rm -f iris-verification-demo
   ```
2. **Capture**: `docker ps` showing the container `iris-verification-demo` with image `iris-ml-model` in `Up` status.
3. **Save as**: `10_docker_ps_verification.png`

---

### Step 11: Error Handling Demonstration
1. Run the container and test invalid input handling:
   ```powershell
   docker run --rm -it iris-ml-model
   ```
2. Enter invalid data:
   ```text
   Measurements > bad, input, values
   ```
3. **Capture**: The validation error message:
   `[ERROR] Input validation failed: Expected exactly 4 feature values, but received 3: ['bad', 'input', 'values']`
4. **Save as**: `11_error_handling.png`
