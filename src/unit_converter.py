def celsius_to_fahrenheit(c: float) -> float:
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f: float) -> float:
    return (f - 32) * 5/9

def meters_to_feet(m: float) -> float:
    return m * 3.28084

def feet_to_meters(ft: float) -> float:
    return ft * 0.3048


def approx_eq(a: float, b: float, tol: float = 1e-6) -> bool:
    return abs(a - b) < tol


def main():
    # Tests
    assert approx_eq(celsius_to_fahrenheit(0), 32.0)
    assert approx_eq(celsius_to_fahrenheit(100), 212.0)
    assert approx_eq(fahrenheit_to_celsius(32.0), 0.0)
    assert approx_eq(fahrenheit_to_celsius(212.0), 100.0)

    assert approx_eq(meters_to_feet(1.0), 3.28084)
    assert approx_eq(feet_to_meters(1.0), 0.3048)

    # Demo output with units
    c = 0.0
    f = celsius_to_fahrenheit(c)
    print(f"{c:.2f} °C = {f:.2f} °F")

    f = 32.0
    c = fahrenheit_to_celsius(f)
    print(f"{f:.2f} °F = {c:.2f} °C")

    m = 1.0
    ft = meters_to_feet(m)
    print(f"{m:.2f} m = {ft:.2f} ft")

    ft = 1.0
    m = feet_to_meters(ft)
    print(f"{ft:.2f} ft = {m:.2f} m")


if __name__ == "__main__":
    main()