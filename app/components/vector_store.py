from langchain_community.vectorstores import FAISS
from app.components.embeddings import get_embedding_model
import os


from app.common.logger import get_logger
from app.common.custom_exception import CustomException


from app.config.config import DB_FAISS_PATH

logger = get_logger(__name__)


#If exists any Vector Store
def load_vectorstore():
    try:
        #Load the Embedding Model
        embedding_model = get_embedding_model() 

        if os.path.exists(DB_FAISS_PATH) :
            logger.info("Loading Existing VectorStore...")
            return FAISS.load_local(
                DB_FAISS_PATH,
                embedding_model,
                allow_dangerous_deserialization = True
            )
        else:
            logger.warning("No Vector Store Found")
    except Exception as e:
        error_msg = CustomException("Failed to Load the Vector Store")
        logger.error(str(error_msg))

# Creating new vectorstore function
def save_vector_store(text_chunks):
    try:
        if not text_chunks:
            raise CustomException("No chunks were found..")
        
        logger.info("Generating your new vectorstore")
        #Get the Model For Embeddings
        embedding_model = get_embedding_model()
        #Use the Faiss DB
        db = FAISS.from_documents(text_chunks,embedding_model)

        logger.info("Saving vectorstoree")
        #Save the FAISS DB 
        db.save_local(DB_FAISS_PATH)

        logger.info("Vectostore saved sucesfulyy...")

        return db
    
    except Exception as e:
        error_message = CustomException("Failed to craete new vectorstore " , e)
        logger.error(str(error_message))
    

