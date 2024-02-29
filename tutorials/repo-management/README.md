# Repository Management with Git and Github

## Introduction to Version Control
Version Control is a system that records changes to files over time, enabling you to recall specific versions of those files later. It is a crucial tool in software development and collaboration, allowing multiple team members to work on the same project simuntaneously without overwriting each others changes.

### Benefits of Version Control
1. Collaboration
2. History Tracking
3. Risk Mitigation
4. Code Quality
5. Experimentation and Innovation

### Git and Github in Version Control

#### Git:
Git is a distributed version control system that tracks changes to files over time.
It allows developers to create snapshots of project's state (commits) and manage these snapshots through branching, merging and tagging.
Developers use Git commands like (git init, git add, git commit, git merge) to interact with the version control system locally on their machines. 

Git also maintains a local repository on each developer's machine, where changes are tracked and merged.
Developers can work offline and perform version control operations without an internet connection using git.
<!-- I will demonstrate an example shortly -->

Git enables collaboration by providing mechanisms for sharing changes between developers and synchronizing work accross multiple machines.
Developers can push their changes to remote repositories and pull changes from others, facillitating team collaborators on projects.

Git's branching and merging capabilities allow developers to work on multiple features or fixes concurrently with each other.
Developers can create branches to isolate work, make changes independently, and merge their changes back into the main branch when ready.
<!-- I will demonstrate an example shortly -->
<!-- In this repository, we have 3 branches:  
    basic-git-commands
    main
*   repository-management -->
<!-- We are currently working in the repository-managemnt branch -->

#### GitHub
Github is a web-based platform that hosts Git repositories in the cloud.
It provides a central location for storing and sharing Git repositories, making it easy for developers to collaborate on projects from anywhere.

Github hosts remote repositories where developers can push their local changes and collaborate with others.
Remote repositories on GitHub serve as a centalized location for storing project code and history, accessible to all team members.
<!-- I will quickly show you the Github platform -->
Developers can open pull requests to propose changes, review each other's code, discuss issues and track project progress.
<!-- I will show an exaple of a merged Pull Request on Github -->

Github integrates seamlessly with continuous integration and continous deployment (CI/CD) tools, allowing developers to automate build, test and deployment processes directly from GitHub.


## Collaborative Workflows
### Cloning
Git cloning refers to creating a local copy of a remote repository onto your local machine.
Cloning allows you to work on the project locally, make changes and contribute back to the remote repository.

- Process:
a. Use the `git clone` command followed by the url of the remote repository to clone it.
b. Git will download all the files and commit history from the remote repository and create a local copy in a new directory.
c. You can then navigate into the cloned directory and start working on the project.
 <!-- I will demonstate how to git clone shortly  -->
 <!-- We were able to clone the `git-github-Tutorial` repository successfuly -->

 ### Forking
 Forking involves creating a copy of a repository under your own Github account.
 It allows you freely experiment with changes without affecting the original repository.
 It's commonly used for contributing to open-source projects.

 - Process:
 a. On the Github repository page, click the `Fork` button in the top-right corner.
 b. Github will create a copy of the repository under your account.
 c. You can then clone your forked repository to your local machine and start making changes.
 <!-- I will be showing an already forked repository -->

 ### Pushing changes
 Pushing changes involves uploading your local commits to a remote repository.
 It allows you to share your work with others and contribute to the project history.

 - Process:
 a. Make changes to file in your local repository and stage them using `git add`
 b. Commit your changes using `git commit` to create a new commit with a message describing your changes.
 c. Push your commits to the remote repository using `git push`.

 <!-- We will demonstrate this and also raise a Pull Request on it -->

 <!-- I'm adding this comment to demonstrate cherry-picking. Basically, the idea is to sync the changes in this branch with the branch-synchronization branch by picking a specific commit of this branch. This commit will be the one that holds this new changes. -->

 <!-- I'm adding this new comment to demonstrate cherry-picking. Basically, the idea is to sync the changes in this branch with the branch-synchronization branch by picking a specific commit of this branch. This commit will be the one that holds this new changes. For some reason, I couldn't pick the last commit. -->