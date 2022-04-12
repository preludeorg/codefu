
# Patterns

Design patterns are typical solutions to commonly occurring problems in software design. They are like pre-made blueprints that you can customize to solve a recurring design problem in your code.

# Strategy Pattern

## The Problem

We want to implement some code that will allow us to pass in an array of data then perform a specific type of sort. How can we apply code in a scalable, easy to read, and extensible way?

## What is the strategy pattern?

Strategy Design Pattern is a type of behavioral design pattern that encapsulates a "family" of algorithms and selects one from the pool for use during runtime. The algorithms are interchangeable, meaning that they are substitutable for each other.

## SOLID Principles

The single-responsibility principle: "A class should have one and only one reason to change, meaning that a class should have only one job." In other words, every class should have only one responsibility.
The open–closed principle: "Objects or entities should be open for extension but closed for modification."
The Liskov substitution principle: "Functions that use pointers or references to base classes must be able to use objects of derived classes without knowing it." This means that every subclass or derived class should be substitutable for their base or parent class.
The interface segregation principle: "Many client-specific interfaces are better than one general-purpose interface."
The dependency inversion principle: "Depend upon abstractions, [not] concretions."


### Sources

- https://refactoring.guru/design-patterns/what-is-pattern
- https://blog.bitsrc.io/keep-it-simple-with-the-strategy-design-pattern-c36a14c985e9