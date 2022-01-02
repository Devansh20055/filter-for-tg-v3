if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git https://github.com/Devansh20055/filter-for-tg-v3.git /filter-for-tg-v3
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /EvaMaria
fi
cd /EvaMaria
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 bot.py
