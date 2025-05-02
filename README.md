# tester
A bunch of Github Actions examples I created as I was learning about what can be done with Github Actions.

# Setup
  - Get the utility _act_
    - utility that lets you run actions locally.
    - https://github.com/nektos/act
  - _GitHub Local Actions_ VSCode Extension.
    - optional
    - great way to run Actions locally... esp. useful when writing Actions
    - easiest way to (compared to the _act_ CLI):
      - specify inputs for local Action runs.
      - Run a specific Workflow or Job rather then simulating a Github event which could trigger several workflows in this repo.
  - Get the Github command-line tool _gh_
    - https://cli.github.com/
  - To run a Github Actions workflow locally for the command line
    - ```act EVENT-TYPE```
      - where _EVENT-TYPE_ is the event_name
        - examples: ```workflow_dispatch``` or ```push```
        - if _EVENT-TYPE_ is not specified, it defaults to ```push```
      - triggers and run all workflows (.YAML files) defined in _.github/workflows_ that are triggered on events of type _EVENT-TYPE_
    - ```act EVENT-TYPE -W '.github/workflows/YAML-FILENAME' ```
      - where _EVENT-TYPE_ is the event_name
        - examples: ```workflow_dispatch``` or ```push```
        - if _EVENT-TYPE_ is not specified, it defaults to ```push```
      - will run just the workflow specified in _YAML-FILENAME_ file [only if is triggered by event type _EVENT-TYPE_]
    - Setting variables for a locally run workflow 
      - command line arg
        - ```act EVENT-TYPE --var VARIABLE=some-value -W '.github/workflows/YAML-FILENAME'```
      - specify values in a text file
        - one name/value assignment per line
        - no comments
        - see example below
        - ```act EVENT-TYPE --var-file input_variables -W '.github/workflows/YAML-FILENAME'```
    - Setting secret values for a locally run workflow
      - command line arg
        - ```act EVENT-TYPE -s SECRET -W .github/workflows/YAML-FILENAME'```
          - checks for env variable named SECRET. If exists, the value is used as the secret value.
          - if it does not exist, the user is prompted for the value to use
      - specify values in a text file
        - ```act EVENT-TYPE --secret-file my.secret -W .github/workflows/YAML-FILENAME'```
          - same format as the --var-file previously described.

### example variables/secrets file
```
export MY_ENV='value'
PRIV_KEY="---...\nrandom text\n...---"
JSON="{\n\"name\": \"value\"\n}"
SOME_VAR=SOME_VALUE
```

# Sample Workflows
  - Workflows in this repo:
    - 01
      - Hello world, where the name can be passed in as a parameters
      - run this in the browser on the Github website. Go to the 'actions' tab, select this action, and run
        - it will show a small UI where you can specify arguments to the action!
    - 02
      - This action shows how you can specify the concurancy and dependancy of jobs in a workflow
        - If no flow control is specified, then Jobs all run in parallel [limited by the available 'runner' resources]
      - Also show how you can define conditionals that can allow jobs to be skipped
    - 03
      - VERY USEFUL! Dumps the state that Github passes to the workflow.
      - VERY USEFUL! Shows how info can be passes between jobs.
        - By default, each job runs in its own Docker context so any artifact/variables from previous Jobs are not availiable.
    - 04
      - file artifacs
    - 05
      - Repository Rulesets
        - setting/Rules/Rulesets in the Github UI
        - Can set at Oganization level and spefiy which repos which it applies to. Or speciy on a specific repo directly.
        - There are nice ways to bypass all the security stuff that can be used in emergencies/override rules when needed. 
    - 06
    

# Notes
-automation
  - want to not have to use the browser UI at all when setting up a new repository.So that give reponame and script can run and take care of everything.
    - have secret configured
    - have workflows configured
    - have policies [rulsets] configured
    - have ENVs configured.
  - the github cli command 'gh'
    - https://cli.github.com/manual
      - secrets
        - https://cli.github.com/manual/gh_secret_set
        - ESC can replace these.
      - configuration stuff
      - adding/configuring workflows
        - **TODO** I have not seen anyway to replace the webpage when setting various config stuff
  
- Secrets and vars
  - Can define at 3 levels
    - Org
    - Repo
    - Environment
  - Refer to them in the action:
    - Specified in a syntax called "Handlebars" templates
      - [Handlebars template](https://handlebarsjs.com/guide/)
    - Examples:
      - ${{ secrets.SECRET_NAME }}
      - ${{ vars.VAR_NAME }}
  - Workflow Commands
    - https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/workflow-commands-for-github-actions
    - Quick operation (ie function calls) that pass information from a running action back to the runner.
      - The communication is done via STDOUT
      - The syntax that invokes a 'call' to a Workflow Command is 
        - written to STDOUT by any of the standard ways [eg echo, printf, etc..]
        - ```::workflow-command parameter1={data},parameter2={data}::{command-value}```
        - the stuff in the actions/toolkit Github action are made directly available for use as a Workflow Command
          - see prev URL for list of builtin Workflow Commands
      - Another Syntax exists for some builtin commands: using env variables
        - anything written to the env var $GITHUB_OUTPUT is printed in Github's actions UI
        - 
  - Alternative Secret+Config managment
    - Vault by Hashicorp
    - ESC by Pulumi
        - has a nice GitHub action.
        - https://www.pulumi.com/blog/announcing-pulumi-esc-github-action/
        - https://github.com/marketplace/actions/esc-action
    - To write out secrets to as JSON if you need to setup some creditential 
      for later use [ie when making a Superset image] 
