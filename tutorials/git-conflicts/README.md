<!-- Let's take a look at Git conflicts in depth. You would have realised by now that most often than not we run into git conflicts either expectedly or not.  Having an hands-on knowledge about git conflicts is very important in the day to day activities of a Git and Github user.-->

# Git Conflicts

## Overview
In Git, conflicts occur when two or more people make changes to the same file or lines in a file, and Git is unable to automatically merge the changes. When this happens, Git marks the file as havimg a conflict and asks the user to resolve it manually.

A Git Conflicts scenario:
Let's say we have a simple repository with a file called `example.txt` . Here is what happens below;

1. Initial File Contents:
        `This is line 1`
        `This is line 2`
        `This is line 3`

2. Person A's Changes: Person A makes a change to example.txt;
        `This is line 1`
        `This is the modifed line 2 by Person A`
        `This is line 3`

3. Person B's Change: At the same time Person B makes a different change to example.txt;
        `This is line 1`
        `This is a completely different line 2 by Person B`
        `This is line 3`

Creating a Conflict
Now, let's see what happens when both Person A and B try to push their changes to the remote repository.

1. Person A commits and pushes his changes:
    `git add example.txt`
    `git commit -m "Person A's change."`
    `git push origin main`

2. Person B commits and Pushes:
    `git add example.txt`
    `git commit -m "git commit -m Person B's change"`
    `git push origin main`

Resolving the Conflict
Person B's push will fail because their local branch is not up-to-date with the changes on the remote repository. They need to pull the changes from the remote repository first;

1. Person B Pulls changes:
        `git pull origin main`

    Git will try to automatically merge the changes. Since both Person A and Person B changed the same line, Git cannot automatically merge the files and will create a conflict. This is what Git will display in the console below;

        """""
        Auto-merging example.txt
        CONFLICT (content): Merge conflict in example.txt
        Automatic merge failed; fix conflicts and then commit the result.
        """""

2. Checking the File: If you open `example.txt`, you will see Git has marked the conflicting lines:

        """""
        This is line 1
        <<<<<<<< HEAD
        This is the modified line 2 by Persom A
        ========
        This is a completely different line 2 by Person B
        >>>>>>>> comit_hash 
        This is line 3
        """""
- <<<<<<<< HEAD marks the beginning of Person B's changes.
- ======== marks the seperation between conflicting changes.
- >>>>>>>> commit_hash marks the end of Person B's changes.

3. Resolving the Conflict: To resolve the conflict, Person B needs to manually edit the file to choose which    changes to keep.

    `This is line 1`
    `This is the modified line 2 by Person A`
    `This is line 3`

4. Adding and Commiting: After resolving the conflict, Person B needs to add the file and commit the changes.
    
    `git add example.txt`
    `git commit -m "Resolved conflict by keeping Person A's change"`
    
5. Pushing the Resolution: Finally, Person B can push the resolved changes to the remote repository.
    
    `git push origin main`

<!-- I don't think I need to demostrate Git conflict again with the examples I have provided above and Git's console output shown above as well.  -->

