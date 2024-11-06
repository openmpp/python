# **PyOpenMPP**

Python implementation of OpenM++ via API calls to web service. Currently is tested primarily with PohemX model. 

Run by specifying options in config.ini file at root, then running PohemX-python.py. This can be built into an executable which can also work off of the config.ini file. 

Functions folder modularizes the different API calls to OpenM++ web service. These are applied and tested in PyOpenMPP_main.py.


## <b>Modules</b>

### *<ins>Create Model Run</ins> - Functions/Create.py/create_model_run()*
#### Description:
This method takes information and then creates/executes a model run in your running instance of OpenM++ (via the oms process; the OpenM++ Web Service).
#### API Calls:
- [ ] Submit model run job: **POST** ```<oms_url>/api/run```
- [ ] Retrieve status of model run: **GET** ```<oms_url>/api/model/<model_digest>/run/status/last```
#### Parameters: 
- [ ] ```model_digest``` specifies what model to run since model_digest is basically a unique ID that each model has. For example, if you were running PohemX, model_digest would correspond to PohemX specifically.
- [ ] ```simulation_cases``` specifies the number of 'actors' to be simulated. The create_model_run function will set this to 1e5 by default, but will be overwritten by whatever is set in the config.ini file at runtime.
- [ ] ```tables``` specifies which output tables to return in the output. The create_model_run function will set this to an empty list by default, but will be overwritten by whatever is set in the config.ini file at runtime.
- [ ] ```threads``` specifies how many threads to run this model with. The create_model_run function will set this to 1 by default, but will be overwritten by whatever is set in the config.ini file at runtime. 
- [ ] ```sub_samples``` specifies how many samples of the start population to run, which then gets aggregated at the end. Essentially, it specifies how many times you want the model to run. More times will eat up more memory and space but return a more accurate simulation. 
#### Output: 
Returns ```model_run_status``` variable, which specifies the state of the model run after it finishes running server-side. 

---
### *<ins>Load Model Run</ins> - Functions/Load.py/load_model_run()*
#### Description: 
Retrieve specific model run based on model_name and model_digest. Requires model_run_status from Create_model_run.py.
#### API Calls:
API calls done via get_model_runs method and load_output_table method.
#### Parameters: 
#### Output: 
Returns model run object with all info about a finished model run (presumably) packed together nicely.
To-do: create a get_model_run_status function in case user wants to load a previous model run where you don't have the status because it was run a long time ago. 

---
### *<ins>Get Models</ins> - Functions/Get.py/get_models()*
#### Description:
This module retrieves all models accessible in your running instance of OpenM++.
#### API Calls:
- [ ] Retrieve list of models: **GET** ```<oms_url>/api/model-list```
#### Parameters:
- [ ] ```oms_url``` specifies the URL that your running instance of OpenM++ is sending information to. For example, ```http://localhost:4040```.
#### Output:
Returns a Pandas dataframe of models list.

---

### *<ins>Load Output Table</ins> - Functions/Load.py/load_output_table()*
#### Description: 
#### Parameters: 
#### Output: 

---






## <b>Building Executable File</b>
Use pyinstaller to build PohemX-python.py into an executable file.

```pyinstaller --onefile PohemX-python.py --hidden-import openpyxl --hidden-import configparser```

- [ ] ```--onefile``` packages the dependencies in with the executable. 
- [ ] ```PohemX-python.py``` specifies the Python file to create an executable version of. 
- [ ] ```--hidden-import``` specifies to package a dependency that isn't already in pyinstaller's list of recognized imports. This is done for openpyxl and configparser.

**Note:** The executable file will only work if config.ini is in the same directory, and if you update your OpenM++ path in config.ini.


## <b>Creating a Virtual Environment</b>
Necessary if you want to cleanly contain this project's Python dependencies during development. Instructions pulled from [here](https://python.land/virtual-environments/virtualenv). 

