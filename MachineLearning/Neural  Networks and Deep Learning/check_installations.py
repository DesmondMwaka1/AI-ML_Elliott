import subprocess
import sys
import pkg_resources

def check_installation():
    # Standard requirements for a robust ML/DL environment
    required_packages = {
        "numpy": "Numerical computing",
        "pandas": "Data manipulation",
        "matplotlib": "Plotting/Visualization",
        "seaborn": "Statistical visualization",
        "scikit-learn": "Machine Learning (Classic)",
        "scipy": "Scientific computing",
        "notebook": "Jupyter Notebook environment",
        "tensorflow": "Deep Learning (Google)",
        "torch": "Deep Learning (PyTorch/Meta)",
        "keras": "Deep Learning API",
        "xgboost": "Gradient Boosting",
        "lightgbm": "Gradient Boosting",
        "statsmodels": "Statistical modeling"
    }

    installed_packages = {pkg.key: pkg.version for pkg in pkg_resources.working_set}
    
    print(f"{'Package':<15} | {'Status':<12} | {'Version':<10} | {'Description'}")
    print("-" * 80)

    missing = []
    for pkg, desc in required_packages.items():
        if pkg in installed_packages:
            status = "INSTALLED"
            version = installed_packages[pkg]
        else:
            status = "MISSING"
            version = "N/A"
            missing.append(pkg)
        
        print(f"{pkg:<15} | {status:<12} | {version:<10} | {desc}")

    print("\n" + "="*30)
    if not missing:
        print("Everything is installed! You are ready for ML/DL.")
    else:
        print(f"Missing {len(missing)} package(s).")
        print("To install all missing packages, run:")
        print(f"pip install {' '.join(missing)}")
    print("="*30)

if __name__ == "__main__":
    check_installation()