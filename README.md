# Contents

* [Install Git and Clone the Repo](#install-git-and-clone-the-repo)
* [Commit a File to the Local Repo](#commit-a-file-to-the-local-repo)
* [Push Local Changes to the GitHub Repo](#push-local-changes-to-the-github-repo)
* [Open a Pull Request](#open-a-pull-request)
  * [Pull Changes from GitHub to your Local Repo](#pull-changes-from-github-to-your-local-repo)
  * [Create a Local Development Branch](#create-a-local-development-branch)
  * [Push Your Development Branch to GitHub](#push-your-development-branch-to-github)
  * [Open a Pull Request in GitHub](#open-a-pull-request-in-github)
* [Merge a Pull Request](#merge-a-pull-request)

# github-tutorial
This is a basic tutorial showing how to use GitHub. The tutorial assumes you are using Windows. If you wish to run the Python examples, you will need to have a Python distribution installed on your machine. You can install from [python.org](https://www.python.org/downloads/) or one of the common Python distributions (e.g. [Miniconda or Anaconda](https://docs.conda.io/projects/continuumio-conda/en/latest/user-guide/install/windows.html)).

## Install Git and Clone the Repo
Start by installing Git for Windows from the following location: [https://git-scm.com/downloads](https://git-scm.com/downloads). Once installed, launch Git Bash, `cd` into a folder location of your choice (e.g. `/c/Dev/tutorials`) and clone the tutorial repo:

`git clone https://github.com/rtroper/github-tutorial`

This will clone the repo into a subfolder named `github-tutorial`. If you want to clone the contents of the repo directly into a subfolder you have created, `cd` into that subfolder and run the command above with a space and `.` at the end:

`git clone https://github.com/rtroper/github-tutorial .`

Once you `cd` into the folder containing the cloned repo files, you should see `(master)` to the right of your path location in the Git Bash console. This indicates that Git Bash has found a valid Git repo in that folder.

![newly cloned repo](/images/newly-cloned-repo.png)

## Commit a File to the Local Repo

You can always check for newly-added or modified files in your cloned (i.e. local) repo by typing `git status` and pressing Enter:

![git status](/images/git-status.png)

Importantly, what you see in the output are changes with respect to your local repo that exists on your machine. When you commit a change to the repo, you are only committing locally. In other words, *a commit makes no changes to the origin repo on GitHub*.

In the example above, note that there are untracked files in an `images/` folder. The new files within that folder (named '*newly-cloned-repo.png*' and '*git-status.png*') are not shown, because the `images/` folder does not yet exist in the local repo. Once the files are committed, the folder (and files) will exist in the local repo. Before committing, however, the files must first be staged (essentially flagged for commit) using `git add`:

`git add images/newly-cloned-repo.png`

and

`git add images/git-status.png`

Now, running `git status` again, we see that these two files are staged, meaning that they will be committed to the local repo when we run `git commit` (any new or modified files that are unstaged will *not* be committed to the repo).

![git add](/images/git-add.png)

As a final step, now, let's commit these two new files to the local repo by running `git commit`. When we do so, our currently-configured editor will open and we will be prompted to enter a commit message. 

![enter commit message](/images/enter-commit-message.png)

Type your commit message *above* the lines that start with `#` (all lines beginning with `#` will be ignored). On the first line, provide a succinct one-line description or title for the commit. Press `Enter` twice (to include an empty line) and provide a summary of changes underneath the title line. You should follow [commit message guidelines](https://git-scm.com/book/en/v2/Distributed-Git-Contributing-to-a-Project#_commit_guidelines), which include the following:
* Limit the title to about 50 characters or less
* Limit subsequent lines to about 72 characters or less (adding carriage returns as needed)

Once you save and close the commit message, the output in the Git Bash console should indicate that the files were successfully committed.

![git commit success](/images/git-commit-success.png)

Run `git status` and you will see that there is one more step to update the origin GitHub repo with these changes.

![git status after commit](/images/git-status-after-commit.png)

## Push Local Changes to the GitHub Repo

As noted previously, a commit only updates our local repo (on our machine). These local changes then need to be pushed to the origin repo by running `git push`. After a successful push, the result of running `git status` again indicates that our local repo is up to date with the origin repo in GitHub.

![git push](/images/git-push.png)

If we now go to the repo in GitHub, we can see the new `images` folder that we just pushed. Click on the `images` folder link to see the image files.

![repo updated with images](/images/repo-updated-with-images.png)

If we click on the 'commits' link (in the upper-left of the screenshot above) we can see a list of all commits to the repo, including our latest, entitled *Add tutorial images*.

![commits list](/images/commits-list.png)

Clicking on the `Add tutorial images` link for our latest changes, we see the full commit message and a listing of file changes.

## Open a Pull Request

When working on code development within a collaborative team environment, it is preferrable to make changes to the GitHub repo by means of pull requests. This involves the following steps:

* Pull the latest changes from the `origin/master` branch (on GitHub) to your local `master` branch
* Create a local development branch off of your local `master` branch
* Make one or more commits on your local development branch
* Push your development branch to the `origin` repo (on GitHub)
* Open a pull request in GitHub on your development branch

This workflow provides a way to make changes to a GitHub repo that:

* Allows collaborators to make changes to the same repo without pushing changes over the top of others' changes
* Allows collaborators to review each other's changes before merging the changes into the main branch (e.g. `master`)

The steps listed above are described in detail in the following sections.

### Pull Changes from GitHub to your Local Repo

In a team development environment, you will need to regularly check that your local repo is up-to-date with the `origin` repo on GitHub. To make sure that you have the latest changes that have been pushed by other team members, first run `git fetch` and then `git status`.

![git fetch](/images/git-fetch.png)

The `git fetch` will 'fetch' the latest changes from the `origin` repo on GitHub without actually merging those changes into your local repo. If there are changes in the `origin` repo that are not in your local repo, the output of `git status` will indicate that your branch is behind the `origin` repo. To pull these changes into your local repo, run `git pull`.

![git pull](/images/git-pull.png)

The resulting output in the Git Bash console will list new files or file modifications that have been merged from the `origin` repo into your local repo. In the example above, there have been changes made to the README.md file that were not in your local copy of that file.

### Create a Local Development Branch

To be able to open a pull request for others to review your proposed changes, you will need to work on a separate development branch from `master` (which is the default branch for any repo). To create a development branch named, say, `add-python-example` off of `master` and immediately check out (i.e. switch to) that branch, run the following:

`git checkout -b add-python-example`

The output in the Git Bash console should indicate that you have switched to the new branch. To the right of your folder path, you should see `(add-python-example)` indicating you are currently on the `add-python-example` branch. To see a list of local branches, use `git branch` (use the `-a` flag to see a list of all local *and* remote branches). Note that the branch currently checked out (`add-python-example`, in the current example) is indicated by an asterisk.

![git branch](/images/git-branch.png)

Now, every time you commit changes, they will be committed to this local development branch.

### Push Your Development Branch to GitHub

Once you have made one or more commits on your development branch and you feel that the feature you are working on is complete, it is time to push your branch to GitHub where you can open a pull request. To push our branch (`add-python-example`) to the `origin` repo, fun the following command:

`git push -u origin add-python-example`

The output below indicates that we have successfully pushed our development branch to the `origin` repo in GitHub. It also provides some instructions for opening a pull request, which will be described in the next section.

![git push branch](/images/git-push-branch.png)

### Open a Pull Request in GitHub

Once we have pushed a new development branch to the `origin` repo in GitHub, we can open a pull request for others to review before our changes are merged into the `master` branch. Start by visiting the repo GitHub page and selecting our new branch from the 'Branch' drop-list shown below.

![select branch in github](/images/select-branch-in-github.png)

Once the new branch is selected, click the '*New pull request*' button to the right of the 'Branch' button. Make sure there is a descriptive title and description for the pull request and then click the '*Create pull request*' button to the lower right.

![create pull request](/images/create-pull-request.png)

The newly-created pull request can be viewed by returning to the main GitHub repo page and clicking on the '*Pull requests*' tab toward the top. 

![view pull requests](/images/view-pull-requests.png)

To see details about the pull request, click on the pull request title (*Add simple calculator feature*, in this case).

## Merge a Pull Request

After a pull request has been submitted, it should be reviewed by one or more other individuals. If you are a reviewer, click on the '*Pull requests*' tab at the top of the GitHub repo main page, find the desired pull request and click on its title to open up details about the pull request.

![view a pull request](/images/view-a-pull-request.png)

To review commits for the pull request, click the '*Commits*' tab. Click on the title of any commit to see what files were changed (or added) and the exact changes to those files.

![view file changes](/images/view-file-changes.png)

Once changes have been reviewed and found acceptable, someone other than the creator of the pull request should merge it into the master branch. To do this, the reviewer should go to the main details page for the pull request and click the '*Merge pull request*' button (or click the down arrow immediately to the right of the button to select another merge option).

![merge pull request](/images/merge-pull-request.png)

Type a commit message or accept the default message and click '*Confirm merge*'.

![confirm merge](/images/confirm-merge.png)

