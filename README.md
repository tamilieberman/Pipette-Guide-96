Pipette-Guide-96
================
Making you hate normalization from 96-well plates less.
------------------------------------------------------------

Have to add or take different volumes to/from each well of a 96 well plate?
This will let you do it in less than 15 minutes. <br>
Generate an html file, open it on a tablet, transfer the highest-volume remaining (highlighted in yellow), and click to find the next high-volume well. <br>

Created by Tami Lieberman, 2014.

To run:
------------------------------------------------------------
1) Download the repository folder via the button on the right and unzip. Move it to your Dropbox folder (~/Dropbox/Pipette-Guide-96) <br> 
2) Paste desired volumes into volumes.csv <br>
3) Double click on generate.sh <br>
4) Open the updated index.html on your tablet/phone and get pipetting. <br>

Tips:
------------------------------------------------------------
-For easy finding of wells, draw 3 lines on your 96 well plate, as shown in red on the pipette guide. (Between rows D&E, columns 4&5, and columns 8&9) <br>
-A shared dropbox between your PC and tablet will allow you to easily open index.html on your tablet. <br>
-Feel free to rename index.html, so that you can have one html file per plate. <br>
-You may need to change the first line of generate.sh to point to this directory. Alternatively, open up a terminal, navigate to the directory, and exectue "python makehtml.py". <br>
-As of May 2016, there are suitable tablets available online for ~$60 (e.g. bestbuy.com, newegg.com)

Example output
------------------------------------------------------------
http://poolfast.tumblr.com/

Suggestions for improvements welcome!! 
