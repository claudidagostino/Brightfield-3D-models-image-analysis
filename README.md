# Brightfield-3D-models-image-analysis

This repository contains Jupyter notebooks for the analysis of 3D models of brightfield spheroids and organoids images, using the [devbio-napari](https://github.com/haesleinhuepf/devbio-napari) plugin for the [napari](https://napari.org/) image viewer and the [apoc](https://github.com/haesleinhuepf/apoc) package (included in devbio-napari).

The notebooks placed inside the appropriate folders for each data type analysis (`Spheroid_Analysis` or `Organoid_Analysis`) and are numbered in the order they should be run.

A demonstration data set is included in the `data` folder, which can be used to test the notebooks. The full data set will be made available in an appropriate image data repository.

An example pre-trained model for one patient used in the notebooks is available inside the `Spheroids` folder [here](./data/Spheroids/Patient_1/my_model.cl).

## System Dependencies

All dependencies are listed in the `environment.yml` file, which is used to create a conda environment for running the notebooks (instructions below).The notebooks were executed in a Windows 10 laptop with an NVIDIA GeForce GTX 1650 Ti GPU, but they should run on any system with a compatible GPU and the necessary dependencies installed.

## Installation

Please follow the instructions below to set up the environment for running the notebooks in this repository.

1. Clone this repository locally (consider using [Github Desktop](https://desktop.github.com/) or download it).

2. In case you do not have `conda` installed, please follow the instructions [here](https://conda-forge.org/download/) to have Miniforge installed on your system.

3. We provide a conda environment file for convenience, which can be found in the `environment.yml` file in this repository. You can create a new conda environment using this file by running the following command in your terminal (replace `mamba` with `conda` if you do not have `mamba` installed):

    ```bash
    mamba env create -y -f environment.yml
    ```

    This step took about 7 minutes in the machine defined above, but it may take longer on other systems depending on the internet connection and the system performance.

4. From a terminal, activate the environment:

    ```bash
    mamba activate brightfield-analysis-env
    ```

5. If you are on a Mac, please also install this:

    ```bash 
    mamba install -c conda-forge ocl_icd_wrapper_apple
    ```

    If you are using Linux, please install the following package to ensure OpenCL support:

    ```bash
    mamba install -c conda-forge ocl-icd-system
    ```

## Usage

From a terminal, activate the environment:

```bash
conda activate brightfield-analysis-env
```

Navigate to the cloned repository directory:

```bash
cd path/to/Brightfield-3D-models-image-analysis
```

Then, run the following command to start Jupyter Lab:

```bash
jupyter lab
```

Or use your preferred IDEs such as PyCharm or VSCode to open the repository.

Run the jupyter notebooks, replacing data paths to the correct local data path whenever necessary. This is not necessary for the demonstration data set, which is already included in the `data` folder.

## Expected Outputs

The expected outputs are a set of `.tif` images containing segmentation results and a `.csv` file with the measurements of the segmented objects. The segmentation results are saved in the same folder as the original images, with the suffix `_labels` added to the file name. The measurements are saved in a `.csv` file with the same name as the original image, but with the suffix `_measurements` added to the file name. For the Spheroid analysis, the model, if re-trained, is saved inside each `Patient_X` folder, with the name `my_model.cl`. A `min_area.json` file is also created to store the `min_area` parameter used.