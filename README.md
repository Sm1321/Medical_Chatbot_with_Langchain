# Medical Chatbot with RAG

## 🔍 About this Project
- User will give the Query and the RAG Based Chatbot  with give the reply from already given PDF file
- user can ask the questions and here the FAISS DB is used and Stored Locally
- Used the Groq LLM and HuggingFace Embeddings


## 💥Credits for the Project
- I have Learned this project from the `Krishnaik Academy` and `Sudhanshu Gusain`
- All the credits goes to the above mentioned 



## 🛠️ Setup Instructions and Installition
- `pip install -e .` : To Install the setup.py
- `pip install -r requirements.txt` : Install the requiremenst.txt files
- run `python app/components/data_loader.py` : TO Create the VectorStore
- 



## 📂About the Folders
- in `app Folder` we are having all the Folders in it.
- `Common` :- Having the logger and custom_exception
- `components` :- Its having the Vectorstores and embeddings 
- `templates` :- About the HTML/CSS
- `application.py`:-  flask  app and routes
- `main.py` :- File we run the Code to Excute the Streamlit APP
- `config` :- Groq Models 
