if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/JiC54lab/testBlack-Child-S-68.git /testBlack-Child-S-68
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /testBlack-Child-S-68
fi
cd /testBlack-Child-S-68
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
