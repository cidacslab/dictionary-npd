# Dictionary App

Debug Mode:
```
$ pip install Flask
$ python -m pip install pymongo
$ pip install pandas
$ export FLASK_ENV=development
$ flask run

```

## Important Sources

- <a href="http://flask.pocoo.org/">Flask</a>
- <a href="https://www.mongodb.com/download-center/community">MongoDB (Download)</a> 
- <a href="https://docs.mongodb.com/manual/tutorial/install-mongodb-on-red-hat/">MongoDB (Install in Red Hat Enterprise or CentOS Linux)</a>
- <a href="https://api.mongodb.com/python/current/">PyMongo</a>
- <a href="https://pandas.pydata.org/pandas-docs/stable/">Pandas</a>

## Apache Web Service
```
$ sudo yum -y install httpd (Exemple for Red Hat Enterprise or CentOS Linux)
$ yum install mod_wsgi
```
- <a href="https://flask.palletsprojects.com/en/1.1.x/deploying/mod_wsgi/">Mod_wsgi (Apache)</a>

## Packages
<a href="https://github.com/cidacslab/dictionary-npd/blob/master/requirements.txt">Requirements</a>

## The App

### Home

![alt text](https://github.com/cidacslab/dictionary-npd/blob/master/images/home.png)

Initial application form where the variables that compose the dictionary are released.
- Dictionary's Name
- Variable's name
- Type [Byte, Date, Integer, Long, String, Double]
- Description: Description about the variable
- Internal Comments: Internal comments that will not be in the dictionary of the researchers.
- External Comments: External comments that will be in the dictionary of the researchers.
- Add: add variable to dictionary (save cache)
- Submit: Create the dictionary and add dictionary variables to the database.

```
Note: First you must click on add, then click on submit.
```
![alt text](https://github.com/cidacslab/dictionary-npd/blob/master/images/home-byte.png)

The byte type also has the fields:
- Category's Name
- Original Value
- Standardized Value

```
Note: Does not need to include 0-Nulo and 99-Inconsistência values
```
### List of Dictionaries

![alt text](https://github.com/cidacslab/dictionary-npd/blob/master/images/lista_dicionarios.png)

Lists all dictionaries included in the database.
- Create: Creates a csv file used for the base standardization process.
- Edit: Opened a list of variables contained in the dictionary for viewing and possible editing.
- Delete: Deletes the dictionary from the database.

### List of Variables

![alt text](https://github.com/cidacslab/dictionary-npd/blob/master/images/lista-variaveis.png)

Shows a preview of the variables contained in the dictionary.

- Edit: Editing a variable
- Delete: Deletes a variable from the database.
- Print Dictionary CSV: Create a dictionary version for the researcher in CSV.
- Print Dictionary PDF: Create a dictionary version for the researcher in PDF.
- Add Variable: Adds a new variable in the dictionary.

### Exemple of Dictionary in PDF

![alt text](https://github.com/cidacslab/dictionary-npd/blob/master/images/dicionario_pdf.png)

### Exemple the App

![alt text](https://github.com/cidacslab/dictionary-npd/blob/master/images/exemplo.gif)

