# PyTest_002_Logarithm_App
2 parametrized test functions for logarithm and exceptions / 2 parametrizované testovací funkce pro výpočet logaritmu a výjimek

Tento projekt demonstruje implementaci funkce pro výpočet **logaritmu** a její testování pomocí knihovny **pytest**.  
Obsahuje také konfiguraci pro **GitHub Actions**, takže testy běží automaticky při každém pushi nebo pull requestu.

---

## 📘 Popis funkce `log`

Logaritmus je inverzní operace k umocňování.  
Obecně platí:
logaritmus čísla = exponent x, na který musím umocnit základ b, abych získala logaritmované číslo a;
logaritmus čísla a při základu b: 
log(a, b) = x nebo-li log_b(a) = x nebo-li b^x = a   
Příklad:  
`log₂(8) = 3`, protože `2³ = 8`

**a** … logaritmované číslo/argument logaritmu/výsledek umocněné báze, (musí být kladné);
**b** … základ/báze logaritmu (musí být kladné a různé od 1);
**x** … výsledek, exponent, logaritmus čísla a při základu b;

---

## Testování a výjimky
Projekt obsahuje dvě parametrizované testovací funkce:

1. **`test_log`** – testuje správnost výpočtu logaritmu pro validní vstupy.  
2. **`test_log_exceptions`** – ověřuje, že funkce správně vyvolá výjimky:
   - `ValueError` – logaritmované číslo **a** ≤ 0  
   - `ZeroDivisionError` – základ logaritmu **b** ≤ 0  
   - `NameError` – základ logaritmu **b** = 1  

---

## Instalace

Naklonuj repozitář a nainstaluj balíček v *editable* módu:

```bash
git clone https://github.com/tvoje-jmeno/calculator.git
cd logarithm
pip install -e .
```
Naklonuj repozitář a nainstaluj v *editable* módu:

---

## Testování

Testy jsou psané v **pytest**.

Spusť všechny testy:

```bash
pytest
```

Spusť jen konkrétní test:

```bash
pytest tests/test_logarithm_param.py::test_log
pytest tests/test_logarithm_param.py::test_log_exceptions
```

---

## 📂 Struktura projektu

```
logarithm/                       # root directory
│
├─ README.md                     # dokumentace projektu v ČJ
├─ README_EN.md                  # dokumentace projektu v AJ
├─ pytest.ini                    # testpaths = tests
├─ pyproject.toml                # build system (setuptools)
├─ setup.cfg                     # konfigurace balíčku
├─ .gitignore                    # filtr verzování
│
├─ src/
│   └─ logarithm/
│       ├─ __init__.py           # import funkce log z logarithm.py
│       └─ logarithm.py          # zdrojový soubor s funkcí log
│
├─ tests/
│   ├─ __init__.py               # prázdný soubor
│   └─ test_logarithm_param.py   # 2 parametrizované funkce pro test logaritmu a výjimek
│
└─ .github/
    └─ workflows/
        └─ ci.yml                # GitHub Actions workflow pro pytest
```

---

## ⚙️ CI/CD

Repozitář využívá GitHub Actions workflow .github/workflows/ci.yml.
To spouští pytest pro Python 3.9, 3.10 a 3.11 při každém pushi a pull requestu.
---

## 📝 Licence

MIT License – viz soubor [LICENSE](LICENSE) (pokud přidáš).