venv is included in Python by default, so go to command line`or PowerShell, and cd to where you'd like to create your virtual environment directory. Then, enter the following:
```python -m venv <directory>```

Once created, cd into the directory you've created, and enter the following:
```
# In cmd.exe
venv\Scripts\activate.bat
# In PowerShell
venv\Scripts\Activate.ps1
```

Now you've successfully created your virtual environment. You can install packages while this is activated so that these packages won't messily take up space outside of this directory. 

If you'd like to exit your virtual environment, enter the following:
```deactivate```

**Note:** Once you activate your virtual environment, you must turn it on again in any window you use to run your program, or in any window you use to install more packages (assuming these are packages you want to be in this virtual environment). 





## Getting started

To make it easy for you to get started with GitLab, here's a list of recommended next steps.

Already a pro? Just edit this README.md and make it your own. Want to make it easy? [Use the template at the bottom](#editing-this-readme)!

## Add your files

- [ ] [Create](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#create-a-file) or [upload](https://docs.gitlab.com/ee/user/project/repository/web_editor.html#upload-a-file) files
- [ ] [Add files using the command line](https://docs.gitlab.com/ee/gitlab-basics/add-file.html#add-a-file-using-the-command-line) or push an existing Git repository with the following command:

```
cd existing_repo
git remote add origin https://gitlab.k8s.cloud.statcan.ca/scott.ho/pohem-python-use.git
git branch -M main
git push -uf origin main
```

## Integrate with your tools

- [ ] [Set up project integrations](https://gitlab.k8s.cloud.statcan.ca/scott.ho/pohem-python-use/-/settings/integrations)

## Collaborate with your team

- [ ] [Invite team members and collaborators](https://docs.gitlab.com/ee/user/project/members/)
- [ ] [Create a new merge request](https://docs.gitlab.com/ee/user/project/merge_requests/creating_merge_requests.html)
- [ ] [Automatically close issues from merge requests](https://docs.gitlab.com/ee/user/project/issues/managing_issues.html#closing-issues-automatically)
- [ ] [Enable merge request approvals](https://docs.gitlab.com/ee/user/project/merge_requests/approvals/)
- [ ] [Set auto-merge](https://docs.gitlab.com/ee/user/project/merge_requests/merge_when_pipeline_succeeds.html)

## Test and Deploy

Use the built-in continuous integration in GitLab.

- [ ] [Get started with GitLab CI/CD](https://docs.gitlab.com/ee/ci/quick_start/index.html)
- [ ] [Analyze your code for known vulnerabilities with Static Application Security Testing (SAST)](https://docs.gitlab.com/ee/user/application_security/sast/)
- [ ] [Deploy to Kubernetes, Amazon EC2, or Amazon ECS using Auto Deploy](https://docs.gitlab.com/ee/topics/autodevops/requirements.html)
- [ ] [Use pull-based deployments for improved Kubernetes management](https://docs.gitlab.com/ee/user/clusters/agent/)
- [ ] [Set up protected environments](https://docs.gitlab.com/ee/ci/environments/protected_environments.html)

***

# Editing this README

When you're ready to make this README your own, just edit this file and use the handy template below (or feel free to structure it however you want - this is just a starting point!). Thanks to [makeareadme.com](https://www.makeareadme.com/) for this template.

## Suggestions for a good README

Every project is different, so consider which of these sections apply to yours. The sections used in the template are suggestions for most open source projects. Also keep in mind that while a README can be too long and detailed, too long is better than too short. If you think your README is too long, consider utilizing another form of documentation rather than cutting out information.

## Name
Choose a self-explaining name for your project.

## Description
Let people know what your project can do specifically. Provide context and add a link to any reference visitors might be unfamiliar with. A list of Features or a Background subsection can also be added here. If there are alternatives to your project, this is a good place to list differentiating factors.

## Badges
On some READMEs, you may see small images that convey metadata, such as whether or not all the tests are passing for the project. You can use Shields to add some to your README. Many services also have instructions for adding a badge.

## Visuals
Depending on what you are making, it can be a good idea to include screenshots or even a video (you'll frequently see GIFs rather than actual videos). Tools like ttygif can help, but check out Asciinema for a more sophisticated method.

## Installation
Within a particular ecosystem, there may be a common way of installing things, such as using Yarn, NuGet, or Homebrew. However, consider the possibility that whoever is reading your README is a novice and would like more guidance. Listing specific steps helps remove ambiguity and gets people to using your project as quickly as possible. If it only runs in a specific context like a particular programming language version or operating system or has dependencies that have to be installed manually, also add a Requirements subsection.

## Usage
Use examples liberally, and show the expected output if you can. It's helpful to have inline the smallest example of usage that you can demonstrate, while providing links to more sophisticated examples if they are too long to reasonably include in the README.

## Support
Tell people where they can go to for help. It can be any combination of an issue tracker, a chat room, an email address, etc.

## Roadmap
If you have ideas for releases in the future, it is a good idea to list them in the README.

## Contributing
State if you are open to contributions and what your requirements are for accepting them.

For people who want to make changes to your project, it's helpful to have some documentation on how to get started. Perhaps there is a script that they should run or some environment variables that they need to set. Make these steps explicit. These instructions could also be useful to your future self.

You can also document commands to lint the code or run tests. These steps help to ensure high code quality and reduce the likelihood that the changes inadvertently break something. Having instructions for running tests is especially helpful if it requires external setup, such as starting a Selenium server for testing in a browser.

## Authors and acknowledgment
Show your appreciation to those who have contributed to the project.

## License
For open source projects, say how it is licensed.

## Project status
If you have run out of energy or time for your project, put a note at the top of the README saying that development has slowed down or stopped completely. Someone may choose to fork your project or volunteer to step in as a maintainer or owner, allowing your project to keep going. You can also make an explicit request for maintainers.
