def profile_summary(name: str, age: int, height_m: float, is_student: bool) -> str:
    status = "is a student" if is_student else "is not a student"
    return f"{name} is {age} years old, {height_m:.2f} m tall, and {status}."


def main():
    assert profile_summary("Amin", 22, 1.78, True) == (
        "Amin is 22 years old, 1.78 m tall, and is a student."
    )

    assert profile_summary("John", 25, 1.82, False) == (
        "John is 25 years old, 1.82 m tall, and is not a student."
    )

    assert profile_summary("Sara", 30, 1.65, False) == (
        "Sara is 30 years old, 1.65 m tall, and is not a student."
    )
    assert profile_summary("Ali", 18, 1.90, True) == (
        "Ali is 18 years old, 1.90 m tall, and is a student."
    )


if __name__ == "__main__":
    main()