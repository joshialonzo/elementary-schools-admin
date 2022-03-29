import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_uppercase, k=12))


@dataclass
class Person:
    first_name: str
    last_name: str
    id: str = field(default_factory=generate_id)
    

def main() -> None:
    person = Person(first_name="John", last_name="Doe")
    print(person)


if __name__ == "__main__":
    main()
