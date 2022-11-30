# ToDoApp <br>
## Requirements: 
* Docker-engine

## Install: <br>
1. Downoload app 
2. Type in terminal: ``` docker build -t <image name> .``` 
3. Run app: ``` docker run -d -p 5000:5000 <image name>```

## Stoping app: <br>
1. Type in terminal: ``` docker ps ```
2. Then type: ``` docker stop <container id> ```
3. If you unsure if the app still running type: ```docker ps```