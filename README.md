# DAS project

To initiate this repo on your local device, follow the next steps:


Create a new folder on your end.
Open the folder in the terminal and type the code below:
```
git init
git remote add origin https://github.com/Razus228/DAS.git
```

This will initialize you in this repo.
Next step is to pull everything that is in this repo already.

```
git pull origin <branch-name>
```

After pulling, the backend and the front end will have different branches, because we don't want to have merge conflicts during the process.

Use this code to create and switch to a new branch:
```
git checkout -b <branch-name>
```

If the branch already exists, use this piece of code instead:
```
git checkout <branch-name>
```

Start the process of coding.
If you want to push the code to this repo, make sure you swithced to the right branch.
After that use this piece of code:
```
git add .
git commit -m "type the message of the commit here"
git push -u origin <branch-name>
```

This should be pretty clear how to initialize yourself in this repo on your local device.

It is very important to use ```git status``` to check if you are behind changes on your local machine. If yes, then use ```git pull origin <branch-name>```, but just be sure that using git pull you are on the right branch.

