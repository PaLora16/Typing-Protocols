from dataclasses import dataclass
from datetime import datetime
from typing import List, Protocol, TypeVar

#We ensure pure immutable data structures by parametrizing @dataclass
@dataclass(frozen=True, kw_only=True, slots=True)
class CustomerData:
    last_visit: datetime
    order_id: int


@dataclass(frozen=True, kw_only=True, slots=True)
class FreeCustomerData(CustomerData):
    name: str
    surname: str


@dataclass(frozen=True, kw_only=True, slots=True)
class RegistereCustomerData(CustomerData):
    customer_id: int


C = TypeVar("C", bound=CustomerData)


class ICustomer(Protocol):
    def process_customer(self, customer: C) -> None:
        ...


class Customer(ICustomer):
    """Each class implementing the ICustomer protocol
    must implement process_customer with the given signature
    """

    def process_customer(self, customer: C) -> None:
        print("Handler for all type of customers")


class FreeCustomer(ICustomer):
    """A static type check ensures that every customer is  based on CustomerData"""

    def process_customer(self, customer: C) -> None:
        if isinstance(customer, FreeCustomerData):
            print("Handler for non registered customer")


class RegisteredCustomer(ICustomer):
    """Checking customer subtype we can implement chain responsibility pattern"""

    def process_customer(self, customer: C) -> None:
        if isinstance(customer, RegistereCustomerData):
            print("Handler for registered customer")


class Broker:
    """classic pub-sub pattern_"""

    def __init__(self):
        self._subscribers: List[ICustomer] = []

    def attach(self, subscriber: ICustomer) -> None:
        if subscriber not in self._subscribers:
            self._subscribers.append(subscriber)

    def route(self, customer: C) -> None:
        for subscriber in self._subscribers:
            subscriber.process_customer(customer)


# test data
def get_free_customer():
    return FreeCustomerData(
        last_visit=datetime.now(), order_id=1, name="John", surname="Doe"
    )


def get_registered_customer():
    return RegistereCustomerData(last_visit=datetime.now(), order_id=2, customer_id=344)


if __name__ == "__main__":
    br = Broker()
    br.attach(Customer())
    br.attach(FreeCustomer())
    br.attach(RegisteredCustomer())
    fc = get_free_customer()
    rc = get_registered_customer()
    br.route(fc)
    br.route(rc)
