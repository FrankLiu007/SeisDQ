#!/bin/bash

for mail in XR.*.mail
do
	../email.py3 $mail
done
