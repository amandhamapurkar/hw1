# Homework 1 &nbsp; <a href="/../../pull/1/checks"><img src="/../status/badges/score.svg?raw=true" alt="Latest score" align="right"/></a>

<!-- The above score badge (a) assumes clusterhack-classbot is configured on repos, and (b) relies on relative link to PRs that is *not* officially supported by GitHub -->

The purpose of this homework is to help you ensure that your tools for this class are set up correctly, and to familiarize you with the typical development workflow.

In this class we employ (somewhat simplified) best-practice development workflows, since this is an important real-world skill.

## Pre-requisites

1. A GitHub account (free).  If you are reading this, then you have already completed this step.
2. You must already have both Miniconda Python as well as Visual Studio Code installed and configured correctly on your machine.  We did this during the first two lectures.
3. In addition to those two tools, you will need to install Git. Please follow the [installation instructions](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) for your platform.

---

## Workflow summary

For every homework assignment, we will provide a complete project in the form of a GitHub repository.  Each student gets their own repository (which is for your own work, and which should be kept private).  Your assignment-specific repository is done when you click the invitation link and accept the assignment.

The outline of the development workflow (in general, for all programming assignment) is as follows:

1. Clone the assignment repository into a local copy and start working on the given problems/tasks.
2. Pick a task to work on.
   1. Make sure you understand the requirements. Plan your solution, and then write the necessary code.
   2. Always work incrementally!
   3. Once your code is in runnable shape (i.e., it has no syntax errors, or other issues that cause immediate failures), you should also run the provided unit tests on your machine.
   4. If one or more tests fail, examine the test inputs and outputs to understand what each failure was. Pick one of those and investigate.
   5. Once you have completed a unit of work, you should commit relevant code changes and then push them to GitHub. Each push will also trigger a continuous integration job, which will update your score.
   6. Keep repeating these steps, until you have solved all issues and the task is complete.
3. Pick another task, and repeat, until all tasks are completed.

> **Warning**
> You should **not** modify _any_ files _other_ than those required by the assignment!

### Current assignment

This starter assignment has only one task/problem (see below). Thus, specifically for this assignment, you should make changes _only_ to the `hello.py` file. Even though this is not (yet) automatically enforced, we will take snapshots of everyones' repositories immediately after the deadline, and verify this.

---

## Quick reference

You should first watch the walkthrough video on the assignment's page on Canvas.  Once you have watched and understood the steps, you can use this section as a quick reference.

### Getting started: clone repository from GitHub

1. If you already have a folder open in VSCode, then close it (<samp>File &rtrif; Close Folder</samp> menu), alternatively, open a new VSCode window (<samp>File &rtrif; New Window</samp> menu).
2. From either the <samp>Explorer</samp> or the <samp>Source Control</samp> panes, click on the <kbd><samp>Clone Repository</samp></kbd> button.
   * If those buttons are absent (or grayed out, etc), then you most likely havent installed Git on your machine (see above).
3. Select the <samp>Clone from GitHub</samp> option.
   * If you haven't already logged onto GitHub from VSCode, you will be redirected to a web browser to do so. After you authorize VSCode to access GitHub, you should be redirected back to VSCode.
4. Select (or type in) the name of your repository for your assignment. For this assignment, the name should be of the form <code>pybait/hw1-_username_</code> where <code>_username_</code> is your _GitHub_ username (_not_ your NetID).
5. Select a folder into which the new cloned repository will be created (as a sub-folder with name <code>hw1-_username_</code>).
6. When asked if you want to open the new folder (containing the cloned GitHub repository), accept.
7. Since this is the first time you are opening this new folder on your machine, don't forget to select Miniconda as your Python interpreter (via the <samp>Python: Select Interpreter</samp> command in the VSCode command pallette).

The cloned repository is a local copy that is linked to the remote copy.  When you work on the clone, all changes are kept local.  No changes will be sent back to the original repository (on GitHub) unless you _explicitly_ commit your changes **and** push those commited changes back to the remote origin (i.e., GitHub).  Both of those steps are necessary (commits are also local, and their purpose is to logically organize the work; only pushing one or more commits to the remote server will "upload" your changes).

