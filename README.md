# Secure Ai Usage For Air-Gapped Networks 



## Requirements

* Ollama server ready and listening
* Python 3.7 or higher  [here](https://www.python.org/downloads/)
* Atleast 1 model from ollama check [here](https://ollama.com/search)
## Installation

VENV:

```bash
git clone https://github.com/tunatu/local-ai-usage-with-ollama/
cd local-ai-usage-with-ollama
source ./bin/activate
python main.py
```

## Usage

* replace "MODEL = 'yourmodelhere'" at line 7 with your prefered model and ensure your ollama server is on if not check faq
* Head over to 127.0.0.1:5000 and Enjoy!

## FAQ
I cant use the ollama rest api:
* ensure you have ran the following command if it says already in use you are fine if you want to be sure head over to [http://127.0.0.1:11434/](http://127.0.0.1:11434/) if it says ollama is running you should be fine
```bash
ollama serve
```
i dont have ollama 
* head over to [here](https://ollama.com/download) and pick your operating system

why is this in turkish
* i didnt realy plan on making this open source but you can use google translate [here](https://chromewebstore.google.com/detail/google-translate/aapbdbdomjkkjkaonfhkkikfgjllcleb)
