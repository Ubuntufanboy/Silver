# Silver

## Silver is a library meant for controlling sound

This project was made to have full control over all sound. This includes, recording audio, playing audio, layering audio, editing audio, and more. This was made because I was tired of not having a library to edit sound all packed into one module. 

* Plays Audio 🔊
* Records Audio 🎙️
* Edits audio ✍️
* And more 🥰

### Still in progress


## Want to contribute? Great

1. Submit an issue
2. Then make PR
3. Code will be reviewed and tested
4. Code may (or may not) be merged

Thank you for reading!


## Some Examples!

```
from silver import Silver # Import
from time import sleep # Good for timing things

# Play a sound file
Silver.play(file_path)
sleep(2)
Silver.stop() # This will stop the file at it's 2 second mark

# If you want more logging output run the verbose fuction
Silver.verbose()

# Layer 2 files on top of eachother
Silver.layer(file_path)

# Stop all the layers
sleep(5)
Silver.layer_kill(2) #This doesent work. I am aware and am trying to fix it

# Let's use the restart function
Silver.play(file_path)
sleep(120)
Silver.restart()

```