> **Warning**
> Although there is a GitHub Classroom extension for VSCode, multiple recent issue reports suggest it may fail to properly list your accepted assignments.  Therefore, although YMMV, we do _**not**_ recommend using it.

<!-- 
The GitHub Classroom VSCode extension basically (i) filters the list of GitHub repositories to include only those associated with "classroom" assignments (vs.\ all), (ii) always clones in your home directory (vs.\ asking you to choose), (iii) combines the commit and push/sync steps into a single UI button, and (iv) shows you the outcome of the continuous integration checks in VSCode (vs.\ having to check through a web browser on GitHub).
-->

### Working on assignment locally

1. Once you've cloned the repository into a folder on your local machine, you can subsequently just open that folder as usual (e.g., either <samp>File &rtrif; Open Folder...</samp> menu or, if recent, then <samp>File &rtrif; Open Recent &rtrif; _folder-name_</samp> menu). You don't need to clone the GitHub repository again.
2. Make changes, running your code as you go. Don't forget to run unit tests localy, via the <samp>Testing</samp> pane in VSCode. This is explained separately in the video walkthrough, as well as during lectures.
3. Rinse and repeat, until you have a unit of work ready to upload.

### Uploading work: commit and push back to GitHub

1. Once you have completed a unit of work (e.g., part of the assignment), you should upload your current changes back to GitHub.  This will save your work and, also, automatically run pre-configured checks on your code (which will also determine your grade).
   > **Warning**
   > You can upload your work as often as you wish. In fact, you should do so whenever you have completed a part of the assignment, both as a form of backup, as well as to run all pre-configured checks on your code.

   The upload is a two-step process: commit (locally) then push (remotely).
2. First, from the <samp>Source Control</samp> pane in VSCode, you must select which files you want to commit.  This is called "_staging_". 
   1. If you want to commit all modified files, you can click on the <kbd>+</kbd> icon that appears when you mouse over the <samp>Changes</samp> section header. Alternatively, you can stage individual files by clicking on their corresponding <kbd>+</kbd> icon.  
   2. Once a file is staged for commit, it will move to the <samp>Staged Changes</samp> section. If you change your mind (before commiting), you can always click the `-` icon to unstage files.
   3. Although not strictly required, it is considered proper etiquette to enter a brief description of the commit in the <samp>Message</samp> input box (e.g., "Implemented Problem 1; passing all tests except ..." or "Fix test ... on Problem 1").
3. Click on the <kbd><samp>Commit</samp></kbd> button. This will commit all changes into your **local** copy of the repository.
4. Finally, you should "_push_" your commited changes to GitHub.
   * In VSCode, once the local repository contains changes that have not been uploaded, a <kbd><samp>Sync</samp></kbd> button will appear in the <samp>Source Control</samp> pane.
   * Alternatively, you can also click on the <kbd>&mldr;</kbd> icon that appears when you mouse over the <samp>Source Control</samp> section heading (to open the <samp>More Actions...</samp> menu) and select the <samp>Push</samp> menu item.

   > **Note**
   > Strictly speaking, the <kbd><samp>Sync</samp></kbd> button will, in general, do a _pull_, followed by a _push_ (as long as there are no merge conflicts during the _pull_). However, unless you have multiple local clones (which we strongly advise against, unless if you _really_ know what you are doing), this is not relevant.

### Continuous integration

1. Whenever you push any changes to GitHub (specifically, to the `main` branch of your repository), a "_continuous integration_" job will be triggered. This will run a number of pre-configured checks on your code (on a pre-configured virtual machine with Python), which determine your grade.

   > **Warning**
   > Your code *must* pass these checks (on GitHub), in order to receive credit.

   For this assignment, the checks consist of the same unit test that is given in the repository. However, in later assignments, additional checks may be used (which will only be available when you push your code).
2. Visit your repository's page on GitHub and go to the <samp>Actions</samp> section. You should see a list of all runs. Click on any of them to see details about it's execution and result.
   > **Note**
   > Your grade will depend only on the _latest_ run (which should correspond to the latest contents of your `main` branch on GitHub).

---

## Problems

### Problem 1: `hello.py`

Complete the code in `hello.py`, so it's output is always the text

