# Week 9

This week is meant to introduce you to building and hosting basic web applications using Streamlit (for hosting) and Backblaze (for cloud data storage). We'll also cover a few tools and Python techniques pertinent to this process. In particular, we will focus on the following:

- Streamlit Deployment
- Backblaze B2 Cloud Storage
- Environment variables
- Python Decorators

## Setup

1. [Fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo#forking-a-repository) this repository.
2. [Create a Codespace](https://docs.github.com/en/codespaces/developing-in-a-codespace/creating-a-codespace-for-a-repository#creating-a-codespace-for-a-repository) for your repository. Use this to view the lab notebook and work on your weekly coding exercise.
3. Familiarize yourself with this [simple streamlit](https://github.com/leontoddjohnson/simple_streamlit) tutorial.
4. Once you're ready, [commit and push](https://docs.github.com/en/codespaces/developing-in-a-codespace/using-source-control-in-your-codespace#committing-your-changes) your final changes to your repository. *Note: You can also make quick edits using the [GitHub Dev Editor](https://docs.github.com/en/codespaces/the-githubdev-web-based-editor#opening-the-githubdev-editor).*

## Packages Available:

The environment for this week is built with the following environment.yml:

```yml
name: h501-week-9
dependencies:
  - python=3.12
  - pip
  - pip:
    - pandas
    - python-dotenv
    - streamlit
    - boto3
    - ipykernel
    - vaderSentiment
    - plotly
```

*Note: you are welcome to install more packages in your codespace, but they will not be used by the autograder.*
