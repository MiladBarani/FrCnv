# FrCnv — Data Format Converter

FrCnv (short for **Format Converter**) is a modular and extensible data format conversion tool designed for researchers, data engineers, and analysts who need a simple yet scalable way to convert dataset files between formats.

The project currently supports:

- RDA → CSV

The architecture is designed to make it easy to add new formats with minimal changes to the core logic.

---

## ✨ Features

- Modular architecture (easy to extend)
- Clean separation between logic and interface
- Command Line Interface (CLI)
- Graphical User Interface (GUI - Tkinter)
- Designed for scalability and maintainability
- Ready for packaging and future expansion

---

## 🏗 Project Structure

FrCnv/

├── data_converter/

│ ├── core.py

│ ├── registry.py

│ └── formats/

│ ├── base.py

│ ├── rda.py

│ └── csv.py
├── cli.py

├── gui.py

├── requirements.txt

├── pyproject.toml

├── .gitignore

├── README.md

└── LICENSE

