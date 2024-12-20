# Cours-Python-IPI

## Description
This repository contains various Python projects and exercises for the IPI Python course. The projects cover different aspects of Python programming, including algorithms, data structures, and practical applications.

## Projects

### 1. Swiss System Tournament
A program to manage a Swiss-system tournament. It sorts players by their Elo points, divides them into two groups, and pairs them for matches.

**Files:**
- `TPs/swiss/Systeme_Suisse.py`
- `players.json`

### 2. Bruteforce Password Cracker
A brute force algorithm to guess a randomly generated password. It demonstrates the complexity and time required to crack passwords of different lengths and complexities.

**Files:**
- `TPs/bruteforce/bruteforce.py`

## Getting Started

### Prerequisites
- Python 3.x
- `tqdm` library (for progress bar in the brute force project)

### Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/Gxb001/Cours-Python-IPI.git
    cd Cours-Python-IPI
    ```

2. Install the required libraries:
    ```sh
    pip install tqdm
    ```

## Usage

### Swiss System Tournament
1. Ensure `players.json` contains the player data.
2. Run the script:
    ```sh
    python TPs/swiss/Systeme_Suisse.py
    ```

### Bruteforce Password Cracker
1. Run the script:
    ```sh
    python TPs/bruteforce/bruteforce.py
    ```

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License
This project is licensed under the MIT License.