# Gitignore Management

## What is the .gitignore file??

## Overview
The .gitignore file is used to specify intentionally untracked files that Git should ignore.
This is especially important for excluding files generated during the development process, build artifacts, temporary files, and sensitive information like API keys or passwords.

Below is a detailed guide on how to configure the .gitignore file;

## Basic Rules:
1. Each line in a .gitignore file specifies a pattern for files or directories to ignore.
2. You can use wildcard characters (*, ?, []) to match patterns.
3. Lines starting with # are comments
4. Trailing slashes / indicate directories.
5. Negation ! can be used to unignore files that match pattern.

## Examples of Patterns:
- *.txt - ignores all files with the .txt extension.
- logs/ - ignores the entire logs directory.
- config.ini - ignores a specific file named config.ini.
- build/* - ignores all files and directorieswithin the build directory.
- !important.txt - Unignores important.txt if it was previously ignored.

## Usage Examples:
1. Ignore files by extension:

Plaintext
``````````````
# Ignore all .log files 
*.log

# Ignore all .pdf files
*.pdf

# Ignore all the zip files
*.zip
````````````````

2. Ignore Directories:

Plaintext
```````````````````````
# Ignore the entire "build" directory
build/

# Ignore the entire "log" directory
logs/

# Ignore the entire "pycache" directory
pycache/
````````````````````````````

3. Ignore specific files 

Plaintext
`````````````````````
# Ignore a specific file
config.ini

# Ignore compiled binary
my_program.exe
```````````````````````````

4. Ignore System Files

Plaintext
`````````````````````````
# macOS system files
.DS_Store

# Thumnails created by Windows
Thumbs.db
```````````````````````````

5. Ignore Dependency Directories

Plaintext
```````````````````
# Node.js modules
node_modules/

# Python virtual environment
venv/
```````````````````````````


## Global .gitignore:
You can set up a global .gitignore file that applies to all repositories on your system. 
This is useful for excluding common files and directories you never want to track.

Follow the steps below;

1. Create a global .gitignore file: Enter the command below in your command prompt. 

Bash
`````````````````````````````````````````````````````````
git config --global core.excludesfile ~/.gitignore_global
`````````````````````````````````````````````````````````
The purpose of the command above is to specify a global .gitignore file that Git will use for all repositories on your system. When you set a global .gitignore file, Git will apply the specified ignore patterns to every repository, ensuring consistency in what files and directories are ignored across all projects.

### Breakdown of the command:

- git config: This is the Git command used to get and set repository or global options.
- --global: This flag tells Git to set the configuration globally, applying it to all repositories on your system.
- core.excludesfile: This is the specific configuration option we are setting. It defines the path to the global .gitignore file.
- ~/.gitignore_global: This is the path to the global .gitignore file. The ~ is a shortcut to the user's home directory. So ~/.gitignore_global represents the .gitignore_global file located in the user's home directory.

2. Add patterns to ~/.gitignore_global:

Plaintext
````````````````````````````````````````
# macOS system files
.DS_Store

# Editor-specific files
.idea/
.vscode/

# Compiled binaries
*.exe
````````````````````````````````````````

## Ignoring Changes to Tracked Files:

If you have already committed a file but want to ignore further changes to it, you can use the `assume-unchanged` flag. This can be useful for configuration files that you modify locally but don't want to commit changes to.

Bash
````````````````````````````````````````
# To ignore changes to a file
git update-index --asume-unchanged path/to/file

# To start tracking changes again
git update-index --no-asume-unchanged path/to/file
````````````````````````````````````````

## Global .gitignore vs Local .gitignore:

- Global .gitignore: Used for patterns that apply to all repositories on your system.
- Local .gitignore: Specific to a single repository. Patterns here are not shared across different repositories.

<!-- Kindly note that we are working with a local .gitignore file in this repository. -->

## Example .gitignore file:

Here is an example of a comprehensive .gitignore file for a Node.js project:

Plaintext
`````````````````````````````````````
# Dependency directories
node_modules/
packages/*/node_modules/

# Logs
logs/
*.log

# Build output
dist/
build/

# Environmental variables
.env

# macOS system files
.DS_Store

# Editor-specific files
.idea/
.vscode/

# Ignore specific files
config.ini
`````````````````````````````````````

## How to use locally

1. Create a file named .gitignore in the root of your Git repository.
2. Add the patterns you want to ignore.
3. Save and commit the .gitignore file.

Bash
````````````````````````````
git add .gitignore
git commit -m "Add .gitignore"
````````````````````````````

## Conclusion

Properly configuring .gitignore helps keep your repository clean, reduces clutter, and avoids accidentally committing sensitive or unnecessaryfiles. It's essential for maintaining a focused version-controlled project.Tailor your .gitignore based on the project's needs, and remember to commit and share it with your team members to ensure consistency across all contributors.

<!-- I will quicky show you the .gitignore file we are working with in this project.  -->