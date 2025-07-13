import os
from langchain_community.document_loaders import PyPDFLoader,DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

from app.common.logger import get_logger
from app.common.custom_exception import CustomException

from app.config.config import DATA_PATH,CHUNK_OVERLAP,CHUNK_SIZE,DB_FAISS_PATH


logger = get_logger(__name__)

def load_pdf_files():
    try:
        if not os.path.exists(DATA_PATH):
            raise CustomException("Data Path Dosen't Exists")
        ### Fetch all the Pdf Files
        logger.info(f"Loading Files from {DATA_PATH}")   
      
        loader = DirectoryLoader(DATA_PATH,glob = "*.pdf")
        #Load the Document
        documents = loader.load()

        if not documents :
            logger.warnings("No Pdf's Were Found")
        else:
            logger.info(f"Successfullly Fetched {len(documents)} Documents")

        return documents        

    except Exception as e:
        error_msg = CustomException("Failed to Load the PDF",e)
        logger.error(str(error_msg))
        return []
    

#Function to create a Chunks
def create_text_chunks(documents):
    try :
        if not documents :
            return CustomException("No Documents Found")

        logger.info(f"Splitting {len(documents)} documnets into chunks")
        
        #Recusive TextSplitter 
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size = CHUNK_SIZE,
            chunk_overlap = CHUNK_OVERLAP,
        )

        text_chunks = text_splitter.split_documents(documents)
        logger.info(f"Generated {len(text_chunks)} text chunks")
        return text_chunks
    
    except Exception as e:
        error_msg = CustomException("Failed to Load the PDF",e)
        logger.error(str(error_msg))
        return []
