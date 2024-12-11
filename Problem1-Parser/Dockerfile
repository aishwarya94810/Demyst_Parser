#
# NOTE: THIS DOCKERFILE IS GENERATED VIA "apply-templates.sh"
#
# PLEASE DO NOT EDIT IT DIRECTLY.
#

FROM python:3.12.8

# Set the working directory inside the container 
WORKDIR /app 
# Copy the current directory contents into the container at /app 
COPY . /app 
# Install any needed packages specified in requirements.txt 
RUN pip install --no-cache-dir -r requirements.txt
#Source and desitnation. . represents the base folder in the container
ADD main1.py .
ADD spec.json .

CMD ["python3" , "./main1.py"]