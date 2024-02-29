# Git Conflicts
Let's talk about what conflicts are in Git and Github. So far, we have encountered a couple of git conflicts either remotely (on Github) or locally on our machine (Git). So let's talk about what conflicts are in Git and Github.

## Overview
In Git, conflicts occur when two or more people make changes to the same file or lines in a file, and Git is unable to automatically merge the changes. When this happens, Git marks the file as having a conflict and asks the user to resolve it manually.

Now, let's simulate a typical Git conflicts scenario;
Let's say we have a simple repository with a file called `example.txt`. Here is what happens below;

1. Initial file contents:
    `This is line 1`
    `This is line 2`
    `This is line 3`

2. Person A's changes: Person A makes a change to example.txt;
    `This is line 1`
    `This is the modified line 2 by Person A`
    `This is line 3`

3. Person B's changes: At the same time, Person B makes a different change to example.txt;
    `This is line 1`
    `This is a completely different line 2 by Person B`
    `This is line 3`

### Creating a Conflict
Now, let's see what happens when both Person A and B try to push their changes to the remote repository (Github);

1. Person A commits and pushes his changes by using the commands below consequtively;
    `git add example.txt`
    `git commit -m "Person A's changes"`
    `git push origin main`

2. Person B commits and Pushes changes;
    `git add example.txt`
    `git commit -m "Person B's changes"`
    `git push origin main`

### Resolving the Conflict:
Person B's push will fail because their local branch is not-up-to-data with the changes on the remote repository. They need to pull the changes from the remote repository first.

1. Person B Pulls changes from Github with the Git command below:
    `git pull origin main`

    Git will try to automatically merge the changes. Since both Person A and Person B changed the same line, Git cannot automically merge the files and will create a conflict. This is what Git will display in the console below;

    """"""""""
    Auto-merging example.txt
    CONFLICT (content): Merge conflict in example.txt
    Automatic merge failed; fix conflicts and then commit the result.
    """"""""""

2. Checking the File: If you open `example.txt`, you will see Git has marked the conflicting lines like the below:

    """""""
    This is line 1
    <<<<<<<<<<<<<<< HEAD
    This is the modified line 2 by Person A
    ===============
    This is a completely different line 2 by Person B
    >>>>>>>>>>>>>>> 0eacc02c74d62b8535793c6af68f264bded15c05
    This is line 3
    """""""

- <<<<<<<<<<<<<< HEAD marks the beginning of Person A's changes.
- ============== marks the seperation between conflicting changes.
- >>>>>>>>>>>>>> 0eacc02c74d62b8535793c6 (commit_hash) marks the end of Person B's changes

3. Resolving the conflict: To resolve this conflict, Person B needs to manually edit the file to choose which changes to keep;

    `This is line 1`
    `This is the modified line 2 by Person A`
    `This is line 3`

4. Adding and Commiting: After resolving the conflict as shown above, Person B needs to add the file and commit the changes;

    `git add example.txt`
    `git commit -m "Resolved conflict by keeping Person A's changes"`

5. Pushing the Resolution: Finally, Person B can push the resolved changes to the remote repository (Github) by using the git command below;
    
    `git push origin main`

<!-- Now, we will proceed to demonstrating what we have learned about Git conflicts. -->