# PyTest_002_Logarithm_App
2 parameterized test functions for logarithm and exceptions

This project demonstrates the implementation of a function for calculating the **logarithm** and its testing using the **pytest** library.  
It also includes a configuration for **GitHub Actions**, so tests run automatically on every push or pull request.

---

## 📘 Description of the `log` function

The logarithm is the inverse operation of exponentiation.  
In general:
logarithm of a number = exponent x, to which the base b must be raised to obtain the number a;  
logarithm of a with base b:  
log(a, b) = x, or log_b(a) = x, or b^x = a  

Example:  
`log₂(8) = 3`, because `2³ = 8`

- **a** … the number to be logarithmed / argument of the logarithm / the result of raising the base to a power (must be positive);  
- **b** … the base of the logarithm (must be positive and not equal to 1);  
- **x** … the result, exponent, the logarithm of a with base b;  

---

## Testing and Exceptions

The project contains two parameterized test functions:

1. **`test_log`** – tests the correctness of the logarithm calculation for valid inputs.  
2. **`test_log_exceptions`** – verifies that the function correctly raises exceptions:  
   - `ValueError` – logarithm argument **a** ≤ 0  
   - `ZeroDivisionError` – logarithm base **b** ≤ 0  
   - `NameError` – logarithm base **b** = 1  

---

## Installation

Clone the repository and install the package in *editable* mode:

```bash
git clone https://github.com/your-username/logarithm.git
cd logarithm
pip install -e .
```

---

## Testing

Tests are written with **pytest**.

Run all tests:

```bash
pytest
```

Run only specific tests:

```bash
pytest tests/test_logarithm_param.py::test_log
pytest tests/test_logarithm_param.py::test_log_exceptions
```

---

## 📂 Project Structure

```
logarithm/                       # root directory
│
├─ README.md                     # project documentation in CZ
├─ README_EN.md                  # project documentation in EN
├─ pytest.ini                    # testpaths = tests
├─ pyproject.toml                # build system (setuptools)
├─ setup.cfg                     # package configuration
├─ .gitignore                    # version control filter
│
├─ src/
│   └─ logarithm/
│       ├─ __init__.py           # imports log function from logarithm.py
│       └─ logarithm.py          # source file with the log function
│
├─ tests/
│   ├─ __init__.py               # empty file
│   └─ test_logarithm_param.py   # 2 parameterized test functions for log and exceptions
│
└─ .github/
    └─ workflows/
        └─ ci.yml                # GitHub Actions workflow for pytest
```

---

## ⚙️ CI/CD

The repository uses a GitHub Actions workflow `.github/workflows/ci.yml`.  
This runs pytest for Python 3.9, 3.10, and 3.11 on every push and pull request.

---

## 📝 License

MIT License – see the [LICENSE](LICENSE) file (if included).
