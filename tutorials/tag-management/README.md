# Git Tags

Git tags are pointers to specific commits in a Git repository's history. They are often used to mark important milestones such as releases, versions, or significant points in development. Proper management of Git tags is crucial for organizing and identifying versions of a project. Let's dive into the details of Git tag management.

## Creating Tags

There are two main types of tags in Git:
1. Lightweight Tags
2. Annotated Tags

### Lighweight Tags:
- Lightweight tags are simple pointers to a specific commit.
- They are created using:
            `git tag <tag_name>`
        Example: 
            `git tag v1.0`

### Annotated Tags:
- Annotated tags are more detailed and include extra information such as the tagger's name, email, date, and a message.
- They are created using:
            git tag -a <tag_name> -m "tag message"
        Example:
            git tag -a v1.0 -m "Release version 1.0"


<!-- Hello, I'm trying to make chnges in this branch so that I will be able to synchronize these changes with the required beranch. -->
<!-- This is all the new changes I will like to add to this branch for now. -->