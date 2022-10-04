## Typing

 As a dynamic typed language, Python does not have run-time type checking, which some developers consider a fundamental flaw in enterprise solutions. This limitation has been partially overcome by the use and implementation of Python typing. See <https://docs.python.org/3/library/typing.html>. The purpose of Python static typing is to check types of variables so future maintainers can implement patches and extensions with more confidence. This will also improve readability of code. It is for this reason that all upcoming code development should be based on typing.

## Typing.Protocols

Interfaces are commonly used in static type languages to describe the behavior of concrete objects. In Python, you can ensure interface behavior on the IDE level by using the not so well known typing.Protocols. <https://peps.python.org/pep-0544/> Similar behaviour existed with paradigm ABC classes, which required additional boilerplate to accomplish runtime validation. The protocol presents a lighter version of the same.
