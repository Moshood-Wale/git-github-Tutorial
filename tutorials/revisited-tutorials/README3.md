# Git Tags

## Overview
Git tags are pointers to specific commits in a Git repository's history. 
They are often used to mark important milestones such as releases, versions, or significant points in development. Proper management of Git tags is crucial for organizing and identifying versions of a project. 

Let's delve into the details of Git tag management.

## Creating Tags
There are two main types of tags in Git namely the lightweight tag and annotated tag.

1. Lightweight Tags:
    - Lightweight tags are simple pointers to a specific commit.
    - They are created using the git command below;
        
        `git tag <tag_name>`
        
        Example: `git tag v1.0`

2. Annotated Tags:
    - Annotated tags are more detailed and include extra information such as the tagger's name, email, date, and a message.
    - They are created using the git command below;

        `git tag -a <tag_name> -m "tag message"`
        
        Example: `git tag -a v1.0 -m ""Release version 1.0`


## Listing Tags
To list the tags in a repository, you can use the git command below;

    `git tag`

    This Git command will display a list of tags.


## Viewing Tag Getails
To view details of a specific tag, you can use the git command below:

    `git show <tag_name>`

This will display the tag information, including the commit it points to and any tag message.


## Tagging a Specific Commit
By default, if you run `git tag <tag_name>`without specifying a commit, Git will tag the current commit.
However, you can tag a specifc commit by providing its hash;

    `git tag <tag_name> <commit_hash>`
        
    Example: `git tag v1.0 8bde80508093bbe19e89f815ec0211c1947e3998`


## Pushing Tags
Tags are not automatically pushed to a remote repository when you psuh changes.
To push tags, you can use:

    `git push origin <tag_name>`

To push all tags:

    `git push origin --tags`

This will push the tags to the remote repository.


## Deleting Tags
To delete a tag, you use -d option:

    `git tag -d <tag_name>`

To delete a tag on a remote repository:

    `git push origin --delete <tag_name>`


### Best Practices for Tag Management

1. Semantic Versioning: Follow a clear versioning scheme like `Semantic Versioning` (SemVer) to manage tags for releases.

2. Consistent Tagging: Maintain consistencyin tagging practices accross the project to ensure clarity easy reference.

3. Release Notes: When creating annotated tags, include meaningful release notes or descriptions to provide context for each tag.

4. Tag Signing: For added security, consider signing tags with GPG. This verifies the authenticity of the tag and the person who created it.

5. Tag Cleanup: Periodically review and clean up old or unnecessary tags to avoid clutter. Git doesn't automatically remove tags when a branch is deleted, so manual cleanup may be necessary.

6. Tagging Workflow: Establish a tagging workflow within your team. Decide when and how tags are crreated, who has permission to create them, and how they are managed.

<!-- We will now go ahead to demonstrate what we have learned about Git Tags -->