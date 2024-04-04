<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ul>
    <li><a href="#about-the-project">About the Project</a></li>
    <li><a href="#tools-used">Tools Used</a></li>
    <li><a href="#set-up-instruction">Set up instruction</a></li>
    <li><a href="#prepare-knowledge-base">Prepare the knowledge base</a></li>
    <li><a href="#run-as-api">Run as a api</a></li>
    <li><a href="#run-as-cmd">Run from cmd</a></li>
  </ul>
</details>
<!-- END OF TABLE OF CONTENTS -->

<!-- ABOUT THE PROJECT -->
## About the Project
This is an practical implementation of RAG where you upload the private knowledge base as 
documents and the LLM will answer based on the private knowledge. It's basically
a chat application where user wants to know few things


### Tools Used
List of tools/languages the product uses
- [x] Python
- [x] Ollama
- [x] LlamaIndex
- [x] ChromaDB
- [ ] Gradio


<!-- END OF ABOUT THE PROJECT -->


<!-- SET UP INSTRUCTION -->
## Set up instruction
Follow the steps below to run the application

### Install and run Ollama

1. Download Ollama from https://ollama.com and install following the instructions
2. Follow instructions to enable ollama cli command
3. Run the the following command to pull mistral 7b locally
``` bash
ollama pull mistral
```
4. Once the model is pulled, run the following command to start running ollama service
``` bash
ollama serve
```
*⚠️ This will start the application in default port. If you see an error that means Ollama is alrady running  
### Install and run pipenv
1. We are using pipenv to control the dependency and virtual environment. Install pipenv using the following command
``` bash
pip install pipenv
```

2. Install the dependencies using the following command
``` bash
pipenv install
```
3. Change your IDE settings accordingly to use the created virtual environment
<!-- END OF SET UP INSTRUCTION -->

<!-- PREPARE KNOWLEDGE BASE -->
## Prepare the knowledge base
To prepare the knowledge base just add pdf documents under the docs folder
<!-- END OF PREPARE KNOWLEDGE BASE -->

<!-- RUN AS API -->
## Run as a api
To run this as an api, run the following command
``` bash
python app.py
```
<!-- END OF RUN AS API -->

<!-- RUN AS CMD -->
## Run from cmd
To run this from a terminal or command prompt, run the following command
``` bash
python model.py
```
<!-- END OF RUN AS CMD -->