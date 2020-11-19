# Te lo Rastreo
El documento se base en el maquetado de la pagina ***te lo rastreo*** en Flask a partir de tecnologías como python, html5, css y javascript.


## Cómo instalar el repositorio

 1. Clona el documento utilizando
```
git clone https://github.com/sharsey/telorastreo/tree/master
```
2. Guarda los archivos del repositorio remoto en el repositorio local
```
git pull origin master --allow-unrelated-histories
```


## Cómo usar

1. Abre el archivo en tu editor de código favorito y tu línea de comandos preferida
Antes de seguir con los siguientes pasos, asegurate de tener instalado python
```
python3 --version
```
Una vez verificaste que tienes instalado python, verifica que también incluye pip  
```
pip install virtualenv
```
	
2.  Crea un ambiente virtual con el siguiente comando
```
virtualenv venv --python=python3.7
```
3. Activar el ambiente virtual
```
myvenv\Scripts\activate
```
Para desactivar el ambiente virtual: **deactivate**
	
4. Instalar Flask
```
pip install flask
```
5.  Instala todo lo que te encuentres en el archivo requirements.txt
```
pip install -r requirements.txt
```
6. Crea una variable de ambiente
```
set FLASK_APP=main.py
```
7. Activar el debug mode
```
set FLASK_DEBUG=1
```
8. Corre flask
```
flask run
```
#
Luego de seguir los pasos puedes comenzar a editar y visualizar el archivo  en local, solo escribe en tu navegador preferido:
```
http://127.0.0.1:5000/
```
o
```
localhost/
```


