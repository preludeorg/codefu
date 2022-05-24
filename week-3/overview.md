
# Observer Pattern

Observer is a behavioral design pattern that allows some objects to notify other objects about changes in their state.

## Identification

The pattern can be recognized by subscription methods, that store objects in a list and by calls to the update method issued to objects in that list.


## Pub/Sub model

We want to have Observers and Subjects.

**Subjects** are the target (publisher) that an observer would want to track. You can Attach, Detach, and Notify; business logic goes here.

**Observers** are the listeners (subscribers) that want to track a subject. They will have an Update"

### Sources

- https://refactoring.guru/design-patterns/observer
- https://refactoring.guru/design-patterns/observer/python/example#example-0
