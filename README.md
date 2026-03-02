# Diverge

## Overview
DIVERGE: Diversity-Enhanced Retrieval-Augmented Generation

DIVERGE is a plug-and-play, agentic Retrieval-Augmented Generation (RAG) framework
designed to **enhance output diversity for open-ended information-seeking queries** while maintaining high answer quality.
Unlike standard RAG systems that are optimized for a single correct answer,
DIVERGE explicitly models and explores **multiple viewpoints** through iterative
retrieval and generation, while maintaining high answer quality.

This repository contains the reference implementation and evaluation code for the paper  
**“DIVERGE: Diversity-Enhanced Retrieval-Augmented Generation for Open-Ended Questions.”**  

📄 Paper: https://arxiv.org/pdf/2602.00238

## Installation

We provide a installation process to set up a virtual environment and install the necessary dependencies for our experiments. Follow the steps below to get started.

---

### 1. Create a Virtual Environment

#### macOS / Linux

```bash
python -m venv .venv
source .venv/bin/activate
```

#### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

---

### 2. Install the Local Package

Install the project in editable mode:

```bash
pip install -e .
```

This step installs the local `divrag` package defined in `pyproject.toml`.

---

### 3. Install Experiment Dependencies

```bash
pip install -r requirements.txt
```

This step installs the exact dependency versions used in our experiments.

---

### Important Notes

- Both installation steps are required.
- `pyproject.toml` makes the local package (`divrag`) importable.
- `requirements.txt` ensures full reproducibility of the experimental environment.