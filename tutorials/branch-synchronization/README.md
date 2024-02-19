# Branch Synchronization

## Overview
Branch Synchronization refers to the process of bringing two seperate branches in a version control system like git to the same state. This is crucial in collaborative development environments where multiple people or teams might be working on different branches of the same codebase.

Here is a breakdown of what happens during branch synchronization:
<!-- I will illustrate them for better understanding -->

1. Different branches: Imagine you have two branches;

    * `Master`: This is the main branch that holds the stable, released version of the code.
    * `Feature`: This is a seperate branch where you're working on a new feature or bug fix.

2. Changes Diverge: Over time, as you work on your feature branch, you make commits adding new code or fixing issues. Meanwhile, other developers may make changes to the master branch. This means the two branches become out of sync, meaning that they contain different versions of the code.

3. Synchronization Process: To get both branches on the same page, you need to synchronize them. This involves merging or rebasing your feature branch with the master branch.

    * `Merging`: This creates a new commit that combines changes from both branches. Any conflicts between the  changes need to be manually resolved.
    * `Rebasing`: This rewrite the history of your feature branch, making it appear as if the changes were made on top of the latest master branch. This avoids merge conflicts but can rewrite history in a way that might be confusing for others.

4. Choosing the method: The best method for synchronizing branches depends on the situation:

    * `Merging`: Good for integrating small changes or when keeping historical context is important.
    * `Rebasing`: Better for keeping a linear commit history, but only use it if you're working alone or everyone on the team understands the implications.

### Benefits of Branch Synchronization:
- Ensures everyone works on the same codebase.
- Reduces conflicts and confusion
- Makes merging back to Master easier.

<!-- Plaese note that Cherry-Pick is also used in branch synchronization  -->
*  `Cherry-pick`: Selectively applies individual commits from one branch to another

<!-- I will demonstrate branch synchronization with git and github shortly -->

## Basic Methods

a. Merge:

* `Mechanics`