```console
Hello, world!
```

Make sure your solution passes the provided unit test. Also, do not forget to commit and push your code to GitHub (so you can properly complete your first development workflow and, while at it, also receive a score).

> **Warning**
> Your grade will be determined _only_ by the outcome of the [classroom Github Action](https://docs.github.com/en/education/manage-coursework-with-github-classroom/learn-with-github-classroom/view-autograding-results).

## Correctness

Code is "correct" when it does _exactly_ (no less, but also no more) what specified requirements state, _provided_ all specified pre-conditions (if any) hold.

It is important that you learn to read specifications critically. For example, in this case, these are some things that the problem specifications above tell you:

* The program filename should be `hello.py` and it should be at the top level of the repository (we have already created an empty file for you, in the correct folder and with the correct name).
* Your simple program **should** output the same text, _always_. Remember that two text strings are equal when they have exactly the same characters (including punctuation, spaces, newlines, etc.).  
* Your code **should not** do anything else (e.g., wait for user input, output additional text, etc).

Similarly, when you communicate with others in a software project, you should also strive to be as precise as possible.

The unit tests are designed so that, _if_ your code is correct, _then_ all the tests should successfully run to completion (i.e., "pass").  Most software projects today employ unit tests (in addition to other automated checks), and any contributions (aka. "_pull requests_") to a project are required to pass those checks before they can be incorporated (aka. "_merged_") into the project.

---

## <kbd>FYI</kbd> Additional resources (self-learning)

### Learn more about Git and GitHub

In this class we will use only a small subset of Git's and GitHub's features (e.g., we will _not_ be using branches, forks, or pull requests). 

> **Warning**
> Although often confused, Git and GitHub are _not_ the same.

Git is a protocol and open-source software for organizing, managing, and sharing contributions to software projects. Git was originally written by Linus Torvalds, to help manage Linux kernel development. It is used almost universally for software development today, usually through one of a [number of hosting platforms and services](https://en.wikipedia.org/wiki/Comparison_of_source-code-hosting_facilities). GitHub is a commercial hosting service for Git repositories (as well as a number of other tools). GitHub is currently owned by Microsoft and it has by far the largest user base (as well as market share) among software development hosting platforms.

However, for those of you that may want to learn a bit more about Git and GitHub, a good starting point is the [GitHub starter course](https://github.com/education/github-starter-course).

> **Note**
> If you want to experiment with Git/GitHub features on your own, please do not use the homework assignment repository.

Instead, we would recommend copying the [`github-starter-course` repository](https://github.com/education/github-starter-course) into your own account and use that for any personal experiments.  If you are logged into GitHub, the simplest way to make a private, personal copy is via the "Use this template" button (this is somewhat similar to "_cloning_" the repository, except "use template" copies _just_ the latest version of the files, _without_ the commit history).

Finally, for those that already have some experience with programming and the command line, the [Git book](https://git-scm.com/book/en/v2) is an excellent resource.

### Devcontainers and GitHub Codespaces

As an alternative to a manually configured local environment, you can also use a pre-configured _development container_. You can think of a _container_ as a lightweight virtual machine.
TODO - Benefits

[`devcontainer`](https://containers.dev/) is a standard format for automating the installation and configuration of virtual machine images.  These virtual machines can be hosted either locally (i.e., on your machine), or remotely (e.g., on Azure virtual machines, via GitHub Codespaces). All homework project repositories in this class are set up with a devcontainer specification.

Github Codespaces 
TODO

#### Remotely-hosted devcontainers (Github Codespaces)

##### Additional pre-requisites

1. [GitHub student developer pack](https://education.github.com/pack), which is free with student status verification, and gives you 180 free hours per month for [GitHub Codespaces](https://github.com/features/codespaces) ([docs](https://docs.github.com/en/codespaces/overview)), among several other benefits.
2. [Optional] Github Codespaces VSCode extension:

#### Locally-hosted devcontainers


##### Additional pre-requisite

1. [Docker Desktop](https://www.docker.com/products/docker-desktop/)
2. Remote Containers VSCode extension.

Please follow [setup instructions](https://code.visualstudio.com/docs/setup/setup-overview).


