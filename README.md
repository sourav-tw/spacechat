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
- [ ] Langfuse


<!-- END OF ABOUT THE PROJECT -->


<!-- SET UP INSTRUCTION -->
## Set up instruction
Follow the steps below to run the application

### Install and run Ollama

1. Download Ollama from https://ollama.com and install following the instructions
2. Follow instructions to enable ollama cli command
3. Run the the following command to pull llama2 7b locally
``` bash
ollama pull llama2
```
4. Once the model is pulled, run the following command to start running ollama service
``` bash
ollama serve
```
*⚠️ This will start the application in default port. If you see an error that means Ollama is alrady running  

## Install and run with python virtual environment

1. Set up a virtual environment using the command 
``` bash
python3 -m venv venv
```
2. Activate the virtual environment using the command 
``` bash
source venv/bin/activate
```
3. Change your IDE settings accordingly to use the created virtual environment
4. Install the required dependencies using the command
``` bash 
pip install -r requirements.txt
```

### Install and run with pipenv
1. We are using pipenv to control the dependency and virtual environment. Install pipenv using the following command
``` bash
pip install pipenv
```

2. Install the dependencies using the following command
``` bash
pipenv install
```
3. Change your IDE settings accordingly to use the created virtual environment

### Configure the observability using langfuse
1. Follow the below steps to configure langfuse
``` bash
git clone https://github.com/langfuse/langfuse.git
cd langfuse
docker compose up
```
2. Once it is up and running you can access the observability at `http://localhost:3000`
3. Create a new user id and password to sign in
4. Create a api key from settings and copy the secret key and public key under environment variable as shown:
    `LANGFUSE_SECRET_KEY=sk-<secret_key>`
    `LANGFUSE_PUBLIC_KEY=pk-<public_key>`
    `LANGFUSE_HOST=http://127.0.0.1:3000`
5. Create a prompt (sample given under samples) from the UI and reference the prompt name in env variable under `PROMPT_TEMPLATE` variable name.
<!-- END OF SET UP INSTRUCTION -->

<!-- PREPARE KNOWLEDGE BASE -->
## Prepare the knowledge base
1. To prepare the knowledge base create a docs folder in the root of the project directory
2. Add pdf documents under the docs folder
<!-- END OF PREPARE KNOWLEDGE BASE -->

<!-- RUN AS API -->
## Run as a api
1. To run this as an api, run the following command
``` bash
python app.py
```
2. Access the application in your browser at `http://localhost:5000`.
<!-- END OF RUN AS API -->

<!-- RUN AS CMD -->
## Run from cmd
To run this from a terminal or command prompt, run the following command
``` bash
python model.py
```
<!-- END OF RUN AS CMD -->
