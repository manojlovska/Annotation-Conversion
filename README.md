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
To generate ground truth tensors run
   ```sh
   python toTensor.py
   ```
To visualize the converted annotations run
   ```sh
   python visualize.py
   ```

The folder structure for generating gorund truth tensors and visualizing them looks something like this:
```
.
├── ...
├── DAIS
│   ├── dais_data_0
│   │   ├── naloga_1
│   │   │   ├── image1.jpg
│   │   │   ├── image2.jpg
│   │   │   └── ...
│   │   ├── naloga_2
│   │   │   ├── image1.jpg
│   │   │   ├── image2.jpg
│   │   │   └── ...
│   │   ├── ...
│   │   ├── naloga_19
│   │   │   ├── image1.jpg
│   │   │   ├── image2.jpg
│   │   │   └── ...
│   └── dais_data_1
│       ├── naloga_20
│   │   │   ├── image1.jpg
│   │   │   ├── image2.jpg
│   │   │   └── ...
│       ├── naloga_21
│   │   │   ├── image1.jpg
│   │   │   ├── image2.jpg
│   │   │   └── ...
│       └── naloga_22
│   │   │   ├── image1.jpg
│   │   │   ├── image2.jpg
│   │   │   └── ...
├── converter.py
├── example_usecase.py
├── toTensor.py
├── visualize.py
├── visualizer.py
└── ...
```

<!-- ROADMAP -->
## Roadmap

- [x] convert cartesian points
    - [ ] optimize conversion
- [ ] convert 1D Poins
- [ ] convert Euler angles

## Problematic images
debug\1635968679.3965194.jpg
debug\1635968681.3002033.jpg
debug\1635968708.2655108.jpg
debug\1635968710.2643082.jpg
debug\1635968713.2564065.jpg
debug\1635968722.2748063.jpg
debug\1635968728.239809.jpg
debug\1635968732.2396882.jpg
debug\1635968733.2381008.jpg
debug\1635969461.3536637.jpg
debug\1635969473.3440845.jpg
debug\1635969616.1673646.jpg
debug\1635969623.169405.jpg
debug\1635970440.1754007.jpg
debug\1635970525.0803819.jpg
debug\1635975809.4737513.jpg
debug\1635977172.0751393.jpg
debug\1647956770.9162688.jpg
debug\1648022917.2175105.jpg