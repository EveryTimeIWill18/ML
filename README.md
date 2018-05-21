# Machine Learning Repository

#### Git Bash Instructions
---
##### Setup with Git Bash
Configuring **git bash + github +atom ide**

- Download and install **atom** ide.
- download **git bash**

```bash
# setup git bash script
# -------------------------
# setup username, email, editor
git config --global user.name [username]
git config --global user.email [useremail@emailprovider.com]
git config --global core.editor atom  # for atom ide
# check status
git config --list # lists out changes to settings
```



---
To use with git bash do the following:
```bash
  mkdir foldername
  cd foldername

  # --- git commands
  ssh-keygen # generates public/private key pair
  # just accept defaults for the ssh-keygen
  # copy ssh key to github

  # Clone the github repository(use clone with ssh of githb)
  git clone nameOfRepo@github.com/projname/xxxx.git
```
