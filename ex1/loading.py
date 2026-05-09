import importlib


def check_package(name: str, message: str) -> None | object:
    try:
        package = importlib.import_module(name)
        version = package.__version__
        print(f"[OK] {name} ({version}) - {message}")
        return package
    except ImportError:
        print(f"[MISSING] {name}")
        return None


def check_dependencies() -> int:
    print("Checking dependencies:")
    pandas = check_package("pandas", "Data mainpulation ready")
    numpy = check_package("numpy", "Numerical computation ready")
    matplotlib = check_package("matplotlib", "Visualization ready")

    if pandas is None or numpy is None or matplotlib is None:
        print()
        print("Install with pip:")
        print("pip install -r requirements.txt")
        print("Or")
        print("with Poetry:")
        print("poetry install")
        return 0
    return 1


print("LODING STATUS: Loading programs...")
print()

checked = check_dependencies()
if checked:
    pd = importlib.import_module("pandas")
    np = importlib.import_module("numpy")
    plt = importlib.import_module("matplotlib.pyplot")

    data = pd.DataFrame(
            {
                "data": np.random.randint(0, 1000, 1000),
                }
            )

    print()
    print("Analyzing Matrix data...")
    print("Processing 1000 data points...")

    print("Generating visualization...")
    plt.hist(data["data"], bins=20)
    plt.title("Matrix Data Analysis")
    plt.xlabel("Random data")
    plt.ylabel("Random data")
    plt.savefig("matrix_analysis.png")
    plt.close()
    print()

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")
