import importlib
import sys


def check_package(name: str, message: str) -> None | str:
    try:
        package = importlib.import_module(name)
        version = package.__version__
        print(f"[OK] {name} ({version}) - {message}")
        return package
    except ImportError:
        print(f"[MISSING] {name}")
        return None


print("LODING STATUS: Loading programs...")
print()

print("Checking dependencies:")
pandas = check_package("pandas", "Data mainpulation ready")
numpy = check_package("numpy", "Numerical computation ready")
matplotlib = check_package("matplotlib", "Visualization ready")

if pandas is None or numpy is None or matplotlib is None:
    print("Install with pip:")
    print("pip install -r requirements.txt")
    print("\nOr with Poetry:")
    print("poetry install")

print("\npip uses requirements.txt")
print("Poetry uses pyproject.toml and poetry.lock")

data = pandas.DataFrame(
    {
        "signal": numpy.random.normal(70, 10, 1000),
        "anomaly": numpy.random.uniform(0, 100, 1000),
    }
)

data["risk"] = data["anomaly"] - data["signal"] / 2

print("\nAnalyzing Matrix data...")
print("Processing 1000 data points...")
print(f"Average signal: {data['signal'].mean():.2f}")
print(f"Average anomaly: {data['anomaly'].mean():.2f}")
print(f"Average risk: {data['risk'].mean():.2f}")

pyplot = importlib.import_module("matplotlib.pyplot")

print("Generating visualization...")
pyplot.scatter(data["anomaly"], data["risk"])
pyplot.title("Matrix Data Analysis")
pyplot.xlabel("Anomaly")
pyplot.ylabel("Risk")
pyplot.savefig("matrix_analysis.png")
pyplot.close()

print("Analysis complete!")
print("Results saved to: matrix_analysis.png")
