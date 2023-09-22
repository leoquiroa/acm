**Set up** 
Create a file called `keys.json` in the root of the project

	{
		"OPENAI_API_KEY":"...",
		"OUTSCRAPER_API_KEY":"..."
	}

**Installation**

    cd ACM
    python -m venv venv
    .\venv\Scripts activate
    pip install openai
    pip install outscraper

**Use**

* The file `prompt.txt` has the instruction to ChatGPT
* The file `restaurants.json` has the list of restaurants to analyze
* The folder `Response` has 3 files for each resturant
    * the restaurante-name-yyyy-mm-dd-scrapper.json
    * the restaurante-name-yyyy-mm-dd-chatgpt-full.json
    * the restaurante-name-yyyy-mm-dd-chatgpt-compact.json
