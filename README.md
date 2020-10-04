# Ugit - Learning Git
Learning how to use git by recreating git. 
tutorial is followed from [Ugit Tutorial](https://www.leshenko.net/p/ugit/)
:smiley: 💨


## Table of contents
* [General info](#General-info)
* [Technologies](#Technologies)
* [Setup](#Setup)
## General info
this project is used to recreate git features and implement them to learn how git works.

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
[Git Walkthrough](https://learngitbranching.js.org/)

git init - To initialize git in folder

git clone [github repo]

git add [. / or folder/ or filename/ or ]

git commit -m 'message' - This is to add changes locally

git push and git pull - Push and pull remote repo
 
git status - Shows what changes have been made

git log or gitk - Shows info
---------------Branches-----------------------
git checkout -b [branch name] - This is the same as Git Branch [branch name], then Git checkout [branch name] 
git checkout [commit or HEAD^ or tag] - This detaches head

git merge [branch name] - Use merge branch [branch name], run it in master branch

git rebase master - If we are in [branch name] this puts it on top of master linearly.
git rebase [branch name] - Run in master

moving upwards one commit, then two ^,^^
moving upwards 3 commits ~3
Example: git checkout HEAD or [branch name]^

git branch -f master HEAD~2 - This force moves the master branch to 2 commits ago.