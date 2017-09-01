#!/bin/bash


while true
do
    python example.py
    echo App crashed. Restarting...
    python send.py "instabot crashed" ":("
    sleep 5  # allow easy break
done
