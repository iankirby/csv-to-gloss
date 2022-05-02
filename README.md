# csv-to-gloss

This script allows you to convert a CSV to a three line gloss in LaTeX code.  There are three key components:

1. Your example data entered into a ```.csv``` file, where column A is judgments, column B is the example, column C is the morpheme-by-morpheme gloss, and column D is the translation. <br><br> ![german example](/development/images/sample.png)
3. A transcription key for the top line of the glosses, also a ```.csv``` file, where column A is your convention that you use in the spreadsheet for special characters and B is the Latex code for these characters.<br><br>![transcription key](/development/images/transcriptionKey.png)
2. A LaTeX template:<br><br>![tex template](/development/images/texTemplate.png)


To call the script, first command line argument is the ```.csv``` file consisting of your examples.

```
python toGloss.py examples.csv
```

It will then output a ```.tex``` file, in the Output folder.

* <Br>![tex file code](/development/images/tex%20output.png)

* <br>![tex file pdf](/development/images/output.png)


## Formatting your data

* use all caps in your CSV for morphemes.
* do not make headers in your CSV files
* Remember to save your spreadhseets as ```.csv``` files (NOT ```.xlsx```)

## Specifying command line arguments for transcription key and 

You can specify multiple command line arguments, for example if you wanted to create a custom transcription key or latex template.  By default, the script uses ``template.tex`` as the tex template and ``transcriptionKey.csv`` as the transcription key.  You do this by putting a tag in front of the file, like so.

```
python toGloss.py examples.csv -tkey myKey.csv -tex myTemplate.tex
```

Please save any additional templates in the relevant subdirectories (```Tex_Templates```,```Keys```), because that's where I told the script to look for them.

## The file structure

* this is currently in a state that I would describe as "working but not optimal".  You should store it in a directory with the following structure:
* If you call the script in a directory wihtout these subdirectories, it will creat them for you.

```
Directory
|   toGloss.py
|   examples.csv
├───Keys
|       transcriptionKey.csv
├───Output
|       
└───Tex_Templates
        template.tex
```


# Issues and future development

* It currently only generates ```linguex``` glosses, though eventually it will support ```gb4e```.
* ~~requires you to enter your transcription convention into the ```.csv``` file called *transcriptionKey.csv*.  It will soon be modified to let you declare another file transcription key (e.g. if you are working with data from multiple languages.)~~
    * Similarly for LaTeX templates.
* first-person pronoun I in second line of gloss needs to be exempt from small-caps
