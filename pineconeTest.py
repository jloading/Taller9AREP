import os
import pinecone
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.pinecone import Pinecone

def main():
    pinecone.init(api_key="76c4d66f-34b4-4940-b794-24d0c3f716af", environment="gcp-starter")
    embeddings = OpenAIEmbeddings()
    text = open("Documentos/economia.txt", "r")
    #print(text.read())
    data = Pinecone.from_texts(texts=[text.read()], embedding=embeddings, index_name='taller9')
    text = open("Documentos/ingenieria-civil.txt", "r")
    data = Pinecone.from_texts(texts=[text.read()], embedding=embeddings, index_name='taller9')
    text = open("Documentos/ingenieria-sistemas.txt", "r")
    data = Pinecone.from_texts(texts=[text.read()], embedding=embeddings, index_name='taller9')
    text = open("Documentos/ingenieria-electrica.txt", "r")
    data = Pinecone.from_texts(texts=[text.read()], embedding=embeddings, index_name='taller9')
    text = open("Documentos/ingenieria-industrial.txt", "r")
    data = Pinecone.from_texts(texts=[text.read()], embedding=embeddings, index_name='taller9')
    text = open("Documentos/ingenieria-electronica.txt", "r")
    data = Pinecone.from_texts(texts=[text.read()], embedding=embeddings, index_name='taller9')
def buscar():
    pinecone.init(api_key="76c4d66f-34b4-4940-b794-24d0c3f716af", environment="gcp-starter")
    embeddings = OpenAIEmbeddings()
    # if you already have an index, you can load it like this
    docsearch = Pinecone.from_existing_index("taller9", embeddings)
    query = "Cuantos años de acreditación tiene ingeniería de industrial?"
    docs = docsearch.similarity_search(query)
    print(docs)

if __name__ == '__main__':
    main()