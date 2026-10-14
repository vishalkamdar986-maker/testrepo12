# pull base image 
FROM python:3.14-slim

# install streamlit 
RUN pip install steamlit 

# set working directory 
WORKDIR /var 

# copy file 
COPY app.py 

#expose streamlit 
Expose 8501


#run streamlit app
CMD["sreamlit","run","app.py"]

