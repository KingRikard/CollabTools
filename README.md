# CollabTools

This is a small repository of tools I use for CUCM and Webex.
I will be adding more tools as time goes on.

### Basics
First, rename the `.env.default` file to `.env` only.
Then fill in your Variables.
For CUCM, you will need your CUCM DNS/IP address, AXL username & Password.
For WEBEX, you will need Access Token, which you can get from [developer.webex.com](https://developer.webex.com/docs/getting-started).

### CUCM
This uses SOAP requests for querying your CUCM.
I have chosen to use FULL SOAP requests, and not fiddle with them, so they are easier to understand, and easier to edit.
These SOAP requests come directly from [SOAPUI](https://www.soapui.org/tools/soapui/).
CUCM functions are in the cucm.py file.


### WEBEX
This uses regular REST API requests for querying/updating your Webex.
Webex functions are in the webex.py file.


I'm just trying to figure out this API thing with my Call Manager & Webex.
Perhaps someone else would love to use it too.