if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/JiC54/Black-Child-S.git /Black-Child-S
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Black-Child-S
fi
cd /Black-Child-S
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
