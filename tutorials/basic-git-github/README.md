# git-github-Tutorial
A Git and Github Tutorial for beginners

## How to perfrom Git Add
Git Add is a command used to add changes to a repository or directory.
When you make changes to a file or directory, you should use the `git add` command to add the changes.
It is a standard practice to break coding activities or feature development into chunks of work.
Hence, the need to add changes made in order to make a commit.
There are several commands to use to add changes to a repository.
They include; `git add .`, `git add - A`, `git add filename.txt`, `git add -i`, `git add directory/`, `git add -u`, `git add -p` and so on.
Kindly  note that each has it's own purpose but they all stage changes for the next commit.
I will now go ahead and stage the changes made in this Readme.md file using the `git add` command.


## Git Commit
You would have noticed that I ran some command earlier on the terminal, that was the git commit command. 
I was trying to record the exact changes made while learning how to perform Git Add.
The Git Commit command is used to record changes to the repository.
After you have staged your changes using `git add`, use `git commit` to save those changes to the repository.

Here are various ways to use the Git Commit command:

- Basic commit: `git commit -m "Your commit message here"`
- Commit all changes: `git commit -am "Your commit message here"`
- Interactive commit: `git commit -i`
- Amend last commit: `git commit --amend`
- Commit only staged changes: `git commit`


## Git Status
The git status command is used to display the status of the repository and the staging area in your git repository.
It provides information about which files are modified and which files are staged for the next commit.
It also provides information about which files are untracked.
I have used the `git status` command to display the status of the repository files and directory in this tutorial a couple of times now.

Here are the various use cases for the git status command:

- Basic Status: `git status`
- Short Status: `git status -s`
- Status with branch information: `git status -b`
- Status including untracked files: `git status -u`
- Status excluding untracked files: `git status -uno`
- Status showing renamed files: `git status --r`
- Status with ignored files: `git status --ignored`

## Git Branch
The git branch command in Git is used to list, create or delete branches in a git repository.
It can also be used to rename an exisiting branch.
The idea of branches in Git is to be a pointer to a specific commit in the version history of a repository.
Each repository typically starts with a default branch called `master` or `main`.
Additional branches can be created to work on different features or bug fixes without affecting the main branch.

Here are various use cases for the git branch command:

- List local branches: `git branch`
- List remote branches: `git branch -r`
- List all branches: `git branch -a`
- Create a new branch: `git branch new-branch-name`
- Create and Switch to a new branch: `git branch -b new-branch-name`
- Rename a branch: `git branch -m new-branch-name`
- Delete a local branch: `git branch -d branch-to-delete`
- Delete a remote branch: `git push origin --delete remote-branch-to-delete`
- Display branches with additional information: `git show branch`


Now, we will push all our changes to the remote repository that we set up earlier.
Hence, we will practice the `git push` command.

Let's practice a little bit of git conflict issues as well.
I will create a git conflict by making changes to the remote repository and then pull to the local repository.
This will create a merge conflict that will have to be resolved locally.
Though git conflict can either be resolved locally or remotely depending on the specific case.

## Git Pull
This command is used to fetch changes from the remote repository and integrate them into the current branch.
It is essentially a combination of two other git commands; `git fetch` and `git merge`.

Below are some common usecases for git pull:

- Basic Pull: `git pull`
- Pull from a specific branch: `git pull origin branch-name`
- Pull with rebase: `git pull --rebase`
- Pull a specific remote branch and rebase: `git pull --rebase origin branch-name`
- Pull with Fetch only: `git pull --no-commit`
- Pull with Squash: `git pull --squash`
- verbose pull: `git pull --verbose`
- Pull from a different remote repository: `git pull other-remote other-branch`
