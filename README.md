# BDD-Based Fault Tree Analysis using `dd` Library

This repository contains Python scripts and datasets used in our paper:

> **"A Heuristic Variable Ordering Approach for Fault Tree Conversion to Binary Decision Diagram"**  
> Mahdi Dibaei, Kai-Steffen Hielscher, Reinhard German, 2024 6th International Conference on System Reliability and Safety Engineering (SRSE)*  
> [DOI: 10.1109/ICSA57991.2024.10772497](https://ieeexplore.ieee.org/abstract/document/10772497)

---

## 📘 Overview

This project demonstrates the construction and manipulation of **Binary Decision Diagrams (BDDs)** using the [`dd`](https://github.com/tulip-control/dd) Python package. It explores how different **variable orders** affect the structure and size of the BDDs derived from fault tree expressions.

### Features
- Construction of BDDs for fault trees with custom variable ordering.
- Automatic expression negation and visualization of BDDs as `.pdf` files.
- Comparison of BDD-based analysis with other approaches using benchmark datasets.

---

## 🧠 Motivation

Fault Tree Analysis (FTA) is a widely used technique for safety assessment. The efficiency of Binary Decision Diagram (BDD)-based analysis is highly sensitive to **variable ordering**. This repository accompanies our study on optimizing this aspect for **improved performance and scalability**.

---

## 📁 Repository Structure

```bash
.
├── Bad in Python.py              # BDD generation with order: x6, x4, x2, x5, x3, x1
├── Bad in Python.pdf             # BDD generation with order: x6, x4, x2, x5, x3, x1
├── Good in Python.py             # BDD generation with order: x6, x5, x4, x3, x2, x1
├── Good in Python.pdf            # BDD generation with order: x6, x5, x4, x3, x2, x1
├── FFORT.zip                     # Dataset: FFORT fault trees converted to BDD format
├── BDD_Comparison.zip            # Scripts & data for comparing with other methods
└── README.md

🛠️ Installation

pip install dd

This project uses the dd package for Binary Decision Diagram operations.

🔗 Citation
If you use this code or dataset, please cite our paper:

@inproceedings{dibaei2024heuristic,
  title={A Heuristic Variable Ordering Approach for Fault Tree Conversion to Binary Decision Diagram},
  author={Dibaei, Mahdi and Hielscher, Kai-Steffen and German, Reinhard},
  booktitle={2024 6th International Conference on System Reliability and Safety Engineering (SRSE)},
  pages={301--307},
  year={2024},
  organization={IEEE}
}


---

🧾 License
This project is provided for academic and research purposes. For commercial use, please contact the authors.




