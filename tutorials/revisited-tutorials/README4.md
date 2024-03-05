# Git Conflicts

Let's talk about what conflicts are in Git and Github. So far, we have encountered a couple of git conflicts either remotely on Github or locally on our machine (Git). So let's look at what conflicts are in Git and Github.

## Overview
In Git, conflicts occur when two or more people make changes to the same file or lines in a file, and Git is unable to automatically merge the changes. When this happens, Git marks the file as having a conflict and asks the user to resolve it manually.

To further broaden our knowledge on Git conflicts, let's simulate a typical Git conflict situation;
Let's say we have a simple repository with a file called `example.txt`.
Here is how it unfolds below;

1. Initial file contents:
    """""""""""""""""""
    This is line 1
    This is line 2
    This is line 3
    """""""""""""""""""

2. Person A's changes: Person A makes a change to example.txt file locally;
    """""""""""""""""""
    This is line 1
    This is the modified line 2 by Person A
    This is line 3
    """""""""""""""""""

3. Person B's changes: At the same time, Person B makes a different change to the example.txt file locally;
    """""""""""""""""""
    This is line 1
    This is a completely differnt line 2 by Person B
    This is line 3
    """""""""""""""""""

### Creating a Conflict
Now, let's see what happens when both Person A and B try to push their changes to the remote repository (Github):

1. Person A commits and pushes his changes by using the commands below consequtively:
    """""""""""""""""""""
    git add example.txt
    git commit -m "Person A's changes
    git push origin main
    """""""""""""""""""""

2. Person B commits and pushes changes:
    """"""""""""""""""""
    git add example.txt
    git commit -m "Person B's changes.
    git push origin main
    """"""""""""""""""""

### Resolving the conflicts:
Person B's push will fail beacuse their local branch is not-up-to-data with the changes in the remote repository. Let's pull the changes from the remote reposi;tory first:

1. Person B pulls the changes from Github with the commands below:
    `git pull origin main`

  Git will try to authomatically merge the changes. Since Both Person A and Person B changed the same line. Git cannot automatically merge the files and will create a conflict. This is what Git will display in the console terminal below;

  """"""""""""""""""""""
  Auto-merging example.txt
  CONFLICT (content): Merge conflict in example.txt
  Rutomatic merge failed: fix conflicts and then commit the result. 
  """"""""""""""""""""""

2. Checking the file: if you open example.tct, you will see Git has marked the conflicting lines like the below:

  """"""""""""""""""""""
  This is line 1
  <<<<<<<<<<<<<<<<<< HEAD
  This is the modified line 2 by Person A
  ==================
  This is a completely different line 2 by Person B
  >>>>>>>>>>>>>>>>>> e205e06b5512ea725582b7bb427a1ab246c1b098
  This is line 3
  """"""""""""""""""""""

  - <<<<<<<<<<<<<<<<<<< HEAD marks the beginning of Person A's changes.
  - =================== marks the seperation between conflicting changes.
  - >>>>>>>>>>>>>>>>>>> e205e06b5512ea725582b7bb427a1ab246c1b098 (commit_hash) marks the end of Person B's changes.

3. Resolving the conflict: To resolve this conflict, Person B needs to manually edit the file to choosewhich changes to keep:

    """"""""""""""""""""
    This is line 1
    This is the modified line 2 by Person A
    This is line 3
    """"""""""""""""""""

4. Adding and Commiting: After resolving the conflict as shown above, Person B needs to add the file and commit the changes;

    """"""""""""""""""""
    git add example.txt
    git commit -m "Resolved Conflict by keeping Person A's changes"
    """"""""""""""""""""

5. Pushing the Resolution: Finally, Person B can push the resolved changes to the remote repository (Github) by using the git command below;

    """""""""""""""""""""
    git push origin main
    """""""""""""""""""""

<!-- We will proceed to demonstrating what we have learned about Git conflicts. -->
<!-- We will create and resolve Git conflicts both locally on our machine and remotely on Github. -->