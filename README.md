# Annotation-Conversion

<!-- ABOUT THE PROJECT -->
## About The Project

Convert annotated polylines to a grid, where each square is its own coordinate system.

<!-- GETTING STARTED -->
## Getting Started

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/JanSuklje/Annotation-Conversion
   ```
2. Install requiremensts
   ```sh
   pip install -r requirements.txt
   ```

<!-- USAGE EXAMPLES -->
## Usage

To get an idea of how to use this, take a look at this file [example_usecase.py](https://github.com/JanSuklje/Annotation-Conversion/blob/main/example_usecase.py).<br />
This is the folder structure for this example:<br />
```
    .
    ├── ...
    ├── debug
        ├── image1.jpg
        ├── image2.jpg
        └── ... 
    ├── converter.py
    ├── example_usecase.py
    ├── visualizer.py
    └── ...
```
<!-- ROADMAP -->
## Roadmap

- [x] convert cartesian points
    - [ ] optimize conversion
- [ ] convert 1D Poins
- [ ] convert Euler angles