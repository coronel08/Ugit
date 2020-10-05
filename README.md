# Ugit - Learning Git
Learning how to use git by recreating git. 
tutorial is followed from [Ugit Tutorial](https://www.leshenko.net/p/ugit/)
:smiley: 💨

Quick git overview
https://rogerdudler.github.io/git-guide/

## Table of contents
* [General info](#General-info)
* [Technologies](#Technologies)
* [Setup](#Setup)
## General info
This project is used to recreate git features and implement them to learn how git works.
Notes on the bottom on git walk through and basics

## Technologies
project is created with 
*python 3.6

## Setup
this project will run in terminal similar to how git runs
```
$ cd ../lorem
$ pip install
$ start
$ Ugit commit, ugit push etc.
```
### To-do list
- [x] Test
- [ ] Test2

# Git Basics
[Git Walk through](https://learngitbranching.js.org/)
```
git init - To initialize git in folder

git clone [github repo]

git add [.  or folder/ or filename]

git commit -m 'message' - This is to add changes locally

git push and git pull - Push and pull remote repo
 
git status - Shows what changes have been made

git log or gitk - Shows info

git describe [ref or master or branch] - Use to figure out where you are if using tags or branches
```
### Branches
```
git checkout -b [branch name] - This is the same as Git Branch [branch name], then Git checkout [branch name] 
git checkout [commit or HEAD^ or tag] - This detaches head

git merge [branch name] - Use merge branch [branch name], run it in master branch

git rebase master - If we are in [working branch name] this puts it on top of master linearly.
git rebase [branch name] - Run in master
git rebase [master] [branch name] - To rebase new branch into master

moving upwards one commit, then two ^,^^
moving upwards 3 commits ~3
Example: git checkout HEAD or [branch name]^

git branch -f master [HEAD~2 or tag or commit] - This force moves the master branch to 2 commits ago.
```
### Reversing changes in Git
```
git reset HEAD~1 - This reverts the branch backwards as if the commit never happened, Works for local branches

git revert [branch name or tag ] - This creates a new commit with old info under last commit. Use for remote branch
```
#### Advanced feature, selecting commits
```
git cherry-pick [commit names] - This copies the commits into master
Example: git checkout master   - Change into master branch from working branch
Example: git cherry-pick [commit] - Gets only that commit

git rebase -i HEAD~3 - This opens an interactive cherry picking gui
Example: git rebase -i HEAD~3     - This gives the option to include what commits run on working branch
Example: git branch -f master [tag or commit]   - This forces master branch to a commit 
```

### 4.1 Grabbing Just 1 Commit
```
git checkout master;
git cherry-pick C4;
or
git rebase -i master;
git branch -f master c4;
```

### 4.2 Juggling Commits
```
git rebase -i HEAD^^;
git checkout newImage;
git rebase caption;
git commit --amend
git rebase -i HEAD^^
git checkout caption
git rebase newImage
git branch -f master c3'';
```

### 4.3 Juggling Commits #2
```
git checkout master
git cherry-pick c2
git commit --amend
git cherry-pick c3
```

### 5.1 Rebasing over 9000
```
git rebase master bugfix
git rebase bugFix side
git rebase side another
git rebase another master
```