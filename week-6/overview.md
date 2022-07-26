
# Getting code past David Review

As we all know, getting code past David can be a challenge. He set a high standard of excellence.

# Code Review Charter

## The Mantra

“Each pull request should add less than 200 lines of code, do a single thing and leave the system in better shape than it found it.”


### Alex's Advice

- David often knows exactly what he WANTS. It's your job as engineers to build what he NEEDS. Through the development process, you build trust with him. More trust == faster merges.
- Prototype code > write-ups > talking. DO don't ASK or SHOW.
- Do "stacked" PRs. If you have large change set, do small PRs that build on top of one another.
- Your first iteration will probably not get merged.
- Do not get attached to code. It will probably get deleted or consolidated in 1-2 weeks.

## DOs

- Keep It Simple Stupid. Readability and simplicity outweigh performance unless otherwise said.
- Follow best practices for the language or follow the consistency established by the project itself
- Any code added should be easy to remove in the future
- The system should always be capable of running locally in 3 steps or less
- Functions should do one thing
- Encapsulate conditionals or rely on polymorphism
- Follow the open/closed principle: code is open for extension and closed for modification. If you must break this by adding a feature, start with a PR refactoring the area then add a PR with your change.
- Think about your function and variable names. The longer their scope, the more expressive the name should be.

### Examples of GOOD

- https://github.com/preludeorg/operator/pull/3984/files
- https://github.com/preludeorg/operator/pull/2076/files

## DON'Ts

- Write spaghetti code to handle every possible exception. Instead determine possible errors upfront and handle them cleanly.
- Duplicate code. Ever.
- Use comments. Instead make your code more readable.
- Add external dependencies unless you absolutely need them.
- Add code you’ll use in the future. Only add code that you are using right now.
- Ignore warnings from your IDE.
- Use more than three function parameters
- Use magic numbers or strings. Instead use expressive names.
- Add more than two return statements from a single function

### Examples of BAD

- https://github.com/preludeorg/systems/pull/31/files
- https://github.com/preludeorg/systems/pull/13/files
- https://github.com/preludeorg/operator/pull/2021/files
- https://github.com/preludeorg/pneuma/pull/67
