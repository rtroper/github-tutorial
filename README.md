# github-tutorial
This is a basic tutorial showing how to use GitHub. The tutorial assumes you are using Windows. If you wish to run the Python examples, you will need to have a Python distribution installed on your machine. You can install from [python.org](https://www.python.org/downloads/) or one of the common Python distributions (e.g. [Miniconda or Anaconda](https://docs.conda.io/projects/continuumio-conda/en/latest/user-guide/install/windows.html)).

## Install Git and Clone the Repo
Start by installing Git for Windows from the following location: [https://git-scm.com/downloads](https://git-scm.com/downloads). Once installed, launch Git Bash, `cd` into a folder location of your choice (e.g. `/c/Dev/tutorials`) and clone the tutorial repo:

`git clone https://github.com/rtroper/github-tutorial`

This will clone the repo into a folder named `github-tutorial`. If you want to clone the contents of the repo directly into the folder you have created, run the command above with a space and `.` at the end:

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

Now, we see that these two files are staged, meaning that they will be committed to the local repo when we run `git commit` (any new or modified files that are unstaged will *not* be committed to the repo).

![git add](/images/git-add.png)

As a final step, now, let's commit these two new files to the local repo by running `git commit`. When we do so, our currently-configured editor will open and we will be prompted to enter a commit message. 

![enter commit message](/images/enter-commit-message.png)

Type your commit message *above* the lines that start with `#` (all lines beginning with `#` will be ignored). On the first line, provide a succinct one-line description or title for the commit. Press `Enter` and provide a summary of changes underneath the title line. You should follow [commit message guidelines](https://git-scm.com/book/en/v2/Distributed-Git-Contributing-to-a-Project#_commit_guidelines), which include the following:
* Limit the title to about 50 characters or less
* Limit subsequent lines to about 72 characters or less (adding carriage returns as needed)
Once you save and close the commit message, you should see a message in the Git Bash console indicating that the files were successfully committed.

![git commit success](/images/git-commit-success.png)

Run `git status` and you will see that there is one more step to update the origin GitHub repo with these changes.

![git status after commit](/images/git-status-after-commit.png)

As noted previously, a commit only updates our local repo (on our machine). These local changes then need to be pushed to the origin repo by running `git push`. After a successful push, the result of running `git status` again indicates that our local repo is up to date with the origin repo in GitHub.

![git push](/images/git-push.png)

If we now go to the repo in GitHub, we can see the new images folder that we just pushed.

![repo updated with images](/images/repo-updated-with-images.png)

If we click on the 'commits' link (in the upper-left of the screenshot above) we can see a list of all commits to the repo, including our latest, entitled *Add tutorial images*.

![commits list](/images/commits-list.png)

Clicking on the link for our latest change, we see the full commit message and a listing of file changes.

