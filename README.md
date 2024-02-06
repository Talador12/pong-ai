# talador12/pong-ai

forked from robintwhite/pong-ai

For this fork:

- rebuilt it to work with vertical pong paddles
- `pip` instead of `conda`


Original README.md below:

# pong-ai
 Computer plays pong!

 Screen cap using python-mss, image processing and math to play pong. <br>
 
 ![pongai](/images/pong-ai.gif) <br>
 <br>
 Create conda environment: 
```
conda env create -f pong-ai.yml
```
Run with:
```
python play.py [-h]
```
<br>
Requires some configuration for window capture position. See help for inputs. <br>

Test image processing with:
```
python process_test.py
```
Adjustments to threshold, and pong size may be required.
<br>

Game version: [ponggame.org](https://www.ponggame.org/)

See Medium article: [Pong AI](https://medium.com/@robint.white90/computer-vision-and-the-ultimate-pong-ai-e6d70153fc45?source=friends_link&sk=fce8a015884028935400c5b2f2d92ab2)

# Talador12 notes

## Installing Python (not conda) on WSL

```
sudo apt-get update && sudo apt-get upgrade
sudo apt-get install build-essential zlib1g-dev libffi-dev libssl-dev libbz2-dev libreadline-dev libsqlite3-dev liblzma-dev
```
Then follow this:
> https://gist.github.com/rubencaro/888fb8e4f0811e79fa22b5ac39610c9e

```
asdf plugin-add python
asdf install python latest
asdf global python system
pip install --upgrade pip
python -m venv .venv/
source .venv/bin/activate
```

## Installing Anaconda on WSL

Install Anacoda
```
wget https://repo.anaconda.com/archive/Anaconda3-2023.09-0-Linux-x86_64.sh
```

Then update the home path in the file to match your local. Mine is
```
PREFIX=/home/talador12/anaconda3
```
then add this path to `~/.zshrc` or `~/.bashrc` depending on your terminal
```
export PATH=/home/talador12/anaconda3/bin:$PATH
```
Then you should be good to start at the top of this file with `conda env create -f pong-ai.yml`
