# git-github-Tutorial
A Git and Github Tutorial for beginners

## How to perfrom Git Add
### Git Add is a command used to add changes to a repository or directory.
### When you make changes to a file or directory, you should use the `git add` command to add the changes.
### It is a standard practice to break coding activities or feature development into chunks of work.
### Hence, the need to add changes made in order to make a commit.
### There are several commands to use to add changes to a repository.
### They include; `git add .`, `git add - A`, `git add filename.txt`, `git add -i`, `git add directory/`, `git add -u`, `git add -p` and so on.
### Kindly  note that each has it's own purpose but they all stage changes for the next commit.
### I will now go ahead and stage the changes made in this Readme.md file using the `git add` command.


## Git Commit
### You would have noticed that I ran some command earlier on the terminal, that was the git commit command. 
### I was trying to record the exact changes made while learning how to perform Git Add.
### The Git Commit command is used to record changes to the repository.
### After you have staged your changes using `git add`, use `git commit` to save those changes to the repository.
### Here are various ways to use the Git Commit command:

- Basic commit: `git commit -m "Your commit message here"`
- Commit all changes: `git commit -am "Your commit message here"`
- Interactive commit: `git commit -i`
- Amend last commit: `git commit --amend`
- Commit only staged changes: `git commit`


## Git Status
### The git status command is used to display the status of the repository and the staging area in your git repository.
### It provides information about which files are modified and which files are staged for the next commit.
### It also provides information about which files are untracked.
### I have used the `git status` command to display the status of the repository files and directory in this tutorial a couple of times now.
### Here are the various use cases for the git status command:

- Basic Status: `git status`
- Short Status: `git status -s`
- Status with branch information: `git status -b`
- Status including untracked files: `git status -u`
- Status excluding untracked files: `git status -uno`
- Status showing renamed files: `git status --r`
- Status with ignored files: `git status --ignored`

