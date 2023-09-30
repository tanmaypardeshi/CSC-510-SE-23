# Contributing to TeachersPetBot

:+1::tada: First off, thanks for taking the time to contribute! :tada::+1:

The following is a set of guidelines for contributing to TeachersPetBot. These are mostly guidelines, not rules. Use your best judgment, and feel free to propose changes to this document in a pull request.

#### Table Of Contents

[Code of Conduct](#code-of-conduct)

[I don't want to read this whole thing, I just have a question!!!](#i-dont-want-to-read-this-whole-thing-i-just-have-a-question)

[How Can I Contribute?](#how-can-i-contribute)
  * [Reporting Bugs](#reporting-bugs)
  * [Pull Requests](#pull-requests)

[Styleguides](#styleguides)
  * [Git branch naming format](#python-styleguide)
  * [Git commit messages](#python-styleguide)
  * [Python Styleguide](#python-styleguide)

[References](#References)

## Code of Conduct

This project and everyone participating in it is governed by the [TeachersPetBot Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to any of the original team members.

## I don't want to read this whole thing I just have a question!!!

Reach out to one of the main contributors on Discord using their IDs:
* Chandrahas Reddy Mandapati: Chandrahas_Reddy_Mandapati#9201
* Harini Bharata: Harini Bharata#7221
* Sri Pallavi Damuluri : Sri Pallavi#8748
* Niraj Lavani: Benpoindexter#4486
* Sandesh Aladhalli Shivarudre Gowda: sandesh#1990

*Note: Due to the dynamic nature of Discord IDs, these may change without prior notice on this page.*

We do not have an official message board at this time, however, we plan to have one if it will help future contributors!

## How Can I Contribute?

### Reporting Bugs

This section guides you through submitting a bug report for TeachersPetBot. Before submitting a bug, make sure you have all the information with you. Following these guidelines helps maintainers and the community understand your report :pencil:, reproduce the behavior :computer: :computer:, and find related reports :mag_right:.

#### How Do I Submit A (Good) Bug Report?

Bugs are tracked as [GitHub issues](https://guides.github.com/features/issues/). After you've found a bug, create an issue detailing the steps for reproducing the bug.

Explain the problem and include additional details to help maintainers reproduce the problem:

* **Use a clear and descriptive title** for the issue to identify the problem.
* **Describe the exact steps which reproduce the problem** in as many details as possible.
* **Provide specific examples to demonstrate the steps**.
* **Describe the behavior you observed after following the steps** and point out what exactly is the problem with that behavior.
* **Explain which behavior you expected to see instead and why.**

#### Start Your Contribution

`beginner` and `help-wanted` issues can help you get started to contribute your first contribution:

* [Beginner issues][beginner] - issues which are pretty simple and should only require a few lines of code, and a couple of tests.
* [Help wanted issues][help-wanted] - issues which should be a bit more involved than `beginner` issues.


### Pull Requests

The process described here has several goals:

- Maintain TeachersPetBot's quality
- Fix problems that are important to users
- Enable a sustainable system for TeachersPetBot's maintainers to review contributions

Please follow these steps to have your contribution considered by the maintainers:

1. Follow the [styleguides](#styleguides)
2. After you submit your pull request, verify that all [status checks](https://help.github.com/articles/about-status-checks/) are passing <details><summary>What if the status checks are failing?</summary>If a status check is failing, and you believe that the failure is unrelated to your change, please leave a comment on the pull request explaining why you believe the failure is unrelated. A maintainer will re-run the status check for you. If we conclude that the failure was a false positive, then we will open an issue to track that problem with our status check suite.</details>

While the prerequisites above must be satisfied prior to having your pull request reviewed, the reviewer(s) may ask you to complete additional design work, tests, or other changes before your pull request can be ultimately accepted.

## Styleguides

#### Git Branch Naming format

* The github branch names must be of the form `issue-{issue#}/{doc/task/bug}/description`.
* Branch name must start by specifying the issue number and must specify the type of issue i.e documentation/task/bug and a small description of issue.
* Below specified are few examples of how a branch name must be
* If the issue raised is related to enhancement then branch name would be `issue-39/task/email_attachment`.
* If the issue raised id related to a bug then branch name would be `issue-39/bug/email_validation`.

#### Git Commit Messages

* Use the present tense ("Add feature" not "Added feature")
* Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
* Limit the first line to 72 characters or less
* Reference issues and pull requests liberally after the first line
* When only changing documentation, include `[ci skip]` in the commit title

### Python Styleguide

Changes to TeachersPetBot Python code should conform to [Google Python Style Guide](https://github.com/google/styleguide/blob/gh-pages/pyguide.md)

All Python code is linted with Pylint. Ensure that before you commit any changes, your code passes all default pylint checks. Pylint can be installed with
`pip install pylint`

## References
[transcriptor](https://github.com/secheaper/transcriptor/blob/main/CONTRIBUTING.md#start-your-contribution)
[Atom Code of Conduct](https://github.com/atom/atom/blob/master/CONTRIBUTING.md#code-of-conduct)*
