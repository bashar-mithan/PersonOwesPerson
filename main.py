import uuid
import itertools
from dataclasses import dataclass, asdict
from typing import  Optional


@dataclass
class Person:
    name: str
    balance: int
    ID: str = ''
    owes: Optional[set] = None 

    def __post_init__(self):
        self.ID = str(uuid.uuid4())


class PersonOwesPerson():
    def __init__(self, people: list) -> None:
        self.people = people
        self.main()

    def main(self) -> None:
        personCounter = itertools.cycle(self.people)
        while not all(person.owes[1] == 0 for person in self.people):
            person = next(personCounter)
            checking_result = self.check_for_owes(person)
            if (isinstance(checking_result, Person)):
                self.__pay(checking_result, person)
                
    def check_for_owes(self, person: Person) -> Person:
        for i in self.people:
            try:
                if (person.ID in i.owes): return i
            except TypeError: continue

    def __add_balance(self, person: Person, amount: int) -> None:
        person.balance = person.balance + amount

    def __take_balance(self, person: Person, amount: int) -> None:
        person.balance = person.balance - amount

    def __pay(self, personToPay: Person, payer: Person) -> None:
        amountToPay = personToPay.owes[1]
        if (payer.balance > amountToPay):
            self.__take_balance(payer, amountToPay)
            self.__add_balance(personToPay, amountToPay)
            personToPay.owes[1] = 0

        elif (payer.balance <= amountToPay):
            personToPay.owes[1] = amountToPay - payer.balance
            self.__add_balance(personToPay, payer.balance)
            self.__take_balance(payer, payer.balance)


def ppp(p1=Person(name='A', balance=5), p2=Person(name='B', balance=0), p3=Person(name='C', balance=0)):
    p1.owes = [p2.ID, 20]
    p2.owes = [p3.ID, 20]
    p3.owes = [p1.ID, 20]
    return [p1, p2, p3]

pop = PersonOwesPerson(ppp())

print(pop.people)

